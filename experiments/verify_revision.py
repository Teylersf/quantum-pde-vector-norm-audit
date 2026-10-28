"""Deterministic major-revision checks, without modifying canonical checks.

Run: python experiments/verify_revision.py
NumPy only. The field is always 1+b*cos(2*pi*m*x)*cos(2*pi*y).
Exact matrix eigendecomposition is exact semidiscrete evolution up to floating
point error; it is not a continuum PDE solver or a quantum circuit.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


Q, A, B, M = 2 * np.pi, 0.2, 0.5, 4


def rms(value: np.ndarray) -> float:
    return float(np.sqrt(np.mean(np.abs(value) ** 2)))


def symbol(mode: np.ndarray | int, points: int, p: int) -> np.ndarray:
    """Real symbol of D=-i*delta for the centered 2p-order first derivative."""
    theta = 2 * np.pi * np.asarray(mode) / points
    answer = np.zeros_like(theta, dtype=float)
    for k in range(1, p + 1):
        ak = (-1) ** (k + 1) * math.comb(2 * p, p - k) / (k * math.comb(2 * p, p))
        answer += 2 * ak * np.sin(k * theta)
    return points * answer


def lam(mode: np.ndarray | int, points: int, p: int) -> np.ndarray:
    return symbol(mode, points, p) ** 2


def commutator_coefficients(points: int, p: int) -> np.ndarray:
    """Coefficients of sin(q*(m+1)*x), sin(q*(m-1)*x), each times cos(q*y)."""
    l1, lm, lp, ln = (float(lam(r, points, p)) for r in (1, M, M + 1, M - 1))
    return A * B * l1 / 2 * np.array([lp - lm, lm - ln])


def continuum_check() -> dict:
    points = 256
    x, y = np.meshgrid(np.arange(points) / points, np.arange(points) / points, indexing="ij")
    u0 = 1 + B * np.cos(Q * M * x) * np.cos(Q * y)
    uyy = -B * Q**2 * np.cos(Q * M * x) * np.cos(Q * y)
    uxyy = B * M * Q**3 * np.sin(Q * M * x) * np.cos(Q * y)
    retained = -A * Q**2 * np.sin(Q * x) * uyy
    omitted = 2 * A * Q * np.cos(Q * x) * uxyy
    closed = A * B * Q**4 * (
        (M + 0.5) * np.sin(Q * (M + 1) * x)
        + (M - 0.5) * np.sin(Q * (M - 1) * x)) * np.cos(Q * y)
    commutator_norm = A * B * Q**4 / (2 * np.sqrt(2)) * np.sqrt(4 * M**2 + 1)
    printed_numerator = A * B * Q**4 / 2
    assert rms(retained + omitted - closed) < 1e-11
    assert abs(rms(closed) - commutator_norm) < 1e-11
    assert abs(np.mean(u0 * closed)) < 1e-11
    assert abs(rms(u0) - np.sqrt(1 + B**2 / 4)) < 1e-14
    return {
        "initial_field": "1+b*cos(2*pi*m*x)*cos(2*pi*y)",
        "parameters": {"a": A, "b": B, "m": M},
        "coefficients": "kappa_x=1; kappa_y=1+a*sin(2*pi*x)",
        "commutator_convention": "[A,B]=AB-BA; A=d_xx; B=kappa_y*d_yy",
        "analytic_identity": "[A,B]u0=ab*q^4*((m+1/2)*sin(q*(m+1)*x)+(m-1/2)*sin(q*(m-1)*x))*cos(q*y)",
        "commutator_L2": float(commutator_norm),
        "retained_term_L2": rms(retained),
        "omitted_term_L2": rms(omitted),
        "printed_numerator_P0": float(printed_numerator),
        "initial_norm_n0": rms(u0),
        "initial_normalized_comparator_P0_over_2n0": float(printed_numerator / (2 * rms(u0))),
        "small_time_normalized_coefficient": float(commutator_norm / (2 * rms(u0))),
        "actual_to_printed_ratio_R4": float(commutator_norm / printed_numerator),
        "inner_product_u0_commutator_u0": float(np.mean(u0 * closed)),
        "minimum_initial_field": float(np.min(u0)),
        "minimum_diffusivity": float(np.min(1 + A * np.sin(Q * x))),
        "quadrature_points_per_axis": points,
    }


def commutator_refinement() -> dict:
    continuum = A * B * Q**4 * np.array([M + 0.5, M - 0.5])
    printed = A * B * Q**4 / 2
    rows = []
    for p in (1, 2):
        previous = None
        for points in (32, 64, 128, 256, 512, 1024):
            coefficients = commutator_coefficients(points, p)
            # Orthogonality is exact in the quadrature norm on these grids.
            defect = float(np.linalg.norm(coefficients - continuum) / 2)
            norm_comm = float(np.linalg.norm(coefficients) / 2)
            observed_order = None if previous is None else float(np.log2(previous / defect))
            x = np.arange(points) / points
            g0 = B * np.cos(Q * M * x)
            modes = np.fft.fftfreq(points, d=1 / points)
            eigen_a = -lam(modes, points, p)
            diagonal_b = -float(lam(1, points, p)) * (1 + A * np.sin(Q * x))
            apply_a = lambda g: np.fft.ifft(eigen_a * np.fft.fft(g)).real
            direct = apply_a(diagonal_b * g0) - diagonal_b * apply_a(g0)
            closed = coefficients[0] * np.sin(Q * (M + 1) * x) + coefficients[1] * np.sin(Q * (M - 1) * x)
            identity_residual = rms(direct - closed) / np.sqrt(2)
            # FFT cancellation grows with N^2; this is a residual check, not an
            # estimate used to compute the much smaller consistency error.
            assert identity_residual < 1e-7
            if points >= 256:
                assert abs(observed_order - 2 * p) < 0.08
            rows.append({
                "p": p, "points_per_axis": points,
                "commutator_L2": norm_comm,
                "commutator_minus_continuum_L2": defect,
                "observed_order": observed_order,
                "actual_to_continuum_printed_numerator_ratio": norm_comm / printed,
                "exact_symbol_vs_direct_FFT_residual_L2": float(identity_residual),
            })
            previous = defect
    return {
        "exact_symbol": "sigma_p,h(r)=2/h*sum_{k=1}^p a_k*sin(2*pi*r*k*h); lambda_p,h(r)=sigma_p,h(r)^2",
        "stencil_weights": "a_k=(-1)^(k+1)*binom(2p,p-k)/(k*binom(2p,p)) for 1<=k<=p; a_-k=-a_k",
        "exact_discrete_commutator": "(ab*lambda(1)/2)*((lambda(m+1)-lambda(m))*sin(q*(m+1)*x)+(lambda(m)-lambda(m-1))*sin(q*(m-1)*x))*cos(q*y)",
        "fixed_mode_symbol_expansion": "lambda_p,h(r)=(q*r)^2-2*(p!)^2/(2p+1)!*(q*r)^(2p+2)*h^(2p)+O(h^(2p+2))",
        "analytic_conclusion": "For fixed m and p, only modes m-1 and m+1 occur; their coefficients converge with O(h^(2p)) error. Orthogonality therefore gives O(h^(2p)) quadrature-norm commutator convergence. This is a fixed-trigonometric-data statement, not a uniform theorem for arbitrary evolving inputs.",
        "rows": rows,
    }


def norm_full(g: np.ndarray) -> float:
    return float(np.sqrt(1 + np.mean(g * g) / 2))


def normalized_distance(g: np.ndarray, h: np.ndarray) -> float:
    ng, nh = norm_full(g), norm_full(h)
    return float(np.sqrt((1 / ng - 1 / nh) ** 2 + np.mean((g / ng - h / nh) ** 2) / 2))


def normalized_tangent_norm(g: np.ndarray, w: np.ndarray) -> float:
    """||DN_(1+g*cos y)(w*cos y)||, using the exact reduced metric."""
    n = norm_full(g)
    inner = np.mean(g * w) / 2
    value = np.mean(w * w) / (2 * n**2) - inner**2 / n**4
    assert value >= -1e-20
    return float(np.sqrt(max(0.0, value)))


def splitting_check() -> dict:
    points, p = 128, 1
    x = np.arange(points) / points
    modes = np.fft.fftfreq(points, d=1 / points)
    eigen_a = -lam(modes, points, p)
    lambda_y = float(lam(1, points, p))
    diagonal_b = -lambda_y * (1 + A * np.sin(Q * x))
    identity = np.eye(points)
    matrix_a = np.fft.ifft(eigen_a[:, None] * np.fft.fft(identity, axis=0), axis=0).real
    hmatrix = matrix_a + np.diag(diagonal_b)
    assert np.max(np.abs(hmatrix - hmatrix.T)) < 1e-10
    eig, vectors = np.linalg.eigh(hmatrix)
    assert eig[-1] < 0
    g0 = B * np.cos(Q * M * x)
    n0 = norm_full(g0)
    coordinates0 = vectors.T @ g0
    # [B,A]g = B A g - A B g, for the order S=e^(dt B)e^(dt A).
    comm_ba = matrix_a * (diagonal_b[:, None] - diagonal_b[None, :])
    comm_eigenbasis = vectors.T @ comm_ba @ vectors
    initial_printed_numerator = A * B * Q**4 / 2
    initial_comparator = initial_printed_numerator / (2 * n0)
    discrete_small_time = float(np.linalg.norm(commutator_coefficients(points, p)) / (4 * n0))
    coefficient_rows, step_rows = [], []
    for total_time in (1e-8, 1e-6, 1e-5, 0.0002, 0.0005, 0.001, 0.002):
        exact = vectors @ (np.exp(total_time * eig) * coordinates0)
        nT = norm_full(exact)
        # Integral kernel F_ij=int_0^T exp((T-s)*eig_i+s*eig_j) ds.
        # This form avoids catastrophic subtraction and positive exponentials.
        difference = np.abs(eig[:, None] - eig[None, :])
        maximum = np.maximum(eig[:, None], eig[None, :])
        factor = np.full_like(difference, total_time)
        np.divide(-np.expm1(-total_time * difference), difference, out=factor, where=difference != 0)
        kernel = np.exp(total_time * maximum) * factor
        integral = vectors @ ((comm_eigenbasis * kernel) @ coordinates0)
        leading_vector = (total_time / 2) * integral
        coefficient = normalized_tangent_norm(exact, leading_vector) / total_time**2
        # The supremum is analytic: ||g(s)|| decreases because H<=0. With
        # the continuum d_yy on this single-y-mode subspace, ||u_yy||=q^2||g||/sqrt(2).
        # Use q^2 rather than lambda_y in the comparator, conservatively.
        full_sup_comparator = initial_printed_numerator / (2 * nT)
        semidiscrete_sup_comparator = full_sup_comparator * lambda_y / Q**2
        mean_only_upper_comparator = initial_printed_numerator / 2  # nT>=mean(u0)=1.
        sampled = [rms(vectors @ (np.exp(s * eig) * coordinates0)) for s in np.linspace(0, total_time, 33)]
        assert all(first >= second - 1e-13 for first, second in zip(sampled, sampled[1:]))
        assert abs(max(sampled) - B / np.sqrt(2)) < 1e-13
        coefficient_rows.append({
            "T": total_time,
            "exact_final_norm_nT": nT,
            "initial_time_comparator_P0_over_2n0": initial_comparator,
            "full_evolved_supremum_comparator_P0_over_2nT": float(full_sup_comparator),
            "semidiscrete_uyy_supremum_comparator": float(semidiscrete_sup_comparator),
            "mean_lower_bound_upper_comparator_P0_over_2": float(mean_only_upper_comparator),
            "supremum_uyy_continuum_derivative_norm": float(Q**2 * B / 2),
            "supremum_uyy_semidiscrete_derivative_norm": float(lambda_y * B / 2),
            "lim_L_to_infinity_error_times_L_over_T_squared": coefficient,
            "ratio_to_initial_time_comparator": coefficient / initial_comparator,
            "ratio_to_full_evolved_supremum_comparator": coefficient / full_sup_comparator,
            "ratio_to_mean_lower_bound_upper_comparator": coefficient / mean_only_upper_comparator,
            "ratio_to_discrete_small_time_limit": coefficient / discrete_small_time,
        })
        if total_time in (0.0002, 0.0005):
            for steps in (64, 128, 256, 512):
                dt = total_time / steps
                multiplier_a, multiplier_b = np.exp(dt * eigen_a), np.exp(dt * diagonal_b)
                split = g0.copy()
                for _ in range(steps):
                    split = multiplier_b * np.fft.ifft(multiplier_a * np.fft.fft(split)).real
                error = normalized_distance(split, exact)
                measured = error * steps / total_time**2
                assert measured / full_sup_comparator > 3.5
                assert abs(measured / coefficient - 1) < 1e-3
                step_rows.append({
                    "T": total_time, "steps": steps, "normalized_L2_error": error,
                    "measured_error_times_L_over_T_squared": measured,
                    "exact_global_limit_coefficient": coefficient,
                    "full_evolved_supremum_comparator": float(full_sup_comparator),
                    "measured_to_full_supremum_ratio": measured / full_sup_comparator,
                })
    assert abs(coefficient_rows[0]["ratio_to_discrete_small_time_limit"] - 1) < 1e-5
    for total_time in (0.0002, 0.0005):
        selected = [r for r in step_rows if r["T"] == total_time]
        for first, second in zip(selected, selected[1:]):
            assert 1.98 < first["normalized_L2_error"] / second["normalized_L2_error"] < 2.02
    return {
        "grid": [points, points], "p": p, "initial_field": "1+b*cos(2*pi*m*x)*cos(2*pi*y)",
        "method": "Exact invariant single-y-cosine-mode reduction; symmetric eigendecomposition for U_h(t); FFT/pointwise Lie factors; analytic divided differences for the global leading coefficient.",
        "split_order": "S_dt=exp(dt*B_h)exp(dt*A_h)",
        "normalized_coefficient_formula": "c_h(T)=||DN_(U_h(T)u0)((T/2)*int_0^T U_h(T-s)[B_h,A_h]U_h(s)u0 ds)||_h/T^2",
        "initial_time_comparator_formula": "C_init=P0/(2*n0), P0=||kappa_x||inf*||partial_xx kappa_y||inf*||partial_yy u0||=ab*q^4/2",
        "full_evolved_supremum_comparator_formula": "C_sup(T)=(1/(2*nT))*sup_(0<=s<=T)(a*q^2*||partial_yy u_h(s)||_h)=ab*q^4/(4*nT), using the continuum y derivative on the invariant single-mode interpolant",
        "contractivity_proof": "g'=H_h g, H_h=A_h-lambda_y*diag(kappa_y)<=-lambda_y*(1-a)I. Hence d||g||_h^2/dt=2<g,H_h g>_h<=0; both ||partial_yy u_h||_h=q^2||g||_h/sqrt(2) and its normalized version attain their supremum at s=0. In the continuum replace A_h by d_xx and lambda_y by q^2 and integrate by parts.",
        "fixed_grid_small_time_limit": discrete_small_time,
        "fixed_grid_small_time_ratio_to_initial_comparator": discrete_small_time / initial_comparator,
        "why_finite_time_ratio_is_not_R4": "R4 is a continuum, initial-commutator ratio. At fixed h the limiting ratio as T->0 is R_h; at positive T the integral propagates the evolving commutator and final normalization projects the defect at U_h(T)u0. Only after the T->0 and h->0 limits does the ratio approach R4. Neither finite T rows nor 1/L refinement alone should equal R4.",
        "coefficient_rows": coefficient_rows, "step_refinement_rows": step_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "results" / "revision-verification.json")
    args = parser.parse_args()
    result = {
        "source_version": "arXiv:2603.08799v1",
        "scope": "Revision-only cosine-example checks. Finite-grid results and a fixed-trigonometric-data convergence proof; no unconditional PDE splitting theorem or quantum-advantage claim.",
        "numpy_version": np.__version__,
        "checks": {"cosine_continuum_commutator": continuum_check(),
                   "fixed_trigonometric_discrete_commutator_refinement": commutator_refinement(),
                   "normalized_cosine_semidiscrete_splitting": splitting_check()},
        "all_assertions_passed": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print("All revision checks passed. Results: " + str(args.output))


if __name__ == "__main__":
    main()
