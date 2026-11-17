# Verification

From the repository root, run:

```bash
python3 verification/run_all.py
```

Python 3.10 or newer and its standard library suffice; no packages, data downloads,
random trials or experimental records are required. The repository verification
workflow repeats this complete suite. A scientific integration is accepted only
after the suite and that workflow pass at its source tree.

| Program | Evidence provided |
|---|---|
| `certify_constants.py` | Exact Fraction/Taylor inequalities for the ideal, finite-control, dyadic and fixed-width rate comparisons. Writes `conditional_memory_certificate.json`. |
| `check_count_laws.py` | Exact finite PGF convolutions, conditional tails and discrete false-alarm inequalities; selected phase-concentration vectors; deterministic finite-parameter probability sums with Chernoff truncation bounds. Writes `count_laws_report.json`. |
| `check_receiver.py` | Checks the integer detector independently against combinatorial conditional laws and exact false-alarm sums. |
| `receiver.py` | Reusable exact dyadic detector taking rational reflectivity and two observed photon-count integers. |
| `run_all.py` | Runs the scientific checks, validates local reader links and records the checked source hashes in `verification_report.json`. |

The analytical proofs cover all parameters in their stated domains. Finite
identity checks and selected numerical probabilities support those proofs;
they do not replace them. Numerical diagnostics explicitly state their double-
precision tolerance and omitted-tail bounds. Exact constant certificates use
rational arithmetic and do not rely on the displayed decimal approximations.

The optical model includes ideal heterodyne and photon-number measurements.
Finite passive command errors, record range, and dyadic decision arithmetic
are treated in [processing robustness](../science/processing_robustness.md).
No simulation here validates an experimental apparatus or complete energy cost.
