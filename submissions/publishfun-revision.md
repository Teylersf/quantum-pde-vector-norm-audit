# State-dependent splitting errors for anisotropic transport and diffusion: Source-verified counterexamples and an auxiliary estimate

**Taylor Kalin**

[taylorkalin.com](https://taylorkalin.com) | [teylersf@gmail.com](mailto:teylersf@gmail.com) | [509-919-0487](tel:+15099190487)

28 October 2026

## Abstract

We audit the source statements in arXiv:2603.08799v1, identified by a versioned PDF and its hash. An explicit smooth periodic shear contradicts the derivative-norm conservation assertion, which is also verified in the publisher's public Note 10. A positive-coefficient diffusion example exposes omitted mixed third derivatives in the preprint's displayed splitting prefactor. We quote the targeted preprint passages, distinguish a changed publisher note from the inaccessible publisher body, and make no claim that the unverified published diffusion formula is identical. For fixed trigonometric data we give the exact centered-stencil commutator and its order of convergence. Cosine-only numerical checks report initial and evolved-supremum comparators, finite-time limiting coefficients, and step refinement from pinned code. A standard auxiliary autonomous matrix estimate records the intermediate-state hypothesis needed for a corrected analysis; no novelty is claimed for that estimate. The results are specific counterexamples and proof obligations, not an exhaustive audit, an unconditional time-dependent PDE theorem, or a demonstrated quantum speedup.

## Scope, provenance, and standards of evidence

The audited object is the local nine-page PDF identifying itself as arXiv:2603.08799v1, submitted 9 March 2026 [1]. Its SHA-256 is `d03a710413b32ac622700adcfbaa9c3b8604ab9db00e45c348ea06c3d4be8988`. The source record links a published conference chapter [3]; we checked its public metadata, and its publicly exposed Notes, but could not obtain the full subscription chapter text. No finding here is asserted to apply unchanged to an unexamined revision, a later journal treatment, or other work by the same authors.

We distinguish four evidence categories:

1.  **Demonstrated error:** an identity, inequality, or prescription fails as written, with an explicit calculation.

2.  **Missing hypothesis or proof gap:** the intended result may hold under additional assumptions, but the displayed argument does not establish it.

3.  **Discretization limitation:** a property of the selected scheme that does not necessarily destroy its intended convergence regime.

4.  **Editorial ambiguity:** notation or indexing that should be repaired without implying a substantive mathematical failure.

The motivation for vector-norm analysis remains sound. An, Fang, and Lin previously studied circumstances in which state-dependent Trotter estimates avoid large discretized operator norms [2]. A failed prefactor does not by itself invalidate that research program.

## Model and consistent notation

On the unit periodic torus $\mathbb{T}^d$, consider separately

$$
\begin{aligned}
\partial_t f+\sum_{j=1}^d c_j(x,t)\partial_j f&=0\qquad\text{(1)}, \\
\partial_t u=\sum_{j=1}^d \kappa_j(x,t)\partial_j^2u \qquad\text{(2)}.
\end{aligned}
$$

 The source imposes $\partial_jc_j=\partial_j\kappa_j=0$. Under this restriction, (2) equals the divergence-form equation in its Eq. (1). For forward diffusion we explicitly require $\kappa_j\geq0$. The stronger ellipticity condition $\kappa_j\geq\kappa_*>0$ is useful for some regularity arguments, but is not needed for the elementary finite-grid contraction below.

Let $M_j=2^{n_j}$, $h_j=M_j^{-1}$, and $M=\prod_jM_j$. The total number of data qubits is $n_{\rm tot}=\sum_j n_j$. A grid coordinate is $x_j=r_j/M_j$, $0\leq r_j<M_j$; $r_j$ is the integer register label. We use the quadrature norm

$$
\left\lVert v\right\rVert_h^2=M^{-1}\sum_{\boldsymbol r}|v_{\boldsymbol r}|^2.
$$

 This converges to the continuum $L^2$ norm for smooth data on the unit torus. The associated unit quantum state has amplitudes $v_{\boldsymbol r}/(\sqrt M\,\left\lVert v\right\rVert_h)$. An unnormalized grid solution and its normalized quantum encoding are different objects and will not share a symbol silently.

For centered first differences write

$$
\delta_{p,h}v=h^{-1}\sum_{k=-p}^p a_k S^k v,\qquad
 a_{-k}=-a_k,\qquad D_{p,h}=-i\delta_{p,h}.
$$

 Periodic shifts make $D_{p,h}$ Hermitian. Because the coefficient in direction $j$ is independent of that direction, its multiplication matrix commutes with $D_j$. Consequently $-ic_jD_j$ is skew-Hermitian and $-\kappa_jD_j^2$ is Hermitian negative semidefinite when $\kappa_j\geq0$. The source’s directional exponentials then yield unitary transport factors and contractive, generally non-unitary diffusion factors.

## A transport counterexample and energy estimate

### Derivative norms are not generally conserved

Page 6, footnote 10, asserts conservation of the $L^2$ norm of any spatial derivative of $f$. The coefficient conditions stated on page 2 do not imply this. Choose the allowed time-independent periodic shear

$$
c(x,y)=(\sin(2\pi y),0),\qquad f_0(x,y)=\sin(2\pi x).
$$

 Both components are smooth and independent of their own coordinate. The exact solution is

$$
f(x,y,t)=\sin\bigl(2\pi[x-t\sin(2\pi y)]\bigr).
$$

 Direct differentiation and integration give

$$
\begin{aligned}
\left\lVert f(t)\right\rVert_{L^2}&=1/\sqrt2\qquad\text{(3)}, \\
\partial_y f&=-4\pi^2t\cos(2\pi y)
       \cos\bigl(2\pi[x-t\sin(2\pi y)]\bigr)\qquad\text{(4)}, \\
\left\lVert \partial_yf(t)\right\rVert_{L^2}&=2\pi^2|t|\qquad\text{(5)}.
\end{aligned}
$$

 The derivative norm starts at zero and grows. This is an analytic counterexample, not a conclusion inferred from a numerical plot.

### What can replace conservation

The velocity is divergence-free because $\sum_j\partial_jc_j=0$. For a smooth solution, differentiation of (1) gives

$$
(\partial_t+c\cdot\nabla)\nabla f=-(\nabla c)^{\mathsf T}\nabla f,
$$

 where $(\nabla c)_{ij}=\partial_jc_i$. Periodic integration by parts yields

$$
\frac{\mathrm{d}}{\mathrm{d} t}\left\lVert \nabla f(t)\right\rVert_{L^2}^2
 \leq 2\left\lVert \nabla c(t)\right\rVert_{L^\infty,\mathrm{op}}
                 \left\lVert \nabla f(t)\right\rVert_{L^2}^2 .
$$

 Thus

$$
\left\lVert \nabla f(t)\right\rVert_{L^2}\leq
 \exp\!\left(\int_0^t\left\lVert \nabla c(s)\right\rVert_{L^\infty,\mathrm{op}}\mathrm{d} s\right)
 \left\lVert \nabla f_0\right\rVert_{L^2}.
$$

 This bound involves the initial full gradient and the velocity gradients; it does not conserve each coordinate derivative separately. Higher Sobolev estimates require corresponding coefficient derivatives. Constants can therefore depend on the flow and on $T$, even when they are independent of $h$.

### Directional commutators

For $L_j=c_j\partial_j$ and $L_m=c_m\partial_m$,

$$
[L_j,L_m]f=
 c_j(\partial_j c_m)\partial_mf-
 c_m(\partial_mc_j)\partial_jf.
$$

 The transport prefactor on page 6 has this appropriate first-derivative structure. Its use of a supremum over evolved derivatives can remain meaningful. The invalid step is identifying those derivative norms with their initial coordinatewise values.

## Diffusion: missing terms and a counterexample

### Full continuum commutator

Put $A_j=\kappa_j\partial_j^2$. Expanding products of differential operators for $j\ne m$ gives

$$
\begin{aligned}
[A_j,A_m]u={}&
 \kappa_j(\partial_j^2\kappa_m)\partial_m^2u
 +2\kappa_j(\partial_j\kappa_m)\partial_j\partial_m^2u \\
&-\kappa_m(\partial_m^2\kappa_j)\partial_j^2u
 -2\kappa_m(\partial_m\kappa_j)\partial_m\partial_j^2u \qquad\text{(6)}.
\end{aligned}
$$

 The common fourth-derivative term cancels. The mixed third derivatives do not cancel under $\partial_j\kappa_j=0$. The displayed $a'_g$ following the source’s Eq. (8), page 6, contains only the first and third terms of (6) in its norm estimate.

A valid direct continuum estimate is

$$
\begin{aligned}
\left\lVert [A_j,A_m]u\right\rVert_{L^2}\leq{}&
 \left\lVert \kappa_j\right\rVert_\infty\left\lVert \partial_j^2\kappa_m\right\rVert_\infty
       \left\lVert \partial_m^2u\right\rVert_{L^2} \\
&+2\left\lVert \kappa_j\right\rVert_\infty\left\lVert \partial_j\kappa_m\right\rVert_\infty
       \left\lVert \partial_j\partial_m^2u\right\rVert_{L^2} \\
&+\left\lVert \kappa_m\right\rVert_\infty\left\lVert \partial_m^2\kappa_j\right\rVert_\infty
       \left\lVert \partial_j^2u\right\rVert_{L^2} \\
&+2\left\lVert \kappa_m\right\rVert_\infty\left\lVert \partial_m\kappa_j\right\rVert_\infty
       \left\lVert \partial_m\partial_j^2u\right\rVert_{L^2}\qquad\text{(7)}.
\end{aligned}
$$

 It requires control of additional derivatives. This is an identity and triangle-inequality bound in the continuum, not by itself a theorem about all discrete split trajectories.

### Strictly positive coefficients and positive initial data

On $\mathbb{T}^2$ choose, for $0<a,b<1$ and integer $m\geq2$,

$$
\kappa_x=1,\qquad \kappa_y=1+a\sin(2\pi x),\qquad
 u_0=1+b\cos(2\pi m x)\cos(2\pi y).
$$

 The coefficients satisfy all source coordinate restrictions and are strictly positive. The initial data are positive with mean 1. Let $q=2\pi$, $A=\partial_x^2$, $B=\kappa_y\partial_y^2$. Then, with the commutator convention $[A,B]=AB-BA$,

$$
[A,B]u_0=abq^4
 \left[(m+\tfrac12)\sin(q(m+1)x)
 +(m-\tfrac12)\sin(q(m-1)x)\right]\cos(qy).
$$

 Fourier orthogonality gives

$$
\left\lVert u_0\right\rVert_{L^2}^2=1+b^2/4,\qquad
 \left\lVert [A,B]u_0\right\rVert_{L^2}
 =\frac{abq^4}{2\sqrt2}\sqrt{4m^2+1}.
$$

 The quantity built from the two retained terms in the source, before the common factor $1/2$ and normalization, is only

$$
\left\lVert \kappa_x\right\rVert_\infty
 \left\lVert \partial_x^2\kappa_y\right\rVert_\infty
 \left\lVert \partial_y^2u_0\right\rVert_{L^2}
 =abq^4/2 .
$$

 The ratio of the actual commutator norm to that printed comparator is

$$
R_m=\sqrt{(4m^2+1)/2}>1 .
$$

 For $m=4$, $R_m=\sqrt{65/2}\simeq5.700877$.

### Why normalization does not remove this counterexample

For real self-adjoint $A,B$, the commutator is skew-adjoint, so $\left\langle u_0,[A,B]u_0\right\rangle=0$. The differential of $N(v)=v/\left\lVert v\right\rVert$ at $u_0$ is

$$
DN_{u_0}(w)=
 \frac{(I-\hat u_0\hat u_0^{\mathsf T})w}{\left\lVert u_0\right\rVert},
 \qquad \hat u_0=u_0/\left\lVert u_0\right\rVert.
$$

 The leading splitting defect lies perpendicular to $u_0$, and survives normalization unchanged apart from division by $\left\lVert u_0\right\rVert$.

To connect this continuum example to the source’s actual stencil, set $A_\eta=-D_x^2$ and $B_\eta=-K_yD_y^2$ on sufficiently fine centered periodic grids. Acting on this fixed trigonometric data and coefficient family, the discrete derivatives and their commutators converge in quadrature norm to the displayed continuum expressions. The printed initial-time comparator converges to the smaller expression above. Both matrices are real self-adjoint, so the discrete orthogonality also holds exactly. Thus the strict ratio persists on sufficiently fine fixed grids, before taking the time-step limit.

On each such fixed finite grid, the global first-order Lie-splitting expansion is an ordinary matrix Taylor calculation:

$$
\lim_{L\to\infty}L(S_{T/L}^{\,L}-U(T))u_0
 =\frac T2\int_0^T U(T-s)[B,A]U(s)u_0\,\mathrm{d} s ,
$$

 where $U(t)=e^{t(A+B)}$ and $S_h=e^{hB}e^{hA}$. Here $A,B$ denote the fixed-grid matrices just defined. Their autonomous exponentials are analytic, so the matrix expansion is justified. As $T\downarrow0$, the normalized leading coefficient divided by $T^2$ approaches $\left\lVert [B,A]u_0\right\rVert/(2\left\lVert u_0\right\rVert)$. The printed derivative-only prefactor approaches the smaller comparator above divided by $2\left\lVert u_0\right\rVert$. Thus the claimed leading coefficient fails for sufficiently small positive $T$, if the remainder is genuinely $o(1/L)$ as the leading-error interpretation requires. If a remainder is allowed to contain another $1/L$ contribution, the advertised prefactor has not been isolated. This argument concerns a coefficient, not an impossibility of mesh-independent bounds with (7) and adequate regularity.

## Other errors, limitations, and unresolved proof obligations

### Positivity is an essential explicit hypothesis

Page 5, footnote 8, uses contraction for diffusion. This follows from $\kappa_j\geq0$, but that inequality is not among the explicit mathematical assumptions on page 2. Negative constant $\kappa=-1$ satisfies the written smoothness and coordinate restrictions and gives backward heat: $u=e^{(2\pi)^2t}\cos(2\pi x)$. This is a missing hypothesis; it is not a criticism of physically nonnegative thermal conductivity.

### Supplementary discretization caveat: additional centered-stencil zero modes

For $p=1$,

$$
-\delta_{1,h}^2u_r
 =-\frac{u_{r+2}-2u_r+u_{r-2}}{4h^2},
 \qquad \lambda(\theta)=\sin^2\theta/h^2 .
$$

Besides the constant mode, the checkerboard $u_r=(-1)^r$ lies in the kernel on an even grid. For every antisymmetric centered first-derivative stencil, $\sum_k a_k e^{ik\pi}=0$. In $d$ dimensions the tensor parity modes supply at least $2^d$ null modes, including with the source's admissible variable coefficients.

Publisher Note 7 already acknowledges the constant zero-frequency mode: $d_j(0)=0$, conserved mean, and diffusion-propagator norm equality to 1. The additional checkerboard is a Nyquist mode ($\theta=\pi$ in the phase convention above). None of the ten public Notes explicitly discusses checkerboard or tensor parity modes, and Note 7 does not claim the constant mode is the only null mode. The observation is compatible with that note. We classify it as a supplementary discretization caveat, not a contradiction of contractivity or an established error in the version of record; its treatment in the inaccessible full publisher body is unknown.

These additional stationary modes limit strict damping claims outside the constant subspace; they do not contradict convergence on fixed sufficiently smooth resolved inputs. A standard nearest-neighbor negative second difference has symbol $4\sin^2(\theta/2)/h^2$ and removes this extra one-dimensional zero. Its positivity and quantum implementation would need a separate analysis; substitution is not a free algorithmic repair.

### Spatial residuals need stronger derivative control

The source’s page-5 diffusion discussion describes a constant in terms of derivatives through order $2p+1$. But squaring the first derivative gives, for $p=1$,

$$
\delta_{1,h}^2u=u''+\frac{h^2}{3}u^{(4)}+O(h^4).
$$

 The direct $O(h^{2p})$ pointwise consistency argument for the squared stencil needs order $2p+2$ control. Parabolic smoothing or an integrated estimate might weaken initial regularity requirements, but such an argument is not supplied. We classify this as a regularity/proof gap, rather than exclude every possible low-regularity convergence theorem.

### The directional error budget must sum to the target

The page-5 bound has the form $TK\sum_j\left\lVert c_j\right\rVert_\infty h_j^{2p}$. The printed prescription for each $n_j$ assigns an error budget $\epsilon$ to every term. It ensures at most $d\epsilon$ from that inequality, not $\epsilon$. Choose $\epsilon_j>0$ with $\sum_j\epsilon_j\leq\epsilon$, and use

$$
n_j\geq
 \max\!\left\{0,\left\lceil\frac1{2p}
 \log_2\frac{TK\left\lVert c_j\right\rVert_\infty}{\epsilon_j}\right\rceil\right\}
$$

 for nonzero coefficients, with zero-coefficient directions handled separately and any practical minimum grid imposed additionally. An equal split uses $\epsilon_j=\epsilon/d$.

### Normalization and sampling cannot be conflated

Continuum transport conserves its integral $L^2$ norm. Its values sampled on a fixed finite grid need not have exactly constant quadrature norm as the continuum profile evolves. A normalized sampled state obeys an extra derivative-of-normalizer term. Alternatively one can derive a residual equation for fixed-normalizer samples and normalize only after comparison. For diffusion, writing the unnormalized ODE solution as a normalized qubit state introduces a similar distinction. Factors involving the final norm must be retained in a normalized error estimate.

A useful algebraic repair, valid in any Hilbert norm, is

#### Lemma 1: Normalization stability

For nonzero $v,w$,

$$
\left\|\frac v{\left\lVert v\right\rVert}-\frac w{\left\lVert w\right\rVert}\right\|
 \leq\frac{2\left\lVert v-w\right\rVert}{\left\lVert w\right\rVert}.
$$

#### Proof

Insert $v/\left\lVert w\right\rVert$, use the triangle inequality, and apply $|\left\lVert v\right\rVert-\left\lVert w\right\rVert|\leq\left\lVert v-w\right\rVert$. $\square$

For mean-preserving diffusion on the unit torus, $\left\lVert u(T)\right\rVert_{L^2}\geq|\int_{\mathbb{T}^d}u_0|$. For a quantum-normalized input the corresponding bound must divide this mean by $\left\lVert u_0\right\rVert_{L^2}$. The source does impose a nonzero-mean condition on page 7; its later appearance is a scope restriction, not an undiscovered omission. No positive uniform lower bound follows from this route for mean-zero input.

### Remainders and time dependence

A fixed-grid expansion with an $O_h(\Delta t^3)$ remainder is insufficient to establish a bound uniform over grids. Its constant may grow as $h\to0$. Mixed third derivatives in (6), higher nested commutators, stability of partial split trajectories, and time derivatives of coefficients all need suitable uniform control. An $O(T^2/L)$ expression also does not isolate polynomial dependence on $T$ if its prefactor itself contains evolved Sobolev norms growing with $T$.

### What the exponential comparator does and does not show

Writing $M_{\rm axis}=2^n$ on an equal grid, the source’s crude product bound uses $O(M_{\rm axis}^2)$ for transport and $O(M_{\rm axis}^4)$ for diffusion commutators. It is not a lower bound on the work actually needed by an algorithm. For fixed smooth coefficients and a fixed stencil, cancellation already improves a direct operator estimate. Indeed

$$
[C_jD_j,C_mD_m]
 =C_j[D_j,C_m]D_m-C_m[D_m,C_j]D_j,
$$

 and a Lipschitz coefficient gives $\left\lVert [D_j,C_m]\right\rVert=O(1)$. Hence this operator-norm commutator bound is $O(M_{\rm axis})$. For diffusion, $\left\lVert [D_j^2,K_m]\right\rVert=O(M_{\rm axis})$ and

$$
[K_jD_j^2,K_mD_m^2]
=K_j[D_j^2,K_m]D_m^2-K_m[D_m^2,K_j]D_j^2.
$$

 The corresponding bound is $O(M_{\rm axis}^3)$. These are upper bounds, not asserted sharp rates in every case. Constant coefficients commute, giving no directional splitting error in the autonomous case. Therefore the advertised $\Theta(4^n)$ and $\Theta(16^n)$ improvements must be read as comparisons with a particular loose bound, not universal tight speedup factors over all operator-norm analyses.

### Quantum resource and readout assumptions

A non-unitary contraction is not a deterministic ordinary unitary gate on a closed data register. An implementation must specify a dilation, block encoding, measurement/postselection, amplitude amplification, or another realization with its associated costs. For an ideal contraction block with normalization factor 1, success probability on a normalized input is $\left\lVert Vu\right\rVert^2$. Other normalizations or implementations change this cost.

Merely being differentiable does not uniformly bound the size of a Fourier or Walsh approximation, its coefficient-access cost, or the cost of loading arbitrary initial data. The finite-difference symbol has amplitude growing with grid refinement. At fixed stencil order its oscillation count as a function of normalized frequency does not grow, but the associated unitary exponential can become increasingly oscillatory at a fixed time. A gate-level complexity theorem must quantify those dependencies rather than appeal to differentiability alone.

For a fixed observable, an expectation $\left\langle \psi,O\psi\right\rangle$ is invariant under a global phase. In particular $f$ and $-f$ encode the same quantum ray, whereas their signed point values differ. A position projector returns a normalized squared magnitude, not the signed physical field value. Recovering amplitudes requires an appropriate reference, controlled state preparation or overlap protocol, a phase convention, normalization information, and measurement-cost accounting. The measurement discussion on page 5 is therefore incomplete when interpreted as direct field-value recovery by a single expectation.

## An auxiliary conditional splitting estimate

State-dependent Trotter estimates are established tools. An, Fang, and Lin [2, Lemma 3, Theorem 4, Appendix B] give exact error representations and time-dependent unitary global bounds. Their first-order rate is $T^2/L$ and their second-order rate is $T^3/L^2$, with state factors controlled under structural relative-commutator assumptions. Their Lemma 7 handles partial exponential trajectories. We instead assume that difficult uniform control directly through $K$. We claim no novelty for the following auxiliary estimate.

For constant controls, set $A=-iaH_1$, $B=-ibH_2$ in their unitary setting; the displayed defect integral below is the corresponding autonomous first-order representation. Contractive diffusion is not literally their unitary theorem, but the same standard defect/telescoping argument applies to contractive matrices. The explicit factor $1/2$ is the triangular integration area, not a new asymptotic result. Establishing a grid-independent $K$ for the audited stencil remains an unproved additional task.

We deliberately state a finite-dimensional autonomous result. It does not extend silently to the source's time-dependent PDEs.

For each grid $\eta$, let $A_\eta,B_\eta$ be matrices such that $e^{tA_\eta}$, $e^{tB_\eta}$, and $U_\eta(t)=e^{t(A_\eta+B_\eta)}$ are contractions for $t\geq0$. This includes skew-Hermitian transport generators and Hermitian negative semidefinite diffusion generators. Set $S_\eta(s)=e^{sB_\eta}e^{sA_\eta}$.

#### Assumption 1: Uniform state-dependent commutator control

For some $h_0>0$ and $K<\infty$, normalized initial vectors $u_{\eta,0}$ satisfy, on every grid,

$$
\sup_{\substack{0\leq t\leq T\\0\leq r\leq s\leq h_0}}
 \left\lVert [B_\eta,A_\eta]e^{rB_\eta}e^{sA_\eta}
                  U_\eta(t)u_{\eta,0}\right\rVert\leq K .
$$

This explicitly includes intermediate split states. Smoothness of the continuum solution alone is not a proof of this uniform discrete hypothesis.

#### Proposition 1: Auxiliary autonomous contraction estimate

Under Assumption 1, for integer $L$ with $h=T/L\leq h_0$,

$$
\left\lVert S_\eta(h)^L u_{\eta,0}-U_\eta(T)u_{\eta,0}\right\rVert
 \leq \frac{KT^2}{2L}.
$$

 If also $\left\lVert U_\eta(T)u_{\eta,0}\right\rVert\geq m_*>0$ uniformly in $\eta$, and the split output is nonzero, its normalized error is at most $KT^2/(m_*L)$.

#### Proof

Suppress the grid subscript. Direct differentiation gives

$$
S'(s)-(A+B)S(s)=[e^{sB},A]e^{sA}
 =\int_0^s e^{(s-r)B}[B,A]e^{rB}e^{sA}\,\mathrm{d} r.
$$

 Variation of constants provides the exact, remainder-free identity

$$
(S(h)-U(h))v=
 \int_0^h\!\int_0^s
 U(h-s)e^{(s-r)B}[B,A]e^{rB}e^{sA}v\,\mathrm{d} r\,\mathrm{d} s .
$$

 Use $v=U(jh)u_0$ and Assumption 1. Contractivity of the left factors bounds each defect by $Kh^2/2$. Finally the algebraic telescoping identity

$$
S(h)^L-U(h)^L
 =\sum_{j=0}^{L-1}S(h)^{L-1-j}(S(h)-U(h))U(h)^j
$$

 and contractivity bound the sum by $LKh^2/2=KT^2/(2L)$. The normalized conclusion follows from Lemma 1. $\square$

The assumption makes the conclusion conditional but precise: there is no unspecified mesh-dependent Taylor remainder. For diffusion, (7) indicates the necessary higher-derivative quantities in a continuum analogue. Establishing uniform bounds on the actual discrete partial trajectories remains a separate task. For $d>2$, pairwise defects can be summed only after the corresponding partial-product hypotheses are formulated. For time-dependent generators, time-ordered propagators and coefficient-time regularity must also be handled; neither extension is claimed here.

## Reproducible checks and interpretation

The companion repository contains deterministic NumPy checks with analytic references, invariant checks, and grid/step refinement. They are classical computations; none executes a quantum circuit. The transport example tests both conservation of $\left\lVert f\right\rVert$ and nonconservation of $\left\lVert \partial_yf\right\rVert$. The diffusion example checks the full commutator, the missing-term ratio, and normalized split/exact behavior. Stencil checks verify the extra zero mode and second-order consistency on a fixed smooth Fourier mode. A negative-coefficient test illustrates the missing positivity hypothesis.

The first deposited version used a sine field in its numerical table. This revision uses the analytic section's cosine field throughout; no equivalence of the complete sine and cosine evolutions is assumed. Appendix B supplies the exact fixed-mode stencil identity, the comparator formulas, the cosine results, and the order of limits. The original numerical files remain available as historical artifacts; the new revision script generates every new number.

The audit ledger records each finding’s location, classification, support, and proposed repair. Editorial issues include mixing integer labels with dyadic coordinates on page 2, using $n$ for both total and per-direction qubits, the time-order convention implicit in Eq. (6), and a primed/unprimed diffusion-prefactor inconsistency on page 6. These issues should not be promoted to independent physical or algorithmic refutations.

## Limitations and open work

Independent human expert peer review has not been performed. Its strongest conclusions are the displayed identities, analytic counterexamples, and the conditional matrix theorem with a complete proof. The numerical checks supplement those arguments; they do not prove a quantum advantage or an unconditional PDE theorem. An exhaustive error claim would be unjustified.

A full replacement algorithm still needs a mesh-uniform consistency and stability theorem for the chosen stencil, careful treatment of normalized states and zero-mean data, a time-dependent splitting analysis, explicit coefficient and state access models, non-unitary success-cost bounds, observable definitions, and an end-to-end comparison with appropriate classical algorithms. The counterexamples identify repairs needed in the audited version without asserting that these tasks cannot be completed.

## References

[1] J. Zylberman, T. Fredon, N. F. Loureiro, and F. Debbasch. *Quantum algorithm for anisotropic diffusion and convection equations with vector norm scaling*. arXiv:2603.08799v1 (2026). https://arxiv.org/abs/2603.08799v1.

[2] D. An, D. Fang, and L. Lin. *Time-dependent unbounded Hamiltonian simulation with vector norm scaling*. Quantum **5**, 459 (2021). https://doi.org/10.22331/q-2021-05-26-459.

[3] J. Zylberman, T. Fredon, N. F. Loureiro, and F. Debbasch. *Quantum Algorithm for Anisotropic Diffusion and Convection Equations with Vector Norm Scaling*. Conference chapter, pp. 255–263. Public source-linked version of record; full text not audited here. https://doi.org/10.1007/978-3-032-13855-2_23.

## Methods and tool-use disclosure

The research audit, mathematical derivations, verification code, numerical analysis, and manuscript preparation were assisted by OpenAI Codex under the direction of Taylor Kalin. Taylor Kalin is the human author and is accountable for the submitted content. The reported numerical experiments are deterministic classical NumPy computations; no quantum-hardware experiments or external academic peer review are claimed. This disclosure describes tool use separately from the author byline.


## Appendix A: Source quotations and version-specific comparison

The supplied PDF is byte-identical to the publicly downloadable versioned arXiv object [1]: 200,554 bytes and SHA-256 d03a710413b32ac622700adcfbaa9c3b8604ab9db00e45c348ea06c3d4be8988. The following quotations and formulas were checked against its rendered pages. They are explicitly attributed to the preprint, not presumed to reproduce the complete Springer body.

### A.1 Own-coordinate restrictions, arXiv p. 2



> Additionally, we assume that the $c_j$ and the $\kappa_j$ functions are $2p+1$ differentiable, for some integer $p$, and do not depend on the $j$-th variables: $\forall j\in\{1,\ldots,d\}$, $\partial_{x_j}c_j=0$, $\partial_{x_j}\kappa_j=0$.


These hypotheses permit transverse variation. The examples in this note are smooth, periodic, and independent of the coefficients' own differentiation directions. The diffusion example has strictly positive coefficients and initial data of mean 1, so it also meets the later nonzero-mean requirement on arXiv p. 7.

### A.2 arXiv p. 5, footnote 8

> The evolution operator $\hat U$ associated with the discretized convection equation Eq.(3) is unitary thanks to the central finite difference and the assumption that $\forall j,\partial_{x_j}c_j=0$, while the evolution operator associated with the discretized diffusion equation Eq.(4) is non-unitary, but has a spectral norm $\|\hat V\|\leq 1$.

### A.3 arXiv p. 6, footnote 10

> The $L^2$ norm of any derivative of $f$ is constant over time, equal to its initial value at time $t=0$.

### A.4 arXiv p. 6, Eq. (8), remainder wording, and printed coefficient



$$
\left\|
\frac{|\widetilde\phi_\alpha\rangle_T}{\||\widetilde\phi_\alpha\rangle_T\|_{2,N}}
-\frac{|\widetilde\phi\rangle_T}{\||\widetilde\phi\rangle_T\|_{2,N}}
\right\|_{2,N}
\leq a'_\alpha\frac{T^2}{L}+r'_\alpha.
\tag{8}
$$

The prose immediately after it is:

> where $r'_\alpha$ contains higher order terms that are asymptotically negligible and

The coefficient immediately following that sentence is:

$$
\begin{aligned}
a'_g=\frac12\sum_{j=1}^{d-1}\sum_{m=j+1}^{d}\Bigg(
&\|\kappa_j\|_\infty\|\partial_{x_j}^{2}\kappa_m\|_\infty
\max_{t\in[0,T]}
\frac{\|\partial_{x_m}^{2}\phi_t\|_{2,N}}
{\|\widetilde\phi_T\|_{2,N}}\\
{}+{}&\|\kappa_m\|_\infty\|\partial_{x_m}^{2}\kappa_j\|_\infty
\max_{t\in[0,T]}
\frac{\|\partial_{x_j}^{2}\phi_t\|_{2,N}}
{\|\widetilde\phi_T\|_{2,N}}
\Bigg).
\end{aligned}
$$



