# State-dependent splitting errors for anisotropic transport and diffusion

**Counterexamples and a conditional corrected bound**

An independent, AI-assisted technical note auditing **arXiv:2603.08799v1** by
Julien Zylberman, Thibault Fredon, Nuno F. Loureiro, and Fabrice Debbasch.
Prepared with OpenAI Codex at the repository owner's request. **Not peer
reviewed; not an official erratum, a complete error census, or a quantum
speedup demonstration.** The original authors are not authors of this note
and have not endorsed it.

## Read

- **[New paper (PDF)](paper/main.pdf)**
- [LaTeX source](paper/main.tex)
- [Finding-by-finding audit ledger](audit/ledger.md)
- [Reproduction instructions and derivations](experiments/README.md)
- [Machine-readable numerical results](results/verification.json)
- [Source provenance](SOURCE.md)

## Main demonstrated findings

1. **Derivative conservation fails.** An allowed smooth periodic shear preserves
   the field's L2 norm while a derivative norm grows from zero.
2. **The diffusion prefactor omits mixed derivatives.** A strictly positive
   periodic example exceeds the printed commutator comparator by
   sqrt(65/2) = 5.700877... . Normalization preserves the leading discrepancy.
3. **The directional qubit error budget needs a dimension allocation.** Giving
   each direction a budget epsilon bounds the sum by d epsilon, not epsilon.

Additional findings distinguish missing positivity and regularity hypotheses,
normalized-sampling issues, nonuniform remainder concerns, checkerboard
stationary modes, gate/readout costs, and editorial ambiguities. They are not
all classified as false theorems.

The paper proves a **conditional autonomous finite-grid theorem** using an
exact double-integral defect identity. Under an explicit grid-uniform
commutator bound K on intermediate split states, the unnormalized error is
at most K T²/(2L). A normalized-state corollary includes a final-norm lower
bound. This does not prove the original time-dependent PDE theorem or a
complete replacement quantum algorithm.

## Reproduce

Python 3.11 or later and NumPy:

~~~sh
python -m pip install -r requirements.txt
python experiments/verify_claims.py
python experiments/verify_repaired_bound.py
python scripts/make_results_table.py
~~~

The first experiment executes five check groups. The second checks the
replacement theorem on independent contractive and unitary matrix examples.
Assertions test substantive invariants and error bounds. Numerical results
are classical corroboration, not substitutes for the proofs.

Build the paper with [Tectonic](https://tectonic-typesetting.github.io/):

~~~sh
cd paper
tectonic --keep-logs main.tex
~~~

The checked build used Tectonic 0.17.0. The scripts regenerate the result
table from JSON. Floating-point last digits can vary with NumPy/BLAS.

## Scope and publication

Publication date: **28 October 2026**. Published on GitHub by **Teylersf**.
The audited arXiv v1 PDF has nine pages. Its full source text is not
redistributed here. Its public record links a conference version of record;
only that version's public metadata was checked, not its full chapter text.
See [SOURCE.md](SOURCE.md) for exact source identification.

No claim is made to have found every error, to priority for standard
splitting identities, or to having disproved all mesh-independent
vector-norm estimates. This repository makes no assertion about misconduct.
Future corrections should identify the source version, exact equation,
and a derivation or reproducible counterexample.
