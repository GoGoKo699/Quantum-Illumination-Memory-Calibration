# Memory, target and receiver model

[Conditional detection guarantee](conditional_detection.md) · [Calibration reliability limits](calibration_limits.md)

The target detector does not assume that the idler memory has been calibrated successfully. It uses the full collection of idler outputs of a correlation-to-displacement receiver to construct an exact conditional test. Separate estimates of memory loss and added noise remain possible through explicitly charged local probes, but their accuracy is not an assumption of the detection theorem.

## Target and source

There are $`N`$ independently prepared signal–idler pairs. Each pair is a two-mode squeezed vacuum of known mean occupation $`n\gt 0`$ in each mode,

**Equation (M1).**

```math
|\psi_n\rangle_{SI}
=\frac1{\sqrt{n+1}}\sum_{j=0}^{\infty}
\left(\frac n{n+1}\right)^{j/2}|j\rangle_S|j\rangle_I.
```

The source has a common phase convention across the block, so that $`\langle a_Sa_I\rangle=\sqrt{n(n+1)}`$. This phase coherence is needed by the collective idler combiner.

Fix a known background occupation $`B\gt 0`$ and a known power reflectivity $`0\lt \kappa\lt 1`$. Under target absence, the returned mode is an independent thermal state $`\tau_B`$. Under target presence,

**Equation (M2).**

```math
a_R=e^{i\theta}\sqrt\kappa\,a_S+\sqrt{1-\kappa}\,a_E,
\qquad
\langle a_E^\dagger a_E\rangle=\frac B{1-\kappa}.
```

The phase $`\theta\in[0,2\pi)`$ is unknown and constant throughout the block. The target environments are independent across pairs and independent of the source and memory environments. Consequently the returned occupation is $`B+\kappa n`$ under presence. Vacuum illumination gives the same return under either hypothesis: a changed background is not supplied as an additional target signature.

The transmitter is fixed before target interaction. Receiver feedforward does not change the transmitted signals or their energy.

## Unknown stationary Gaussian memory

Each idler passes through the same phase-insensitive Gaussian channel

**Equation (M3).**

```math
\mathcal L_{\eta,\nu}=\mathcal A_\nu\circ\mathcal L_{\eta,0},
\qquad
\mathcal A_\nu(\rho)=\int_{\mathbb C}
\frac{e^{-|a|^2/\nu}}{\pi\nu}
D(a)\rho D(a)^\dagger\,d^2a.
```

Here $`\mathcal L_{\eta,0}`$ is attenuation into vacuum with power transmissivity $`\eta`$, and $`\mathcal A_\nu`$ adds independent circular Gaussian displacement noise of variance $`\nu`$. At $`\nu=0`$, the second channel is the identity. This definition is physical also at $`\eta=1`$ and positive $`\nu`$. It maps a thermal input of occupation $`x`$ to a thermal output of occupation $`\eta x+\nu`$.

The unknown values lie in declared bounds

**Equation (M4).**

```math
0\lt \eta_-\le\eta\le\eta_+\le1,
\qquad
0\le\nu_-\le\nu\le\nu_+\lt \infty.
```

They are fixed across the experiment and are common to the two target hypotheses. Each call has an independent environment. This is stationary independent memory noise, not a parameter redrawn on every use. The parameter $`\nu`$ is output-referred added occupation; it is not the occupation of an attenuator's environmental input.

Define

**Equation (M5).**

```math
m=\eta n+\nu,
\qquad V=B+\kappa n+1,
\qquad A=\frac{\eta\kappa n(n+1)}V,
\qquad e=m-A.
```

The received idler has occupation $`m`$ under either hypothesis. Its correlation with a return is zero under absence and

**Equation (M6).**

```math
\langle a_Ra_{I,\mathrm{out}}\rangle
=e^{i\theta}\sqrt{\eta\kappa n(n+1)}
```

under presence. The residual conditional occupation $`e`$ is nonnegative. Indeed,

**Equation (M7).**

```math
\frac A{\eta n}
=\frac{\kappa(n+1)}{B+\kappa n+1}\lt 1,
```

because $`\kappa\lt B+1`$. With the strict assumptions above, $`e\gt 0`$.

## Identifiability before choosing calibration

Ordinary target-detection pairs at one source brightness cannot identify $`\eta`$ and $`\nu`$ separately under target absence. Their complete return–idler state is

**Equation (M8).**

```math
\rho_{0,\eta,\nu}^{(N)}
=(\tau_B\otimes\tau_m)^{\otimes N}.
```

Whenever two admissible memory pairs have the same $`m=\eta n+\nu`$, these states are identical. No measurement, including a collective quantum measurement, can distinguish those memory pairs from such data. This is an exact identifiability failure, rather than a poor choice of estimator. Correlations under target presence can provide additional information, but do not resolve the failure uniformly over the two hypotheses.

