# Resource accounting and operational comparison

[Model](model.md) · [Detection guarantee](conditional_detection.md) · [Processing robustness](processing_robustness.md)

The primary comparison fixes total mean **transmitted signal energy**. Calibration probes, source idlers, coherent storage, optical controls and measurements remain explicit resources. They are not converted into a wall-clock or complete-apparatus advantage. A separate fixed-width construction limits the coherent apparatus size and still gives a smaller strict transmitted-energy advantage.

## One collective block and local calibration

Write $`N`$ for the number of target-interrogating signal–idler pairs in a collective block. Every signal is transmitted, so the block uses mean signal photon number $`Nn`$ and source idler photon number $`Nn`$. There is no omitted phase-pilot stage: the passive receiver commands and final count statistics are independent of the unknown common target phase. All return heterodyne records, including atypical ones, enter the optical protocol and the proof.

The explicit separate channel-learning experiment uses $`q`$ vacuum probes and $`q`$ thermal probes of known occupation one. These probes never interrogate the target. They still require preparation, full-window memory calls and counting. Their total mean input photon number is $`q`$. They identify loss and added noise separately; the detector does not assume that the resulting estimates are correct. Every separate-calibration record therefore leaves the conditional detection bound unchanged.

| Resource | Detection block | Separate full-memory learning |
| --- | ---: | ---: |
| Target transmissions | $`N`$ | $`0`$ |
| Mean transmitted signal photons | $`Nn`$ | $`0`$ |
| Mean source idler photons | $`Nn`$ | $`0`$ |
| Other mean locally prepared photons | $`0`$ | $`q`$ |
| Gaussian memory calls over the full declared window | $`N`$ | $`2q`$ |
| Returned-mode heterodyne exposures | $`N`$ | $`0`$ |
| Idler/probe photon-counted mode exposures | $`N`$ | $`2q`$ |
| Count statistics needed by the decision | Bright count $`K`$ and aggregate dark count $`S`$ | Two probe-count sums for the estimates |
| Passive network | $`O(N)`$ two-mode mixing and phase controls | A matched storage/detection path |
| Coherent idler width for the collective implementation | $`N`$ modes | At most the parallel calibration width actually provisioned |
| Phase-learning trials | $`0`$ | $`0`$ |

An ideal multimode photon-number counter can aggregate the dark outputs. The theorem requires photon counting over all $`N`$ output modes, not $`N`$ independent detector instruments or individually retained dark records. Conversely, two count statistics do not mean that only two optical modes are measured.

If $`q=\lceil\sqrt N\rceil`$, total memory calls are $`T_N=N+2q`$ and total prepared photon number, excluding pump inefficiency and local oscillators, is $`2Nn+q`$. The detection exponent per total memory call is unchanged because $`N/T_N\to1`$. The local calibration energy also satisfies $`q/(Nn)\to0`$ for fixed $`n\gt 0`$. These limiting statements do not erase either finite cost or assert exponentially reliable separate estimates.

## Source energy and pumps

At frequencies $`\omega_S,\omega_I`$, the two source beams carry energies

**Equation (R1).**

```math
E_S=\hbar\omega_S Nn,
\qquad
E_I=\hbar\omega_I Nn.
```

For ideal three-wave down-conversion, a pump photon at $`\omega_P=\omega_S+\omega_I`$ creates one signal–idler pair. Mean converted source-pump energy is therefore

**Equation (R2).**

```math
E_{P,\mathrm{converted}}
=\hbar(\omega_S+\omega_I)Nn=E_S+E_I.
```

The source pump and the two output energies must not be counted twice in the same energy total. Actual incident pump energy is larger and depends on source efficiency, pulse duration, coupling and stabilization. Neither a TMSV occupation nor a squeezing parameter alone determines its wall-plug cost. Preparing the local thermal calibration probes has its own source and mean optical energy $`\hbar\omega_I q`$.

The correlation-to-displacement combiner is passive. Its ideal transformation creates no photons and has no receiver-parametric-amplifier pump depletion. Active phase shifters, switching, frequency conversion or memory controls in an implementation can consume substantial energy; their use is not made free by the word passive in the mathematical mode transformation.

Heterodyne reception requires a calibrated phase reference and a physical local-oscillator/readout implementation. Let $`E_{\mathrm{LO}}`$ denote its actual supplied optical and electronic energy. The theorem specifies ideal heterodyne measurement statistics and $`N`$ exposures; it does not derive $`E_{\mathrm{LO}}`$ from those statistics. Detector/readout energy $`E_{\mathrm{det}}`$, control energy $`E_{\mathrm{ctrl}}`$, cooling and processing energy $`E_{\mathrm{class}}`$ also remain separate. A full apparatus total would have to include these terms and a similarly specified classical implementation.

## Storage, timing and network size

The collective receiver stores the idlers until the return record is available, the commands have been calculated and the mode-combining network has run. A clean model is a parallel spatial or spectral block with equal full storage windows. If the full window is $`\tau_N`$, idler mode-time is $`N\tau_N`$ and coherent width is $`N`$. The same full-window channel bounds must include buffering, insertion loss and any modeled detection inefficiency. Identical phase-insensitive noise can be moved through the passive network exactly, as proved in [processing robustness](processing_robustness.md).

A serial implementation that stores early idlers much longer than later ones does not automatically realize the stationary identical channel. Likewise, a sequential running combiner can give its retained mode growing extra loss. Such devices require a separate analysis rather than a reinterpretation of $`\eta`$ as storage-only efficiency.

