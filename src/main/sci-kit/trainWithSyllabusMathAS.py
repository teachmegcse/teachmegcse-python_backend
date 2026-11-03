import trainModels
import os
import sys

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)

from main.utils import formatText


allLabels = ['Quadratics',
             'Functions',
             'Coordinate geometry',
             'Circular measure',
             'Trigonometry',
             'Series',
             'Differentiation',
             'Integration',
             'Algebra',
             'Logarithmic and exponential functions',
             'Numerical solution of equations',
             'Forces and equilibrium',
             'Kinematics of motion in a straight line',
             'Momentum',
             "Newton's laws of motion",
             'Energy, work and power',
             'Representation of data',
             'Permutations and combinations',
             'Probability',
             'Discrete random variables',
             'The normal distribution']


text1 = """
1.1 Quadratics
Candidates should be able to:
• carry out the process of completing the square
for a quadratic polynomial ax
2
+ bx + c and use
a completed square form
Notes and examples
e.g. to locate the vertex of the graph of
y = ax
2 + bx + c or to sketch the graph
• find the discriminant of a quadratic polynomial
ax
2
+ bx + c and use the discriminant
e.g. to determine the number of real roots of the
equation ax
2
+ bx + c = 0. Knowledge of the term
‘repeated root’ is included.
• solve quadratic equations, and quadratic
inequalities, in one unknown
By factorising, completing the square and using the
formula.
• solve by substitution a pair of simultaneous
equations of which one is linear and one is
quadratic
e.g. x + y + 1 = 0 and x
2
+ y
2
= 25,
2x + 3y = 7 and 3x
2
= 4 + 4xy.
• recognise and solve equations in x which are
quadratic in some function of x.
e.g. x
4
– 5x
2
+ 4 = 0, 6 1 x x + − = 0,
tan2
x = 1 + tanx.
"""

text2 = """
1.2 Functions
Candidates should be able to:
• understand the terms function, domain,
range, one-one function, inverse function and
composition of functions
Notes and examples
• identify the range of a given function in simple
cases, and find the composition of two given
functions
e.g. range of : x
x
1 f 7 for x H 1 and
range of g f : x x 1 or x R 2 7 + ! . Including the
condition that a composite function gf can only be
formed when the range of f is within the domain of g.
• determine whether or not a given function is
one-one, and find the inverse of a one-one
function in simple cases
e.g. finding the inverse of
: . x 2 3 x 4 x 2
3 h for
2 7 ^ h + − − 1
• illustrate in graphical terms the relation between
a one-one function and its inverse
Sketches should include an indication of the mirror
line y = x.
• understand and use the transformations of the
graph of y = f(x) given by
y = f(x) + a, y = f(x + a),
y = af(x), y = f(ax) and simple combinations of
these.
Including use of the terms ‘translation’, ‘reflection’
and ‘stretch’ in describing transformations. Questions
may involve algebraic or trigonometric functions, or
other graphs with given features.
"""

text3 = """
1.3 Coordinate geometry
Candidates should be able to:
• find the equation of a straight line given
sufficient information
Notes and examples
e.g. given two points, or one point and the gradient.
• interpret and use any of the forms y = mx + c,
y – y1 = m(x – x1), ax + by + c = 0 in solving
problems
Including calculations of distances, gradients,
midpoints, points of intersection and use of the
relationship between the gradients of parallel and
perpendicular lines.
• understand that the equation
(x – a)
2
+ (y – b)
2
= r
2
represents the circle
with centre (a, b) and radius r
Including use of the expanded form
x
2
+ y
2
+ 2gx + 2fy + c = 0.
• use algebraic methods to solve problems
involving lines and circles
Including use of elementary geometrical properties of
circles, e.g. tangent perpendicular to radius, angle in a
semicircle, symmetry.
Implicit differentiation is not included.
• understand the relationship between a graph and
its associated algebraic equation, and use the
relationship between points of intersection of
graphs and solutions of equations.
e.g. to determine the set of values of k for which the
line y = x + k intersects, touches or does not meet a
quadratic curve.
"""

