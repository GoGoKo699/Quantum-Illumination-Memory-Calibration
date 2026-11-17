# Scientific route

An unknown memory affects both the correlations used to detect a target and the
noise against which those correlations are judged. Accurately calibrating a
memory on typical runs does not guarantee exponentially reliable detection.
This project separates three tasks: identifying the channel, certifying its
parameters at an exponential confidence level, and reliably detecting a target.

Start with [the model](model.md). At one input brightness the stored idler gives
only $`m=\eta n+\nu`$, so loss and added noise cannot be identified separately
under target absence. Charged vacuum and nonzero-brightness local probes can
identify them. Nevertheless, the [calibration limits](calibration_limits.md)
show that exponentially reliable added-noise certification requires a linear
number of memory calls even with arbitrarily energetic adaptive quantum probes.
A predetermined one-output OPA detector can inherit that cost because a noise
shift exactly reproduces its target signal.

The positive construction changes what is measured. An established
correlation-to-displacement receiver concentrates the target correlation in one
idler output. Keep and count its other outputs too. The [conditional detector](conditional_detection.md)
uses their total together with the bright count to obtain an exact null law
independent of the unknown memory brightness. Its complete finite-sample proof
includes misleading reference records and all return heterodyne outcomes.
No estimate of the common target phase is required.

| Scientific question | Authoritative page |
|---|---|
| What is fixed, unknown, measured and charged? | [Model](model.md) |
| What does the optical receiver produce, and why is its conditional test valid? | [Exact conditional detection](conditional_detection.md) |
| What happens to rounded controls, common processing loss and coherent width? | [Processing robustness](processing_robustness.md) |
| Why can separate calibration be expensive even with bright quantum probes? | [Calibration limits](calibration_limits.md) |
| How strong is the classical alternative? | [Classical benchmark](classical_benchmark.md) |
| Which energy and apparatus comparisons are supported? | [Resources](resources.md) |
| Which ingredients and receivers are inherited? | [Related work](../references/RELATED_WORK.md) |
| Which constants and finite laws can be reproduced? | [Verification](../verification/README.md) |

The benchmark gives the coherent-mixture receiver its preparation label and the
true phase, and allows global reception and arbitrary mean-energy randomization.
The resulting separation concerns transmitted signal energy. Source-idler,
calibration, storage, measurement, pump and processing costs retain their own
entries in the resource account.
