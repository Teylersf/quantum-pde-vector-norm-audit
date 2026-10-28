"""Record artifact hashes and build/test provenance without private paths."""
import hashlib
import json
import platform
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


if __name__ == "__main__":
    first = json.loads((ROOT / "results/verification.json").read_text())
    second = json.loads((ROOT / "results/repaired-bound.json").read_text())
    assert first["all_assertions_passed"] and second["all_assertions_passed"]
    files = ["paper/main.tex", "paper/main.pdf", "paper/results-table.tex",
             "audit/ledger.md", "experiments/verify_claims.py",
             "experiments/verify_repaired_bound.py", "results/verification.json",
             "results/repaired-bound.json"]
    data = {
        "publication_date": "2026-10-28",
        "status": "AI-assisted technical note; not peer reviewed; non-exhaustive audit",
        "source_version": "arXiv:2603.08799v1",
        "source_sha256": "d03a710413b32ac622700adcfbaa9c3b8604ab9db00e45c348ea06c3d4be8988",
        "source_pdf_pages": 9,
        "new_paper_pdf_pages": 9,
        "build": {"compiler": "Tectonic 0.17.0",
                  "python": platform.python_version(), "numpy": np.__version__},
        "checks": {"source_claim_groups": len(first["checks"]),
                   "replacement_bound_examples": len(second["checks"]),
                   "all_assertions_passed": True},
        "artifacts": {name: {"sha256": sha(ROOT / name),
                             "bytes": (ROOT / name).stat().st_size}
                      for name in files},
    }
    (ROOT / "results/artifact-manifest.json").write_text(
        json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print("Recorded artifact hashes and successful check provenance.")
