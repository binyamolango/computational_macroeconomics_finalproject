
5

130%
University of Heidelberg
Computational Macroeconomics
Final Assignment (graded)
HAND IN ALONE
TeacherDr. Rustam Urdukhanov
hand in in moodle
DEADLINE: 27.02.2025 DEADLINE: 09.08.2026 
1.2 Tasks
1. Write the model in the following form:
Azt = M Etzt+1 + Dzt−1 + ut, (6)
with the vector
Zt = [μt, yt, πt, it]′(7)
and write down the 4x4 matrices A,M and D in your code (Having these
matrices correctly in your code would be enough to answer this question,
and you do not need to hand in your derivations).
2. In the steady state of the model it holds that ut = 0 and zt−1 = zt.
Further (assuming that expectations are correct in steady state), it should
also hold in steady state that Etzt+1 = zt.
Write a function that has as input a vector of 4 coefficeints that can be
interpreted as the guessed values of the steady state of the model. In the
function, set Etzt+1 and zt−1 both equal to this vector of guessed steady
state values. Given that you set ut = 0, it is now possible to calcualte the
right hand side of Equation 6.
After that, your function should calculate the implied zt vector from Equa-
tion 6 and return the differences between this vector and the vector of
guessed steady state values that was the input of the function.
3. Use fsolve on the function you have just defined to show that the steady
state of the model is (very close to) 0, so that it is indeed correct to
not include a constant term in the minimum state variable solution in
Equation 5.
4. Define a new function. The function should have four matrices as input
arguments. The first three are the matrices A,M and D and the fourth
input argument should be an initial guess for the matrix F that contains
all coefficients on lagged values in the MSV solution.
Your new function should return the solution for the matrices F and Q
that satisfy zt = F zt−1 + Qut. That is, define a function that applies the
linear time iteration algorithm which you have worked with in Assignment
4.
Hint remember the formulas
F new = (A −M F )−1D
and
Q = (A −M F new)−1
3
5. ’Call’ the function that you just defined with the matrices you defined in
question 1 to obtain the general solution, zt = F zt−1 + Qut, of the model
of this graded assignment.
6. Save the correct columns of the matrices F and Q as vectors that corre-
spond to the 5 vectors in the minimum state variables solution: Cμ, Cy,
Cπ , Cμ and Ci.
7. Calculate impulse responses to a shock to μt of size μ
0 = 0.01 in the same
waye you did in Assignment 4:
Make a loop of 30 periods, where you set μ
t = 0.01 in the first period,
and μ
t = 0 in all later periods. Further set it = 0 in all periods.
In the loop you can then in each period calculate the variables in zt, using
the vectors Cμ, Cy, Cπ , Cμ and Ci of the MSV solution.
8. In a similar way, calculate impulse responses to a shock to it of size i0 =
0.01.
9. Make two figures, each with four subfigures. The subfigures should contain
the 4 variables in zt. In the first figure, plot the impulse responses to the
shock μt and in the second figure plot the impulse responses to the shock
it.
Make sure that
• All lines are thick (e.g. 4pt)
• Each line in a figure has a different color or linestyle
• The subfigures fit well in the figure.
10. Interpret the impulse responses that you have plotted. What is the eco-
nomic intuition for the variables to respond in the way they do? What
difference do you notice between responses to the auto-correlated and the
not auto-correlated shock? Does the model return immediately to steady
state when the shock to the nominal interest rate is over? Why or why
not?
11. Now run a time series simulation of 500 periods of your model, where
you draw random values for μ
t and it in each period. Save your resulting
time series of Yt and πt in a pandas DataFrame with column names that
indicate which column corresponds to which variable.
12. Use the MSV solution (which you have obtained above) to calculate ex-
plicitly what rational expectations in any given period about inflation in
the next period are. That is, calculate Etπt+1. Include this new variable
in your pandas DataFrame.
Hint: under rational expectations it is assumed that agents know the cur-
rent value of shocks, and, therefore, also the current values of endogenous
variables (inflation etc). These you can, therefore, assume to be known
4
when you calculate expectations based on the (1-period-forwarded) MSV
solution.
13. Calculate the forecast errors of the inflation expectations that you have
just obtained (πt+1 −Etπt+1).
Hint: think about the timing of the columns in the data frame. You may
need to ’shift’ a column.
14. Run an OLS regression of forecast errors about inflation on the level of
inflation in the period that the forecast was made. Or put differently,
estimate β (and α) of the following regression model.
πt+1 −Etπt+1 = α + βπt + et (8)
How can you interpret your result?
5