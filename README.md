# Runge-Kutta
The final project of K.N.Toosi University of Technology at Spring 2023.</br>
The Runge-Kutta method is a numerical technique used to solve ordinary differential equations (ODEs) of the form $\color{green}{dy/dx = f(x, y), y(0) = y0.}$
</br> The 4th order Runge-Kutta (RK4) method is a popular and commonly used method that gives approximate solutions to ODEs. It can only solve first order ODEs or higher order ODEs that are reduced to first order.
The RK4 method provides the approximate value of y for a given point x.</br> The formula for the fourth-order Runge-Kutta method is given by:
$\color{green}{y1 = y0 + (1/6) (k1 + 2k2 + 2k3 + k4).}$
Here, k1, k2, k3, and k4 are slopes at different points in the interval $\color{orange}{[x0, xn]}$ and h is the step size.</br></br>
The formula basically computes next value $\color{green}{Yn+1}$ using current $\color{green}{Yn}$ plus weighted average of four increments.</br> 

+ $\color{orange}{k1}$ is the increment based on the slope at the beginning of the interval, using y
+ $\color{orange}{k2}$ is the increment based on the slope at the midpoint of the interval, using y + hk1/2.
+ $\color{orange}{k3}$ is again the increment based on the slope at the midpoint, using  y + hk2/2.
+ $\color{orange}{k4}$ is the increment based on the slope at the end of the interval, using y + hk3.</br></br>
In addition of above descriptions i should to say that after finding the $\color{green}{Yn}$ in this code,a Secondary Axis will be drawn and show to you the 2D coordinates of them clearly.</br>
I did this with $\color{yellow}{Turtle}$ Library in python.
