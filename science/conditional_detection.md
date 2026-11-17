# Exact conditional detection with unknown memory

[Model and charged calibration](model.md) · [Calibration reliability limits](calibration_limits.md)

Counting the orthogonal outputs of a correlation-to-displacement receiver gives an exact conditional test whose false-alarm law does not contain the unknown idler-memory brightness. The theorem below provides an operational decision rule and a finite-sample error bound. It includes misleading internal-reference records and every heterodyne outcome. It does not claim the optimal quantum exponent.

## 1. Experiment and error convention

Use the stationary independent Gaussian-memory and matched-background target model of [the model page](model.md). The source brightness $`n`$, background $`B`$ and reflectivity $`\kappa`$ are known. The memory parameters $`\lambda=(\eta,\nu)`$ are fixed but unknown, and the same $`\lambda`$ applies under both target hypotheses. The target phase $`\theta`$ is unknown and common to all $`N`$ pairs.

For a decision rule $`\delta_N`$ taking value one for target presence, write

**Equation (D1).**

```math
\alpha_N(\lambda)=\Pr_{0,\lambda}(\delta_N=1),
\qquad
\beta_N(\lambda,\theta)=\Pr_{1,\lambda,\theta}(\delta_N=0),
```

and use the same-memory worst-case symmetric risk

**Equation (D2).**

```math
R_N=\sup_{\lambda,\theta}
\frac{\alpha_N(\lambda)+\beta_N(\lambda,\theta)}2.
```

The upper bound also holds if the two errors are maximized separately, since both will be bounded uniformly. No parameter is switched between the hypotheses within a physical experiment.

The optical policy heterodynes all returns, concentrates the conditional idler displacement into one output with the recorded weights $`z_j/\Vert z\Vert`$, and photon-counts that output and all orthogonal outputs. Let $`K`$ be the bright count, $`S`$ the sum of orthogonal-output counts and $`M=K+S`$.

Define

**Equation (D3).**

```math
m=\eta n+\nu,
\qquad V=B+\kappa n+1,
\qquad A=\frac{\eta\kappa n(n+1)}V,
\qquad e=m-A.
```

All equations below are exact at fixed $`N`$ and fixed $`\kappa`$.

## 2. Exact optical-to-classical reduction

### Conditional Gaussian state

Under target presence, the return heterodyne vector has density

**Equation (D4).**

```math
f_1(z)=\frac{e^{-\Vert z\Vert^2/V}}{(\pi V)^N}.
```

Put $`c=\sqrt{\eta\kappa n(n+1)}`$. Gaussian conditioning leaves the idlers in a product of displaced thermal states with occupation $`e=m-c^2/V`$ and displacements

**Equation (D5).**

```math
d_j=e^{i\theta}\frac{c z_j^*}{V}.
```