text4 = """
1.4 Circular measure
Candidates should be able to:
• understand the definition of a radian, and use the
relationship between radians and degrees
Notes and examples
• use the formulae s r A r 2
1
and 2 = = i i
in solving problems concerning the arc length
and sector area of a circle.
Including calculation of lengths and angles in
triangles and areas of triangles.
"""

text5 = """
1.5 Trigonometry
Candidates should be able to:
• sketch and use graphs of the sine, cosine and
tangent functions (for angles of any size, and
using either degrees or radians)
Notes and examples
Including e.g. y = 3 sinx, y = 1 – cos 2x,
y tan x . 4
1 = + c m r
• use the exact values of the sine, cosine and
tangent of 30°, 45°, 60°, and related angles
e.g. cos s 150 , in 2
1 3 4
3
2
1 c = = − r .
• use the notations sin–1
x, cos–1
x, tan–1
x to denote
the principal values of the inverse trigonometric
relations
No specialised knowledge of these functions is
required, but understanding of them as examples of
inverse functions is expected.
• use the identities
cos
sin
/ tan i
i i and
sin cos 1 2 2 i i + /
e.g. in proving identities, simplifying expressions and
solving equations.
• find all the solutions of simple trigonometrical
equations lying in a specified interval (general
forms of solution are not included).
e.g. solve 3 2 sin x x + 1 0 = for − r r 1 1 ,
3 5 sin cos 1 0 for 0 360 2
i i − − = c c G G i .
2.3 Trigonometry
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
forms Rsin^ h i a ! and Rcos^ h i a ! .
e.g. simplifying cos s ^ ^ x x − 30c c h h − 3 in − 60 .
e.g. solving tan c i i + ot = 4, 2 5 sec tan 2
i i - = ,
3 2 cos s i i + in = 1.
"""

text6 = """
1.6 Series
Candidates should be able to:
• use the expansion of (a + b)
n
, where n is a
positive integer
Notes and examples
Including the notations n
r
f p and n!
Knowledge of the greatest term and properties of the
coefficients are not required.
• recognise arithmetic and geometric progressions
• use the formulae for the nth term and for the
sum of the first n terms to solve problems
involving arithmetic or geometric progressions
Including knowledge that numbers a, b, c are ‘in
arithmetic progression’ if 2b = a + c (or equivalent)
and are ‘in geometric progression’ if b2
= ac (or
equivalent).
Questions may involve more than one progression.
• use the condition for the convergence of a
geometric progression, and the formula for
the sum to infinity of a convergent geometric
progression.
"""