An ideal binary-tree combiner has $`O(N)`$ passive two-mode operations and $`O(\log N)`$ optical layers with suitable connectivity. Classical command latency and switching time precede or overlap these layers according to the actual architecture. No wall-clock advantage follows from an exponent per transmitted mode. The target round-trip time, available number of parallel modes, mode rate, detector bandwidth and control latency must be supplied for a time comparison.

The [finite-width protocol](processing_robustness.md#a-fixed-width-protocol-with-a-strict-advantage) fixes a block of $`L=\lceil2\times10^6/\kappa\rceil`$ modes and repeats it $`J`$ times. It has coherent width $`L`$, total target transmissions $`JL`$, and idler mode-time $`JL\tau_L`$. At fixed known rational $`\kappa`$, the asymptotic limit increases $`J`$ while storage quality is required only for this fixed apparatus. The width is very large and has not been optimized. The certified $`1.05`$ transmitted-energy factor is an existence result, not a practical crossover study.

Separate calibration may use $`q=\lceil\sqrt{JL}\rceil`$ probes of each brightness across this repeated-block experiment, each experiencing the same declared full-window channel. The ledger then contains $`JL+2q`$ memory calls, $`JL n`$ transmitted photons and $`2JL n+q`$ prepared photons. Calibration can be performed in a preliminary stage without assuming any favorable outcomes.

## Classical arithmetic and stored records

The optical weights require $`O(N)`$ norms and two-mode mixing parameters in a real-arithmetic model. Finite precision matters. The [explicit rounded construction](processing_robustness.md#finite-classical-records-and-controls) uses $`O(\log N)`$ bits per return-vector component and per passive command, giving $`O(N\log N)`$ classical record and command bits. Arithmetic and transcendental evaluation must be performed accurately enough to meet its deterministic error budget. Its finite coordinate range and small-norm exceptions have a total probability at most $`2e^{-0.19N}`$, included in the detection error bound; there is no uncharged probabilistic per-gate success assumption.

The count decision itself uses two integers. One can evaluate its binomial ratio using exact integer arithmetic:

**Equation (R3).**

```math
p_N(K,M)
=\frac{\binom{M-K+N-1}{N-1}}
{\binom{M+N-1}{N-1}}.
```

For the [dyadic decision variant](processing_robustness.md#an-exact-integer-decision-with-a-dyadic-cutoff), cross-multiply these integers against $`2^{\lceil N\kappa/13400\rceil}`$. The [reference implementation](../verification/receiver.py) uses this exact comparison. No logarithm or approximate threshold comparison is needed by the actual decision. The [reference implementation](../verification/receiver.py) cancels the binomial ratio into $`K`$ rational-product updates. Reduced integer operands have at most $`O(N+M+j_N)`$ bits, since the unreduced binomial coefficients are bounded by $`2^{N+M-1}`$. Thus each record has finite polynomial arithmetic cost; the negative-binomial total has mean $`Nm`$ and finite moments, giving finite expected bit storage and processing at fixed $`N`$. Photon counts are unbounded, so no deterministic finite register size holds for every record without an additional overflow rule. At bounded $`m`$, their mean total is $`Nm`$ and their generating function gives explicit exponential tails; expected bit storage and processing are finite. A physical implementation that truncates counts must charge and bound its overflow event on the same scale as detection. The theorem itself retains every count and does not silently discard an overflow record.

Aggregating repeated fixed-width blocks requires only a running count of positive block decisions. It adds $`O(J)`$ elementary decision updates and $`O(\log J)`$ bits beyond each block's optical-record computation. This reduces persistent classical storage but does not remove the block's optical or measurement costs.

## What the classical comparison establishes

The strong benchmark is a fixed classical mixture of coherent signals under the same total mean transmitted signal-photon budget. It can retain its preparation label, know the true target phase and use arbitrary global quantum reception. Its optimal symmetric-error exponent is $`\kappa nC_B`$ per mean-$`n`$ signal mode, with $`C_B=(\sqrt{B+1}-\sqrt B)^2`$. The result is not a comparison only with classical noise radar, heterodyne-only reception or a particular receiver circuit.

The ideal collective conditional detector certifies a $`\gt 2.2`$ transmitted-energy factor. Its finite-range, finite-control variant with exact dyadic decisions certifies $`\gt 2.17`$. At equal frequencies, charging both source beams doubles the prepared-photon budget. The latter collective mathematical limit therefore retains a factor $`\gt 1.085`$ against the **receiver-cost-relaxed** coherent benchmark given the same source output energy, with sublinear local calibration energy included asymptotically. This is a source preparation-energy comparison. It excludes incident-pump inefficiency, local oscillators, storage, control, detectors, cooling and processing, and hence does not establish complete-apparatus superiority.

For unequal frequencies, a transmitted-energy factor $`r`$ becomes $`r\omega_S/(\omega_S+\omega_I)`$ under this source-output-energy normalization. A high-frequency idler can remove that advantage. The fixed-width construction certifies only a $`\gt 1.05`$ transmitted-energy factor and consequently does not certify an improvement when equal-frequency source idlers are charged.

The strongest supported practical conclusion is therefore conditional: quantum illumination can retain a strict detection-reliability advantage with unknown, bounded full-window Gaussian memory noise and explicitly counted calibration and measurement resources. Whether an actual apparatus offers a better energy, time, size or monetary tradeoff requires a matched hardware model and measured parameters. No such apparatus crossover is claimed here.