For example, the heterodyne covariance adds one vacuum unit to the return occupation, giving the Schur-complement subtraction $`c^2/(B+\kappa n+1)`$ in the idler occupation. This is the noisy-memory version of the conditional state used in [Chen and Zhuang, Section III](https://arxiv.org/html/2212.08190v1). Correlation-to-displacement conversion and unknown-phase bright-output counting are inherited receiver ingredients.

A passive transformation with first row $`z_j/\Vert z\Vert`$ takes the displacement vector to

**Equation (D6).**

```math
\left(e^{i\theta}\frac{c\Vert z\Vert}{V},0,\ldots,0\right).
```

The conditional thermal covariance is proportional to the identity, so the transformation leaves it a product of identical thermal covariances. Thus, conditioned on $`z`$, the orthogonal outputs are mutually independent thermal states of occupation $`e`$ and are independent of the bright output. Their conditional law does not depend on $`z`$, which also proves unconditional independence of $`K`$ and $`S`$ after the return record is integrated.

Under target absence, the idlers are $`\tau_m^{\otimes N}`$, independent of the return measurements. This product state is invariant under every passive transformation. Consequently all $`N`$ output counts are independent geometric counts of mean $`m`$, even though the commanded transformation depends on the return record.

### Integrating every heterodyne record

For $`v\ge0`$, let

**Equation (D7).**

```math
d_v(t)=1+v(1-t),\qquad 0\le t\le1.
```

A displaced thermal state of residual occupation $`e`$ and displacement energy $`D`$ has photon-count probability generating function

**Equation (D8).**

```math
F_{e,D}(t)=\frac1{d_e(t)}
\exp\left[-\frac{D(1-t)}{d_e(t)}\right].
```

One derivation integrates the coherent-state photon generating function against the thermal state's circular Gaussian displacement density. The formula extends continuously to $`e=0`$.

Here $`D=c^2\Vert z\Vert^2/V^2`$ and $`\Vert z\Vert^2/V`$ has a gamma distribution of shape $`N`$ and unit scale. Its exact Laplace transform gives

**Equation (D9).**

```math
\begin{aligned}
\mathbb E_1[t^K]
&=\frac1{d_e(t)}
\left[1+\frac{A(1-t)}{d_e(t)}\right]^{-N}\\
&=\frac{d_e(t)^{N-1}}{d_m(t)^N}.
\end{aligned}
```

This integration includes rare small and large return norms. It is not a replacement of the return norm by its expectation.

Let $`\mathrm{Geom}(v)`$ denote the distribution on nonnegative integers of mean $`v`$, with probabilities $`v^k/(1+v)^{k+1}`$. Let $`\mathrm{NB}(r,v)`$ denote the sum of $`r`$ such independent counts. The exact laws are

**Equation (D10).**

```math
\begin{array}{c|c|c}
 & K&S\\\hline
H_0&\mathrm{Geom}(m)&\mathrm{NB}(N-1,m)\\[2pt]
H_1&\displaystyle\mathbb E_1[t^K]=\frac{d_e(t)^{N-1}}{d_m(t)^N}
&\mathrm{NB}(N-1,e).
\end{array}
\qquad K\perp S.
```

Equivalently, the joint generating function under presence is

**Equation (D11).**

```math
\mathbb E_1[t^K u^S]
=\frac{d_e(t)^{N-1}}{d_m(t)^N d_e(u)^{N-1}}.
```

For an explicitly positive representation of the bright distribution, let $`K_e\sim\mathrm{Geom}(e)`$ and let $`W_1,\ldots,W_N`$ be independent of it. Each $`W_j`$ is zero with probability $`1-A/(1+m)`$ and otherwise is a positive geometric count of mean $`1+m`$. Then

**Equation (D12).**

```math
K\overset{d}=K_e+\sum_{j=1}^N W_j,
\qquad
\mathbb E[t^{W_j}]=\frac{d_e(t)}{d_m(t)}.
```

This representation uses $`0\le A\le m`$ and verifies the positivity of the generating-function law directly.

### Total count is a hypothesis-neutral reference

Setting $`t=u`$ in (D11) cancels the residual occupation. Under either hypothesis,

**Equation (D13).**

```math
M=K+S\sim\mathrm{NB}(N,m).
```

This also follows from conservation of total idler photon number by the controlled passive transformation. In particular, $`M/N`$ estimates the true memory occupation $`m`$ with mean $`m`$ and variance $`m(1+m)/N`$ under both hypotheses. The dark sum alone has mean $`(N-1)e`$ under presence and must not be treated as a separate target-independent calibration stream.

Every displayed count probability is independent of $`\theta`$. The receiver does not estimate the common target phase, so its guarantee has no omitted phase-learning failure event.

## 3. An exact conditional-null test

Under absence, condition on a total $`M`$. The joint geometric probability of an allocation $`(k_1,\ldots,k_N)`$ depends only on that total. Every allocation of $`M`$ nonnegative photons among $`N`$ outputs therefore has the same conditional probability. For $`N\ge2`$,

**Equation (D14).**

```math
\Pr_0(K=k\mid M)
=\frac{\binom{M-k+N-2}{N-2}}
{\binom{M+N-1}{N-1}},\qquad 0\le k\le M.
```

The sum of these masses over $`k\ge K`$ is the exact conditional upper tail

**Equation (D15).**

```math
p_N(K,M)=
\frac{\binom{M-K+N-1}{N-1}}
{\binom{M+N-1}{N-1}}.
```

It contains neither $`m`$ nor the memory parameters. As an ordinary discrete tail p-value, it is super-uniform:

**Equation (D16).**

```math
\Pr_0\{p_N(K,M)\le\epsilon\mid M\}\le\epsilon,
\qquad 0\le\epsilon\le1.
```

To check this without a continuity approximation, select the smallest count whose upper tail is at most $`\epsilon`$. The rejection event is that upper tail, so its probability is at most $`\epsilon`$. If no such count exists, the rejection event is empty. At $`M=0`$, $`p_N=1`$. Thus the construction remains meaningful also at the degenerate null $`m=0`$, although that case is outside the positive-memory box of the separation theorem.

For any declared $`r\gt 0`$, the test

**Equation (D17).**

```math
\delta_N=1\quad\Longleftrightarrow\quad
p_N(K,M)\le e^{-Nr}
```

has $`\alpha_N(\lambda)\le e^{-Nr}`$ for every memory occupation, at finite $`N`$. It uses no plug-in estimate of the null distribution.

## 4. Uniform finite-sample advantage theorem

Assume the explicit bounded regime

**Equation (D18).**

```math
n=\frac1{1000},\quad B=10,\quad
\eta\in\left[\frac9{10},1\right],\quad
\nu\in\left[0,\frac1{1000}\right],\quad
0\lt \kappa\le\frac1{10},\quad N\ge20.
```

Set

**Equation (D19).**

```math
m_* =\frac1{500},\qquad
\bar m=\frac3{1000},\qquad
u_2=1-e^{-2},
```

**Equation (D20).**

```math
A_* =\frac{(9/10)\kappa n(n+1)}{B+\kappa n+1},
\qquad
L=\log\left(1+\frac{19/20}{\bar m}\right),
```

and

**Equation (D21).**

```math
C=-\log\left(1-\frac{A_*u_2}{1+m_*u_2}\right),
\qquad
r=\frac{CL}{L+2}.
```

The symbol $`u_2`$ is a fixed Chernoff constant, unrelated to the physical added-noise parameter $`\nu`$. All logarithms are natural. These constants use only declared bounds and known target/source quantities.

**Theorem.** The operational test (D17), with (D19)–(D21), satisfies

**Equation (D22).**

```math
\boxed{\quad
R_N\le\frac32 e^{-Nr},
\qquad
r\gt \frac{11}{5}\,\kappa n C_B,
\qquad
C_B=(\sqrt{B+1}-\sqrt B)^2.
\quad}
```

The bound is uniform over all memory parameters in (D18) and every fixed common target phase. It is a finite-sample upper bound with its prefactor displayed. It guarantees a large-sample exponent exceeding $`2.2`$ times the strong phase-informed coherent-mixture exponent at the same transmitted signal energy. It does not assert that the two receivers' actual finite-sample errors are ordered for every $`N\ge20`$, nor that $`r`$ is the optimal quantum exponent.

### Proof: exact false-alarm control

Equation (D16), averaged over the total count, gives

**Equation (D23).**

```math
\alpha_N(\lambda)\le e^{-Nr}.
```

No favorable reference record is assumed.

### Proof: separate a misleading-reference event

For $`M\gt 0`$, the product form of (D15) gives

**Equation (D24).**

```math
p_N(K,M)
=\prod_{j=0}^{K-1}\frac{M-j}{M+N-1-j}
\le\left(\frac M{M+N-1}\right)^K.
```

The empty product at $`K=0`$ is one. On $`0\lt M\le N\bar m`$ with $`N\ge20`$,

**Equation (D25).**

```math
\log\left(1+\frac{N-1}{M}\right)
\ge\log\left(1+\frac{1-1/N}{\bar m}\right)
\ge L.
```

Consequently $`M\le N\bar m`$ and $`K\ge\lceil Nr/L\rceil`$ imply target acceptance. The event $`M=0`$ has $`K=0\lt \lceil Nr/L\rceil`$, so it is covered as well. Every miss is therefore in

**Equation (D26).**

```math
\{M\gt N\bar m\}\ \cup\ 
\left\{K\lt \left\lceil\frac{Nr}{L}\right\rceil\right\}.
```

The first event includes reference records whose excessive total count could conceal a target. It is bounded rather than discarded.

### Proof: total-count tail

For geometric observations define

**Equation (D27).**

```math
d(x\Vert y)
=x\log\frac xy-(x+1)\log\frac{x+1}{y+1}.
```

Because $`M\sim\mathrm{NB}(N,m)`$ under presence and $`m\le m_*\lt \bar m`$, the geometric Chernoff bound yields

**Equation (D28).**

```math
\Pr_1(M\gt N\bar m)
\le e^{-N d(\bar m\Vert m_*)}.
```

For completeness, the moment generating function of one geometric count is $`[1-y(e^t-1)]^{-1}`$. Optimizing the exponential Markov bound at an upper-tail threshold $`x\gt y`$ gives (D27). Increasing the geometric mean increases the upper-tail probability, so replacing the unknown $`m`$ by $`m_*`$ is valid. Equation (D13), rather than an assumption about the dark modes' mean, is essential here.

The second derivative of $`d(x\Vert y)`$ in $`x`$ is $`1/[x(1+x)]`$. Taylor's theorem on $`[m_*,\bar m]`$ gives

**Equation (D29).**

```math
d(\bar m\Vert m_*)
\ge\frac{(\bar m-m_*)^2}{2\bar m(1+\bar m)}
=\frac1{6018}\gt 10^{-4}.
```

### Proof: bright-output lower tail

Use (D9) at $`t=e^{-2}`$. Since $`e\ge0`$, $`A\ge A_*`$ and $`m\le m_*`$,

**Equation (D30).**

```math
\begin{aligned}
\mathbb E_1 e^{-2K}
&=\frac1{1+e u_2}
\left(1-\frac{A u_2}{1+m u_2}\right)^N\\
&\le\left(1-\frac{A_*u_2}{1+m_*u_2}\right)^N
=e^{-NC}.
\end{aligned}
```

The bracket is positive because $`A\le m`$. Each inequality is uniform in the true memory parameters.

Set $`a=Nr/L`$. An integer $`K\lt \lceil a\rceil`$ satisfies $`K\le\lceil a\rceil-1\lt a`$. Applying exponential Markov with this strict inequality introduces no ceiling prefactor:

**Equation (D31).**

```math
\Pr_1\left(K\lt \left\lceil\frac{Nr}{L}\right\rceil\right)
\le e^{2Nr/L}\mathbb E_1e^{-2K}
\le e^{-N(C-2r/L)}
=e^{-Nr}.
```

The final equality is exactly the choice $`r=CL/(L+2)`$.

Finally $`r\lt C\lt 10^{-5}`$. To verify the upper bound, put

**Equation (D32).**

```math
A_{\max}=\frac{(9/10)(1/10)n(n+1)}{B+1}.
```

Then $`A_*\le A_{\max}`$ and $`C\le A_{\max}/(1-A_{\max})\lt 10^{-5}`$, using $`-\log(1-v)\le v/(1-v)`$ for $`0\le v\lt 1`$. Thus (D29) is larger than $`r`$. Combining (D26), (D28) and (D31) gives $`\beta_N(\lambda,\theta)\le2e^{-Nr}`$. Together with (D23), this proves the risk bound in (D22).

### Proof: strict strong-classical separation

The elementary strict inequality $`-\log(1-v)\gt v`$ yields

**Equation (D33).**

```math
\frac r{\kappa n C_B}
\gt 
\frac{(9/10)(1+n)}{B+1+(1/10)n}
\frac{u_2}{1+m_*u_2}
\frac{L}{L+2}\frac1{C_B}.
```

The factors $`u/(1+m_*u)`$ and $`L/(L+2)`$ are increasing. The following rational lower bounds suffice:

**Equation (D34).**

```math
u_2\gt \frac{4323}{5000},\qquad
L\gt \frac{144}{25},\qquad
\frac1{C_B}=21+2\sqrt{110}\gt 
21+2\frac{1311}{125}.
```

For the first inequality, the positive Taylor sum obeys $`\sum_{j=0}^{10}2^j/j!\gt 5000/677`$. For the second, use the explicit positive-series bound

**Equation (D34a).**

```math
e^x\le\sum_{j=0}^{40}\frac{x^j}{j!}
+\frac{x^{41}}{41!}\frac1{1-x/42},
\qquad x=\frac{144}{25}.
```

The ratio of every successive omitted term is at most $`x/42\lt 1`$. Direct rational evaluation makes the right-hand side smaller than $`953/3=1+(19/20)/\bar m`$. For the last bound in (D34), $`(1311/125)^2\lt 110`$. Substitution into (D33) gives the exact rational comparison

**Equation (D35).**

```math
\frac r{\kappa n C_B}
\gt \frac{19617520706784}{8907123109777}
\gt \frac{11}{5}.
```

The accompanying exact-arithmetic verification evaluates these inequalities, including the exponential remainders, without floating-point assertions. The script checks the constants; the optical state reduction and statistical argument above supply the theorem.

## 5. What is and is not charged by this guarantee

All $`N`$ signals, idlers, return heterodynes, passive-network controls and photon-counted output modes belong to this protocol. The orthogonal outputs reuse idlers already prepared for target detection, but measuring them is an additional readout resource compared with bright-only reception. The conditional statistic does not make their measurement or coherent storage free.

The decision integrates over every return record through (D9) and covers every total-count reference record through (D26)–(D31). It never estimates $`\theta`$. Optional separate full-memory calibration can contain arbitrarily misleading records: neither the optical weights nor the test threshold relies on those estimates, so averaging over those records preserves (D22).

With $`q=\lceil\sqrt N\rceil`$ vacuum probes and the same number of occupation-one thermal probes, the experiment uses $`N+2q`$ memory calls. Equation (D22) still refers to the $`N`$ target signals; per total memory call its guaranteed asymptotic rate is $`rN/(N+2q)\to r`$. The extra mean calibration input energy is $`q`$ photons and can be significant at finite $`N`$ when $`n=10^{-3}`$.

At total transmitted signal energy $`Nn`$, the phase-informed coherent-mixture benchmark has optimum asymptotic exponent $`\kappa nC_B`$, allowing arbitrary fixed coherent mixtures, arbitrary energy randomization at that mean-energy budget and arbitrary global reception. Giving that receiver the true phase strengthens the comparison. The theorem establishes a separation from that benchmark in transmitted-energy reliability. Additional idler preparation, source pumping, local oscillators, coherent multimode storage and receiver operation must be priced before claiming an apparatus-energy or elapsed-time advantage.

## 6. Scope of the result

The achieved statement is an explicit finite-sample guarantee in a nonzero uncertainty box and over a nonzero reflectivity interval. It is not obtained by inserting an estimated memory loss into a known-parameter error formula. Exact conditional-null calibration removes the unknown brightness, and the miss bound retains the rare records that could defeat it.

The theorem assumes a common source phase, stationary independent memory parameters, equal complete storage windows, ideal known measurement responses and ideal controlled processing after the specified memory channel. It does not cover drifting memory, independently redrawn target phase, unknown detector response, arbitrary combiner loss or a sequential network whose growing dwell time changes its memory channel. Those are physical changes to the model, rather than calibration failures already covered by the proof.
