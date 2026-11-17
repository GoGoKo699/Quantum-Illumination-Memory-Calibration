# Processing noise, finite controls and bounded coherent width

[Model](model.md) · [Conditional detection](conditional_detection.md) · [Resources](resources.md)

The statistical guarantee does not require infinitely precise passive controls. A finite-range, finite-precision implementation preserves a certified advantage when it captures at least 99 percent of the bright displacement on a declared return-record event; the probability of every excluded record is explicitly charged. Identical phase-insensitive Gaussian noise during processing can also be included in the memory parameters. Neither statement makes arbitrary hardware imperfections harmless: nonuniform loss, unmodeled detector response and growing storage loss remain material restrictions.

## Common processing noise is part of the memory

Let $`\mathcal L_{\eta,\nu}`$ be the phase-insensitive channel in the [model](model.md), and let $`U`$ be any passive transformation on $`N`$ modes. Then

```math
\mathcal L_{\eta,\nu}^{\otimes N}\!\left(U\rho U^\dagger\right)
=U\mathcal L_{\eta,\nu}^{\otimes N}(\rho)U^\dagger.
\tag{P1}
```

To verify this, apply the multimode Weyl characteristic function. Uniform attenuation replaces its argument by $`\sqrt\eta z`$ and multiplies it by a circular factor depending only on $`\|z\|^2`$. A passive unitary rotates $`z`$ without changing that norm. The two operations therefore commute. Equivalently, identical vacuum-loss environments and an independent circular Gaussian displacement vector are invariant under the same passive rotation.

This identity holds separately for every recorded return vector $`z`$. Thus it also holds for the record-controlled transformation $`U(z)`$, even though $`z`$ is correlated with the conditional idler state. Moving an idler channel does not alter the distribution of a measurement already made on the returns.

Suppose a pre-processing memory $`\mathcal L_{\eta,\nu}`$ is followed, after the controlled combiner, by an identical channel $`\mathcal L_{\lambda,\xi}`$ on every output. The complete experiment is exactly equivalent to the same combiner preceded by

```math
\mathcal L_{\eta_{\mathrm{eff}},\nu_{\mathrm{eff}}}^{\otimes N},
\qquad
\eta_{\mathrm{eff}}=\lambda\eta,
\qquad
\nu_{\mathrm{eff}}=\lambda\nu+\xi.
\tag{P2}
```

The same argument moves identical channels between passive network layers to the beginning. Compose their attenuation and noise parameters in their actual temporal order. Uniform known detection inefficiency is vacuum loss and can be included in this way. Additional known, identical phase-insensitive detector noise can be included only when its physical response is exactly the stated Gaussian channel followed by ideal photon counting.

The numerical memory box must bound these **effective full-window** parameters, including the declared storage, buffering, passive insertion loss and modeled detection inefficiency. Bounds for an isolated storage element are insufficient. Calibration probes intended to learn these parameters must experience the same full-window channel. Unequal losses or temperatures across modes generally do not commute with the combiner and are not covered by (P1).

If each of $`D`$ layers has fixed power efficiency $`\lambda<1`$, the full efficiency contains $`\lambda^D`$. A growing-depth network therefore need not stay inside a fixed efficiency box. Commutation accounts for that loss; it does not remove it. The fixed-width construction below avoids requiring a sequence of devices of unbounded coherent width to keep the same full-window parameters.

## Arbitrary passive control errors preserve the null test

Under target absence, the $`N`$ idlers are $`\tau_m^{\otimes N}`$. Their joint density is a function of total photon number:

```math
\tau_m^{\otimes N}
=\frac1{(1+m)^N}
\left(\frac m{1+m}\right)^{\widehat N_{\mathrm{tot}}}.
\tag{P3}
```

Every passive $`U(z)`$ preserves $`\widehat N_{\mathrm{tot}}`$. Consequently the null output remains exactly $`\tau_m^{\otimes N}`$ for **any** implemented passive control law, including rounded commands or a poorly aligned bright row. The conditional-null tail and its finite-sample false-alarm guarantee remain exact. A control failure can reduce detection power, but cannot invalidate null calibration within this model.

Let $`w(z)`$ be the normalized first row actually implemented. For $`z\ne0`$, define its captured displacement fraction

```math
\gamma(z)
=\frac{\left|\sum_{j=1}^N w_j(z)z_j^*\right|^2}{\|z\|^2}.
\tag{P4}
```

First suppose a deterministic guarantee $`\gamma(z)\ge\gamma_0>0`$ holds for every nonzero record. The finite-range construction below instead proves it on a specified event and charges its complement. The choice at $`z=0`$ is arbitrary and has zero displacement under either hypothesis.

