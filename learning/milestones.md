# Thirty milestones: unknown memory and reliable quantum illumination

The central problem is to detect a weak reflector when stored idlers have an unknown, stationary Gaussian loss and added noise. Learning those channel parameters, certifying them with exponentially small failure, and detecting the reflector are different operational tasks. The route below connects those distinctions to an exact conditional detector and to a contrasting calibration obstruction.

The allocation is **10 background/preliminary milestones (M01–M10)** and **20 narrative/contribution milestones (M11–M30)**. The background builds from one optical mode to a complete noisy quantum testing experiment. The narrative builds the detector from its measured records, establishes the strong classical comparison, explains the obstruction, and then integrates implementation and resource limits. Dependencies always point backward; the map identifies the main conceptual structure rather than every proof detail.

The single educational anchor is **Weedbrook et al., “Gaussian Quantum Information,” Reviews of Modern Physics 84, 621–669 (2012)**. Section labels below refer to the available [full author manuscript, arXiv:1110.3234v1](https://arxiv.org/html/1110.3234v1), submitted 14 October 2011; the [published identity](https://doi.org/10.1103/RevModPhys.84.621) is retained separately. “GQI” below means that manuscript. Primary research papers supply attribution and research-level ingredients; they are not additional educational anchors. The [scientific route](../science/README.md) and its topic pages are authoritative for this project's definitions and proofs.

## Background and preliminaries

### M01 — Optical modes, photon occupation and energy

**Central question:** What is counted when a weak signal is said to contain a fraction of a photon per mode?

**Understanding target:** Distinguish a mode, a realized integer photon count, its mean occupation, and energy at a specified frequency. Recognize that a weak thermal mode can still produce an unusually large count.

**Dependencies and story role:** None. This fixes the physical objects and units used throughout both phases.

**Conceptual connection:** The signal occupation sets the transmitted-energy budget, while idlers and local probes carry separately charged energy.

**Sources and project route:** [GQI](https://arxiv.org/html/1110.3234v1), Secs. II.1 and II.2.1; [model, Target and source](../science/model.md#target-and-source), Eq. (M1); [resources, Source energy and pumps](../science/resources.md#source-energy-and-pumps), Eqs. (R1)–(R2).

### M02 — Gaussian states and the meaning of their moments

**Central question:** Which data specify an optical Gaussian state, and which correlations matter for this experiment?

**Understanding target:** Read means, occupations and intermode correlations as properties of a quantum state. Distinguish a Gaussian state description from a classical record with a Gaussian probability density, and track the vacuum-normalization convention.

**Dependencies and story role:** M01. Moves from counted quanta to the compact state description used by the receiver calculation.

**Conceptual connection:** Gaussian conditioning will turn a return–idler correlation into an idler displacement and a reduced residual occupation.

**Sources and project route:** [GQI](https://arxiv.org/html/1110.3234v1), Secs. I.4, II.1.1 and II.3.3; [model](../science/model.md), Eqs. (M5)–(M7); [conditional detection, Conditional Gaussian state](../science/conditional_detection.md#conditional-gaussian-state), Eqs. (D3)–(D6).

### M03 — A correlated source with thermal marginals

**Central question:** How can each signal or idler look thermal while their joint preparation supplies a quantum sensing resource?

**Understanding target:** Connect the two-mode squeezed-vacuum pair to its thermal marginal occupation and phase-sensitive correlation. Explain why a classical signal marginal alone does not determine whether the joint transmitter belongs to the classical benchmark.

**Dependencies and story role:** M01–M02. Introduces the particular source before either noisy channel acts.

**Conceptual connection:** The source's correlation, rather than a change in the idler's unconditional brightness under target presence, drives the detection signature.

**Sources and project route:** [GQI](https://arxiv.org/html/1110.3234v1), Sec. II.2.7; [model](../science/model.md#target-and-source), Eqs. (M1), (M6); [classical benchmark, Preparation class and theorem](../science/classical_benchmark.md#preparation-class-and-theorem).

### M04 — Loss, added noise and the two hypotheses

**Central question:** What physical experiment does an unknown but common memory channel describe?

**Understanding target:** Interpret attenuation followed by random displacement, the output-referred added occupation, and independent channel environments. Distinguish fixed unknown parameters from parameters redrawn on each use, and recognize why the matched-background convention removes a vacuum-only target signature.

**Dependencies and story role:** M02–M03. Places source, target and memory into one repeated experiment.

**Conceptual connection:** A common nuisance parameter can obstruct inference without physically changing between target absence and presence.

**Sources and project route:** [GQI](https://arxiv.org/html/1110.3234v1), Secs. V.1–V.2; [Eisert and Wolf, full manuscript](https://arxiv.org/html/quant-ph/0505151v1), Sec. 2.3; [model](../science/model.md#unknown-stationary-gaussian-memory), Eqs. (M2)–(M7).

### M05 — Heterodyne measurement and a conditional idler state

**Central question:** What changes in an idler description after the correlated return is heterodyned?

**Understanding target:** Separate the return's measured complex outcome from the conditional quantum state of the idler. Account for the added vacuum unit in the heterodyne variance and the resulting subtraction from the conditional idler occupation.

**Dependencies and story role:** M02–M04. Supplies the local optical-to-classical step from which collective reception is built.

**Conceptual connection:** The conditional mean carries the target correlation, while conditional covariance determines its thermal noise.

**Sources and project route:** [GQI](https://arxiv.org/html/1110.3234v1), Secs. II.5.2–II.5.3; [Chen and Zhuang, full manuscript](https://arxiv.org/html/2212.08190v1), Sec. III; [conditional detection](../science/conditional_detection.md#conditional-gaussian-state), Eqs. (D4)–(D5).

### M06 — Passive mixing and conserved total photon number

**Central question:** What can a controlled passive network change, and what must it preserve?

**Understanding target:** Explain displacement concentration by a normalized mode combination, invariance of an equal-temperature thermal product under passive controls chosen from return or independent calibration records, and conservation of total photon number. Distinguish passive optical action from the paid controls that select it.

**Dependencies and story role:** M02, M05. Connects one conditional idler to a coherently processed block.

**Conceptual connection:** The same symmetry makes a useful bright mode possible and protects the null law against passive control errors.

**Sources and project route:** [GQI](https://arxiv.org/html/1110.3234v1), Secs. II.1.2, II.2.6 and II.3.2; [model, Collective receiver](../science/model.md#collective-receiver); [processing robustness](../science/processing_robustness.md#arbitrary-passive-control-errors-preserve-the-null-test), Eq. (P3).

### M07 — From optical states to exact count laws

**Central question:** How do thermal fluctuations, displacements and independent repetitions become count distributions?

**Understanding target:** Identify geometric thermal counts, negative-binomial sums, and probability generating functions. Explain how multiplying generating functions represents independent sums and why a displaced thermal output requires more than its mean to characterize detection tails.

**Dependencies and story role:** M01–M02, M05–M06. Establishes the language for an exact distributional calculation.

**Conceptual connection:** The receiver proof integrates the random displacement distribution instead of replacing its energy by an average.

**Sources and project route:** [GQI](https://arxiv.org/html/1110.3234v1), Secs. II.2.1–II.2.2 and II.5.4; locally supplied [count-law derivation](../science/conditional_detection.md#integrating-every-heterodyne-record), Eqs. (D7)–(D12).

### M08 — Uniform detection risk and the scale of reliability

**Central question:** Why is a usually accurate calibration insufficient to establish an error exponent?

**Understanding target:** Distinguish false alarm, miss probability, symmetric risk, consistency and exponential decay. Interpret a uniform bound as covering every allowed fixed memory and phase, with all trials and rare records included.

**Dependencies and story role:** M04, M07. Defines the task whose difficulty the optical calculations must resolve.

**Conceptual connection:** The rate of a preliminary failure can control the final risk even when the preliminary estimator is consistent.

**Sources and project route:** [GQI](https://arxiv.org/html/1110.3234v1), Secs. III.1.1 and III.1.4; [conditional detection](../science/conditional_detection.md#1-experiment-and-error-convention), Eqs. (D1)–(D2); [model, Identifiability before choosing calibration](../science/model.md#identifiability-before-choosing-calibration).

### M09 — Exponential bounds that retain rare records

**Central question:** How can an exact transform bound an unlikely count without declaring the record typical?

**Understanding target:** Explain exponential Markov bounds, a Chernoff parameter, and a union bound as tools for bounding explicit failure events. Distinguish these classical record-tail arguments from a quantum Chernoff bound on optimized state discrimination.

**Dependencies and story role:** M07–M08. Adds the reliability tool needed to convert exact laws into finite-sample guarantees.

**Conceptual connection:** A reference upper tail and a bright-count lower tail can be charged separately without assuming their independence.

**Sources and project route:** Locally derived [detection proof](../science/conditional_detection.md#4-uniform-finite-sample-advantage-theorem), Eqs. (D26)–(D31); [GQI](https://arxiv.org/html/1110.3234v1), Sec. III.1.2, for the distinct quantum Chernoff setting.

### M10 — Quantum testing, information and comparison experiments

**Central question:** How can a result constrain every receiver rather than a chosen measurement?

**Understanding target:** Connect the Helstrom error to trace distance and understand that granting information or extra receiver freedom can only improve discrimination. Assemble the source, channels, measurements and risk into one experiment before comparing protocols.

**Dependencies and story role:** M01–M09. Integrates the background into the quantum and statistical framework required by both the positive theorem and the obstruction.

**Conceptual connection:** A preparation-label genie strengthens the classical alternative, while a common channel component limits even adaptive quantum calibration.

**Sources and project route:** [GQI](https://arxiv.org/html/1110.3234v1), Secs. III.1.1 and V.7; [classical benchmark, Revealing the preparation label](../science/classical_benchmark.md#revealing-the-preparation-label); [calibration limits, Theorem L1](../science/calibration_limits.md#2-an-energy-independent-calibration-bound).

## Narrative and contribution

### M11 — Exact nonidentifiability at one input brightness

**Central question:** What can the complete target-absent quantum record reveal about unknown loss and added noise?

**Understanding target:** Explain why only $`m=\eta n+\nu`$ is identifiable from ordinary pairs at one brightness under absence. Use equality of full quantum states to rule out separate parameter recovery by any measurement, while distinguishing this failure from target detectability.

**Dependencies and story role:** M03–M04, M08, M10. The narrative starts by identifying the inference problem before choosing an estimator.

**Conceptual connection:** Full memory identification is stronger than learning the nuisance combination relevant to a null distribution.

**Sources and project route:** [Model, Identifiability before choosing calibration](../science/model.md#identifiability-before-choosing-calibration), Eq. (M8); Gaussian-channel background in [GQI](https://arxiv.org/html/1110.3234v1), Sec. V.2.

### M12 — Charged two-brightness learning

**Central question:** Which extra experiment identifies the channel, and what does its success establish?

**Understanding target:** Interpret vacuum and occupation-one probe means as two independent equations for loss and added noise. Explain clipping, uniform consistency, the full-window matching requirement, and why sublinear probe counts do not provide exponential-confidence certification on the detection scale.

**Dependencies and story role:** M07–M09, M11. Provides a concrete optional learning protocol and its complete finite resource cost.

**Conceptual connection:** Channel learning can remain operationally useful even when the detector's correctness cannot depend on a favorable learning record.

**Sources and project route:** [Model](../science/model.md#identifiability-before-choosing-calibration), Eq. (M9); [resources, One collective block and local calibration](../science/resources.md#one-collective-block-and-local-calibration); [calibration limits, Corollary L2](../science/calibration_limits.md#2-an-energy-independent-calibration-bound).

### M13 — Inherited CtoD reception without phase learning

**Central question:** How can unknown-phase correlations be concentrated without first estimating the target phase or memory?

**Understanding target:** Explain why the recorded return vector determines the combiner row, while the unknown common phase remains only an overall bright displacement phase. Distinguish phase-invariant photon counting from phase estimation, and retain the required common source coherence.

**Dependencies and story role:** M03, M05–M06, M11. Selects a measured correlation that does not require separately identified memory parameters.

**Conceptual connection:** Removing an estimation stage removes its failure event only because the actual optical statistics are phase invariant.

**Sources and project route:** [Chen and Zhuang](https://arxiv.org/html/2212.08190v1), Secs. III–IV; [Angeletti et al.](https://arxiv.org/html/2303.18206v1), Secs. V–VIII; [model](../science/model.md#collective-receiver), Eq. (M10); [conditional detection](../science/conditional_detection.md#conditional-gaussian-state), Eq. (D6).

### M14 — The joint bright and dark count experiment

**Central question:** What exact observations result when the usually discarded CtoD outputs are also counted?

**Understanding target:** Explain the bright-count generating function, the negative-binomial dark sum and their independence in the ideal concentration model. Identify where the Gamma-distributed return norm is integrated and why the dark occupation under presence is $`e=m-A`$, rather than $`m`$.

**Dependencies and story role:** M07, M13. Converts the optical construction into the complete classical experiment used by the new decision rule.

**Conceptual connection:** An internal reference can carry hypothesis information; it cannot automatically be treated as independent external calibration.

**Sources and project route:** [Conditional detection, Integrating every heterodyne record](../science/conditional_detection.md#integrating-every-heterodyne-record), Eqs. (D7)–(D12); noisy conditional-state antecedent in [Angeletti et al.](https://arxiv.org/html/2303.18206v1), Secs. V–VI.

### M15 — A hypothesis-neutral total count

**Central question:** Which observed statistic has the same distribution under both target hypotheses despite the bright displacement?

**Understanding target:** Explain cancellation in the joint generating function and its physical origin in conservation of total idler photon number. Interpret $`M=K+S`$ as a noisy estimate of the true occupation under both hypotheses, while retaining its rare large values in the analysis.

**Dependencies and story role:** M06, M14. Identifies the specific internal reference on which the conditional test can be based.

**Conceptual connection:** Correlation concentration redistributes photons; it does not create an unconditional total-idler-energy signature.

**Sources and project route:** [Conditional detection, Total count is a hypothesis-neutral reference](../science/conditional_detection.md#total-count-is-a-hypothesis-neutral-reference), Eq. (D13); [processing robustness](../science/processing_robustness.md#arbitrary-passive-control-errors-preserve-the-null-test), Eq. (P6).

### M16 — Conditioning removes the unknown null brightness

**Central question:** Why does fixing the observed total produce an exact test without a plug-in estimate?

**Understanding target:** Explain equal-probability photon allocations under the null, the combinatorial bright-count upper tail, and discrete super-uniformity. Include zero-total records and distinguish exact conditional calibration from training a threshold on estimated null data.

**Dependencies and story role:** M07–M08, M15. Establishes the central nuisance-elimination mechanism before considering detection power.

**Conceptual connection:** The total determines how much thermal activity occurred; the allocation tests whether too much of it concentrated in the chosen bright output.

**Sources and project route:** [Conditional detection, An exact conditional-null test](../science/conditional_detection.md#3-an-exact-conditional-null-test), Eqs. (D14)–(D17); CFAR precedent and distinction in [related work](../references/RELATED_WORK.md#unknown-memory-and-conditional-false-alarm-control), including [Wang and Wong](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/rsn2.12592), Secs. 3.2 and 5.2.

### M17 — Detection power with every misleading record included

**Central question:** How is a miss bounded when the internal reference itself may be misleading?

**Understanding target:** Trace the sufficient rejection event and the union of a total-count upper tail with a bright-count lower tail. Explain the uniform bounds, the integer threshold, and why integrating all return records leaves no hidden typical-calibration or phase-learning assumption.

**Dependencies and story role:** M09, M13–M16. Supplies the reliability argument that an exact false-alarm test alone does not provide.

**Conceptual connection:** Robust null calibration and strong detection power require different arguments; both must cover the same operational record space.

**Sources and project route:** [Conditional detection, Uniform finite-sample advantage theorem](../science/conditional_detection.md#4-uniform-finite-sample-advantage-theorem), Eqs. (D23)–(D32); [What is and is not charged](../science/conditional_detection.md#5-what-is-and-is-not-charged-by-this-guarantee).

### M18 — A strict finite-sample theorem on an explicit parameter box

**Central question:** What exactly is certified beyond an asymptotic known-memory approximation?

**Understanding target:** State the declared source, background, memory and reflectivity regime, the finite-sample prefactor, and the uniform rate lower bound. Distinguish an achieved exponent from the optimal quantum exponent and a rigorous rational certificate from a numerical plot.

**Dependencies and story role:** M12, M17. Assembles the positive construction into its first complete theorem, with optional misleading calibration records already covered.

**Conceptual connection:** A nonzero uncertainty box and an interval of positive reflectivities make the result an operational unknown-memory statement.

**Sources and project route:** [Conditional detection](../science/conditional_detection.md#4-uniform-finite-sample-advantage-theorem), Eqs. (D18)–(D22), (D33)–(D35); [exact constant certificate](../verification/certify_constants.py); [stored certificate](../verification/conditional_memory_certificate.json).

### M19 — The strongest classical alternative in the stated preparation class

**Central question:** Why does the comparison survive phase information, energy randomization and arbitrary global reception?

**Understanding target:** Specify the joint conditional-coherent preparation class, its mean transmitted-energy budget and retained label-conditioned states. Explain the preparation-label genie, displaced-thermal reduction and finite-energy converse; distinguish a converse from a quantum Chernoff achievability bound.

**Dependencies and story role:** M03, M08–M10, M18. Establishes the competing ceiling before interpreting the quantum rate ratio.

**Conceptual connection:** A receiver-specific classical simulation would be insufficient; the inherited converse bounds every receiver in the stated class.

**Sources and project route:** [Classical benchmark](../science/classical_benchmark.md), especially its thermal testing and label-genie proofs; [Nair and Gu](https://arxiv.org/html/2002.12252v2), Eq. (6); pinned [Quantum-Illumination-Feedback proof](https://github.com/GoGoKo699/Quantum-Illumination-Feedback/blob/2b47472b7930168b5aab53f040c6730a4bbb4cf9/science/classical_limit.md).

### M20 — What a certified exponent separation means

**Central question:** Which performance comparison follows from the two theorems, and which requires additional work?

**Understanding target:** Compare the achieved quantum rate with the optimum phase-informed coherent-mixture rate at equal transmitted energy. Explain why the ideal factor above 2.2 concerns large-sample reliability and does not order the actual errors at every finite block size or establish a complete-apparatus advantage.

**Dependencies and story role:** M18–M19. Integrates the positive theorem and its strongest classical comparison before turning to the contrasting obstruction.

**Conceptual connection:** Uniform nuisance handling preserves a consequential advantage, but the chosen normalization controls its physical meaning.

**Sources and project route:** [Detection theorem](../science/conditional_detection.md#4-uniform-finite-sample-advantage-theorem), Eq. (D22); [classical benchmark, Scope of the comparison](../science/classical_benchmark.md#scope-of-the-comparison); [resources, What the classical comparison establishes](../science/resources.md#what-the-classical-comparison-establishes).

### M21 — A common channel component limits quantum calibration

**Central question:** Why can arbitrary calibration photon energy fail to replace a sufficient number of memory calls?

**Understanding target:** At fixed attenuation, explain the overlap of two positive Gaussian displacement densities as a shared completely positive channel component. Follow its all-common branch through arbitrary adaptive calibration and retained quantum registers to the energy-independent trace-distance and certification bounds.

**Dependencies and story role:** M04, M08, M10, M12. Introduces the obstruction's information-theoretic ingredient independently of the chosen target measurement.

**Conceptual connection:** Repeated calls suppress a common indistinguishable branch; arbitrarily bright probes do not eliminate that branch in one use.

**Sources and project route:** [Calibration limits, Theorem L1 and Corollary L2](../science/calibration_limits.md#2-an-energy-independent-calibration-bound), Eqs. (L2)–(L9); channel representation in [Eisert and Wolf](https://arxiv.org/html/quant-ph/0505151v1), Sec. 2.3, and [calibration limits](../science/calibration_limits.md#1-memory-channel-and-calibration-experiment), Eqs. (L1)–(L1a).

### M22 — Exact confounding in a frozen OPA output

**Central question:** When does separate calibration become the only distinguishing part of a target-detection record?

**Understanding target:** Identify the fixed-gain, supplied-phase, single-counted-output restrictions and the noise shift that exactly matches the main count laws. Explain the cross-parameter comparison in a uniform-risk proof, the zero exponent with sublinear calibration, and why no memory physically changes with the hypothesis.

**Dependencies and story role:** M08, M11, M21. Applies the channel bound to a specified receiver rather than claiming a universal QI no-go.

**Conceptual connection:** What the main measurement discards can turn an otherwise avoidable nuisance into a calibration bottleneck.

**Sources and project route:** [Calibration limits, Exact confounding](../science/calibration_limits.md#3-exact-confounding-in-a-frozen-one-output-opa-receiver), Theorem L3 and Eqs. (L10)–(L14); original architecture in [Guha and Erkmen](https://arxiv.org/html/0911.0950v1), “The OPA Receiver”; [related-work qualification](../references/RELATED_WORK.md#the-calibration-obstruction-is-receiver-specific).

### M23 — A sharp allocation law for one calibration strategy

**Central question:** How much detection reliability is lost when a fixed OPA output is calibrated by direct thermal counting?

**Understanding target:** Interpret the two-sample rate minimization, nuisance-direction projection and calibration-to-main ratio. Explain the leading retention factor, the square-root optimum per total memory call, the order of limits and why this is not an optimum over quantum probes or receivers.

**Dependencies and story role:** M07–M09, M12, M22. Quantifies the calibration tax within one explicit architecture after the general obstruction is understood.

**Conceptual connection:** A calibration allocation optimum depends on the resource denominator and the measurement model being held fixed.

**Sources and project route:** [Calibration limits, Restricted appendix](../science/calibration_limits.md#4-restricted-appendix-the-exact-direct-count-calibration-allocation-law), Theorem L4, Eqs. (L15)–(L25), and its [resource interpretation](../science/calibration_limits.md#43-resource-meaning).

### M24 — Full-window memory and common processing noise

**Central question:** Which additional optical losses and noises can be absorbed into the theorem's unknown channel?

**Understanding target:** Explain why identical phase-insensitive channels commute with passive mixing, including record-controlled mixing, and compose their effective attenuation and added occupation. Distinguish a full-window bound from a storage-element specification, and recognize the failure of this argument for nonuniform or growing unaccounted losses.

**Dependencies and story role:** M04, M06, M13, M20. Moves the abstract receiver toward a defined hardware interface without treating processing noise as free.

**Conceptual connection:** A valid effective-channel reduction changes the parameters to be bounded and calibrated; it does not remove physical loss.

**Sources and project route:** [Processing robustness, Common processing noise](../science/processing_robustness.md#common-processing-noise-is-part-of-the-memory), Eqs. (P1)–(P2); [model, Physical and resource boundary](../science/model.md#physical-and-resource-boundary); Gaussian-channel formalism in [GQI](https://arxiv.org/html/1110.3234v1), Sec. V.1.

### M25 — Passive control errors separate calibration from power

**Central question:** What survives if the commanded combiner captures only part of the intended displacement?

**Understanding target:** Explain exact null invariance for passive control laws selected from return records or independent calibration records, and a captured-fraction bound for detection power. Use conservation of the total count when imperfect concentration destroys the ideal bright–dark independence after averaging; selecting a favorable payload-idler measurement outcome is outside this claim.

**Dependencies and story role:** M06, M15–M17, M24. Identifies the symmetry that makes controlled imperfections analyzable.

**Conceptual connection:** A bad passive command can weaken the target signature while leaving conditional false-alarm control exact.

**Sources and project route:** [Processing robustness, Arbitrary passive control errors](../science/processing_robustness.md#arbitrary-passive-control-errors-preserve-the-null-test), Eqs. (P3)–(P10a); [conditional-null law](../science/conditional_detection.md#3-an-exact-conditional-null-test).

### M26 — Finite record range and finite command precision

**Central question:** How can finite optical controls retain a rigorous guarantee without ignoring overflow or small-norm records?

**Understanding target:** Connect the declared good-record event, coordinate rounding, deterministic gate-error budget and captured displacement fraction. Explain the charged complement event, the logarithmic word lengths, and the finite-control factor above 2.18 under the ideal measurement model.

**Dependencies and story role:** M09, M17, M25. Replaces a control-precision idealization with an explicit finite construction.

**Conceptual connection:** A deterministic per-record control bound and a probabilistic record exclusion must be charged separately; neither is an assumed per-gate success rate.

**Sources and project route:** [Processing robustness, Finite classical records and controls](../science/processing_robustness.md#finite-classical-records-and-controls), Eqs. (P11)–(P16); [resources, Classical arithmetic and stored records](../science/resources.md#classical-arithmetic-and-stored-records); [constant certificate](../verification/certify_constants.py).

### M27 — An exact dyadic decision and its arithmetic cost

**Central question:** How can the final comparison avoid an approximate real-number threshold?

**Understanding target:** Explain the rational-reflectivity input, dyadic cutoff and integer cross-multiplication. Account for the threshold ceiling and its finite prefactor, and distinguish finite arithmetic on each record from a deterministic finite register capable of storing every unbounded photon count.

**Dependencies and story role:** M16–M18, M26. Completes the finite-control protocol with an exact classical decision and a certified factor above 2.17.

**Conceptual connection:** Exact statistics can be implemented without a floating-point likelihood boundary, while count overflow remains an explicit physical design issue.

**Sources and project route:** [Processing robustness, Exact integer decision](../science/processing_robustness.md#an-exact-integer-decision-with-a-dyadic-cutoff), Eqs. (P17)–(P21); [reference receiver](../verification/receiver.py); [independent receiver checks](../verification/check_receiver.py); [arithmetic resource account](../science/resources.md#classical-arithmetic-and-stored-records).

### M28 — Fixed coherent width and repeated blocks

**Central question:** Can a strict transmitted-energy advantage survive without increasing coherent apparatus width indefinitely?

**Understanding target:** Explain the fixed block width chosen from known reflectivity, repeated independent block decisions and majority bound. State the factor above 1.05 and the limit of increasing block repetitions at fixed width; retain the very large explicit width and its full-window memory requirement.

**Dependencies and story role:** M09, M20, M24, M27. Resolves one asymptotic apparatus assumption with a different, weaker certified comparison.

**Conceptual connection:** Bounded coherent width changes the achieved rate and does not preserve the collective protocol's equal-source-beam energy advantage.

**Sources and project route:** [Processing robustness, Fixed-width protocol](../science/processing_robustness.md#a-fixed-width-protocol-with-a-strict-advantage), Eqs. (P22)–(P24); [resources, Storage, timing and network size](../science/resources.md#storage-timing-and-network-size); [exact certificate](../verification/conditional_memory_certificate.json).

### M29 — Every trial and every resource denominator

**Central question:** Which advantage remains after signal energy, local learning, idler preparation and receiver operation are charged?

**Understanding target:** Reconstruct the ledger of target uses, memory calls, calibration photons, stored modes, all measured modes, controls and processing. Explain converted pump energy without double counting the output beams, unequal-frequency source costs, and the distinction between source-output energy and complete apparatus energy or time.

**Dependencies and story role:** M01, M12, M20, M24, M26–M28. Places all protocol variants on explicit and compatible resource scales.

**Conceptual connection:** Sublinear calibration preserves an asymptotic rate per memory call but can be expensive at finite size; passive mixing and two retained count statistics do not make apparatus costs vanish.

**Sources and project route:** [Resources](../science/resources.md), especially the full ledger, Eqs. (R1)–(R3), and [comparison scope](../science/resources.md#what-the-classical-comparison-establishes); [model, Physical boundary](../science/model.md#physical-and-resource-boundary).

### M30 — The complete result, its inheritance and its decisive boundaries

**Central question:** What has changed scientifically once reliable detection is separated from reliable memory certification?

**Understanding target:** Connect exact conditional nuisance removal, uniformly charged rare events, the strong classical separation and the receiver-specific calibration obstruction. Locate inherited CtoD, phase invariance and classical converse; identify the new use of retained outputs and the assumptions whose violation needs a new theorem. Distinguish analytical proof, finite verification and an experimental apparatus claim.

**Dependencies and story role:** M11–M29. Integrates the narrative into one bounded contribution and explains why the positive and negative results coexist.

**Conceptual connection:** Receiver design can make unknown channel parameters irrelevant to a valid decision even when certifying those parameters at exponential confidence is costly.

**Sources and project route:** [Scientific route](../science/README.md); [detection scope](../science/conditional_detection.md#6-scope-of-the-result); [calibration obstruction](../science/calibration_limits.md#3-exact-confounding-in-a-frozen-one-output-opa-receiver); [processing and width qualifications](../science/processing_robustness.md); [related work](../references/RELATED_WORK.md); [verification commands and evidence limits](../verification/README.md).
