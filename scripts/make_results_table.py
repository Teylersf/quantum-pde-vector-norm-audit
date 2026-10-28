"""Generate the paper table from the actual checked numerical results."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "results/verification.json").read_text(encoding="utf-8"))
assert data["all_assertions_passed"]
rows = data["checks"]["normalized_semidiscrete_splitting"]["rows"]
lines = [
    r"\begin{table}[ht]",
    r"\centering\small",
    r"\begin{tabular}{rrrrrr}",
    r"\toprule",
    r"$T$ & $L$ & Normalized error & Error $L/T^2$ & Comparator & Ratio \\",
    r"\midrule",
]
for row in rows:
    lines.append(
        f'{row["T"]:.4g} & {row["steps"]} & '
        f'{row["normalized_L2_error"]:.4e} & '
        f'{row["measured_error_times_L_over_T_squared"]:.3f} & '
        f'{row["printed_a_g"]:.3f} & '
        f'{row["measured_to_printed_ratio"]:.3f}' + r" \\"
    )
lines += [
    r"\bottomrule\end{tabular}",
    r"\caption{Classical normalized splitting check: $128\times128$ grid,",
    r"$p=1$, $a=0.2$, $b=0.5$, $m=4$, using the sine variant",
    r"$u_0=1+b\sin(2\pi m x)\sin(2\pi y)$. This has the same",
    r"analytic norm ratio as the cosine example. The comparator reconstructs",
    r"the printed prefactor with the initial continuum derivative norm",
    r"and the semidiscrete final norm. Finite numerical evidence supplements,",
    r"rather than proves, the analytic coefficient objection.}",
    r"\end{table}",
]
(ROOT / "paper/results-table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("Generated paper/results-table.tex from checked results.")