text7 = """
1.7 Differentiation
Candidates should be able to:
• understand the gradient of a curve at a point as
the limit of the gradients of a suitable sequence
of chords, and use the notations
f′(x), f ″(x), x
y
d
d
, and
x
y
d
d
2
2
for first and second
derivatives
Notes and examples
Only an informal understanding of the idea of a limit
is expected.
e.g. includes consideration of the gradient of the
chord joining the points with x coordinates 2 and
(2 + h) on the curve y = x
3
. Formal use of the general
method of differentiation from first principles is not
required.
• use the derivative of x
n
(for any rational n),
together with constant multiples, sums and
differences of functions, and of composite
functions using the chain rule
e.g. find x
y
d
d
, given y x2 5 3 = + .
• apply differentiation to gradients, tangents and
normals, increasing and decreasing functions and
rates of change
Including connected rates of change, e.g. given the
rate of increase of the radius of a circle, find the rate
of increase of the area for a specific value of one of
the variables.
• locate stationary points and determine their
nature, and use information about stationary
points in sketching graphs.
Including use of the second derivative for identifying
maxima and minima; alternatives may be used in
questions where no method is specified.
Knowledge of points of inflexion is not included.
2.4 Differentiation
Candidates should be able to:
• use the derivatives of e
x
, lnx, sin x, cos x,
tan x, together with constant multiples, sums,
differences and composites
Notes and examples
• differentiate products and quotients e.g. x
x
3 2
2 4 −
+ , x
2 lnx, xe
l–x2
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

text8 = """
1.8 Integration
Candidates should be able to:
• understand integration as the reverse process of
differentiation, and integrate (ax + b)
n
(for any
rational n except –1), together with constant
multiples, sums and differences
Notes and examples
e.g. 2 5 x x 1 dx 3 ;^ h − + , x
x
2 3
1 d2 + >
^ h .
• solve problems involving the evaluation of a
constant of integration
e.g. to find the equation of the curve through (1, –2)
for which . x
y 2 1 x d
d = +
• evaluate definite integrals Including simple cases of ‘improper’ integrals, such as
x xd and x xd
0
1 2
1
2
1 3 - - ; ; .
• use definite integration to find
– the area of a region bounded by a curve and
lines parallel to the axes, or between a curve
and a line or between two curves
– a volume of revolution about one of the axes.
A volume of revolution may involve a region not
bounded by the axis of rotation, e.g. the region
between y = 9 – x
2
and y = 5 rotated about the
x-axis.
Knowledge of the content for Paper 1: Pure Mathematics 1 is assumed, and candidates may be required to
demonstrate such knowledge in answering questions.
2.5 Integration
Candidates should be able to:
• extend the idea of ‘reverse differentiation’ to
include the integration of e
ax + b, ax b
1
+ ,
sin(ax + b), cos(ax + b) and sec2
(ax + b)
Notes and examples
Knowledge of the general method of integration by
substitution is not required.
• use trigonometrical relationships in carrying out
integration
e.g. use of double-angle formulae to integrate sin2
x
or cos2
(2x).
• understand and use the trapezium rule to
estimate the value of a definite integral.
Including use of sketch graphs in simple cases to
determine whether the trapezium rule gives an over￾estimate or an under-estimate.
"""

text9 = """
2.1 Algebra
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
e.g. |3x – 2| = |2x + 7|, 2x + 5 < |x + 1|
• divide a polynomial, of degree not exceeding 4,
by a linear or quadratic polynomial, and identify
the quotient and remainder (which may be zero)
• use the factor theorem and the remainder
theorem.
e.g. to find factors and remainders, solve polynomial
equations or evaluate unknown coefficients.
Including factors of the form (ax + b) in which the
coefficient of x is not unity, and including calculation
of remainders.
"""

text10 = """
2.2 Logarithmic and exponential functions
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
e.g. 2 5 x 1 , 3 2 5 3 1 x # 1 − , 3 4 x x 1 2 1 = + − .
• use logarithms to transform a given relationship
to linear form, and hence determine unknown
constants by considering the gradient and/or
intercept.
e.g.
y = kxn
gives ln y = ln k + nlnx which is linear in
ln x and ln y
y = k (ax
) gives lny = ln k + x lna which is linear in
x and ln y.
"""

text11 = """
2.6 Numerical solution of equations
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
of the form xn + 1 = F(xn) relates to the equation
being solved, and use a given iteration, or an
iteration based on a given rearrangement of an
equation, to determine a root to a prescribed
degree of accuracy.
Knowledge of the condition for convergence is not
included, but an understanding that an iteration may
fail to converge is expected.
Knowledge of the content of Paper 1: Pure Mathematics 1 is assumed, and candidates may be required to
demonstrate such knowledge in answering questions.
"""

text12 = """
4.1 Forces and equilibrium
Candidates should be able to:
• identify the forces acting in a given situation
Notes and examples
e.g. by drawing a force diagram.
• understand the vector nature of force, and find
and use components and resultants
Calculations are always required, not approximate
solutions by scale drawing.
• use the principle that, when a particle is in
equilibrium, the vector sum of the forces acting
is zero, or equivalently, that the sum of the
components in any direction is zero
Solutions by resolving are usually expected, but
equivalent methods (e.g. triangle of forces, Lami’s
Theorem, where suitable) are also acceptable; these
other methods are not required knowledge, and will
not be referred to in questions.
• understand that a contact force between two
surfaces can be represented by two components,
the normal component and the frictional
component
• use the model of a ‘smooth’ contact, and
understand the limitations of this model
• understand the concepts of limiting friction
and limiting equilibrium, recall the definition of
coefficient of friction, and use the relationship
F R = n or F R G n , as appropriate
Terminology such as ‘about to slip’ may be used to
mean ‘in limiting equilibrium’ in questions.
• use Newton’s third law. e.g. the force exerted by a particle on the ground
is equal and opposite to the force exerted by the
ground on the particle.
"""

text13 = """
4.2 Kinematics of motion in a straight line
Candidates should be able to:
• understand the concepts of distance and speed
as scalar quantities, and of displacement, velocity
and acceleration as vector quantities
Notes and examples
Restricted to motion in one dimension only.
The term ‘deceleration’ may sometimes be used in
the context of decreasing speed.
• sketch and interpret displacement–time graphs
and velocity–time graphs, and in particular
appreciate that
– the area under a velocity–time graph
represents displacement,
– the gradient of a displacement–time graph
represents velocity,
– the gradient of a velocity–time graph
represents acceleration
• use differentiation and integration with respect
to time to solve simple problems concerning
displacement, velocity and acceleration
Calculus required is restricted to techniques from the
content for Paper 1: Pure Mathematics 1.
• use appropriate formulae for motion with
constant acceleration in a straight line.
Questions may involve setting up more than one
equation, using information about the motion of
different particles.
"""

text14 = """
4.3 Momentum
Candidates should be able to:
• use the definition of linear momentum and show
understanding of its vector nature
Notes and examples
For motion in one dimension only.
• use conservation of linear momentum to solve
problems that may be modelled as the direct
impact of two bodies.
Including direct impact of two bodies where the
bodies coalesce on impact.
Knowledge of impulse and the coefficient of
restitution is not required.
"""

text15 = """
4.4 Newton’s laws of motion
Candidates should be able to:
• apply Newton’s laws of motion to the linear
motion of a particle of constant mass moving
under the action of constant forces, which may
include friction, tension in an inextensible string
and thrust in a connecting rod
Notes and examples
If any other forces resisting motion are to be
considered (e.g. air resistance) this will be indicated in
the question.
• use the relationship between mass and weight W = mg. In this component, questions are mainly
numerical, and use of the approximate numerical
value 10(ms
–2) for g is expected.
• solve simple problems which may be modelled as
the motion of a particle moving vertically or on
an inclined plane with constant acceleration
Including, for example, motion of a particle on a
rough plane where the acceleration while moving
up the plane is different from the acceleration while
moving down the plane.
• solve simple problems which may be modelled as
the motion of connected particles.
e.g. particles connected by a light inextensible string
passing over a smooth pulley, or a car towing a trailer
by means of either a light rope or a light rigid tow￾bar.
"""

text16 = """
4.5 Energy, work and power
Candidates should be able to:
• understand the concept of the work done by a
force, and calculate the work done by a constant
force when its point of application undergoes a
displacement not necessarily parallel to the force
Notes and examples
W F = d cos i;
Use of the scalar product is not required.
• understand the concepts of gravitational
potential energy and kinetic energy, and use
appropriate formulae
• understand and use the relationship between the
change in energy of a system and the work done
by the external forces, and use in appropriate
cases the principle of conservation of energy
Including cases where the motion may not be linear
(e.g. a child on a smooth curved ‘slide’), where only
overall energy changes need to be considered.
• use the definition of power as the rate at which
a force does work, and use the relationship
between power, force and velocity for a force
acting in the direction of motion
Including calculation of (average) power as
Time taken
Work done .
P = Fv.
• solve problems involving, for example, the
instantaneous acceleration of a car moving on a
hill against a resistance.
Questions set will be mainly numerical, and will test principles in probability and statistics without involving
knowledge of algebraic methods beyond the content for Paper 1: Pure Mathematics 1.
Knowledge of the following probability notation is also assumed: P(A), P^ h A B, , P^ h A B+ , P(A|B) and the use
of A′ to denote the complement of A.
"""

text17 = """
5.1 Representation of data
Candidates should be able to:
• select a suitable way of presenting raw
statistical data, and discuss advantages and/or
disadvantages that particular representations
may have
Notes and examples
• draw and interpret stem-and-leaf diagrams, box￾and-whisker plots, histograms and cumulative
frequency graphs
Including back-to-back stem-and-leaf diagrams.
• understand and use different measures of central
tendency (mean, median, mode) and variation
(range, interquartile range, standard deviation)
e.g. in comparing and contrasting sets of data.
• use a cumulative frequency graph e.g. to estimate medians, quartiles, percentiles, the
proportion of a distribution above (or below) a given
value, or between two values.
• calculate and use the mean and standard
deviation of a set of data (including grouped
data) either from the data itself or from given
totals /x and x / 2
, or coded totals /^ h x a −
and x a
2 /^ h − , and use such totals in solving
problems which may involve up to two data sets.
"""

text18 = """
5.2 Permutations and combinations
Candidates should be able to:
• understand the terms permutation and
combination, and solve simple problems
involving selections
Notes and examples
• solve problems about arrangements of objects in
a line, including those involving
– repetition (e.g. the number of ways of
arranging the letters of the word ‘NEEDLESS’)
– restriction (e.g. the number of ways several
people can stand in a line if two particular
people must, or must not, stand next to each
other).
Questions may include cases such as people sitting in
two (or more) rows.
Questions about objects arranged in a circle will not
be included.
"""

text19 = """
5.3 Probability
Candidates should be able to:
• evaluate probabilities in simple cases by means
of enumeration of equiprobable elementary
events, or by calculation using permutations or
combinations
Notes and examples
e.g. the total score when two fair dice are thrown.
e.g. drawing balls at random from a bag containing
balls of different colours.
• use addition and multiplication of probabilities,
as appropriate, in simple cases
Explicit use of the general formula
P P ^ ^ A B, + h h = A B + P P ^ ^ h h − A B is not required.
• understand the meaning of exclusive and
independent events, including determination
of whether events A and B are independent
by comparing the values of P^ h A B+ and
P P ^ ^ A B h h #
• calculate and use conditional probabilities in
simple cases.
e.g. situations that can be represented by a sample
space of equiprobable elementary events, or a tree
diagram. The use of A B B
A B
P P
P + ^ = ^
^ h h
h
may be
required in simple cases.
"""

text20 = """
5.4 Discrete random variables
Candidates should be able to:
• draw up a probability distribution table relating
to a given situation involving a discrete random
variable X, and calculate E(X) and Var(X)
Notes and examples
• use formulae for probabilities for the binomial
and geometric distributions, and recognise
practical situations where these distributions are
suitable models
Including the notations B(n, p) and Geo(p). Geo(p)
denotes the distribution in which pr = p(1 – p)
r–1
for
r = 1, 2, 3, … .
• use formulae for the expectation and variance of
the binomial distribution and for the expectation
of the geometric distribution.
Proofs of formulae are not required.
"""

text21 = """
5.5 The normal distribution
Candidates should be able to:
• understand the use of a normal distribution to
model a continuous random variable, and use
normal distribution tables
Notes and examples
Sketches of normal curves to illustrate distributions
or probabilities may be required.
• solve problems concerning a variable X, where
X N , 2 + _n v i, including
– finding the value of P X x > 1 _ i, or a related
probability, given the values of x1
, n, v.
– finding a relationship between x1
, n and v
given the value of P X x > 1 _ i or a related
probability
For calculations involving standardisation, full details
of the working should be shown.
e.g. Z
X
v
n = _ - i
• recall conditions under which the normal
distribution can be used as an approximation
to the binomial distribution, and use this
approximation, with a continuity correction, in
solving problems.
n sufficiently large to ensure that both np > 5 and
nq > 5.
Knowledge of the content of Paper 5: Probability & Statistics 1 is assumed, and candidates may be required to
demonstrate such knowledge in answering questions. Knowledge of calculus within the content for Paper 3: Pure
Mathematics 3 will also be assumed.
"""

textarr = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14, text15, text16, text17, text18, text19, text20, text21]
data, labels = [], []
for label, chapter_text in zip(allLabels, textarr):
    for chunk in trainModels.chunk_lines(chapter_text):
        data.append(formatText(chunk))
        labels.append(label)

trainModels.train(data, labels, f"{BASE_PATH}/resources/sci-kit/asmath.joblib")
