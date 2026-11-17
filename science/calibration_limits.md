# Calibration reliability and a measurement-specific obstruction

Learning a memory consistently and certifying it with an exponentially small error probability are different tasks. For positive added noise, arbitrarily bright calibration probes cannot replace an adequate number of memory-channel uses. A detector can nevertheless avoid making its reliability depend on that certification task. The results below explain both statements and delimit the architecture to which the detection obstruction applies.

## 1. Memory channel and calibration experiment

The stationary, independently repeated memory is a phase-insensitive Gaussian channel with power transmissivity $`0\lt\eta\le1`$ and added output occupation $`\nu\ge0`$. On an input of occupation $`x`$, its output occupation is $`\eta x+\nu`$. Its first-moment attenuation is $`\sqrt\eta`$.

Write $`\mathcal L_{\eta,0}`$ for vacuum loss. For $`\nu>0`$, the memory has the exact random-displacement representation

```math
\begin{aligned}
\mathcal L_{\eta,\nu}&=\mathcal A_\nu\circ\mathcal L_{\eta,0},\\
\mathcal A_\nu(\rho)&=\int_{\mathbb C}p_\nu(\alpha)
D(\alpha)\rho D(\alpha)^\dagger\,d^2\alpha,\\
p_\nu(\alpha)&=\frac1{\pi\nu}e^{-|\alpha|^2/\nu}.
\end{aligned}
\tag{L1}
```

Here $`\mathbb E|\alpha|^2=\nu`$. Thus the displacement adds occupation $`\nu`$, and the channel is the usual thermal attenuator with environmental occupation $`\nu/(1-\eta)`$ when $`\eta<1`$. At $`\eta=1`$ it is the additive-noise channel. Equation (L1) specifies the channel on arbitrary inputs, including inputs entangled with a reference; it is not only a statement about coherent probes.

One direct verification uses the Weyl characteristic function $`\chi_\rho(z)=\operatorname{Tr}[\rho D(z)]`$. Vacuum loss sends it to $`\chi_\rho(\sqrt\eta z)e^{-(1-\eta)|z|^2/2}`$, and the Gaussian displacement integral multiplies it by $`e^{-\nu|z|^2}`$. Thus (L1) has characteristic function

```math
\chi_{\mathcal L_{\eta,\nu}(\rho)}(z)
=\chi_\rho(\sqrt\eta z)
\exp\!\left[-\left(\frac{1-\eta}{2}+\nu\right)|z|^2\right],
\tag{L1a}
```

