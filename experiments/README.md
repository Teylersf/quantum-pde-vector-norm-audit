# Reproducible checks for arXiv:2603.08799v1

These experiments examine selected statements in the nine-page preprint
*Quantum algorithm for anisotropic diffusion and convection equations with
vector norm scaling*. They are an independent audit, not an official erratum,
a complete verification, or a quantum-hardware benchmark.

## Run

From the repository root, using Python 3.11 or later:

```sh
python -m pip install numpy
python experiments/verify_claims.py
```

The command executes five deterministic check groups and writes
`results/verification.json`. An optional alternative destination is accepted:

```sh
python experiments/verify_claims.py --output results/recheck.json
```

The experiment script depends only on the Python standard library and NumPy.
It uses double-precision calculations, exact trigonometric formulas,
eigendecomposition of a real symmetric 128-by-128 matrix, and FFT operations.
There is no random seed because there are no random inputs. The JSON records
the NumPy version. Last-digit differences across BLAS implementations are
expected; assertions allow numerical rounding and test substantial margins.

## 1. Spatial derivatives need not have conserved norm

**Location:** page 6, footnote 10 and the equality following Eq. (7).

Take the smooth, periodic, admissible velocity and initial field

\[
c=(\sin(2\pi y),0),\qquad f_0=\sin(2\pi x).
\]

The exact transported field is

\[
f(x,y,t)=\sin[2\pi(x-t\sin(2\pi y))].
\]

It satisfies the source's transverse-coefficient restriction. On the unit
two-torus,

\[
\|f(t)\|_2=1/\sqrt2,\qquad
\|\partial_yf(t)\|_2=2\pi^2|t|.
\]

The second identity follows by differentiating and integrating squared cosines;
the code independently checks the integrals by periodic quadrature. At time
zero, the vertical derivative is zero. At times 0.1 and 1 it has norm
1.9739208802 and 19.7392088022 respectively. The field norm stays constant.
Conservation of the transported scalar's norm does not imply conservation of
its derivative norms.

## 2. Diffusion commutator contains a missing mixed derivative

**Location:** page 6, the displayed coefficient `a'_g` following Eq. (8).

Set

\[
A=\partial_{xx},\quad
B=(1+a\sin(qx))\partial_{yy},\quad q=2\pi,
\]

and choose

\[
u_0=1+b\sin(mqx)\sin(qy),\quad 0<a,b<1,\quad m\ge2.
\]

Both diffusion coefficients are positive, smooth, periodic, and independent of
their own differentiation directions. The field is positive with nonzero mean.
The exact product rule gives

\[
[A,B]u=(\partial_{xx}\kappa_y)\partial_{yy}u
       +2(\partial_x\kappa_y)\partial_{xyy}u.
\]

The second term has no counterpart in the source's displayed coefficient.
Dividing the actual commutator norm by the retained triangle-bound expression
gives the exact ratio

\[
\frac{\|[A,B]u_0\|_2}
 {\|\partial_{xx}\kappa_y\|_\infty\|\partial_{yy}u_0\|_2}
=\sqrt{(4m^2+1)/2}.
\]

For `m=4`, `a=0.2`, `b=0.5`, the ratio is **5.7008771255**. The numerator
is 444.2538071129; the printed retained expression without its common
normalization and one-half factors is 77.9272728272. These values are verified
by periodic quadrature. The omitted term has norm 440.8232244439.

Normalization does not remove this counterexample. For self-adjoint real
`A` and `B`, their commutator is skew-adjoint, hence
`<u,[A,B]u>=0`. The derivative of normalization projects out the component
parallel to `u`; the commutator already has zero such component. The numerical
inner product is within `1e-10` of zero.

This algebra proves that the proposed commutator estimate cannot be retained
as written. It does **not** prove that a corrected, grid-independent estimate
with additional smoothness norms is impossible.

## 3. Actual normalized splitting error

To check that the omitted term matters in an actual evolution, the script
implements the source's `p=1` centered-first-derivative-squared discretization
on a 128-by-128 periodic grid. It uses the same positive coefficients and field
as experiment 2.

