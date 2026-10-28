"""Check the conditional splitting bound on independent finite matrices.

The theorem is proved algebraically in the paper. These examples corroborate
it; they neither prove a continuum regularity condition nor a mesh-uniform
PDE theorem. All exponentials are calculated by Hermitian eigendecomposition.
"""
import json
from pathlib import Path
import numpy as np


def exponential(generator, time, unitary):
    hermitian = 1j * generator if unitary else generator
    values, vectors = np.linalg.eigh(hermitian)
    multiplier = np.exp((-1j if unitary else 1) * time * values)
    return (vectors * multiplier) @ vectors.conj().T


def check(unitary):
    H1 = np.array([[1., .3, 0.], [.3, 2., .2], [0., .2, .5]])
    H2 = np.array([[.5, 0., .4], [0., .7, .1], [.4, .1, 1.5]])
    assert np.min(np.linalg.eigvalsh(H1)) > 0
    assert np.min(np.linalg.eigvalsh(H2)) > 0
    A, B = (-1j * H1, -1j * H2) if unitary else (-H1, -H2)
    initial = np.array([1., 2., -1.], dtype=complex)
    initial /= np.linalg.norm(initial)
    T = .8
    exact = exponential(A + B, T, unitary) @ initial
    # Contractive partial trajectories have norm <=1, so the commutator
    # operator norm supplies a valid K for this finite-matrix check.
    K = float(np.linalg.norm(B @ A - A @ B, 2))
    m = float(np.linalg.norm(exact))
    rows = []
    for steps in (4, 8, 16, 32, 64):
        step = exponential(B, T / steps, unitary) @ exponential(A, T / steps, unitary)
        split = np.linalg.matrix_power(step, steps) @ initial
        error = float(np.linalg.norm(split - exact))
        norm_error = float(np.linalg.norm(split / np.linalg.norm(split) - exact / m))
        bound = K * T**2 / (2 * steps)
        normalized_bound = K * T**2 / (m * steps)
        assert error <= bound + 1e-13
        assert norm_error <= normalized_bound + 1e-13
        if unitary:
            assert abs(np.linalg.norm(split) - 1) < 1e-12
        else:
            assert np.linalg.norm(split) <= 1 + 1e-13
        rows.append(dict(steps=steps, error=error, bound=bound,
                         normalized_error=norm_error, normalized_bound=normalized_bound))
    assert rows[-1]["error"] < rows[0]["error"] / 10
    return dict(unitary=unitary, K=K, final_norm=m, T=T, rows=rows)


if __name__ == "__main__":
    data = dict(scope="Finite-matrix corroboration of proved conditional theorem",
                checks=[check(False), check(True)], all_assertions_passed=True)
    out = Path(__file__).resolve().parents[1] / "results/repaired-bound.json"
    out.write_text(json.dumps(data, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print("Both independent repaired-bound check groups passed.")
