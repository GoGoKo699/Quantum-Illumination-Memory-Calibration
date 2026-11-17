# Related work and attribution

The contribution concerns reliable target detection when a stationary Gaussian idler memory has unknown attenuation and added noise. The memory parameters are the same under target absence and presence. The receiver uses the established correlation-to-displacement (CtoD) transformation, retains its undisplaced outputs, and conditions on the total idler photon count to eliminate the unknown null brightness. The optical transformation, phase-insensitive reception, Gaussian channel model, and general principle of conditional testing are inherited ingredients. The new operational account is the resulting nuisance-independent false-alarm guarantee, its uniform finite-sample miss bound, and its comparison with the calibration bottleneck of a specified frozen-output receiver.

Publication details and versioned primary manuscripts are collected in [references.bib](references.bib). The model and proofs in `science/` determine the scope of each claim.

## What the closest results already establish

| Primary antecedent | Established ingredient | Additional question addressed here |
|---|---|---|
| Shi, Zhang and Zhuang, preliminary CtoD account (2022–2023); Shi et al., expanded account (2024) | Return heterodyne measurement, conditional idler displacement, programmable mode selection, and coherent-state information extraction | How undisplaced idler outputs can supply an internal reference when memory brightness is unknown |
| Chen and Zhuang (2023) | CtoD weights independent of target phase and reflectivity; photon counting for uniformly random static phase | An exact conditional-null test uniform over unknown memory parameters, with every misleading reference record included |
| Angeletti et al. (2023) | CtoD with known idler loss/noise, amplifier and detector imperfections, and final collective-idler photon counting | A decision rule that does not require the memory parameters to be supplied or accurately estimated |
| Kim et al. (2023) | Weak-reflectivity Gaussian detection coefficients and known-memory loss/noise thresholds | The operational cost of unknown memory parameters and how the choice of recorded outputs changes it |
| Wang and Wong (2024) | QI detection using OPA/covariance observables and estimated-null CFAR thresholds | Exact conditional false-alarm control without a separately trained null distribution |
| Quantum-Illumination-Feedback | A full-record OPA feedback reliability law with charged phase pilots and a strong classical converse | Unknown memory, joint idler processing, and a different calibration obstruction |

These are scientific differences between specified tasks and receivers. They do not establish that every earlier scheme needs external calibration, that CtoD is a new receiver, or that this is the first use of CFAR ideas in quantum illumination.

## The inherited CtoD receiver

