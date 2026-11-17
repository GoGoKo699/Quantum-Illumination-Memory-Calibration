# Quantum Illumination Memory Calibration

**Unknown idler memory need not make calibration mistakes control quantum target-detection reliability.** An exact conditional detector reuses the outputs of an established correlation-to-displacement receiver as an internal noise reference. It retains a strict advantage over phase-informed coherent mixtures with arbitrary global reception, while counting all calibration, preparation, storage and measurement resources.

At one source brightness, target-absent data identify only the combined memory occupation. Separate loss and added noise require additional probes. Exponentially reliable noise certification can be costly even with arbitrarily bright quantum calibration. The detector below avoids assuming that those estimates are correct.

## Main results

Each of $`N`$ signal–idler pairs has occupation $`n`$ per mode. The return background is $`B`$, power reflectivity is $`\kappa`$, and the common target phase is unknown. The stationary independent Gaussian idler memory has unknown power attenuation $`\eta`$ and output-referred added occupation $`\nu`$.

The explicit separation regime is

```math
n=10^{-3},\qquad B=10,\qquad
\eta\in[0.9,1],\qquad \nu\in[0,10^{-3}],\qquad
0<\kappa\le0.1.
```

| Result | What is established |
|---|---|
| Exact internal reference | The total idler count has the same negative-binomial law under both target hypotheses. Conditioning on this total removes unknown memory brightness from the null bright-count law. |
| Finite-sample detection | For $`N\ge20`$, an explicit test has worst-case symmetric risk $`R_N\le(3/2)e^{-Nr}`$, with $`r>2.2\kappa nC_B`$ and $`C_B=(\sqrt{B+1}-\sqrt B)^2`$. Every return and reference record is included. |
| Finite controls and exact arithmetic | A bounded-range return record, rounded passive commands and an integer-only decision retain a certified rate greater than $`2.17\kappa nC_B`$, with the exceptional-record probabilities charged. |
| Fixed coherent width | Repeating blocks of $`L=\lceil2\times10^6/\kappa\rceil`$ modes gives a rate greater than $`1.05\kappa nC_B`$ as the number of blocks grows. The very large width is explicit. |
| Calibration obstruction | Two positive added-noise channels have a common channel component. Arbitrary adaptive quantum calibration retains exponentially significant ambiguity after $`K`$ calls, independently of probe energy. A specified confounded one-output receiver has zero uniform detection exponent when $`K=o(N)`$. |

The comparator's exact exponent is $`\kappa nC_B`$ at the same transmitted signal energy. It receives the true target phase and preparation label, and may use arbitrary global reception and energy randomization under the mean budget. The quantum receiver makes no target-phase estimate. These are certified lower bounds on achievable rates, rather than claims of optimal quantum reception or an ordering of actual finite-sample errors at every $`N`$.

## The detector

Heterodyne the returns and use their recorded complex amplitudes to combine the stored idlers. Count the concentrated bright output, $`K`$, and the sum $`S`$ of all remaining output counts. With $`M=K+S`$, the conditional null tail is exactly

```math
p_N(K,M)=
\frac{\binom{M-K+N-1}{N-1}}
{\binom{M+N-1}{N-1}}.
```

It contains no memory parameter. Reject target absence when this tail is below the declared cutoff. The proof integrates the random return norm exactly and bounds misleading total-count records; it does not substitute typical calibration or phase-learning outcomes.

Correlation-to-displacement processing and phase-insensitive bright-output counting are inherited from the CtoD literature. The contribution here is the conditional unknown-memory reliability guarantee, its processing/resource boundaries, and the contrasting calibration obstruction. See [related work](references/RELATED_WORK.md).

## Read the science

Start with the [connected scientific route](science/README.md), or follow a direct question.

| Question | Read |
|---|---|
| What is unknown, identifiable and charged? | [Model](science/model.md) |
| Why does the conditional test work, including rare records? | [Exact detection theorem](science/conditional_detection.md) |
| Which processing errors and finite-width implementations are covered? | [Processing robustness](science/processing_robustness.md) |
| Why can separate calibration fail despite bright quantum probes? | [Calibration limits](science/calibration_limits.md) |
| How strong is the classical receiver and transmitter class? | [Classical benchmark](science/classical_benchmark.md) |
| Which energy, storage, pump and processing comparisons are justified? | [Resource account](science/resources.md) |

## Reproduce the checks

```bash
python3 verification/run_all.py
```

The suite uses Python's standard library. It checks the rate constants with exact rational bounds, verifies finite count identities and conditional calibration, checks the exact integer detector, and evaluates selected finite-parameter probabilities with explicit truncation bounds. [Verification instructions](verification/README.md) separate these checks from the analytical all-parameter proofs.

## Scope

The memory is a stationary independent phase-insensitive Gaussian channel, common to both hypotheses. The background, source brightness and reflectivity are known. The target phase stays constant across each coherent block. The memory bounds cover the complete storage and modeled processing window, including uniform losses and detection efficiency. Controls depend on return records and independent local calibration, without measuring payload idlers to select a favorable output.

Nonuniform loss, unmodeled detector response, mode mismatch and parameter drift require additional analysis. The fixed-width construction still needs twenty million coherent modes at $`\kappa=0.1`$. All idler outputs are measured; two sufficient count sums do not mean that only two optical modes are used.

The primary advantage concerns transmitted energy. Charging equal-frequency source idlers still leaves a smaller asymptotic source-output-energy advantage for the collective construction, including sublinear local calibration. Pump inefficiency, local oscillators, storage, controls, readout, cooling and classical processing remain additional costs. A complete-apparatus or wall-clock advantage is not established.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
