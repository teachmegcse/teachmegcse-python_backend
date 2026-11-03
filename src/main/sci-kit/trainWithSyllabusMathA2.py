import trainModels
import os
import sys

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)

from main.utils import formatText


allLabels = ['Algebra',
             'Logarithmic and exponential functions',
             'Trigonometry',
             'Differentiation',
             'Integration',
             'Numerical solution of equations',
             'Vectors',
             'Differential equations',
             'Complex numbers',
             'The Poisson distribution',
             'Linear combinations of random variables',
             'Continuous random variables',
             'Sampling and estimation',
             'Hypothesis tests']


text1 = """
3.1 Algebra
Candidates should be able to:
• understand the meaning of |x|, sketch the
graph of y = |ax + b| and use relations such as
|a| = |b| ⇔ a
2
= b2
and
|x – a| < b ⇔ a – b < x < a + b when solving
equations and inequalities
Notes and examples
Graphs of y = |f(x)| and y = f(|x|) for non-linear
functions f are not included.
e.g. |3x – 2| = |2x + 7|, 2x + 5 < |x + 1|.
• divide a polynomial, of degree not exceeding 4,
by a linear or quadratic polynomial, and identify
the quotient and remainder (which may be zero)
• use the factor theorem and the remainder
theorem
e.g. to find factors and remainders, solve polynomial
equations or evaluate unknown coefficients.
Including factors of the form (ax + b) in which the
coefficient of x is not unity, and including calculation
of remainders.
• recall an appropriate form for expressing rational
functions in partial fractions, and carry out the
decomposition, in cases where the denominator
is no more complicated than
– (ax + b)(cx + d)(ex + f)
– (ax + b)(cx + d)
2
– (ax + b)(cx
2
+ d)
Excluding cases where the degree of the numerator
exceeds that of the denominator
• use the expansion of (1 + x)
n
, where n is a
rational number and x 1 1.
Finding the general term in an expansion is not
included.
Adapting the standard series to expand
e.g. 2 x2
1 1 − −
` j is included, and determining the set
of values of x for which the expansion is valid in such
cases is also included.
"""

text2 = """
3.2 Logarithmic and exponential functions
Candidates should be able to:
• understand the relationship between logarithms
and indices, and use the laws of logarithms
(excluding change of base)
Notes and examples
• understand the definition and properties of e
x
and lnx, including their relationship as inverse
functions and their graphs
Including knowledge of the graph of y = ekx for both
positive and negative values of k.
• use logarithms to solve equations and
inequalities in which the unknown appears in
indices
e.g. 2 5 x 1 , 3 2 < 5 3 1 x # − , 3 4 x x 1 2 1 = + − .
• use logarithms to transform a given relationship
to linear form, and hence determine unknown
constants by considering the gradient and/or
intercept.
e.g.
y = kxn
gives ln y = lnk + n ln x which is linear in lnx
and ln y.
y = k (ax
) gives ln y = lnk + x lna which is linear in
x and ln y.
"""

text3 = """
3.3 Trigonometry
Candidates should be able to:
• understand the relationship of the secant,
cosecant and cotangent functions to cosine, sine
and tangent, and use properties and graphs of
all six trigonometric functions for angles of any
magnitude
Notes and examples
• use trigonometrical identities for the
simplification and exact evaluation of expressions,
and in the course of solving equations, and
select an identity or identities appropriate to the
context, showing familiarity in particular with the
use of
– sec t 1 an 2 2 i i / + and cosec c 1 ot 2 2 i i / +
– the expansions of sin(A ± B), cos(A ± B) and
tan(A ± B)
– the formulae for sin 2A, cos 2A and tan 2A
– the expression of a b sin c i i + os in the
forms Rsin^ h i ! a and Rcos^ h i ! a .
e.g. simplifying cos(x – 30˚) – 3 sin(x – 60˚).
e.g. solving tan c i i + ot = 4, 2 5 sec tan 2
i i − = ,
3 2 cos s i i + in = 1.
"""

text4 = """
3.4 Differentiation
Candidates should be able to:
• use the derivatives of e
x
, lnx, sin x, cos x, tanx,
tan–1
x, together with constant multiples, sums,
differences and composites
Notes and examples
Derivatives of sin–1
x and cos–1
x are not required.
• differentiate products and quotients e.g. x
x
3 2
2 4 −
+ , x
2
ln x, xe
1–x2
.
• find and use the first derivative of a function
which is defined parametrically or implicitly.
e.g. x = t – e2t
, y = t + e2t
.
e.g. x
2
+ y
2
= xy + 7.
Including use in problems involving tangents and
normals.
"""

