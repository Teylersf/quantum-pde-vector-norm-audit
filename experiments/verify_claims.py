"""Deterministic checks for selected statements in arXiv:2603.08799v1.

Run from the repository root: python experiments/verify_claims.py
Requires Python >= 3.11 and NumPy. No quantum hardware or SciPy is used.
Numerical checks corroborate explicit analytic counterexamples; they do not
constitute a complete audit or a theorem about quantum computational cost.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def rms(value: np.ndarray) -> float:
    return float(np.sqrt(np.mean(np.abs(value) ** 2)))


def shear_check() -> dict:
    """Exact smooth periodic solution; sampled quadrature checks its L2 norms."""
    n = 256
    x, y = np.meshgrid(np.arange(n) / n, np.arange(n) / n, indexing="ij")
    rows = []
    for t in (0.0, 0.1, 1.0):
        phase = 2 * np.pi * (x - t * np.sin(2 * np.pi * y))
        f = np.sin(phase)
        fy = -4 * np.pi**2 * t * np.cos(2 * np.pi * y) * np.cos(phase)
        expected = 2 * np.pi**2 * abs(t)
        assert abs(rms(f) - 1 / np.sqrt(2)) < 1e-12
        assert abs(rms(fy) - expected) < 1e-11
        rows.append({"t": t, "field_L2": rms(f), "dy_field_L2": rms(fy),
                     "analytic_dy_field_L2": float(expected)})
    return {"locator": "page 6, footnote 10 and equality following Eq. (7)",
            "velocity": "c=(sin(2*pi*y),0)",
            "initial_field": "sin(2*pi*x)",
            "exact_solution": "sin(2*pi*(x-t*sin(2*pi*y)))",
            "conclusion": "Field L2 norm is conserved; derivative L2 norm is not.",
            "rows": rows}


def continuum_commutator_check() -> dict:
    """[A,B]u for A=d_xx, B=(1+a sin(qx))d_yy on the unit torus."""
    n, m, a, b = 256, 4, 0.2, 0.5
    x, y = np.meshgrid(np.arange(n) / n, np.arange(n) / n, indexing="ij")
    q, k, ell = 2 * np.pi, 2 * np.pi * m, 2 * np.pi
    u = 1 + b * np.sin(k * x) * np.sin(ell * y)
    uyy = -b * ell**2 * np.sin(k * x) * np.sin(ell * y)
    uxyy = -b * k * ell**2 * np.cos(k * x) * np.sin(ell * y)
    ky_x = a * q * np.cos(q * x)
    ky_xx = -a * q**2 * np.sin(q * x)
    retained_term = ky_xx * uyy
    omitted_term = 2 * ky_x * uxyy
    comm = retained_term + omitted_term
    printed_triangle_bound = a * q**2 * rms(uyy)
    analytic_ratio = np.sqrt((4 * m**2 + 1) / 2)
    observed_ratio = rms(comm) / printed_triangle_bound
    inner_product = float(np.mean(u * comm))
    assert np.min(1 + a * np.sin(q * x)) > 0
    assert abs(observed_ratio - analytic_ratio) < 1e-12
    assert abs(inner_product) < 1e-10
    assert observed_ratio > 5
    return {"locator": "page 6, displayed a'_g following Eq. (8)",
            "parameters": {"m": m, "a": a, "b": b, "quadrature_points_per_axis": n},
            "initial_field": "1+b*sin(2*pi*m*x)*sin(2*pi*y)",
            "coefficients": "kx=1, ky=1+a*sin(2*pi*x)",
            "identity": "[A,B]u=ky_xx*u_yy+2*ky_x*u_xyy",
            "actual_commutator_L2": rms(comm),
            "retained_term_L2": rms(retained_term),
            "omitted_term_L2": rms(omitted_term),
            "printed_commutator_bound_without_common_factors": printed_triangle_bound,
            "actual_to_printed_ratio": observed_ratio,
            "analytic_ratio": float(analytic_ratio),
            "inner_product_u_commutator_u": inner_product,
            "conclusion": "The missing mixed derivative term is nonzero. The exact commutator exceeds the printed terms, even with positive coefficients and a positive field. It is orthogonal to u, so leading normalization does not remove it."}


def normalized_distance(g: np.ndarray, h: np.ndarray) -> float:
    """L2 distance between normalized 1+g(x)sin(2pi*y) and 1+h(x)sin(2pi*y)."""
    ng = np.sqrt(1 + np.mean(g * g) / 2)
    nh = np.sqrt(1 + np.mean(h * h) / 2)
    return float(np.sqrt((1 / ng - 1 / nh)**2 + np.mean((g / ng - h / nh)**2) / 2))


def normalized_splitting_check() -> dict:
    """Exact p=1 semidiscrete equations using the invariant single-y-mode subspace.

    This is a two-dimensional N x N problem reduced exactly to N dimensions:
    the constant part is stationary and u=1+g(x,t)sin(2pi*y) stays in this
    subspace. The y-derivative squared eigenvalue is the paper's centered
    first-derivative squared value, not a spectral or standard Laplacian value.
    """
    n, m, a, b = 128, 4, 0.2, 0.5
    x = np.arange(n) / n
    frequencies = np.fft.fftfreq(n, d=1 / n)
    eigen_a = -(n * np.sin(2 * np.pi * frequencies / n))**2
    lambda_y = (n * np.sin(2 * np.pi / n))**2
    diagonal_b = -lambda_y * (1 + a * np.sin(2 * np.pi * x))
    identity = np.eye(n)
    matrix_a = np.fft.ifft(eigen_a[:, None] * np.fft.fft(identity, axis=0), axis=0).real
    matrix = matrix_a + np.diag(diagonal_b)
    assert np.max(np.abs(matrix - matrix.T)) < 1e-10
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    g0 = b * np.sin(2 * np.pi * m * x)
    q = 2 * np.pi
    rows = []
    for total_time in (0.0002, 0.0005):
        exact = eigenvectors @ (np.exp(total_time * eigenvalues) * (eigenvectors.T @ g0))
        norm_exact = np.sqrt(1 + np.mean(exact * exact) / 2)
        # The continuum |u_yy| norm is maximal at t=0: its single-mode
        # coefficient obeys a contractive heat equation with positive potential.
        # This uses the continuum derivative as printed, not the smaller
        # semidiscrete y derivative, making this comparison conservative.
        printed_a_g = 0.5 * (a * q**2) * (b * q**2 / 2) / norm_exact
        for steps in (64, 128, 256, 512):
            dt = total_time / steps
            multiplier_a = np.exp(dt * eigen_a)
            multiplier_b = np.exp(dt * diagonal_b)
            split = g0.copy()
            for _ in range(steps):
                split = multiplier_b * np.fft.ifft(multiplier_a * np.fft.fft(split)).real
            error = normalized_distance(split, exact)
            measured_coefficient = error * steps / total_time**2
            ratio = measured_coefficient / printed_a_g
            assert ratio > 2.5, (total_time, steps, ratio)
            rows.append({"T": total_time, "steps": steps,
                         "normalized_L2_error": error,
                         "measured_error_times_L_over_T_squared": measured_coefficient,
                         "printed_a_g": float(printed_a_g),
                         "measured_to_printed_ratio": ratio})
    for t in (0.0002, 0.0005):
        subset = [row for row in rows if row["T"] == t]
        for first, second in zip(subset, subset[1:]):
            assert 1.98 < first["normalized_L2_error"] / second["normalized_L2_error"] < 2.02
    return {"locator": "page 6, Eq. (8) leading coefficient a'_g",
            "grid": [n, n], "stencil_order": 2, "m": m, "a": a, "b": b,
            "method": "Symmetric eigendecomposition for exact semidiscrete evolution; FFT and pointwise exponentials for Lie splitting. Constant plus one y sine mode is an invariant subspace.",
            "interpretation": "The observed 1/L leading coefficient exceeds printed a'_g. This contradicts that coefficient if its remainder is o(1/L); it does not rule out a corrected grid-independent bound.",
            "rows": rows}


def checkerboard_and_consistency_check() -> dict:
    n = 64
    h = 1 / n
    checkerboard = (-1.0)**np.arange(n)
    first = (np.roll(checkerboard, -1) - np.roll(checkerboard, 1)) / (2 * h)
    squared_first = (np.roll(first, -1) - np.roll(first, 1)) / (2 * h)
    ordinary_laplacian = (np.roll(checkerboard, -1) - 2 * checkerboard + np.roll(checkerboard, 1)) / h**2
    assert rms(first) == 0 and rms(squared_first) == 0
    assert rms(ordinary_laplacian) == 4 / h**2
    rows = []
    for p in (1, 2):
        previous = None
        for count in (16, 32, 64, 128, 256):
            theta = 2 * np.pi / count
            derivative_eigenvalue = count * np.sin(theta) if p == 1 else count * (4 / 3 * np.sin(theta) - 1 / 6 * np.sin(2 * theta))
            error = abs(derivative_eigenvalue**2 - (2 * np.pi)**2)
            ratio = None if previous is None else previous / error
            rows.append({"p": p, "points": count, "eigenvalue_error": float(error),
                         "previous_to_current_error_ratio": None if ratio is None else float(ratio)})
            if count >= 64:
                assert (3.9 < ratio < 4.1) if p == 1 else (15.5 < ratio < 16.2)
            previous = error
    return {"locator": "pages 3-4, Eq. (4) using the square of a centered first derivative",
            "checkerboard_grid_points": n,
            "centered_derivative_checkerboard_norm": rms(first),
            "squared_centered_derivative_checkerboard_norm": rms(squared_first),
            "standard_laplacian_checkerboard_norm": rms(ordinary_laplacian),
            "conclusion": "An even periodic grid has an additional checkerboard null mode. This is a discrete structural limitation, not a refutation of consistency for fixed smooth data.",
            "smooth_sinusoid_consistency": rows}


def positivity_check() -> dict:
    n, mode, t = 64, 4, 0.001
    derivative_squared_eigenvalue = (n * np.sin(2 * np.pi * mode / n))**2
    amplification = np.exp(t * derivative_squared_eigenvalue)
    assert amplification > 1.5
    return {"locator": "page 2 coefficient hypotheses and page 5 footnote 8",
            "coefficient": "kappa=-1 (smooth and independent of x)",
            "grid_points": n, "mode": mode, "T": t,
            "semigroup_amplification": float(amplification),
            "conclusion": "Contractivity requires nonnegative diffusion coefficients. This counterexample applies to the literal displayed assumptions; positivity may have been physically intended by the term thermal conductivity."}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "results" / "verification.json")
    args = parser.parse_args()
    result = {"source_version": "arXiv:2603.08799v1",
              "scope": "Selected analytic counterexamples and deterministic numerical checks, not an exhaustive audit.",
              "numpy_version": np.__version__,
              "checks": {"shear_derivative_growth": shear_check(),
                         "continuum_diffusion_commutator": continuum_commutator_check(),
                         "normalized_semidiscrete_splitting": normalized_splitting_check(),
                         "checkerboard_and_consistency": checkerboard_and_consistency_check(),
                         "positivity_assumption": positivity_check()},
              "all_assertions_passed": True}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print("All five check groups passed. Results: " + str(args.output))


if __name__ == "__main__":
    main()