The complete commutator in Eq. (6) of this note contains terms absent from that displayed coefficient. The source describes the remainder as higher-order and negligible but gives no explicit bound establishing that it is smaller than 1/L uniformly in the grid. Our contradiction to the isolated leading coefficient is conditional on that intended higher-order reading. If another 1/L contribution is hidden in the remainder, the printed coefficient is not a complete leading error coefficient.

### A.5 Public publisher notes: what was and was not compared

The [publisher's public chapter page and Notes](https://link.springer.com/chapter/10.1007/978-3-032-13855-2_23) were inspected directly. They verify the derivative-norm assertion in publisher Note 10. The published operator-norm note is numbered 7, whereas the related preprint footnote is 8. Note 7 states $\|\hat V_\alpha\|=1$ and $d_j(0)=0$, connecting the zero-frequency mode to conserved mean: "which expresses the conservation over time of the average value of the solution function". The preprint footnote gives an upper bound by 1. This is a verified textual difference, so identity of the versions cannot be assumed. The publisher's constant zero mode is already disclosed; we claim no correction of that fact.

| Finding or passage | arXiv v1 evidence | Public version-of-record evidence |
|---|---|---|
| Derivative-norm conservation | Footnote 10, p. 6, quoted above | Same substantive assertion in public publisher Note 10 |
| Convection unitarity and diffusion norm | Footnote 8, p. 5, quoted above | Public Note 7 changes the diffusion-norm statement |
| Constant zero-frequency mode | Present in the centered-stencil symbol | Explicitly acknowledged in public Note 7 through $d_j(0)=0$ and conserved mean; not an error finding |
| Additional checkerboard/parity null modes | Directly derived above for the squared centered stencil | Not explicitly discussed in any of the ten public Notes; full-body coverage unknown; supplementary caveat, not a demonstrated version-of-record error |
| Diffusion prefactor and remainder | Eq. (8) and following coefficient, p. 6, transcribed above | Full publisher formula not obtained or verified |
| Other body-level findings | Locations in the preprint ledger | Full publisher body not compared; persistence not asserted |

The full chapter body was subscription-restricted. A standard official PDF request did not produce an accessible PDF; a bounded search for a lawful author or repository copy found the submitted arXiv version, not an independently authenticated full version of record. No access control was bypassed and no purchase or institutional access is claimed. The formula-based criticism is therefore scoped to arXiv v1. Obtaining the full authorized version of record remains necessary before extending those formula-level findings to its body.


## Appendix B: Exact stencil, comparators, and cosine-only reproduction

Use $q=2\pi$, $a=0.2$, $b=0.5$, $m=4$ and $u_0=1+b\cos(qmx)\cos(qy)$ throughout. The original sine table is superseded for this revision.

### B.1 Explicit fixed-data discrete-to-continuum result

For $h=1/N$ and centered radius $p$, let

$$
a_k=\frac{(-1)^{k+1}(p!)^2}{k(p-k)!(p+k)!},\quad
\sigma_{p,h}(r)=\frac2h\sum_{k=1}^p a_k\sin(qrkh),\quad
\lambda_r=\sigma_{p,h}(r)^2.
$$

For $N>2(m+1)$ the fixed frequencies are nonaliased. Direct shift multiplication for $A_h=-D_x^2$ and $B_h=-K_yD_y^2$ gives exactly

$$
[A_h,B_h]u_0=\frac{ab\lambda_1}{2}
\left[(\lambda_{m+1}-\lambda_m)\sin(q(m+1)x)
+(\lambda_m-\lambda_{m-1})\sin(q(m-1)x)\right]\cos(qy).
$$

The fixed-mode symbol expansion is

$$
\lambda_{p,h}(r)=(qr)^2-\frac{2(p!)^2}{(2p+1)!}(qr)^{2p+2}h^{2p}
+O(h^{2p+2}).
$$

Substitution shows each of the two nonzero Fourier coefficients differs from its continuum value by $O(h^{2p})$. Orthogonality therefore proves the same quadrature-norm rate for the fixed-data commutator. This is the explicit convergence statement used in the counterexample, not an assertion of a general uniform splitting theorem. The new script independently checks the identity using actual FFT stencil products.

| p | N | Commutator convergence defect | Observed order |
|---:|---:|---:|---:|
| 1 | 128 | 13.0005383059 | 1.957354 |
| 1 | 256 | 3.2742614013 | 1.989330 |
| 1 | 512 | 0.8200805535 | 1.997332 |
| 1 | 1024 | 0.2051149526 | 1.999333 |
| 2 | 128 | 0.1798704193 | 3.964563 |
| 2 | 256 | 0.0113089563 | 3.991420 |
| 2 | 512 | 0.0007078526 | 3.997873 |
| 2 | 1024 | 0.0000442571 | 3.999469 |

### B.2 Initial and full evolved-supremum comparators

The retained continuum numerator and initial norm are

$$
P_0=\|\partial_x^2\kappa_y\|_\infty\|\partial_y^2u_0\|_2
=\frac{abq^4}{2},\qquad n_0=\sqrt{1+b^2/4}.
$$

The invariant evolution $u=1+g(x,t)\cos(qy)$ obeys $g_t=g_{xx}-q^2\kappa_y g$, whence

$$
\frac12\frac{d}{dt}\|g\|_2^2
=-\|g_x\|_2^2-q^2\int\kappa_y|g|^2\,dx\leq0.
$$

Thus the full supremum of $\|\partial_y^2u(s)\|_2$ over $0\leq s\leq T$ is its initial value $q^2b/2$. Define

$$
C_{\rm init}=\frac{P_0}{2n_0}=37.8002796450,\qquad
C_{\rm sup}(T)=\frac{P_0}{2n_T},\quad n_T=\|u(T)\|_2.
$$

The initial comparator and the evolved-supremum comparator have different denominators; no initial-state substitution for the evolved supremum is made silently. Since the mean is 1, $n_T\geq1$, giving the conservative upper comparator $P_0/2=38.9636364136$.

On the actual grid, the cosine-mode coefficient obeys $g'=H_hg$ with
$H_h=A_h-\lambda_1\operatorname{diag}(\kappa_y)\leq-\lambda_1(1-a)I$.
The same contraction argument proves the derivative supremum at time zero for the semidiscrete trigonometric interpolant. The table uses its exact semidiscrete final norm for $n_T$, and the continuum y-derivative factor $q^2$; replacing that factor by $\lambda_1<q^2$ makes the comparator smaller.

### B.3 Finite-time coefficient and the order of limits

For the following finite-time table fix $N=128$, $p=1$. Write $W_h(T)=(T/2)\int_0^T U_h(T-s)[B_h,A_h]U_h(s)u_0\,ds$ and

$$
c_h(T)=\frac{\|DN_{U_h(T)u_0}W_h(T)\|_h}{T^2}.
$$

This is the $L\to\infty$ limit of the normalized error multiplied by $L/T^2$. The script evaluates it independently through symmetric eigendecomposition and analytic divided differences, then compares actual Lie steps.

| T | n_T | C_init | C_sup(T) | c_h(T) | c_h(T)/C_sup(T) |
|---:|---:|---:|---:|---:|---:|
| 0.0002 | 1.0236896068 | 37.8002796450 | 38.0619634666 | 182.8108724874 | 4.8029806094 |
| 0.0005 | 1.0159754519 | 37.8002796450 | 38.3509624576 | 149.3819418965 | 3.8951288918 |

At L=512, the scaled cosine errors are 182.8119438296 and 149.3834620525. Step doubling gives first-order convergence. The exact limiting coefficients also exceed the mean-only upper comparator.

Finite-time ratios need not equal $R_4=5.7008771255$. The finite-grid initial ratio is $R_h=5.5378512736$ at N=128,p=1. At positive T, propagation of the evolving commutator and final normalization change the coefficient. At T=1e-8 the ratio is 5.5378115570, approaching $R_h$; only the further mesh limit gives $R_4$. This separates the step, small-time, and mesh limits.

### B.4 Pinned public reproduction

All new numbers are generated by [verify_revision.py at commit 9de1a54c1a2952ab7859b194a8227dce84a6dba0](https://github.com/Teylersf/quantum-pde-vector-norm-audit/blob/9de1a54c1a2952ab7859b194a8227dce84a6dba0/experiments/verify_revision.py).
The [checked JSON at that commit](https://github.com/Teylersf/quantum-pde-vector-norm-audit/blob/9de1a54c1a2952ab7859b194a8227dce84a6dba0/results/revision-verification.json) records NumPy 2.3.5. The original and auxiliary-bound scripts are also present at the pinned revision.

~~~sh
git clone https://github.com/Teylersf/quantum-pde-vector-norm-audit.git
cd quantum-pde-vector-norm-audit
git checkout 9de1a54c1a2952ab7859b194a8227dce84a6dba0
python -m pip install -r requirements.txt
python experiments/verify_claims.py
python experiments/verify_repaired_bound.py
python experiments/verify_revision.py
~~~

The checked environment was Python 3.12.14 with NumPy 2.3.5. Inputs are the analytic trigonometric fields and fixed matrices defined in code; no external dataset or original-paper PDF is needed. Numerical eigendecomposition is exact semidiscrete evolution up to floating-point rounding, not a claim of exact continuum evolution.

Appendix C includes an execution log from a fresh checkout of the exact pinned commit. It records the environment, commands, script hashes, exit codes, output, and complete generated revision JSON, including every B.1 and B.3 table value. All three scripts passed. Generated results match the pinned results semantically and byte-for-byte after CRLF-to-LF normalization. The log is an author-environment record, not independent human peer review or third-party certification. Its embedded numerical output is inspectable within this manuscript without opening GitHub.


## Prior dissemination and parallel-submission disclosure

This is a revised version of the same underlying note deposited at https://github.com/Teylersf/quantum-pde-vector-norm-audit and published as AiraXiv 2610.0107. An agent-byline version is publicly submitted at AgentPub as paper_2026_916ffe; AAES registration has been attempted but is blocked by its server-side GitHub verification error. These are cross-posted versions of one study, not independent new work. Nonexclusive consideration is requested with these facts disclosed. No editorial permission for these parallel deposits has been received or is asserted. The author has not withdrawn them, and makes no exclusivity declaration. We request the editorial office's explicit compatibility decision through this revision response; final acceptance remains conditional on that decision.


## Appendix C: Pinned-code execution record

Execution-log UTF-8 file SHA-256: `62be0a09e004ff666f324773a5a1a9c22579d26647c2897b221de508f05a0e49`. This records author-environment execution; it is not an independent human review.

~~~text
REPRODUCIBILITY EXECUTION LOG
Author-environment execution, not independent human peer review or third-party certification.
GitHub was used to obtain the source; the execution output and complete revision-results JSON are embedded here so they can be inspected without following the host link.
Commands are shown relative to the fresh checkout using the alias python for the actual bundled Python interpreter. Stdout absolute checkout paths are normalized to <checkout>. No command output or numerical value is otherwise altered.
Source: https://github.com/Teylersf/quantum-pde-vector-norm-audit.git
Exact commit: 9de1a54c1a2952ab7859b194a8227dce84a6dba0
Fresh clone/check-out commands:
git clone --no-checkout --quiet https://github.com/Teylersf/quantum-pde-vector-norm-audit.git <checkout>
git -C <checkout> checkout --detach 9de1a54c1a2952ab7859b194a8227dce84a6dba0
git -C <checkout> rev-parse HEAD
Observed HEAD: 9de1a54c1a2952ab7859b194a8227dce84a6dba0
Pre-execution git status --porcelain: empty
Execution started UTC: 2026-10-28T20:56:51.507687+00:00
Python: 3.12.14 (main, Aug 25 2026, 14:01:42) [MSC v.1944 64 bit (AMD64)]
Platform: win32
NumPy: 2.3.5
Sole dependency from requirements.txt: numpy==2.3.5

COMMAND: python -X utf8 experiments/verify_claims.py
Started UTC: 2026-10-28T20:56:51.515698+00:00
Script SHA-256: 02aebf0b5e1b05bc764faa4215027154601d73d23bad62890849eba7b1369d3b
Exit status: 0
STDOUT:
All five check groups passed. Results: <checkout>\results\verification.json
STDERR:
(empty)
Result file: results/verification.json
Checked-in result SHA-256: 53a936d0ae65798c90b264a5e28afdb42c64789fbad49d95c010720f5e4e9eb9
Generated result SHA-256: b524562cc051b9022a57b0518384b02fc861c60a706f0178fc1e1f0762c80499

GENERATED CHECK SUMMARY (check names and assertion flags):
{
  "all_assertions_passed": true,
  "checks": [
    "shear_derivative_growth",
    "continuum_diffusion_commutator",
    "normalized_semidiscrete_splitting",
    "checkerboard_and_consistency",
    "positivity_assumption"
  ]
}

COMMAND: python -X utf8 experiments/verify_repaired_bound.py
Started UTC: 2026-10-28T20:56:51.811101+00:00
Script SHA-256: 464b1380c4ef54bd6ff57b4f560459a8b0889c554a06625aac0c062f738f7340
Exit status: 0
STDOUT:
Both independent repaired-bound check groups passed.
STDERR:
(empty)
Result file: results/repaired-bound.json
Checked-in result SHA-256: ebf74de650bdad8104236b77413eae4910bfe00b0170591387ad7bd64a55a4c2
Generated result SHA-256: 6f0c2d5cb351e2bdbe07aeda6596b2085d49302b56c329fb5f091a40b5585508

GENERATED CHECK SUMMARY (check names and assertion flags):
{
  "all_assertions_passed": true,
  "checks": [
    {
      "unitary": false,
      "K": 0.4880573736764973,
      "final_norm": 0.21688907107603758,
      "T": 0.8,
      "rows": [
        {
          "steps": 4,
          "error": 0.0059373378941003935,
          "bound": 0.03904458989411979,
          "normalized_error": 0.026529367107213,
          "normalized_bound": 0.3600420224072187
        },
        {
          "steps": 8,
          "error": 0.0030483712163287494,
          "bound": 0.019522294947059895,
          "normalized_error": 0.013455286633253967,
          "normalized_bound": 0.18002101120360936
        },
        {
          "steps": 16,
          "error": 0.0015457694972964974,
          "bound": 0.009761147473529947,
          "normalized_error": 0.006777464467914052,
          "normalized_bound": 0.09001050560180468
        },
        {
          "steps": 32,
          "error": 0.0007784866272750414,
          "bound": 0.004880573736764974,
          "normalized_error": 0.003401454549396019,
          "normalized_bound": 0.04500525280090234
        },
        {
          "steps": 64,
          "error": 0.0003906694394702887,
          "bound": 0.002440286868382487,
          "normalized_error": 0.0017039409106379248,
          "normalized_bound": 0.02250262640045117
        }
      ]
    },
    {
      "unitary": true,
      "K": 0.48805737367649726,
      "final_norm": 1.0000000000000002,
      "T": 0.8,
      "rows": [
        {
          "steps": 4,
          "error": 0.03715619267064224,
          "bound": 0.03904458989411979,
          "normalized_error": 0.037156192670642296,
          "normalized_bound": 0.07808917978823957
        },
        {
          "steps": 8,
          "error": 0.018585028812594655,
          "bound": 0.019522294947059895,
          "normalized_error": 0.018585028812594752,
          "normalized_bound": 0.03904458989411978
        },
        {
          "steps": 16,
          "error": 0.009293407085864175,
          "bound": 0.009761147473529947,
          "normalized_error": 0.00929340708586425,
          "normalized_bound": 0.01952229494705989
        },
        {
          "steps": 32,
          "error": 0.004646821367161116,
          "bound": 0.004880573736764974,
          "normalized_error": 0.00464682136716118,
          "normalized_bound": 0.009761147473529946
        },
        {
          "steps": 64,
          "error": 0.0023234269384666637,
          "bound": 0.002440286868382487,
          "normalized_error": 0.0023234269384667145,
          "normalized_bound": 0.004880573736764973
        }
      ]
    }
  ]
}

COMMAND: python -X utf8 experiments/verify_revision.py
Started UTC: 2026-10-28T20:56:52.033439+00:00
Script SHA-256: 24bd3e528e10efaef782c76de0ef8cba679b11088e7d33aa57d48952e1755adf
Exit status: 0
STDOUT:
All revision checks passed. Results: <checkout>\results\revision-verification.json
STDERR:
(empty)
Result file: results/revision-verification.json
Checked-in result SHA-256: 91f3233515f4be075c5e0e670db4f4ebf82b642ec1bc58aa7608012bd8b28a74
Generated result SHA-256: 8278a870bdba9495ed3f0b1bbcd125fc3e59ba3d59618bee5dcf68c8e68154a7

COMPLETE GENERATED REVISION RESULTS JSON (unabridged):
{
  "source_version": "arXiv:2603.08799v1",
  "scope": "Revision-only cosine-example checks. Finite-grid results and a fixed-trigonometric-data convergence proof; no unconditional PDE splitting theorem or quantum-advantage claim.",
  "numpy_version": "2.3.5",
  "checks": {
    "cosine_continuum_commutator": {
      "initial_field": "1+b*cos(2*pi*m*x)*cos(2*pi*y)",
      "parameters": {
        "a": 0.2,
        "b": 0.5,
        "m": 4
      },
      "coefficients": "kappa_x=1; kappa_y=1+a*sin(2*pi*x)",
      "commutator_convention": "[A,B]=AB-BA; A=d_xx; B=kappa_y*d_yy",
      "analytic_identity": "[A,B]u0=ab*q^4*((m+1/2)*sin(q*(m+1)*x)+(m-1/2)*sin(q*(m-1)*x))*cos(q*y)",
      "commutator_L2": 444.25380711285726,
      "retained_term_L2": 55.10290305548867,
      "omitted_term_L2": 440.82322444390934,
      "printed_numerator_P0": 77.92727282720193,
      "initial_norm_n0": 1.0307764064044151,
      "initial_normalized_comparator_P0_over_2n0": 37.80027964504453,
      "small_time_normalized_coefficient": 215.4947495657747,
      "actual_to_printed_ratio_R4": 5.700877125495689,
      "inner_product_u0_commutator_u0": 3.552713678800501e-15,
      "minimum_initial_field": 0.5,
      "minimum_diffusivity": 0.8,
      "quadrature_points_per_axis": 256
    },
    "fixed_trigonometric_discrete_commutator_refinement": {
      "exact_symbol": "sigma_p,h(r)=2/h*sum_{k=1}^p a_k*sin(2*pi*r*k*h); lambda_p,h(r)=sigma_p,h(r)^2",
      "stencil_weights": "a_k=(-1)^(k+1)*binom(2p,p-k)/(k*binom(2p,p)) for 1<=k<=p; a_-k=-a_k",
      "exact_discrete_commutator": "(ab*lambda(1)/2)*((lambda(m+1)-lambda(m))*sin(q*(m+1)*x)+(lambda(m)-lambda(m-1))*sin(q*(m-1)*x))*cos(q*y)",
      "fixed_mode_symbol_expansion": "lambda_p,h(r)=(q*r)^2-2*(p!)^2/(2p+1)!*(q*r)^(2p+2)*h^(2p)+O(h^(2p+2))",
      "analytic_conclusion": "For fixed m and p, only modes m-1 and m+1 occur; their coefficients converge with O(h^(2p)) error. Orthogonality therefore gives O(h^(2p)) quadrature-norm commutator convergence. This is a fixed-trigonometric-data statement, not a uniform theorem for arbitrary evolving inputs.",
      "rows": [
        {
          "p": 1,
          "points_per_axis": 32,
          "commutator_L2": 269.9827619181166,
          "commutator_minus_continuum_L2": 179.5070849887809,
          "observed_order": null,
          "actual_to_continuum_printed_numerator_ratio": 3.464547803652564,
          "exact_symbol_vs_direct_FFT_residual_L2": 1.3195460723775286e-12
        },
        {
          "p": 1,
          "points_per_axis": 64,
          "commutator_L2": 394.9717077852883,
          "commutator_minus_continuum_L2": 50.48747093916346,
          "observed_order": 1.8300434714737925,
          "actual_to_continuum_printed_numerator_ratio": 5.068465679032672,
          "exact_symbol_vs_direct_FFT_residual_L2": 3.4891897822019206e-12
        },
        {
          "p": 1,
          "points_per_axis": 128,
          "commutator_L2": 431.54964707112885,
          "commutator_minus_continuum_L2": 13.000538305893354,
          "observed_order": 1.9573540491629533,
          "actual_to_continuum_printed_numerator_ratio": 5.5378512735593715,
          "exact_symbol_vs_direct_FFT_residual_L2": 1.9358261007066975e-11
        },
        {
          "p": 1,
          "points_per_axis": 256,
          "commutator_L2": 441.0533477915858,
          "commutator_minus_continuum_L2": 3.27426140134946,
          "observed_order": 1.9893299519578864,
          "actual_to_continuum_printed_numerator_ratio": 5.659807302246924,
          "exact_symbol_vs_direct_FFT_residual_L2": 7.815240029213786e-11
        },
        {
          "p": 1,
          "points_per_axis": 512,
          "commutator_L2": 443.45215905969167,
          "commutator_minus_continuum_L2": 0.8200805535145287,
          "observed_order": 1.9973319718097655,
          "actual_to_continuum_printed_numerator_ratio": 5.690589994635314,
          "exact_symbol_vs_direct_FFT_residual_L2": 2.691337091594078e-10
        },
        {
          "p": 1,
          "points_per_axis": 1024,
          "commutator_L2": 444.0532991630936,
          "commutator_minus_continuum_L2": 0.20511495263075427,
          "observed_order": 1.9993329609839416,
          "actual_to_continuum_printed_numerator_ratio": 5.698304111677943,
          "exact_symbol_vs_direct_FFT_residual_L2": 1.9041861704200017e-09
        },
        {
          "p": 2,
          "points_per_axis": 32,
          "commutator_L2": 406.8127939539043,
          "commutator_minus_continuum_L2": 40.27147362201349,
          "observed_order": null,
          "actual_to_continuum_printed_numerator_ratio": 5.220416154636672,
          "exact_symbol_vs_direct_FFT_residual_L2": 2.2836180648812636e-12
        },
        {
          "p": 2,
          "points_per_axis": 64,
          "commutator_L2": 441.6400178676685,
          "commutator_minus_continuum_L2": 2.8080977903533184,
          "observed_order": 3.8420931820061957,
          "actual_to_continuum_printed_numerator_ratio": 5.667335732984949,
          "exact_symbol_vs_direct_FFT_residual_L2": 4.331281256236457e-12
        },
        {
          "p": 2,
          "points_per_axis": 128,
          "commutator_L2": 444.0864880656725,
          "commutator_minus_continuum_L2": 0.1798704192693011,
          "observed_order": 3.9645633258570556,
          "actual_to_continuum_printed_numerator_ratio": 5.698730007534102,
          "exact_symbol_vs_direct_FFT_residual_L2": 2.9913136470192057e-11
        },
        {
          "p": 2,
          "points_per_axis": 256,
          "commutator_L2": 444.2432896339916,
          "commutator_minus_continuum_L2": 0.011308956308613428,
          "observed_order": 3.991420250739752,
          "actual_to_continuum_printed_numerator_ratio": 5.7007421601814405,
          "exact_symbol_vs_direct_FFT_residual_L2": 1.2499434051226693e-10
        },
        {
          "p": 2,
          "points_per_axis": 512,
          "commutator_L2": 444.25314883996384,
          "commutator_minus_continuum_L2": 0.0007078526043938106,
          "observed_order": 3.9978730001792155,
          "actual_to_continuum_printed_numerator_ratio": 5.700868678223386,
          "exact_symbol_vs_direct_FFT_residual_L2": 5.153125003538766e-10
        },
        {
          "p": 2,
          "points_per_axis": 1024,
          "commutator_L2": 444.2537659562937,
          "commutator_minus_continuum_L2": 4.425706226420644e-05,
          "observed_order": 3.9994693853989993,
          "actual_to_continuum_printed_numerator_ratio": 5.700876597355,
          "exact_symbol_vs_direct_FFT_residual_L2": 3.037058017342008e-09
        }
      ]
    },
    "normalized_cosine_semidiscrete_splitting": {
      "grid": [
        128,
        128
      ],
      "p": 1,
      "initial_field": "1+b*cos(2*pi*m*x)*cos(2*pi*y)",
      "method": "Exact invariant single-y-cosine-mode reduction; symmetric eigendecomposition for U_h(t); FFT/pointwise Lie factors; analytic divided differences for the global leading coefficient.",
      "split_order": "S_dt=exp(dt*B_h)exp(dt*A_h)",
      "normalized_coefficient_formula": "c_h(T)=||DN_(U_h(T)u0)((T/2)*int_0^T U_h(T-s)[B_h,A_h]U_h(s)u0 ds)||_h/T^2",
      "initial_time_comparator_formula": "C_init=P0/(2*n0), P0=||kappa_x||inf*||partial_xx kappa_y||inf*||partial_yy u0||=ab*q^4/2",
      "full_evolved_supremum_comparator_formula": "C_sup(T)=(1/(2*nT))*sup_(0<=s<=T)(a*q^2*||partial_yy u_h(s)||_h)=ab*q^4/(4*nT), using the continuum y derivative on the invariant single-mode interpolant",
      "contractivity_proof": "g'=H_h g, H_h=A_h-lambda_y*diag(kappa_y)<=-lambda_y*(1-a)I. Hence d||g||_h^2/dt=2<g,H_h g>_h<=0; both ||partial_yy u_h||_h=q^2||g||_h/sqrt(2) and its normalized version attain their supremum at s=0. In the continuum replace A_h by d_xx and lambda_y by q^2 and integrate by parts.",
      "fixed_grid_small_time_limit": 209.33232677321027,
      "fixed_grid_small_time_ratio_to_initial_comparator": 5.5378512735593715,
      "why_finite_time_ratio_is_not_R4": "R4 is a continuum, initial-commutator ratio. At fixed h the limiting ratio as T->0 is R_h; at positive T the integral propagates the evolving commutator and final normalization projects the defect at U_h(T)u0. Only after the T->0 and h->0 limits does the ratio approach R4. Neither finite T rows nor 1/L refinement alone should equal R4.",
      "coefficient_rows": [
        {
          "T": 1e-08,
          "exact_final_norm_nT": 1.0307760043886884,
          "initial_time_comparator_P0_over_2n0": 37.80027964504453,
          "full_evolved_supremum_comparator_P0_over_2nT": 37.80029438763344,
          "semidiscrete_uyy_supremum_comparator": 37.76994330424299,
          "mean_lower_bound_upper_comparator_P0_over_2": 38.963636413600966,
          "supremum_uyy_continuum_derivative_norm": 9.869604401089358,
          "supremum_uyy_semidiscrete_derivative_norm": 9.861679775340777,
          "lim_L_to_infinity_error_times_L_over_T_squared": 209.3309071185178,
          "ratio_to_initial_time_comparator": 5.537813716834771,
          "ratio_to_full_evolved_supremum_comparator": 5.537811557017966,
          "ratio_to_mean_lower_bound_upper_comparator": 5.372468444589198,
          "ratio_to_discrete_small_time_limit": 0.9999932181774581
        },
        {
          "T": 1e-06,
          "exact_final_norm_nT": 1.03073623043501,
          "initial_time_comparator_P0_over_2n0": 37.80027964504453,
          "full_evolved_supremum_comparator_P0_over_2nT": 37.80175302187333,
          "semidiscrete_uyy_supremum_comparator": 37.771400767298104,
          "mean_lower_bound_upper_comparator_P0_over_2": 38.963636413600966,
          "supremum_uyy_continuum_derivative_norm": 9.869604401089358,
          "supremum_uyy_semidiscrete_derivative_norm": 9.861679775340777,
          "lim_L_to_infinity_error_times_L_over_T_squared": 209.19040940845557,
          "ratio_to_initial_time_comparator": 5.534096873695472,
          "ratio_to_full_evolved_supremum_comparator": 5.533881174436835,
          "ratio_to_mean_lower_bound_upper_comparator": 5.368862577093391,
          "ratio_to_discrete_small_time_limit": 0.9993220475454397
        },
        {
          "T": 1e-05,
          "exact_final_norm_nT": 1.0303769646230374,
          "initial_time_comparator_P0_over_2n0": 37.80027964504453,
          "full_evolved_supremum_comparator_P0_over_2nT": 37.814933515964015,
          "semidiscrete_uyy_supremum_comparator": 37.784570678342234,
          "mean_lower_bound_upper_comparator_P0_over_2": 38.963636413600966,
          "supremum_uyy_continuum_derivative_norm": 9.869604401089358,
          "supremum_uyy_semidiscrete_derivative_norm": 9.861679775340777,
          "lim_L_to_infinity_error_times_L_over_T_squared": 207.91751813172536,
          "ratio_to_initial_time_comparator": 5.5004227504169405,
          "ratio_to_full_evolved_supremum_comparator": 5.4982912516281575,
          "ratio_to_mean_lower_bound_upper_comparator": 5.336193878945754,
          "ratio_to_discrete_small_time_limit": 0.9932413274944499
        },
        {
          "T": 0.0002,
          "exact_final_norm_nT": 1.023689606760302,
          "initial_time_comparator_P0_over_2n0": 37.80027964504453,
          "full_evolved_supremum_comparator_P0_over_2nT": 38.06196346655334,
          "semidiscrete_uyy_supremum_comparator": 38.031402280565445,
          "mean_lower_bound_upper_comparator_P0_over_2": 38.963636413600966,
          "supremum_uyy_continuum_derivative_norm": 9.869604401089358,
          "supremum_uyy_semidiscrete_derivative_norm": 9.861679775340777,
          "lim_L_to_infinity_error_times_L_over_T_squared": 182.8108724873639,
          "ratio_to_initial_time_comparator": 4.836230689402576,
          "ratio_to_full_evolved_supremum_comparator": 4.802980609447738,
          "ratio_to_mean_lower_bound_upper_comparator": 4.691832932296597,
          "ratio_to_discrete_small_time_limit": 0.8733045454819809
        },
        {
          "T": 0.0005,
          "exact_final_norm_nT": 1.0159754518981856,
          "initial_time_comparator_P0_over_2n0": 37.80027964504453,
          "full_evolved_supremum_comparator_P0_over_2nT": 38.350962457610294,
          "semidiscrete_uyy_supremum_comparator": 38.32016922495136,
          "mean_lower_bound_upper_comparator_P0_over_2": 38.963636413600966,
          "supremum_uyy_continuum_derivative_norm": 9.869604401089358,
          "supremum_uyy_semidiscrete_derivative_norm": 9.861679775340777,
          "lim_L_to_infinity_error_times_L_over_T_squared": 149.3819418965322,
          "ratio_to_initial_time_comparator": 3.9518739887448313,
          "ratio_to_full_evolved_supremum_comparator": 3.8951288917884543,
          "ratio_to_mean_lower_bound_upper_comparator": 3.833880911700216,
          "ratio_to_discrete_small_time_limit": 0.7136114340255337
        },
        {
          "T": 0.001,
          "exact_final_norm_nT": 1.0082639887633198,
          "initial_time_comparator_P0_over_2n0": 37.80027964504453,
          "full_evolved_supremum_comparator_P0_over_2nT": 38.64428051366942,
          "semidiscrete_uyy_supremum_comparator": 38.61325176642194,
          "mean_lower_bound_upper_comparator_P0_over_2": 38.963636413600966,
          "supremum_uyy_continuum_derivative_norm": 9.869604401089358,
          "supremum_uyy_semidiscrete_derivative_norm": 9.861679775340777,
          "lim_L_to_infinity_error_times_L_over_T_squared": 107.32003137686496,
          "ratio_to_initial_time_comparator": 2.839133265272925,
          "ratio_to_full_evolved_supremum_comparator": 2.777125876076364,
          "ratio_to_mean_lower_bound_upper_comparator": 2.754363844217655,
          "ratio_to_discrete_small_time_limit": 0.5126777742891809
        },
        {
          "T": 0.002,
          "exact_final_norm_nT": 1.002201379936735,
          "initial_time_comparator_P0_over_2n0": 37.80027964504453,
          "full_evolved_supremum_comparator_P0_over_2nT": 38.87805105203565,
          "semidiscrete_uyy_supremum_comparator": 38.84683460283455,
          "mean_lower_bound_upper_comparator_P0_over_2": 38.963636413600966,
          "supremum_uyy_continuum_derivative_norm": 9.869604401089358,
          "supremum_uyy_semidiscrete_derivative_norm": 9.861679775340777,
          "lim_L_to_infinity_error_times_L_over_T_squared": 57.09412501781803,
          "ratio_to_initial_time_comparator": 1.510415413693979,
          "ratio_to_full_evolved_supremum_comparator": 1.4685439077540536,
          "ratio_to_mean_lower_bound_upper_comparator": 1.4653181856991224,
          "ratio_to_discrete_small_time_limit": 0.27274394689967574
        }
      ],
      "step_refinement_rows": [
        {
          "T": 0.0002,
          "steps": 64,
          "normalized_L2_error": 1.1426216768807494e-07,
          "measured_error_times_L_over_T_squared": 182.8194683009199,
          "exact_global_limit_coefficient": 182.8108724873639,
          "full_evolved_supremum_comparator": 38.06196346655334,
          "measured_to_full_supremum_ratio": 4.803206446813264
        },
        {
          "T": 0.0002,
          "steps": 128,
          "normalized_L2_error": 5.712974044598263e-08,
          "measured_error_times_L_over_T_squared": 182.8151694271444,
          "exact_global_limit_coefficient": 182.8108724873639,
          "full_evolved_supremum_comparator": 38.06196346655334,
          "measured_to_full_supremum_ratio": 4.803093502724626
        },
        {
          "T": 0.0002,
          "steps": 256,
          "normalized_L2_error": 2.8564534285849246e-08,
          "measured_error_times_L_over_T_squared": 182.81301942943517,
          "exact_global_limit_coefficient": 182.8108724873639,
          "full_evolved_supremum_comparator": 38.06196346655334,
          "measured_to_full_supremum_ratio": 4.803037015945873
        },
        {
          "T": 0.0002,
          "steps": 512,
          "normalized_L2_error": 1.4282183111689202e-08,
          "measured_error_times_L_over_T_squared": 182.81194382962178,
          "exact_global_limit_coefficient": 182.8108724873639,
          "full_evolved_supremum_comparator": 38.06196346655334,
          "measured_to_full_supremum_ratio": 4.803008756767538
        },
        {
          "T": 0.0005,
          "steps": 64,
          "normalized_L2_error": 5.835707804828926e-07,
          "measured_error_times_L_over_T_squared": 149.39411980362053,
          "exact_global_limit_coefficient": 149.3819418965322,
          "full_evolved_supremum_comparator": 38.350962457610294,
          "measured_to_full_supremum_ratio": 3.8954464302883496
        },
        {
          "T": 0.0005,
          "steps": 128,
          "normalized_L2_error": 2.9177349193345385e-07,
          "measured_error_times_L_over_T_squared": 149.38802786992838,
          "exact_global_limit_coefficient": 149.3819418965322,
          "full_evolved_supremum_comparator": 38.350962457610294,
          "measured_to_full_supremum_ratio": 3.895287583331148
        },
        {
          "T": 0.0005,
          "steps": 256,
          "normalized_L2_error": 1.4588377330795654e-07,
          "measured_error_times_L_over_T_squared": 149.3849838673475,
          "exact_global_limit_coefficient": 149.3819418965322,
          "full_evolved_supremum_comparator": 38.350962457610294,
          "measured_to_full_supremum_ratio": 3.895208211070693
        },
        {
          "T": 0.0005,
          "steps": 512,
          "normalized_L2_error": 7.294114358034549e-08,
          "measured_error_times_L_over_T_squared": 149.38346205254757,
          "exact_global_limit_coefficient": 149.3819418965322,
          "full_evolved_supremum_comparator": 38.350962457610294,
          "measured_to_full_supremum_ratio": 3.895168529803199
        }
      ]
    }
  },
  "all_assertions_passed": true
}

Execution completed UTC: 2026-10-28T20:56:52.321308+00:00
All three commands exited 0. Internal substantive assertions in each script completed.
No external dataset, quantum computer, or original-paper PDF was used.
This log is a captured execution record, not a guarantee of exact real arithmetic or independent external validation.

PINNED-RESULT REPRODUCTION CHECK
The differing raw generated hashes above are solely Windows CRLF versus repository LF line endings. The following checks compare actual outputs against git show of each pinned result. Numeric/string/array/object values match exactly.
[
  {
    "result": "results/verification.json",
    "JSON_semantically_identical_to_pinned_result": true,
    "bytes_identical_after_CRLF_to_LF_normalization": true,
    "LF_normalized_SHA256": "53a936d0ae65798c90b264a5e28afdb42c64789fbad49d95c010720f5e4e9eb9"
  },
  {
    "result": "results/repaired-bound.json",
    "JSON_semantically_identical_to_pinned_result": true,
    "bytes_identical_after_CRLF_to_LF_normalization": true,
    "LF_normalized_SHA256": "ebf74de650bdad8104236b77413eae4910bfe00b0170591387ad7bd64a55a4c2"
  },
  {
    "result": "results/revision-verification.json",
    "JSON_semantically_identical_to_pinned_result": true,
    "bytes_identical_after_CRLF_to_LF_normalization": true,
    "LF_normalized_SHA256": "91f3233515f4be075c5e0e670db4f4ebf82b642ec1bc58aa7608012bd8b28a74"
  }
]
~~~