text5 = """
3.5 Integration
Candidates should be able to:
• extend the idea of ‘reverse differentiation’ to
include the integration of e
ax + b, ax b
1
+ ,
sin(ax + b), cos(ax + b), sec2
(ax + b)
and
x a
1
2 2 +
Notes and examples
Including examples such as 2 3x
1
2 + .
• use trigonometrical relationships in carrying out
integration
e.g. use of double-angle formulae to integrate sin2
x
or cos2
(2x).
• integrate rational functions by means of
decomposition into partial fractions
Restricted to types of partial fractions as specified in
topic 3.1 above.
• recognise an integrand of the form x
k x
f
fl
^
^
h
h
, and
integrate such functions
e.g. integration of
x
x
1 2 + , tan x.
• recognise when an integrand can usefully be
regarded as a product, and use integration by
parts
e.g. integration of x sin 2x, x
2
e
–x
, ln x, x tan–1
x.
• use a given substitution to simplify and evaluate
either a definite or an indefinite integral.
e.g. to integrate sin2 2x cos x using the substitution
u = sinx.
"""

text6 = """
3.6 Numerical solution of equations
Candidates should be able to:
• locate approximately a root of an equation,
by means of graphical considerations and/or
searching for a sign change
Notes and examples
e.g. finding a pair of consecutive integers between
which a root lies.
• understand the idea of, and use the notation for,
a sequence of approximations which converges
to a root of an equation
• understand how a given simple iterative formula
of the form xn + 1
= F(xn) relates to the equation
being solved, and use a given iteration, or an
iteration based on a given rearrangement of an
equation, to determine a root to a prescribed
degree of accuracy.
Knowledge of the condition for convergence is not
included, but an understanding that an iteration may
fail to converge is expected.
"""

text7 = """
3.7 Vectors
Candidates should be able to:
• use standard notations for vectors, i.e.
x
y
f p, xi + yj,
x
y
z
f p, xi + yj + zk, AB , a
Notes and examples
• carry out addition and subtraction of vectors
and multiplication of a vector by a scalar, and
interpret these operations in geometrical terms
e.g. ‘OABC is a parallelogram’ is equivalent to
OB = OA + OC .
The general form of the ratio theorem is not
included, but understanding that the midpoint of
AB has position vector 2 OA OB 1 _ + i is expected.
• calculate the magnitude of a vector, and use
unit vectors, displacement vectors and position
vectors
In 2 or 3 dimensions.
• understand the significance of all the symbols
used when the equation of a straight line is
expressed in the form r = a + tb, and find the
equation of a line, given sufficient information
e.g. finding the equation of a line given the position
vector of a point on the line and a direction vector, or
the position vectors of two points on the line.
• determine whether two lines are parallel,
intersect or are skew, and find the point of
intersection of two lines when it exists
Calculation of the shortest distance between two
skew lines is not required. Finding the equation of
the common perpendicular to two skew lines is also
not required.
• use formulae to calculate the scalar product of
two vectors, and use scalar products in problems
involving lines and points.
e.g. finding the angle between two lines, and finding
the foot of the perpendicular from a point to a line;
questions may involve 3D objects such as cuboids,
tetrahedra (pyramids), etc.
Knowledge of the vector product is not required.
"""

text8 = """
3.8 Differential equations
Candidates should be able to:
• formulate a simple statement involving a rate of
change as a differential equation
Notes and examples
The introduction and evaluation of a constant of
proportionality, where necessary, is included.
• find by integration a general form of solution for
a first order differential equation in which the
variables are separable
Including any of the integration techniques from
topic 3.5 above.
• use an initial condition to find a particular
solution
• interpret the solution of a differential equation in
the context of a problem being modelled by the
equation.
Where a differential equation is used to model a
‘real-life’ situation, no specialised knowledge of the
context will be required.
"""

text9 = """
3.9 Complex numbers
Candidates should be able to:
• understand the idea of a complex number, recall
the meaning of the terms real part, imaginary
part, modulus, argument, conjugate, and use the
fact that two complex numbers are equal if and
only if both real and imaginary parts are equal
Notes and examples
Notations Re z, Imz, |z|, arg z, z* should be known.
The argument of a complex number will usually
refer to an angle i such that −r r 1 i G , but in
some cases the interval 0 2 G i 1 r may be more
convenient. Answers may use either interval unless
the question specifies otherwise.
• carry out operations of addition, subtraction,
multiplication and division of two complex
numbers expressed in Cartesian form x + iy
For calculations involving multiplication or division,
full details of the working should be shown.
• use the result that, for a polynomial equation
with real coefficients, any non-real roots occur in
conjugate pairs
e.g. in solving a cubic or quartic equation where one
complex root is given.
• represent complex numbers geometrically by
means of an Argand diagram
• carry out operations of multiplication and
division of two complex numbers expressed in
polar form r r cos si in ei i i + / i ^ h
Including the results |z1
z2
| = |z1||z2
| and
arg a _ _ z z1 2i i = rg z z 1 2 + arg_ i, and corresponding
results for division.
• find the two square roots of a complex number e.g. the square roots of 5 + 12i in exact Cartesian
form. Full details of the working should be shown.
• understand in simple terms the geometrical
effects of conjugating a complex number and of
adding, subtracting, multiplying and dividing two
complex numbers
• illustrate simple equations and inequalities
involving complex numbers by means of loci in
an Argand diagram
e.g. |z – a| < k, |z – a| = |z – b|, arg(z – a) = α.
Questions set will be mainly numerical, and will aim to test mechanical principles without involving difficult
algebra or trigonometry. However, candidates should be familiar in particular with the following trigonometrical
results:
sin c ^ h 90c - i / os i, cos s ^ h 90c - i / in i, tan
cos
sin i / i
i , sin cos 1 2 2 i i + / .
Knowledge of algebraic methods from the content for Paper 1: Pure Mathematics 1 is assumed.
This content list refers to the equilibrium or motion of a ‘particle’. Examination questions may involve extended
bodies in a ‘realistic’ context, but these extended bodies should be treated as particles, so any force acting on
them is modelled as acting at a single point.
Vector notation will not be used in the question papers.
"""

