# Black Hole Simulation Equations 

This simulation is based on the video by Alexandro Roussel available [here](https://www.youtube.com/watch?v=PjWjZFwz3rQ).

## General Equations

Geodesic equation : 
$$\frac{\mathrm{d}^{2} x^{\alpha}}{\mathrm{d} s^{2}}+\Gamma_{\mu \nu}^{\alpha} \frac{\mathrm{d} x^{\mu}}{\mathrm{d} s} \frac{\mathrm{d} x^{\nu}}{\mathrm{d} s}=0
$$

Einstein equation : 
$$R_{\mu \nu}=-\frac{8 \pi G}{c^{4}}\left[T_{\mu \nu}-\frac{1}{2} T g_{\mu \nu}\right]$$

## For our sim :

$R_{\mu \nu}=0$

metric tensor : 
$$g_{\mu \nu}=\left[\begin{array}{cccc}
1-\frac{R_{s}}{r} & 0 & 0 & 0 \\
0 & -\frac{1}{1-\frac{R_{x}}{r}} & 0 & 0 \\
0 & 0 & -r^{2} & 0 \\
0 & 0 & 0 & -r^{2} \sin ^{2} \theta
\end{array}\right]
$$
with $R_{s}=\frac{2 G M}{c^{2}}$

As our point of view is light, the geodesic eq is equal to 0, using our definition of the metric tensor : 
$$0=\left[1-\frac{R_{s}}{r}\right] c^{2} \mathrm{~d} t^{2}-\left[\frac{1}{1-\frac{R_{s}}{r}}\right] \mathrm{d} r^{2}-r^{2} \mathrm{~d} \theta^{2}-r^{2} \sin ^{2} \theta \mathrm{d} \phi^{2}$$

Our differential equations to solve our problem is : 
$$\begin{array}{c}
\frac{\mathrm{d}^{2} u}{\mathrm{~d} \phi^{2}}=\frac{3}{2} R_{s} u^{2}-u, \text{ with }
u=\frac{1}{r}
\end{array}$$

To solve this equation, we start to send a "reverse photon", being at distance $D$ from the black hole with an angle $\alpha$, and so our initial conditions are as follows : 
$$  u(0) = \frac{1}{D}, \hspace{1em}
    u^{'}(0) = \frac{1}{D\tan{\alpha}},  \hspace{1em}
    \phi(0) = 0
$$

We will solve this system by increasing step by step $\phi$ by a small amount $\delta \phi$ and updating $u$ and its derivatives using this $\delta \phi$ update.