which specifies the stated Gaussian memory. The random-displacement representation is a standard Gaussian-channel description; see [Eisert and Wolf, Section 2.3, Eq. (9)](https://arxiv.org/html/quant-ph/0505151v1).

A calibration strategy calls the memory at most $`K`$ times. It may prepare arbitrary probe states, retain arbitrary ancillary systems, adapt its quantum operations between calls, and perform any final measurement. No bound on probe energy is imposed. The initial strategy and its controls cannot depend on the unknown noise value. A strategy using fewer than $`K`$ calls can be padded with calls whose outputs are discarded.

The loss $`\eta`$ may be supplied to this calibrator. A lower bound with that information remains a lower bound when the loss is also unknown.

## 2. An energy-independent calibration bound

**Theorem L1 — common component of two noise channels.** Fix $`\eta`$ and two distinct strictly positive noise values $`\nu_0,\nu_1`$. Put

```math
w(\alpha)=\min\{p_{\nu_0}(\alpha),p_{\nu_1}(\alpha)\},
\qquad
\zeta=\int_{\mathbb C}w(\alpha)\,d^2\alpha.
\tag{L2}
```

Then $`0<\zeta<1`$. The two final calibration states of every allowed $`K`$-call strategy satisfy

```math
\frac12\|\sigma_0-\sigma_1\|_1\le1-\zeta^K.
\tag{L3}
```

Their optimal equal-prior discrimination error is therefore at least $`\zeta^K/2`$, independently of the calibration energy.

**Proof.** Define the common channel

```math
\mathcal C(\rho)=\frac1\zeta\int_{\mathbb C}w(\alpha)
D(\alpha)\mathcal L_{\eta,0}(\rho)D(\alpha)^\dagger\,d^2\alpha.
\tag{L4}
```

It is completely positive and trace preserving. For $`i=0,1`$, the residual density $`p_{\nu_i}-w`$ is nonnegative and has integral $`1-\zeta`$. Consequently there are channels $`\mathcal R_i`$ such that

```math
\mathcal L_{\eta,\nu_i}=\zeta\mathcal C+(1-\zeta)\mathcal R_i.
\tag{L5}
```

Expand each of the $`K`$ channel calls in the adaptive strategy using (L5). The branch in which every call uses $`\mathcal C`$ has weight $`\zeta^K`$ under both noise values. Its normalized output state $`\sigma_{\mathcal C}`$ is identical under the two values, since the initial state, every interleaved operation, and all invoked channels on that branch are identical. Thus

```math
\sigma_i=\zeta^K\sigma_{\mathcal C}+(1-\zeta^K)\tau_i,
\tag{L6}
```

for density operators $`\tau_i`$. Taking trace norms gives (L3). The Helstrom formula gives the claimed error lower bound. The argument includes adaptive instruments and retained quantum registers; subsequent measurements and processing cannot increase trace distance. ∎

The overlap is elementary. If $`r=\nu_0/\nu_1>1`$, the Gaussian densities cross at squared radius

```math
s=\frac{\nu_0\nu_1\log r}{\nu_0-\nu_1}.
```

Integration inside and outside that circle yields

```math
\begin{aligned}
\zeta
&=1-e^{-s/\nu_0}+e^{-s/\nu_1}\\
&=1-r^{-1/(r-1)}+r^{-r/(r-1)}\\
&=1-(r-1)r^{-r/(r-1)}.
\end{aligned}
\tag{L7}
```

For example, $`r=2`$ gives $`\zeta=3/4`$.

**Corollary L2 — certification requires memory uses.** Suppose an estimator must estimate $`\nu`$ with absolute error at most $`\epsilon<|\nu_0-\nu_1|/2`$ uniformly at these two points. Then

```math
\max_{i=0,1}
\Pr_{\nu_i}(|\widehat\nu-\nu_i|>\epsilon)
\ge\frac12\zeta^K.
\tag{L8}
```

Indeed, choosing the nearer of $`\nu_0,\nu_1`$ from the estimate produces a binary test whose error is no larger than the estimation failure probability. If the required uniform failure probability is at most $`e^{-r_0N}`$, with $`r_0>0`$, then necessarily

```math
K\ge\frac{r_0N-\log2}{|\log\zeta|}.
\tag{L9}
```

The result does not prevent consistent estimation with $`K=o(N)`$. It prevents exponentially reliable certification on the scale $`N`$ with that number of calls, even when calibration photons are unrestricted. The two selected noise values must be strictly positive; no overlap claim is made between a zero-noise point and a positive-noise point.

## 3. Exact confounding in a frozen one-output OPA receiver

This section adds a particular target-detection stage. It is an architectural obstruction, not a lower bound for every quantum-illumination receiver.

The target stage uses $`N`$ independent two-mode squeezed-vacuum pairs of brightness $`n>0`$. Reflectivity $`0\lt\kappa\lt1`$ and background occupation $`B>0`$ are known, with the matched-background convention. Give the receiver the true target phase and fix the OPA gain $`G>1`$ before calibration. Each return–idler pair is measured at that aligned phase, retaining only one OPA output photon count. The other quantum outputs are discarded.

The calibration stage has no target interaction. Its inputs are prepared independently of the main pairs. Its records may be used for the final decision, including an arbitrary final measurement of a retained calibration quantum register together with the classical main record. They do not change the main-stage gain, phase, brightness or measurement. No calibration ancilla is coupled coherently to a main signal, idler or return before its prescribed photon count. Independent channel environments make the calibration and main stages a product experiment at each fixed physical parameter.

For the selected OPA output, put

```math
\begin{aligned}
q(\nu)&=G(\eta n+\nu)+(G-1)(B+1),\\
b&=2\sqrt{G(G-1)\eta n(n+1)},\\
\delta&=(G-1)n\kappa.
\end{aligned}
\tag{L10}
```

The count law is geometric. Its mean is $`q(\nu)`$ under absence and $`q(\nu)+b\sqrt\kappa+\delta`$ under presence at the supplied aligned phase.

**Theorem L3 — sublinear local calibration cannot repair this receiver.** Suppose the allowed noise interval contains two strictly positive values satisfying

```math
\nu_0-\nu_1=\frac{b\sqrt\kappa+\delta}{G}.
\tag{L11}
```

For every allowed $`K`$-call quantum calibration strategy and every final decision using its complete output and all main counts, the uniform common-parameter risk obeys

```math
R_{N,K}
=\sup_{\nu}\frac{\alpha_{N,K}(\nu)+\beta_{N,K}(\nu)}2
\ge\frac14\zeta^K,
\tag{L12}
```

where $`\zeta`$ is the overlap in (L2) for $`\nu_0,\nu_1`$. In particular, if $`K=o(N)`$, the optimal risk has zero error exponent per main target use.

**Proof.** Equation (L11) gives the exact identity

```math
q(\nu_0)=q(\nu_1)+b\sqrt\kappa+\delta.
\tag{L13}
```

Thus the complete main-count record has identical law under $`H_0,\nu_0`$ and $`H_1,\nu_1`$, for every $`N`$. Their accessible final states are $`\sigma_0\otimes Q_N`$ and $`\sigma_1\otimes Q_N`$, with one common classical law $`Q_N`$. Theorem L1 gives

```math
\alpha_{N,K}(\nu_0)+\beta_{N,K}(\nu_1)\ge\zeta^K.
\tag{L14}
```

Since all error probabilities are nonnegative,

```math
R_{N,K}
\ge\frac12\max\{\alpha_{N,K}(\nu_0),\beta_{N,K}(\nu_1)\}
\ge\frac14\zeta^K.
```

The constant-guess decision has risk $`1/2`$. Together with (L12), this shows that $`-N^{-1}\log R_{N,K}^*\to0`$ when $`K=o(N)`$. ∎

For the stronger convention $`[\sup_\nu\alpha(\nu)+\sup_\nu\beta(\nu)]/2`$, the lower bound is $`\zeta^K/2`$. The factor $`1/4`$ in (L12) is appropriate when one common nuisance value remains inside the displayed hypothesis average.

Every actual experiment still has a single memory channel common to target absence and presence. The proof compares two different admissible parameter points because one uniform decision procedure must work at both. It does not posit a channel that changes with the hypothesis.

If the allowed noise interval has nonzero width, condition (L11) can be met for sufficiently small fixed positive $`\kappa`$. The obstruction already holds with loss and target phase supplied, and with arbitrarily energetic adaptive quantum calibration. Its cause is exact confounding in the prescribed main measurement. A receiver retaining a correlation statistic that cannot be imitated by a memory-noise shift is outside this theorem. Calibration-dependent main measurements and joint quantum coupling to calibration ancillas are also outside its assumptions.

## 4. Restricted appendix: the exact direct-count calibration allocation law

This appendix quantifies the calibration tax for one explicit, narrower strategy. It is not an optimum over all quantum calibration probes or all target receivers.

Supply the loss $`\eta>0`$ and target phase. Keep a fixed gain $`G>1`$. Let $`m=\eta n+\nu`$ range over a nondegenerate compact interval $`[m_-,m_+]`$, with $`m_->0`$. Take $`K_N`$ local calibration probes whose input states are thermal of known occupation $`n`$, and directly photon-count the memory outputs. Their counts are independent geometric variables of mean $`m`$. They transmit no signal toward the target. The $`N`$ main counts are those in (L10). Let

```math
\frac{K_N}{N}\longrightarrow\rho>0,
\qquad
q(m)=Gm+(G-1)(B+1),
\qquad t=\sqrt\kappa.
\tag{L15}
```

All calibration and main counts are available to the final decision. Let $`R_{N,K_N}^*`$ be the minimum common-parameter risk for these prescribed measurements. Define

```math
\begin{aligned}
D_m&=m(1+m),&D_q&=q(m)[1+q(m)],\\
J(m)&=\frac{b^2}{D_q},&
\lambda(m)&=\frac{G^2D_m}{D_q}.
\end{aligned}
\tag{L16}
```

**Theorem L4 — sharp allocation law for this strategy.** At every fixed $`0\lt\kappa\lt1`$, the large-$`N`$ exponent exists. For every fixed $`\rho>0`$, as $`\kappa\downarrow0`$ it satisfies

```math
\begin{aligned}
E_\rho(\kappa)
&=\lim_{N\to\infty}-\frac1N\log R_{N,K_N}^*\\
&=\frac{\kappa J(m_+)}8
\frac{\rho}{\rho+\lambda(m_+)}+O(\kappa^{3/2}).
\end{aligned}
\tag{L17}
```

The order is $`N\to\infty`$ first and then $`\kappa\downarrow0`$, with $`n,B,G,\eta,[m_-,m_+],\rho`$ fixed. No assertion about a joint limit with $`\rho\downarrow0`$ is made.

### 4.1 Exact count-rate formula

For geometric counts define

```math
d(z\Vert\mu)
=z\log\frac z\mu-(z+1)\log\frac{z+1}{\mu+1},
\qquad z\ge0,\quad\mu>0,
\tag{L18}
```

with its continuous value at zero. For the calibration and main sample means $`z=(z_c,z_d)`$, put

```math
\begin{aligned}
I_0(z;m)&=\rho d(z_c\Vert m)+d(z_d\Vert q(m)),\\
I_1(z;m)&=\rho d(z_c\Vert m)
+d(z_d\Vert q(m)+bt+(G-1)nt^2).
\end{aligned}
\tag{L19}
```

Then

```math
\begin{aligned}
E_\rho(\kappa)
&=\inf_{z_c,z_d\ge0}
\max\left\{\min_m I_0(z;m),\min_m I_1(z;m)\right\}\\
&=\inf_{z_c,z_d\ge0,\,m_0,m_1\in[m_-,m_+]}
\max\{I_0(z;m_0),I_1(z;m_1)\}.
\end{aligned}
\tag{L20}
```

To verify existence and (L20), the sum of $`M`$ geometric counts has mass

```math
Q_{M,\mu}(s)=\binom{s+M-1}{M-1}
\frac{\mu^s}{(1+\mu)^{s+M}}.
```

Its exact type bounds are

```math
\frac{M}{(M+s)(M+s+1)}e^{-M d(s/M\Vert\mu)}
\le Q_{M,\mu}(s)\le e^{-M d(s/M\Vert\mu)}.
\tag{L21}
```

The two count sums are sufficient, and their parameter-independent combinatorial factors cancel in the composite likelihood ratio. The full-record GLRT compares the two minimized rates in (L20). On a bounded box there are polynomially many count types. On its error region, the actual rate is at least the maximum of those two minimized rates. Uniform exponential geometric tails handle the complement, since all model means lie in a compact positive interval. These observations give the exponent lower bound for that test.

Conversely, fix a point in the minimization (L20), round the two count sums to the nearest admissible types, and apply the lower bound in (L21) under its two chosen nuisance values. The overlap of those types is at least a polynomial factor times the exponential of the negative maximum rate. Every final test therefore has a risk at least one quarter of this overlap under the common-parameter convention. Continuity, followed by minimization, gives the converse. Compactness of the nuisance interval and coercivity in the two observed means justify passage to minima on sufficiently large boxes. Replacing $`\rho`$ by $`K_N/N`$ has no effect on the limit.

### 4.2 Uniform local expansion

There is a candidate in (L20) of order $`t^2`$, obtained by taking a common interior $`m`$ and observed means halfway between the two mean vectors. Thus any minimizing sequence can be restricted to objective at most $`Ct^2`$ for a constant $`C`$.

Uniform positivity and compactness of the model means, together with coercivity of (L18), first bound the observed means. The only zero of $`d(z\Vert\mu)`$ is $`z=\mu`$; its second derivative there is $`1/[\mu(1+\mu)]`$. Hence an objective of order $`t^2`$ forces every observed mean to lie within $`O(t)`$ of both corresponding model means. In particular $`m_1-m_0=O(t)`$. On that localized set the Taylor expansion

```math
d(z\Vert\mu)=\frac{(z-\mu)^2}{2\mu(1+\mu)}+O(t^3)
\tag{L22}
```

is uniform. The constants can depend on the fixed positive $`\rho`$ and fixed model interval.

Write $`m=(m_0+m_1)/2`$ and $`h=(m_1-m_0)/t`$. To leading order the two calibration/main mean vectors differ by

```math
t\,(h,Gh+b).
```

For fixed $`m,h`$, minimizing the maximum of the two quadratic distances over the observed record gives one eighth of the squared separation. This follows from the triangle inequality in the weighted Euclidean norm; equality occurs at the midpoint. The local coefficient is therefore

```math
\frac18\min_{h\in\mathbb R}
\left\{\frac{\rho h^2}{D_m}+\frac{(Gh+b)^2}{D_q}\right\}.
\tag{L23}
```

Direct minimization gives

```math
h_*=-\frac{GbD_m}{\rho D_q+G^2D_m},
\qquad
\min_h\left\{\frac{\rho h^2}{D_m}+\frac{(Gh+b)^2}{D_q}\right\}
=\frac{b^2\rho}{\rho D_q+G^2D_m}
=J(m)\frac{\rho}{\rho+\lambda(m)}.
\tag{L24}
```

Both $`D_m`$ and $`D_q`$ increase with $`m`$, so the smallest coefficient is at $`m_+`$. The endpoint does not obstruct attainment: choose $`m_0=m_+`$ and $`m_1=m_++h_*t`$. Since $`h_*<0`$ and the interval has nonzero width, these are admissible for sufficiently small $`t`$. Their midpoint observed record is positive. The uniform expansion changes its coefficient only by $`O(t)`$ and its rate by $`O(t^3)`$. This supplies the matching upper bound; the unrestricted minimization in (L23) and the same uniform expansion supply the lower bound. Equations (L17) follow.

### 4.3 Resource meaning

There are $`N+K_N`$ memory-channel uses, $`N`$ target uses, target signal occupation $`Nn`$, and calibration input occupation $`K_Nn`$ in this appendix. Source preparation, storage, pump operation, measurements and processing are additional apparatus resources; none is supplied by the error coefficient.

Per total memory use, the leading coefficient in (L17) is divided by $`1+\rho`$. Within this calibration strategy it is maximized at

```math
\rho_* =\sqrt{\lambda(m_+)},
\qquad
\max_{\rho>0}
\frac{\rho}{(\rho+\lambda)(1+\rho)}
=\frac1{(1+\sqrt\lambda)^2}.
\tag{L25}
```

This is an allocation optimum for the stated direct-count calibration and fixed-gain main measurement. It is not a universal quantum calibration bound.

For comparison at equal transmitted target energy $`Nn`$, let

```math
C_B=(\sqrt{B+1}-\sqrt B)^2,
\qquad A=\frac{J(m_+)}{8nC_B}.
```

The strong phase-informed coherent-mixture benchmark has exponent $`\kappa nC_B`$ per main use. The leading ratio for this prescribed calibrated receiver is $`A\rho/(\rho+\lambda)`$. If $`A>1`$, it exceeds one exactly when $`\rho>\lambda/(A-1)`$. Local calibration sends no target photons here. Per total memory use, both equal-transmitted-energy exponents acquire the factor $`1/(1+\rho)`$. Comparing instead with a classical transmitter using brightness $`n`$ in all $`N+K_N`$ slots grants it additional transmitted energy and is a different resource comparison.