text10 = """
6.1 The Poisson distribution
Candidates should be able to:
• use formulae to calculate probabilities for the
distribution Po^ hm
Notes and examples
• use the fact that if X + Po^ hm then the mean
and variance of X are each equal to m
Proofs are not required.
• understand the relevance of the Poisson
distribution to the distribution of random events,
and use the Poisson distribution as a model
• use the Poisson distribution as an approximation
to the binomial distribution where appropriate
The conditions that n is large and p is small should be
known; n > 50 and np < 5, approximately.
• use the normal distribution, with continuity
correction, as an approximation to the Poisson
distribution where appropriate.
The condition that m is large should be known;
m 2 15, approximately.
"""

text11 = """
6.2 Linear combinations of random variables
Candidates should be able to:
• use, when solving problems, the results that
– E(aX + b) = aE(X) + b and
Var(aX + b) = a
2Var(X)
– E(aX + bY) = aE(X) + bE(Y)
– Var(aX + bY) = a
2Var(X) + b2Var(Y) for
independent X and Y
– if X has a normal distribution then so does
aX + b
– if X and Y have independent normal
distributions then aX + bY has a normal
distribution
– if X and Y have independent Poisson
distributions then X + Y has a Poisson
distribution.
Notes and examples
Proofs of these results are not required.
"""

text12 = """
6.3 Continuous random variables
Candidates should be able to:
• understand the concept of a continuous random
variable, and recall and use properties of a
probability density function
Notes and examples
For density functions defined over a single interval
only; the domain may be infinite,
e.g.
x
3
4 for x H 1.
• use a probability density function to solve
problems involving probabilities, and to calculate
the mean and variance of a distribution.
Including location of the median or other percentiles
of a distribution by direct consideration of an area
using the density function.
Explicit knowledge of the cumulative distribution
function is not included.
"""

text13 = """
6.4 Sampling and estimation
Candidates should be able to:
• understand the distinction between a sample and
a population, and appreciate the necessity for
randomness in choosing samples
Notes and examples
• explain in simple terms why a given sampling
method may be unsatisfactory
Including an elementary understanding of the use of
random numbers in producing random samples.
Knowledge of particular sampling methods, such as
quota or stratified sampling, is not required.
• recognise that a sample mean can be regarded as
a random variable, and use the facts that
E_X i = n and that X
n
Var
2 v _ i =
• use the fact that _X i has a normal distribution if
X has a normal distribution
• use the Central Limit Theorem where appropriate Only an informal understanding of the Central Limit
Theorem (CLT) is required; for large sample sizes,
the distribution of a sample mean is approximately
normal.
• calculate unbiased estimates of the population
mean and variance from a sample, using either
raw or summarised data
Only a simple understanding of the term ‘unbiased’ is
required, e.g. that although individual estimates will
vary the process gives an accurate result ‘on average’.
• determine and interpret a confidence interval for
a population mean in cases where the population
is normally distributed with known variance or
where a large sample is used
• determine, from a large sample, an approximate
confidence interval for a population proportion.
"""

text14 = """
6.5 Hypothesis tests
Candidates should be able to:
• understand the nature of a hypothesis test, the
difference between one-tailed and two-tailed
tests, and the terms null hypothesis, alternative
hypothesis, significance level, rejection region
(or critical region), acceptance region and test
statistic
Notes and examples
Outcomes of hypothesis tests are expected to
be interpreted in terms of the contexts in which
questions are set.
• formulate hypotheses and carry out a hypothesis
test in the context of a single observation from
a population which has a binomial or Poisson
distribution, using
– direct evaluation of probabilities
– a normal approximation to the binomial or
the Poisson distribution, where appropriate
• formulate hypotheses and carry out a hypothesis
test concerning the population mean in cases
where the population is normally distributed with
known variance or where a large sample is used
• understand the terms Type I error and Type II
error in relation to hypothesis tests
• calculate the probabilities of making Type I and
Type II errors in specific situations involving
tests based on a normal distribution or direct
evaluation of binomial or Poisson probabilities.
"""

textarr = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14]
data, labels = [], []
for label, chapter_text in zip(allLabels, textarr):
    for chunk in trainModels.chunk_lines(chapter_text):
        data.append(formatText(chunk))
        labels.append(label)

trainModels.train(data, labels, f"{BASE_PATH}/resources/sci-kit/a2math.joblib")