[Shi, Zhang and Zhuang](https://arxiv.org/abs/2207.06609v3) introduced the CtoD conversion module. Their Sec. II.2 describes heterodyne measurements of the returns, the resulting product of displaced thermal idlers, and a passive combiner concentrating the displacement into one output. The [expanded account by Shi et al.](https://doi.org/10.1103/PhysRevApplied.21.034004), particularly Secs. IV–VII and the [version-2 manuscript](https://arxiv.org/abs/2309.12629v2), develops mode selectors and information extractors. Its model assumes lossless idler storage and treats undisplaced outputs as noise to remove or neglect. The receiver architecture and conditional Gaussian-state calculation used here come from this lineage.

[Chen and Zhuang](https://doi.org/10.1103/PhysRevA.107.062405), Secs. III–IV and Eqs. (13)–(21) of their [version-1 manuscript](https://arxiv.org/abs/2212.08190v1), show that the combiner weights can depend only on the heterodyne record, independently of the unknown static return phase and reflectivity. They analyze photon counting after averaging a common phase uniformly over the experiment. The present count law is phase invariant for each fixed phase; avoiding phase estimation is therefore an inherited capability, rather than a new phase-learning protocol. The published title says “correlation-to-displacement”; the earlier manuscript title says “correlation-to-coherence.”

[Angeletti et al.](https://doi.org/10.1103/PhysRevApplied.20.024030), Secs. V–VIII of the [author manuscript](https://arxiv.org/abs/2303.18206v1), already include a known thermal-loss idler channel. Their Eqs. (16)–(24) give the idler's noisy covariance, residual conditional thermal occupation, and collective displacement distribution. They analyze on/off and number-resolving detection of the collective bright idler output. Extending those formulas to another supplied loss or noise value is not the contribution claimed here.

Keeping the other outputs follows from the same conditional Gaussian state: a passive transformation of equal-temperature independent thermal residual modes leaves their covariance unchanged. The change here is their statistical use. With known memory these outputs can be dispensable for the leading detection signature; with unknown memory they provide a reference for how surprising the bright count is. Under presence their occupation is reduced by conditioning on the returns, so they are included in the joint detection law rather than treated as target-independent calibration samples.

[Kim et al.](https://doi.org/10.1103/PhysRevResearch.5.033010), Theorem IV.1 and Sec. V, give the known-memory weak-reflectivity coefficients. In this repository's occupation convention, their TMSV specialization with supplied memory brightness $`m=\eta n+\nu`$ is

```math
\gamma_{\rm col}=
\frac{\kappa\eta n(n+1)}
 {\bigl[\sqrt{Bm}+\sqrt{(B+1)(m+1)}\bigr]^2}+o(\kappa),
\qquad
\gamma_{\rm loc}=
\frac{\kappa\eta n(n+1)}{2(1+B+m+2Bm)}+o(\kappa).
```

Their thermal-environment parametrization has $`\nu=(1-\eta)N_L`$. These coefficients describe optimized known-state discrimination in their respective reception classes. They neither certify the present conditional receiver's finite-sample performance nor account for learning an unknown memory.

## Unknown memory and conditional false-alarm control

Let $`K`$ be the bright photon count and $`S`$ the sum of the other $`N-1`$ output counts. Under absence, all $`N`$ outputs have the same unknown thermal occupation. Conditioning on $`M=K+S`$ removes that occupation from the allocation distribution. The resulting upper-tail probability is

```math
p_N(K,S)=
\frac{\binom{S+N-1}{N-1}}
     {\binom{S+K+N-1}{N-1}}.
```

This is a conditional-testing construction, proved directly from the geometric photon-count law. Its application here gives exact discrete false-alarm control for every admissible memory brightness, including vacuum. The finite-sample detection bound separately includes the probability of misleading dark-output records and the lower tail of the bright count. It makes no replacement of a learned parameter by its typical value.

[Wang and Wong](https://doi.org/10.1049/rsn2.12592) explicitly discuss Neyman–Pearson and CFAR criteria in Sec. 3.2. Their Sec. 5.2 sets OPA and covariance-detector thresholds from repeated measurements of a known no-target region; the displayed numerical procedure repeats those samples 1000 times. They therefore provide a direct antecedent for CFAR as a QI goal. The distinction here is the exact conditional null law of the same idler block, rather than estimating a null density and assuming it is sufficiently accurate.

[Murchie, Pritchard and Jeffers](https://doi.org/10.1103/PhysRevApplied.21.064008) also give a calibration-free likelihood threshold for coincidence and noncoincidence click records. Their model parameters determine the likelihoods, and their classical comparison uses a thermal source with the same phase-insensitive click measurements. This differs from unknown Gaussian memory and a phase-informed coherent-mixture benchmark with unrestricted global reception. Likewise, the optical background-rejection protocols of [Gregory et al.](https://doi.org/10.1038/s41598-021-01122-8) address photon-pair imaging and accidental coincidences, rather than this conditional idler-number test.

Related CtoD work on [noisy entanglement testing by Liao and Zhuang](https://doi.org/10.1103/PhysRevApplied.22.024007) uses multiple return hypotheses and conditional nulling for ranging and communication. Its [model](https://arxiv.org/abs/2312.15047v1) supplies a perfectly stored idler and known thermal occupations. It does not supply the unknown-memory conditional-null result above. Conditional nulling, a sequence of optical displacement decisions, is a different operation from conditioning a statistical test on the total observed photon number.

## The calibration obstruction is receiver specific

[Guha and Erkmen](https://doi.org/10.1103/PhysRevA.80.052310) introduced the one-output OPA and balanced phase-conjugate receivers. The phase-conjugate receiver already cancels a common mean baseline through balanced photon-number differences. [Karsa and Pirandola](https://doi.org/10.1109/MAES.2020.3004019) derive its statistics for general correlated Gaussian sources with added noise. Noise cancellation itself is therefore established receiver design.

The obstruction here concerns a fixed-gain, known-phase, single counted OPA output whose unknown memory-noise shift can exactly mimic the target-present mean. Separate memory calibration then carries the distinguishing information. The proof gives a common completely positive component to the two candidate memory channels, so even high-energy, entangled or adaptive calibration probes cannot make a sublinear number of channel uses support a positive detection exponent in that specified architecture. This does not prohibit sublinear calibration for all receivers; the CtoD conditional test is an explicit counterexample to that broader claim.

The channel decomposition into attenuation followed by Gaussian random displacement is standard. [Eisert and Wolf](https://arxiv.org/abs/quant-ph/0505151v1), Sec. 2.3, Eqs. (9)–(13), give the random-displacement and thermal-loss representations. [Weedbrook et al.](https://doi.org/10.1103/RevModPhys.84.621), Sec. V, review the same Gaussian channel classes. The common-component argument and its consequence for the specified calibrated detection task are proved in this repository.

Separate identification of attenuation and added noise is another task. [Monras and Illuminati](https://doi.org/10.1103/PhysRevA.83.012315) analyze simultaneous damping and temperature estimation. [Gong and Bash](https://doi.org/10.1103/kmnp-11ch) treat two-stage quantum estimation with nuisance parameters, including unknown phase in transmittance sensing. Their [version-3 theorem](https://arxiv.org/abs/2402.17922v3) gives consistency and asymptotic normality with sublinear preliminary samples. Such estimation statements do not imply an exponentially reliable detection guarantee. Local probes used for full memory identification are explicitly counted here; their estimates are not needed by the conditional detector.

## Classical benchmark and the preceding feedback project

[Tan et al.](https://doi.org/10.1103/PhysRevLett.101.253601) established Gaussian QI and the coherent-state comparison. [Nair and Gu](https://doi.org/10.1364/OPTICA.391335), Eq. (6), give the standard phase-informed classical-illumination exponent. The benchmark used here is deliberately strong: fixed preselected mixtures of coherent signals at a total mean transmitted-energy budget, arbitrary retained label-conditioned states, the true return phase, and arbitrary collective reception.

The finite-energy converse accommodating arbitrary energy randomization is inherited from [Quantum-Illumination-Feedback, `science/classical_limit.md`](https://github.com/GoGoKo699/Quantum-Illumination-Feedback/blob/2b47472b7930168b5aab53f040c6730a4bbb4cf9/science/classical_limit.md). That proof uses thermal-state testing, the spectral distributions of [Nussbaum and Szkoła](https://doi.org/10.1214/08-AOS593), and a preparation-label genie. The [Audenaert et al.](https://doi.org/10.1103/PhysRevLett.98.160501) Chernoff trace inequality supplies coherent achievability, not the converse. The exact optimum coefficient and this proof are not counted as new results of the present project.

The same preceding project's charged phase-feedback exponent assumes ideal idler storage and quantum operations within each return–idler pair. This project uses collective coherent processing of the idlers, a materially larger apparatus resource. Its transmitted-energy detection guarantee consequently does not establish an overall apparatus advantage. Preparation and storage, source and control pumps, heterodyne local oscillators, multimode coherent processing, all photon measurements, and classical processing remain separate resource charges.

The surviving advance is therefore a specific reliable capability: unknown memory brightness can be removed exactly from the false-alarm decision using idler outputs already generated by CtoD, while retaining a rigorous detection guarantee and a strict strong-classical separation in a stated nonzero-noise regime. The paired obstruction explains why this capability is not obtained merely by calibrating an otherwise frozen one-output detector. Neither optimality over all receivers nor a universal calibration-free QI claim is asserted.