The constant field is stationary. The remaining single sine mode in `y` forms
an invariant subspace, so the two-dimensional system reduces *exactly* to

\[
\dot g=(A_N+B_N)g,\qquad
u_{ij}=1+g_i\sin(2\pi j/N).
\]

Here `A_N` has Fourier eigenvalues
`-[N sin(2pi k/N)]^2`, and `B_N` is the diagonal matrix
`-[N sin(2pi/N)]^2 [1+a sin(2pi x_i)]`.
The exact semidiscrete result is calculated by a symmetric eigendecomposition.
The split result applies `exp(h B_N) exp(h A_N)` repeatedly. Every comparison
uses the normalized fields, not just unnormalized vectors.

The source's displayed coefficient uses the continuum `u_yy` norm. Its maximum
is attained initially in this example, since the continuum single-mode equation
has a contractive heat operator plus a nonnegative potential. The script uses
that continuum norm, making the comparison conservative relative to replacing
it by the smaller discrete derivative norm.

| T | L | Normalized error | error L / T^2 | Printed a'_g | Ratio |
|---:|---:|---:|---:|---:|---:|
| 0.0002 | 64 | 1.1426216764e-7 | 182.81947 | 38.06196 | 4.80321 |
| 0.0002 | 128 | 5.7129740613e-8 | 182.81517 | 38.06196 | 4.80309 |
| 0.0002 | 256 | 2.8564534678e-8 | 182.81302 | 38.06196 | 4.80304 |
| 0.0002 | 512 | 1.4282183498e-8 | 182.81195 | 38.06196 | 4.80301 |
| 0.0005 | 64 | 5.8357078046e-7 | 149.39412 | 38.35096 | 3.89545 |
| 0.0005 | 512 | 7.2941144221e-8 | 149.38346 | 38.35096 | 3.89517 |

Errors halve when `L` doubles, supporting first-order splitting behavior. Their
leading coefficient substantially exceeds the displayed coefficient. This
contradicts the proposed bound if its higher-order remainder is interpreted
as `o(1/L)` at fixed `T`. Finite numerical observations do not prove the
asymptotic remainder assertion; the independent product-rule identity and
the small-time expansion supply the underlying analytic objection.

## 4. Extra checkerboard null modes and smooth consistency

**Location:** pages 3-4, the `D_j^2` spatial discretization in Eq. (4).

For an even periodic grid, `v_j=(-1)^j` is annihilated by every antisymmetric
centered first-derivative stencil. Squaring that stencil still annihilates it.
The standard three-point Laplacian instead maps it to `-4 v_j/h^2`.

For the tested 64-point grid, the centered first derivative and its square
give exactly zero on the checkerboard. The standard Laplacian has output
RMS 16384. Thus `1+b*(-1)^j` is a positive nonuniform stationary field for
the squared-centered stencil, although physical positive diffusion damps this
grid-scale modulation.

This is a structural limitation rather than a failure of convergence on fixed
smooth initial data. A checkerboard family changes its spatial frequency as
the grid is refined. To make that distinction explicit, the script also
checks a fixed smooth sine mode: eigenvalue errors converge at second order
for `p=1` and fourth order for `p=2`.

## 5. Contractivity needs a sign assumption

**Location:** page 2's mathematical coefficient assumptions and page 5,
footnote 8's claim of a contractive diffusion propagator.

The literal displayed smoothness and directional-independence assumptions
allow `kappa=-1`. Then the source's generator is `+D^2` and amplifies every
nonzero derivative mode. A 64-point, mode-4 example amplifies by
1.8218369625 over `T=0.001`.

This demonstrates the necessity of writing `kappa_j >= 0` for contractivity.
It is an assumption gap, not a claim that negative thermal conductivity is
physically intended by the authors.

## Limits

These checks do not establish an exhaustive list of errors, determine whether
the published conference version contains the same statements, disprove a
corrected vector-norm theorem, or measure a computational speedup. They test
specific formulas and structural properties of the supplied arXiv v1.