Separate full-channel learning needs a second known input brightness or another independently justified probe. One explicit option uses $`q`$ vacuum probes and $`q`$ independent thermal probes of occupation one. They pass through the same memory channel for the same specified storage window. Their output photon-count means are respectively $`\nu`$ and $`\eta+\nu`$. If $`Z_0,Z_1`$ are the two sample means, use

**Equation (M9).**

```math
\widehat\nu=\Pi_{[\nu_-,\nu_+]}(Z_0),
\qquad
\widehat\eta=\Pi_{[\eta_-,\eta_+]}(Z_1-Z_0),
```

where $`\Pi`$ denotes clipping to an interval. The law of large numbers proves consistency as $`q\to\infty`$. On a compact parameter box, geometric-count variances are uniformly bounded, so Chebyshev's inequality also gives uniform consistency. This does not make fixed-accuracy failures exponentially negligible on the $`N`$-trial detection scale when $`q=o(N)`$.

These probes are local: they do not interrogate the target, and they do not reveal its phase. They still consume $`2q`$ prepared temporal or spatial modes, $`2q`$ full-window memory calls, $`2q`$ measured-mode exposures, processing, and mean input energy $`q`$ photons. The detector below neither uses their estimates as exact parameters nor conditions its guarantee on their success. Thus every possible separate-calibration record, including a misleading one, leaves the detection guarantee valid.

## Collective receiver

Heterodyne every returned mode, obtaining $`z=(z_1,\ldots,z_N)\in\mathbb C^N`$. Retain the idlers coherently. Apply a passive $`N`$-mode transformation whose first row is

**Equation (M10).**

```math
w_j=\frac{z_j}{\Vert z\Vert}.
```

Choose any orthonormal completion of that row. At the probability-zero event $`z=0`$, declare one fixed unitary. This is a complete receiver policy: its weights depend on recorded heterodyne outcomes and do not require $`\eta,\nu`$ or $`\theta`$.

The first output is the bright output; photon-count it to obtain $`K`$. Count all other outputs and let $`S`$ be their total count. Write $`M=K+S`$. The final decision uses the exact conditional-null tail

**Equation (M11).**

```math
p_N(K,M)
=\frac{\binom{M-K+N-1}{N-1}}
{\binom{M+N-1}{N-1}},
\qquad N\ge2.
```

The [detection proof](conditional_detection.md) derives the state reduction, the joint count law and a threshold with an explicit finite-sample error guarantee. No common-phase estimate is formed. Photon-number statistics are independent of that phase exactly.

This receiver inherits correlation-to-displacement conversion and phase-insensitive bright-output photon counting from [Chen and Zhuang](https://arxiv.org/html/2212.08190v1), particularly their Section III. The present test keeps the orthogonal idler outputs as an internal statistical reference. Their existence and the optical concentration operation are not new claims.

## Physical and resource boundary

The theorem treats the specified memory channel as covering each idler's complete declared storage window. After that channel it assumes ideal controlled passive processing, correctly matched modes, known ideal heterodyne and photon-counting responses, and no additional unmodeled loss or noise. A clean realization of this mathematical interface is a parallel multimode block with equal storage windows and explicitly provisioned feedforward buffering. A sequential combiner whose running mode acquires growing additional storage noise is a different model.

All $`N`$ target signals are counted, giving mean transmitted energy $`Nn`$ photons, or $`\hbar\omega_S Nn`$. The source also prepares mean idler energy $`Nn`$ photons, or $`\hbar\omega_I Nn`$. The detector uses $`N`$ heterodyne measurements, a passive network with $`O(N)`$ mixing and phase controls, and photon counting over all $`N`$ idler output modes. Only $`K`$ and the sum $`S`$ need be retained as count statistics; $`N`$ separate detector instruments are not required.

The coherent storage width is $`N`$ idler modes. Classical weight preparation requires $`O(N)`$ real-arithmetic operations, but arithmetic precision, command latency, local-oscillator energy, detector and control energy, cooling, optical insertion loss, pump conversion efficiency and elapsed time are separate apparatus costs. A transmitted-energy exponent advantage is not a claim about complete apparatus energy or wall-clock performance.

If separate full-memory learning uses $`q=\lceil\sqrt N\rceil`$ probes of each brightness, the total number of memory calls is $`N+2q`$, with extra mean input energy $`q`$ photons. The finite-resource ledger retains these costs. The ratio $`N/(N+2q)\to1`$ explains why their inclusion does not alter the large-sample exponent per total memory call; it does not remove their finite cost or assume favorable calibration outcomes.
