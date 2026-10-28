# Audit ledger: arXiv:2603.08799v1

Scope: all nine pages of the supplied arXiv v1, including equations,
footnotes, figure, and references. This is a systematic audit, **not a
guarantee of finding every error**. The full conference chapter and later
related publications were not audited.

Categories deliberately distinguish demonstrated errors from missing proofs,
implementation qualifications, limitations, and editorial issues. Numbered
items are findings to assess, not a count of independently disproved theorems.
Derivations are in the new paper; experiments are linked below.

| ID | Source location | Classification | Finding and repair |
|---|---|---|---|
| E1 | p6, footnote10; equality below Eq7 | Demonstrated error | Coordinate derivative L2 norms are not conserved by all permitted flows. Allowed periodic shear creates a y derivative from an initially y-independent field. Replace by evolved derivative suprema or coefficient-dependent Sobolev energy estimates. |
| E2 | p6, displayed a'_g below Eq8 | Demonstrated error | The diffusion commutator bound omits two mixed third-derivative terms. Positive coefficients and positive initial data give a norm ratio sqrt(65/2)>5.7 relative to the retained bound. The defect survives normalization. Add the complete commutator and suitable intermediate-state regularity. |
| E3 | p5, directional n_j prescription | Demonstrated error in stated budget guarantee | Giving each directional contribution epsilon only proves a total at most d epsilon from the displayed sum. Allocate epsilon_j summing to epsilon. The clipped/nonzero-coefficient formula in the new note also handles practical indexing edge cases. |
| H1 | p2 coefficient hypotheses; p5 footnote8 | Missing explicit hypothesis | Contraction requires kappa_j>=0. Negative constant kappa meets the written smoothness/coordinate restrictions but amplifies modes. Thermal conductivity may physically imply the intended sign; write it explicitly. |
| L1 | pp3-4, square D_j² in Eq4 | Discretization limitation | An even-grid checkerboard is annihilated by every antisymmetric centered first derivative, and hence by its square. At least 2^d parity modes remain stationary in d dimensions. This is not a counterexample to convergence on fixed smooth data. |
| H2 | p5, diffusion spatial-error discussion | Regularity/proof gap | The direct residual estimate for the squared stencil needs control through order 2p+2, while the text refers to 2p+1. For p1 the leading residual is h² u''''/3. A weaker smoothing-based global theorem would need a separate proof. |
| H3 | p5, normalized f state and residual equation | Normalization/proof gap | A sampled continuum solution need not have exactly time-invariant quadrature norm. Differentiating an instantaneously normalized sample adds a normalization derivative. Use fixed-normalizer samples then apply a normalization lemma, or keep the extra term. |
| H4 | pp5-7, normalized diffusion and mean estimate | Normalization clarification | Separate raw PDE fields from unit amplitude states. The normalized error has a final-norm denominator. The mean lower bound requires absolute value and consistent initial scaling. The nonzero-mean condition IS stated on p7; it is not wholly absent. Mean-zero data merely fall outside that particular lower-bound argument. |
| H5 | pp6-7, remainders r_alpha and r'_alpha | Uniformity/proof gap | Higher-order at each fixed grid does not imply a remainder uniform in grid size. Bound exact defects on partial split trajectories or supply uniform higher-commutator estimates. |
| H6 | p7, L=O(T²/epsilon) | Time-dependence qualification | The prefactor contains evolved derivative norms and coefficient bounds, which can depend on T. Mesh independence alone does not establish polynomial dependence on T. |
| Q1 | abstract; pp6-7, 4^n and16^n comparison | Comparator qualification | Those factors compare against a particular crude product-of-operator-norm estimate. Basic smooth-coefficient commutator cancellations already improve the upper bounds to O(M_axis) and O(M_axis³). These are not universal tight quantum runtime speedups. Constant autonomous coefficients commute exactly. |
| Q2 | p4, phrase describing unitary factors; Eq5 diffusion | Wording and implementation gap | Diffusion factors are nonunitary contractions, as the source acknowledges elsewhere. A realization and its postselection/amplification/normalization costs must be specified. This does not mean nonunitary quantum implementation is impossible. |
| Q3 | pp3-4, efficient state/diagonal synthesis claims | Complexity qualification | Differentiability alone is not a uniform gate-complexity bound. Specify representation, coefficient access, approximation sparsity, accuracy, and parameter dependence. The finite-difference symbol's amplitude grows with refinement; it is the unitary exponential, not the fixed-stencil symbol itself, that can gain oscillations. |
| Q4 | p5, observables and point values | Readout qualification | A fixed expectation is invariant to global phase; signed field values are not. A projector gives normalized squared amplitude. Specify a reference/control protocol, phase convention, norm recovery, and measurement costs for signed amplitude or raw field recovery. |
| T1 | p2, dyadic coordinate definition | Editorial error | A fractional x_j=sum q_k/2^(k+1) belongs to {r/2^n_j}, not the displayed integer set. Separate spatial coordinates and register labels. |
| T2 | abstract versus p2; norm notation | Editorial ambiguity | Distinguish n per dimension from total sum n_j; distinguish grid cardinality from normalization constants; define the discrete 2,N norm convention. |
| T3 | p4, product in Eq6 | Editorial ambiguity | Specify chronological order of the time-step product. The source specifies a directional product order but the time product convention should also be explicit. |
| T4 | p6, a'_s comparison | Likely typographical error | The diffusion comparison uses an unprimed a_g in a place expected to contain a'_g. Correct the prime consistently. |
| T5 | p7, derivative/norm limit display | Likely typographical error | A second derivative in the preceding numerator becomes a first derivative in the displayed continuum-limit expression. Preserve the intended derivative order. |

## What remains valid

- With the transverse-coefficient assumption, the convection generator has
  the correct sign and is skew-Hermitian under periodic centered differences.
- Per-axis QFT diagonalization works in the mixed position/frequency basis
  permitted by that assumption.
- Positive diffusion coefficients make the directional factors contractive.
- Conservation of the field L2 norm for divergence-free transport is valid;
  conservation of every derivative norm does not follow.
- First-order splitting convergence can survive a wrong leading coefficient.
- Vector-norm analysis can still yield mesh-independent bounds with appropriate
  regularity, normalization, implementation, and uniformity hypotheses.

## Evidence

- [New paper: formulas, counterexamples, proof](../paper/main.pdf)
- [Five reproducible check groups](../experiments/verify_claims.py)
- [Experiment derivations and limits](../experiments/README.md)
- [Actual check results](../results/verification.json)
- [Independent checks of the replacement matrix bound](../experiments/verify_repaired_bound.py)
- [Replacement-bound check results](../results/repaired-bound.json)

Numerical tests are corroboration, not proofs of an end-to-end algorithm or
an exhaustive audit. No allegation about author intent or misconduct is made.