Under presence, conditional covariance remains $`eI`$ after any passive transformation. The bright displacement energy is at least $`\gamma_0 A\|z\|^2/V`$, using the [model's](model.md) $`A,e,V`$. Put $`u=1-t`$ for $`0<t<1`$. Conditional photon-count generating functions and the exact Gamma law of $`\|z\|^2/V`$ give

```math
\begin{aligned}
\mathbb E_1[t^K]
&\le\frac1{1+eu}
\left(1+\frac{\gamma_0 A u}{1+eu}\right)^{-N}\\
&\le\left(1-
\frac{\gamma_0 A_-u}{1+m_+u}\right)^N.
\end{aligned}
\tag{P5}
```

Here $`A\ge A_-`$, $`m\le m_+`$, and $`e+\gamma_0 A\le m`$. The first inequality includes all atypical return heterodyne records exactly. There is no typical-norm replacement.

With imperfect concentration, the dark outputs can retain displacement, and bright and dark counts need not be independent after averaging over return records. Independence is unnecessary for the following bound. Let $`M=K+S`$ be total idler count. Passive processing preserves it, so under **both** hypotheses

```math
M\sim\mathrm{NB}(N,m).
\tag{P6}
```

In particular $`S\le M`$. For any $`\bar m>m_+`$,

```math
\Pr_1(M>N\bar m)
\le\exp[-N d(\bar m\Vert m_+)],
\tag{P7}
```

where

```math
d(a\Vert b)=a\log\frac ab
-(a+1)\log\frac{a+1}{b+1}.
\tag{P8}
```

Use the constants of the [detection proof](conditional_detection.md), now with the overlap included:

```math
\begin{gathered}
\bar m=0.003,\quad m_+=0.002,\quad u_2=1-e^{-2},\\
L_0=\log\left(1+\frac{19/20}{\bar m}\right),\\
C_{\gamma_0}=-\log\left(1-
\frac{\gamma_0 A_-u_2}{1+m_+u_2}\right),\qquad
r_{\gamma_0}=\frac{C_{\gamma_0}L_0}{L_0+2}.
\end{gathered}
\tag{P9}
```

For $`N\ge20`$, reject when $`p_N(K,M)\le e^{-Nr_{\gamma_0}}`$. The sufficient rejection event is $`M\le N\bar m`$ and $`K\ge\lceil Nr_{\gamma_0}/L_0\rceil`$. Equations (P5)–(P7) give

```math
\begin{aligned}
\alpha_N&\le e^{-Nr_{\gamma_0}},\\
\sup_{\eta,\nu,\theta}\beta_N
&\le e^{-N d(\bar m\Vert m_+)}+e^{-Nr_{\gamma_0}}.
\end{aligned}
\tag{P10}
```

This is a finite-sample guarantee for the actually implemented passive network. It includes misleading internal-reference records, imperfect concentration and every return heterodyne outcome. It remains conditional on the declared effective memory and measurement model.

For the certified box $`n=10^{-3}`$, $`B=10`$, $`\eta_{\mathrm{eff}}\in[0.9,1]`$, $`\nu_{\mathrm{eff}}\in[0,10^{-3}]`$, and $`0<\kappa\le0.1`$, the outward coefficient bound of the detection certificate gives

```math
\frac{r_{\gamma_0}}{\kappa nC_B}
>2.2024530777\,\gamma_0.
\tag{P10a}
```

In particular $`\gamma_0=0.99`$ preserves a strict $`2.18`$ factor. The inequality uses $`-\log(1-v)\ge v`$; the exact rate is not assumed linear in overlap. The [exact rational certificate](../verification/certify_constants.py) and its [stored endpoints](../verification/conditional_memory_certificate.json) also verify $`d(\bar m\Vert m_+)\ge r_{0.99}`$, the finite-control overlap, the dyadic cutoff constants and the fixed-width comparison below.

## Finite classical records and controls

The following construction discretizes ideal heterodyne outcomes with a finite range and uses finite passive commands. It charges every record outside the range used for its power guarantee. It is not a model of finite-local-oscillator measurement statistics.

Under either hypothesis, return variance is between $`v_-=11`$ and $`v_+=11.0001`$. Define

```math
\mathcal G_N=
\left\{\frac{Nv_-}{2}\le\|z\|^2\le2Nv_+\right\}.
\tag{P11}
```

The normalized squared return norm has a Gamma distribution of shape $`N`$. The exponential-sum Chernoff bounds at $`1/2`$ and $`2`$ give

```math
\begin{aligned}
\Pr(\mathcal G_N^c)
&\le e^{-N(\log2-1/2)}+e^{-N(1-\log2)}\\
&\le2e^{-0.19N}.
\end{aligned}
\tag{P12}
```

Use a uniform real-coordinate grid of spacing $`h=10^{-3}`$. Put $`R=\sqrt{2Nv_+}`$ and retain the codes $`kh`$ with $`|k|\le\lceil R/h\rceil`$, so the actual range is $`[-R_h,R_h]`$, where $`R_h=h\lceil R/h\rceil<R+h`$. Flag values outside that actual range. On $`\mathcal G_N`$ there is no overflow, and nearest-code rounding has error at most $`h/2`$ in every real coordinate. If $`\widetilde z`$ is the rounded vector, its relative error obeys

```math
\varepsilon
=\frac{\|z-\widetilde z\|}{\|z\|}
\le\frac{h\sqrt{N/2}}{\sqrt{Nv_-/2}}
=\frac h{\sqrt{v_-}}<10^{-3}.
\tag{P13}
```

Thus $`\widetilde z\ne0`$ on this event. The passive row aligned to $`\widetilde z`$ captures amplitude from the original record at least $`(1-\varepsilon)/(1+\varepsilon)`$, by Cauchy–Schwarz and the two triangle inequalities.

An $`N`$-mode passive combiner with a prescribed first row can be constructed from $`N-1`$ two-mode rotations and phase controls, arranged serially or as a binary tree with appropriate connectivity. Suppose its actual passive unitary differs from that intended for $`\widetilde z`$ by operator norm at most $`\delta_U=10^{-3}`$. The actual captured fraction then satisfies

```math
\gamma(z)\ge
\left(\frac{1-\varepsilon}{1+\varepsilon}-\delta_U\right)^2
>\left(\frac{999}{1001}-\frac1{1000}\right)^2
>\frac{99}{100}.
\tag{P14}
```

Finite angle commands suffice for the stated unitary error. Decompose each two-mode gate into at most three phase or real rotation controls. Rounding each angle to a $`2\pi2^{-b}`$ grid gives gate operator-norm error at most $`3\pi2^{-b}`$. Telescoping the $`N-1`$ gate products gives

```math
\|\widetilde U-U\|\le3\pi(N-1)2^{-b}.
\tag{P15}
```

For example, $`b\ge\lceil\log_2[3000\pi(N-1)]\rceil`$ makes this at most $`10^{-3}`$. The same deterministic budget must include arithmetic and actuator errors if they are present; the rounding allowance cannot simultaneously be spent twice. On overflow or when the rounded vector is zero, apply any declared fixed passive unitary. Such records lie outside the event on which (P14) is required and are charged by (P12). Under absence, any fallback still preserves exact conditional-null calibration.

The coordinate range grows as $`\sqrt N`$, so coordinate and control words both use $`O(\log N)`$ bits. Total recorded and command data use $`O(N\log N)`$ bits. Norms, rotations, certified angle evaluation, switching and feedforward latency remain paid classical and apparatus operations.

On the good event, apply (P5) to the restricted expectation $`\mathbb E[t^K\mathbf1_{\mathcal G_N}]`$ and bound it by the unrestricted Gamma integral. Adding the bad-event term gives

```math
\begin{aligned}
\alpha_N&\le e^{-Nr_{0.99}},\\
\sup_{\eta,\nu,\theta}\beta_N
&\le e^{-Nd(\bar m\Vert m_+)}
+e^{-Nr_{0.99}}+2e^{-0.19N}\\
&\le4e^{-Nr_{0.99}},\\
R_N&\le\frac52e^{-Nr_{0.99}},
\qquad r_{0.99}>2.18\,\kappa nC_B.
\end{aligned}
\tag{P16}
```

The final comparison uses $`d(\bar m\Vert m_+)\ge r_{0.99}`$ and $`0.19>r_{0.99}`$ throughout the certified box. All range, small-norm and misleading-reference records have now been counted. No probabilistic per-gate success assumption is used.

## An exact integer decision with a dyadic cutoff

The optical rounding result above still uses a real exponential cutoff. An exact dyadic cutoff also removes that classical decision-precision idealization. For this variant assume that the known $`\kappa`$ is supplied as a positive rational number in $`(0,0.1]`$. Set

```math
j_N=\left\lceil\frac{N\kappa}{13400}\right\rceil,
\qquad
c_d=\frac{\kappa\log2}{13400},
\qquad
\delta_N=1\ \Longleftrightarrow\ p_N(K,M)\le2^{-j_N}.
\tag{P17}
```

The decision can be made with finite exact integer arithmetic on each observed record:

```math
2^{j_N}\binom{M-K+N-1}{N-1}
\le\binom{M+N-1}{N-1}.
\tag{P18}
```

There is no approximate floating point comparison at a likelihood boundary. The [reference implementation](../verification/receiver.py) evaluates this integer decision. Unbounded counts still require record-dependent integer storage, as explained in [resources](resources.md).

The certificate bounds $`0.693<\log2<0.694`$ and $`1/C_B>41.976`$ give

```math
\frac{c_d}{\kappa nC_B}
>\frac{0.693\times41976}{13400}>2.17,
\qquad
c_d<r_{0.99}.
\tag{P19}
```

For the second inequality, $`c_d/\kappa<0.694/13400<2.18/42000`$ while $`r_{0.99}>2.18\kappa nC_B`$ and $`nC_B>1/42000`$.

False alarm is at most $`2^{-j_N}\le e^{-Nc_d}`$. On $`M\le N\bar m`$, the sufficient bright-count threshold becomes $`\lceil j_N\log2/L_0\rceil`$. Its Chernoff bound gains at most

```math
\exp\left(\frac{2\log2}{L_0}\right)
=2^{2/L_0}<1.3
\tag{P20}
```

from the ceiling in $`j_N`$. The inequality $`c_d\le r_{0.99}`$ makes the remaining exponent at least $`c_d`$. Adding the total-count and return-record failure terms therefore gives

```math
\alpha_N\le e^{-Nc_d},\qquad
\beta_N<4.3e^{-Nc_d},\qquad
R_N\le3e^{-Nc_d}.
\tag{P21}
```

Thus finite coordinate range, finite passive commands, an exact integer decision and every bad-record probability retain a certified exponent greater than $`2.17\kappa nC_B`$. The continuous heterodyne and ideal photon-counting measurement models remain explicit physical assumptions.

## A fixed-width protocol with a strict advantage

The single-block asymptotic factor uses increasing coherent block size. One can instead fix the coherent width at a finite value selected from the known reflectivity and repeat that apparatus. The resulting certified factor is smaller, but it avoids assuming uniform memory quality for an unbounded family of block widths.

For a fixed known $`0<\kappa\le0.1`$, choose

```math
L=\left\lceil\frac{2\times10^6}{\kappa}\right\rceil,
\qquad
c_d=\frac{\kappa\log2}{13400},
\qquad
C_B=(\sqrt{B+1}-\sqrt B)^2.
\tag{P22}
```

Use $`L`$ modes per block and the preceding finite-range, finite-control receiver with exact dyadic decisions. Equation (P21) implies that each type of error is at most $`\delta=5e^{-Lc_d}<1/2`$. Here $`L\ge2\times10^7`$ and $`Lc_d>100`$, so the displayed bound is well inside $`1/2`$.

Run $`J`$ independent blocks using the same stationary full-window memory, and declare presence when more than half the block decisions declare presence, with any fixed tie rule. Their errors are independent under each hypothesis, and the phase does not enter their count laws. The binomial Chernoff bound gives

```math
R_{J,L}\le
\bigl[2\sqrt{\delta(1-\delta)}\bigr]^J,
\tag{P23}
```

so the error exponent per transmitted signal is at least

```math
\frac{-\log[2\sqrt{\delta(1-\delta)}]}L
\ge\frac{c_d}2-\frac{\log20}{2L}
>1.05\,\kappa nC_B.
\tag{P24}
```

For the last strict inequality, $`c_d/(\kappa nC_B)>2.17`$, $`nC_B>1/42000`$, $`\log20<3`$ and $`L\kappa\ge2\times10^6`$ suffice: the ratio is greater than $`1.085-0.0315=1.0535`$. The width $`L`$ is large; at $`\kappa=0.1`$ it is twenty million idler modes. This is an existence theorem with an explicit finite apparatus width, not a near-term size estimate or an optimized block construction.

The large-sample limit in (P24) is $`J\to\infty`$ at fixed $`L,\kappa`$. Full-window attenuation and added noise need remain inside the box for this one fixed block apparatus, rather than for devices of increasing width. The same fixed channel must repeat independently across blocks. All $`JL`$ target signals, all local calibration probes, and all block decisions are counted.

The $`1.05`$ factor concerns transmitted signal energy. It does not retain a certified factor above two, so it does not establish an advantage after charging both source beams equally. Its role is to resolve the growing-coherent-width assumption while retaining a strict comparison with the phase-informed coherent-mixture benchmark allowing global reception.
