# From Gaussian optics to detection with an unknown memory

[Learning route](README.md) · [Thirty milestones](milestones.md) · [Scientific route](../science/README.md)

A quantum-illumination source creates correlated signal–idler pairs. The signals interrogate a noisy target region; the idlers wait in a memory. A weak reflected signal can leave a useful correlation even when the return looks overwhelmingly thermal. The difficulty here is that the memory's attenuation and added noise are unknown. A detector must not silently treat an unreliable calibration estimate as the true noise level.

The project resolves that difficulty by changing the statistical reference. An established receiver concentrates the correlation into one idler output. The other outputs are kept and counted too. Conditioning on their total with the bright output produces a null distribution that contains no unknown memory brightness. The optical processing is Gaussian; the photon-count decision is not.

## The selected source and a short route through it

The educational anchor is Christian Weedbrook and coauthors, [*Gaussian Quantum Information*, Reviews of Modern Physics 84, 621–669 (2012)](https://doi.org/10.1103/RevModPhys.84.621). The section and equation pointers below refer specifically to the [14 October 2011 manuscript, arXiv:1110.3234v1](https://arxiv.org/html/1110.3234v1). Its linked HTML numbers subsections as II.2.1, for example; use the accompanying titles if another edition displays lettered subsections.

| Source location | Use in this project |
| --- | --- |
| I.4; II.1, Eqs. (6)–(7); II.1.1, Eq. (15) | Quadrature and covariance conventions |
| II.2.1, Eq. (27) | Thermal photon-count law |
| II.2.7, Eqs. (41)–(42) | Signal–idler source |
| II.2.6, Eqs. (37)–(38); II.3.2 | Passive mode mixing |
| II.5.2–II.5.3, Eq. (65) | Heterodyne conditioning |
| II.5.4 | Photon-number measurement |
| III.1.1 and III.1.4 | Decision error and collective reception |
| V.1, Eqs. (108)–(109); V.2 | Gaussian memory channel |
| V.7, including Fig. 4 | Signal–idler channel discrimination |

The source supplies the Gaussian machinery. The unknown-memory identifiability argument, conditional count test, calibration obstruction and certified resource comparisons are developed in this repository. Correlation-to-displacement receiver attribution is given separately in [related work](../references/RELATED_WORK.md).

## 1. Translate the units before using a covariance matrix

The repository primarily uses occupation numbers: $`n=\langle a^\dagger a\rangle`$ means mean photons in a mode. Quadrature covariance and photon occupation are related quantities, rather than interchangeable units.

Use the anchor's quadratures

```math
q=a+a^\dagger,\qquad p=i(a^\dagger-a),\qquad
[q,p]=2i,\qquad a=\frac{q+ip}{2}.
```

Then

```math
a^\dagger a=\frac{q^2+p^2-2}{4}.
```

For a zero-mean thermal mode of occupation $`x`$, the covariance is $`(2x+1)I_2`$. The vacuum has covariance $`I_2`$ and occupation zero. A coherent displacement $`\alpha`$ changes the mean to $`(2\mathrm{Re}\alpha,2\mathrm{Im}\alpha)`$ and adds $`|\alpha|^2`$ photons.

| Quantity | Covariance notation used in the bridge | Occupation notation in the project |
| --- | --- | --- |
| Thermal mode | $`\Gamma=(2x+1)I_2`$ | $`x`$ photons |
| Vacuum | $`\Gamma=I_2`$ | $`x=0`$ |
| Displaced thermal mode | Mean $`(2\mathrm{Re}\alpha,2\mathrm{Im}\alpha)`$, covariance $`(2x+1)I_2`$ | Residual occupation $`x`$, displacement energy $`|\alpha|^2`$ |
| Symmetric EPR variance parameter in source Eq. (42) | Rename it $`v_{\mathrm{EPR}}=2n+1`$ | Pair occupation $`n`$ |
| Added memory noise here | Adds $`2\nu I_2`$ to quadrature covariance | Adds $`\nu`$ output photons |

The source's EPR variance symbol must not be confused with this project's $`\nu`$, which means added memory occupation. Likewise, the source's channel-noise matrix is not the number $`N`$ of signal–idler pairs.

If quadratures with commutator $`i`$ are preferred, divide both $`q`$ and $`p`$ by $`\sqrt2`$ and divide the covariance by two. A thermal covariance then becomes $`(x+1/2)I_2`$. The occupation $`x`$ and the experiment do not change. These are dimensionless quadrature conventions; physical energies still use $`\hbar\omega`$. The repository's error exponents use natural logarithms.

## 2. Build the pair, target and memory

Choose the pair's phase convention so its correlation is positive real. With $`Z=\mathrm{diag}(1,-1)`$, its covariance is

```math
\Gamma_{SI}=
\begin{pmatrix}
(2n+1)I_2&2\sqrt{n(n+1)}Z\\
2\sqrt{n(n+1)}Z&(2n+1)I_2
\end{pmatrix}.
```

Thus each marginal is thermal, but the two modes have correlation $`\langle a_Sa_I\rangle=\sqrt{n(n+1)}`$. A local phase change accounts for a different sign convention in a source's squeezed-state expansion.

The target-absent return is thermal of occupation $`B`$. With a target, its occupation is $`B+\kappa n`$, and its phase-sensitive correlation with the stored idler is

```math
\langle a_Ra_{I,\mathrm{out}}\rangle
=e^{i\theta}\sqrt{\eta\kappa n(n+1)}.
```

The target phase $`\theta`$ is constant across a coherent block but unknown. The matched-background convention makes vacuum illumination produce the same return under both hypotheses; background removal is not a free target signature.

The memory is attenuation into vacuum followed by independent circular Gaussian displacement. In the bridge's covariance units,

```math
\Gamma\longmapsto\eta\Gamma+(1-\eta+2\nu)I_2.
```

For a thermal input this immediately gives

```math
(2n+1)I_2\longmapsto(2m+1)I_2,
\qquad m=\eta n+\nu.
```

The same fixed unknown $`\eta,\nu`$ apply to every memory use and under both target hypotheses. The environments are independent. The numerical bounds must cover the complete storage and modeled processing window, including any uniform insertion loss and modeled detection inefficiency.

### Why the two memory parameters are not automatically learnable

Under absence, the entire return–idler state is a product of thermal states of occupations $`B`$ and $`m`$. It contains $`m`$ but no separate record of $`\eta`$ and $`\nu`$.

For example, at $`n=0.001`$, the two memories

```math
(\eta,\nu)=(0.9,0.001)
\quad\hbox{and}\quad
(\eta,\nu)=(1,0.0009)
```

both give $`m=0.0019`$. They produce identical target-absent return–idler states, even for a global quantum measurement. More observations at this one brightness cannot repair that exact ambiguity.

Separate local probes can. Vacuum input has output mean $`\nu`$; a thermal input of occupation one has output mean $`\eta+\nu`$. Their count means identify the two parameters. These are additional prepared modes, memory calls and measurements, with additional energy. Consistency of those estimates does not imply exponentially reliable calibration on the target detector's error scale.

## 3. Heterodyne conditioning supplies the useful displacement

Put

```math
c^2=\eta\kappa n(n+1),\qquad
V=B+\kappa n+1,\qquad
A=\frac{c^2}{V},\qquad e=m-A.
```

The symbol $`V`$ here is a scalar complex heterodyne variance, not a quadrature covariance matrix. The return heterodyne outcome $`z`$ has density $`e^{-|z|^2/V}/(\pi V)`$ under presence.

The anchor's heterodyne conditioning formula makes the residual idler covariance transparent. Before measurement, the idler covariance block is $`(2m+1)I_2`$, the return block is $`[2(B+\kappa n)+1]I_2`$, and the cross block $`C_\theta`$ satisfies $`C_\theta C_\theta^T=4c^2I_2`$. Therefore

```math
\begin{aligned}
\Gamma_{I\mid z}
&=(2m+1)I_2-
C_\theta\bigl([2(B+\kappa n)+1]I_2+I_2\bigr)^{-1}C_\theta^T\\
&=(2m+1)I_2-\frac{2c^2}{B+\kappa n+1}I_2\\
&=(2e+1)I_2.
\end{aligned}
```

The extra identity matrix is the heterodyne measurement contribution. Losing it would give the wrong residual noise and the wrong detection guarantee.

The conditional idler is displaced by

```math
d_j=e^{i\theta}\frac{c z_j^*}{V}.
```

The crucial structure is shared across all pairs: the displacement vector is one unknown common phase times the conjugate of the recorded return vector.

## 4. Concentrate the correlation and retain the other outputs

For $`z=(z_1,\ldots,z_N)\ne0`$, choose a passive combiner with first row $`w_j=z_j/\Vertz\Vert`$. Its first displacement is

```math
\sum_{j=1}^N w_jd_j
=e^{i\theta}\frac{c\Vertz\Vert}{V}.
```

All orthogonal outputs have zero displacement in the ideal construction. Because every conditional thermal covariance is the same, passive mixing leaves a product thermal covariance. There is one displaced thermal bright output and $`N-1`$ undisplaced thermal outputs of residual occupation $`e`$.

The controls need the return record, but need no estimate of $`\eta,\nu`$ or $`\theta`$. An arbitrary fixed unitary is declared at $`z=0`$, a probability-zero record. Photon counting removes the remaining common phase from the measurement probabilities exactly. There is no phase-estimator success event to assume.

Count the bright output as $`K`$ and sum every other output count as $`S`$. This project keeps those orthogonal outputs as a statistical reference. Keeping two count sums does not mean that only two optical modes are measured.

## 5. Move from Gaussian states to exact count laws

A thermal mode of occupation $`x`$ produces a geometric count,

```math
\Pr(K=k)=\frac{x^k}{(1+x)^{k+1}},\qquad k=0,1,2,\ldots.
```

The sum of $`r`$ independent such counts has a negative-binomial distribution, denoted $`\mathrm{NB}(r,x)`$. Under target absence, all $`N`$ counted idler outputs are independent geometric counts of mean $`m`$.

Under presence, the bright displacement depends on the random return norm. That norm must be integrated, not replaced by its typical value. Define $`d_x(t)=1+x(1-t)`$. The exact result is

```math
\mathbb E_1[t^K]=\frac{d_e(t)^{N-1}}{d_m(t)^N},
\qquad S\sim\mathrm{NB}(N-1,e),\qquad K\perp S.
```

Multiplying the generating functions gives a particularly useful cancellation:

```math
M=K+S\sim\mathrm{NB}(N,m)
\qquad\hbox{under both hypotheses}.
```

The total $`M`$ estimates the actual memory brightness without a target-dependent bias. The dark sum $`S`$ alone has a different mean under presence and is not such a reference. A large total count can still be misleading for the target decision; the theorem explicitly bounds that event.

## 6. Condition away the unknown null brightness

Under absence, a particular allocation $`(k_1,\ldots,k_N)`$ with total $`M`$ has probability

```math
\frac{m^M}{(1+m)^{M+N}}.
```

It is the same for every allocation with that total. Once $`M`$ is specified, all $`\binom{M+N-1}{N-1}`$ allocations are equally likely, whatever the unknown $`m`$. Counting the allocations whose bright count is at least the observed $`K`$ gives

```math
p_N(K,M)=\Pr_0(K'\ge K\mid M)
=\frac{\binom{M-K+N-1}{N-1}}
{\binom{M+N-1}{N-1}}.
```

For any cutoff $`\epsilon`$, rejecting absence when $`p_N\le\epsilon`$ has false-alarm probability at most $`\epsilon`$, conditionally on every total and hence unconditionally. This is a discrete tail probability; it can be conservative rather than equal to the cutoff. No estimated memory value enters its null law.

### A complete tiny count example

Take $`N=4`$ outputs. Suppose the bright count is $`K=2`$ and the dark counts are $`(1,0,0)`$, so $`S=1`$ and $`M=3`$. There are $`\binom63=20`$ null allocations of three photons among four modes. Bright count at least two occurs in four: three allocations with bright count two, and one with bright count three. Thus

```math
p_4(2,3)=\frac{\binom43}{\binom63}
=\frac4{20}=\frac15.
```

At an illustrative cutoff $`1/10`$, that record does not reject absence. If instead the bright count is three and all dark counts are zero, the total is still three but

```math
p_4(3,3)=\frac{\binom33}{\binom63}=
\frac1{20}\le\frac1{10}.
```

That record does reject. Given this total, the actual false-alarm probability of the illustrative rule is $`1/20`$, below the declared $`1/10`$. The reference concerns where the photons appeared, not only how many appeared.

This four-mode example illustrates the exact counting law. The uniform numerical advantage theorem below requires $`N\ge20`$ and its specified physical parameter box; the example is not a numerical instance of that theorem.

## 7. Reliability requires the rare records too

A detector can look excellent after replacing the return norm and memory estimate by their usual values while still fail on exponentially significant exceptional records. Here the proof retains the exact return-norm distribution and separates a miss into two events: an excessively large total idler count, or an insufficiently large bright count. Exact negative-binomial and generating-function bounds cover both.

In the regime

```math
n=10^{-3},\qquad B=10,\qquad
\eta\in[0.9,1],\qquad \nu\in[0,10^{-3}],\qquad
0\lt \kappa\le0.1,
```

the ideal collective rule has an explicit positive rate $`r`$ such that, for $`N\ge20`$,

```math
R_N\le\frac32e^{-Nr},\qquad
r\gt 2.2\,\kappa nC_B,\qquad
C_B=(\sqrt{B+1}-\sqrt B)^2.
```

The risk maximizes the symmetric error over the unknown memory and common target phase. These are a finite-sample upper bound and a certified achievable rate, not an exact optimum-exponent formula.

The comparator is unusually strong: fixed mixtures of coherent signals at the same total mean transmitted signal energy, arbitrary energy randomization, the preparation label and true phase supplied to the receiver, and arbitrary global reception. Its optimum exponent is $`\kappa nC_B`$. The proof does not compare only against coherent heterodyne reception or a particular classical radar.

| Supported receiver variant | Certified transmitted-energy rate comparison | Limit and resource qualification |
| --- | --- | --- |
| Ideal collective block | $`r\gt 2.2\kappa nC_B`$ | Increasing coherent block size, exact declared optical model |
| Finite return range and passive commands, exact integer decision | $`c_d\gt 2.17\kappa nC_B`$ | Known rational $`\kappa`$; exceptional return records are charged; ideal heterodyne and modeled photon-count response remain assumptions |
| Repeated fixed-width apparatus | Rate $`\gt 1.05\kappa nC_B`$ | $`J\to\infty`$ at fixed $`L=\lceil2\times10^6/\kappa\rceil`$ modes per block; width is twenty million at $`\kappa=0.1`$ |

The finite-control constants and the fixed-width rate belong to distinct constructions. The fixed-width result does not inherit the factor $`2.2`$, and its factor $`1.05`$ does not certify an advantage after charging equal-frequency source idlers as well as signals. The [processing proof](../science/processing_robustness.md) states the exact bounds and limiting orders.

## 8. Why a bright calibration probe is not always a substitute for more calls

The detector's conditional reference avoids a parameter-certification assumption. It does not prove that the memory itself can be certified cheaply.

For two strictly positive added-noise values at the same fixed attenuation, the circular Gaussian displacement densities overlap. Their common part defines a channel that occurs with a positive common weight $`\zeta`$ under either noise value. In any adaptive $`K_{\mathrm{cal}}`$-call quantum calibration strategy, the branch that uses this common part on every call has weight $`\zeta^{K_{\mathrm{cal}}}`$ and gives identical accessible states. Consequently even the optimal binary calibration error is at least $`\zeta^{K_{\mathrm{cal}}}/2`$, regardless of probe energy or ancillary systems.

Consistent estimation with a growing sublinear call count remains possible. Uniform error $`e^{-cN}`$ for distinguishing fixed positive noise values requires a call count proportional to $`N`$. A specified frozen one-output OPA detector can inherit that cost because a change in memory noise exactly imitates its target-induced count shift. This obstruction is measurement-specific; the conditional CtoD detector escapes that confounding. The [calibration limits](../science/calibration_limits.md) prove the general calibration statement and the restricted detection consequence separately.

## 9. Keep the full resource ledger beside the advantage

| Resource | One collective block, with separate channel learning if used |
| --- | --- |
| Target signals and mean transmitted photons | $`N`$ and $`Nn`$ |
| Source idlers and their mean photons | $`N`$ and $`Nn`$ |
| Separate vacuum/occupation-one probes | $`q`$ of each; $`2q`$ additional memory calls and counted modes, $`q`$ mean input photons |
| Coherent storage and optical reception | $`N`$ idler modes through the full declared window, $`N`$ return heterodyne exposures, $`O(N)`$ passive mixing and phase controls |
| Photon readout | All $`N`$ idler output modes; sufficient sums are $`K`$ and $`S`$ |
| Classical operations | Record processing, norm and command preparation, finite-precision controls, and an exact count decision; none is supplied by the error exponent |

For $`q=\lceil\sqrt N\rceil`$, the extra calibration calls and energy are asymptotically sublinear, but can be substantial at finite $`N`$ because each target signal is so dim. Every possible calibration record leaves the detector's guarantee intact.

At equal signal and idler frequencies, the source prepares twice the transmitted signal energy before local calibration. The collective constructions retain a smaller certified source-output-energy advantage after that charge, but incident-pump inefficiency, local oscillators, storage, controls, readout, cooling and classical processing remain additional apparatus costs. Converted pump energy and its signal–idler outputs are the same energy transfer and must not be counted twice. No complete-apparatus, wall-clock or monetary advantage is established.

The [resource account](../science/resources.md) gives the exact denominators and hardware assumptions. In particular, the memory bounds must cover the full window, and a sequential apparatus with growing unequal dwell times is not automatically represented by the stationary channel used in this proof.

## Continue into the scientific account

The [model](../science/model.md) fixes the physical promises and identifiability question. The [conditional detection proof](../science/conditional_detection.md) derives the exact probabilities and finite-sample separation. The [processing analysis](../science/processing_robustness.md) states what survives finite controls, common processing noise and a fixed coherent width. The [classical benchmark](../science/classical_benchmark.md), [calibration limits](../science/calibration_limits.md) and [resource account](../science/resources.md) complete the comparison. The [milestone map](milestones.md) turns this same route into thirty project-specific understanding targets.
