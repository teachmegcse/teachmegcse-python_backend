import trainModels
import os
import sys

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)

from main.utils import formatText


allLabels = ['Number',
             'Algebra and graphs',
             'Coordinate geometry',
             'Geometry',
             'Mensuration',
             'Trigonometry',
             'Transformations and vectors',
             'Probability',
             'Statistics']


text1 = """
1 Number
C1.1 Types of number Notes and examples
Identify and use:
• natural numbers
• integers (positive, zero and negative)
• prime numbers
• square numbers
• cube numbers
• common factors
• common multiples
• rational and irrational numbers
• reciprocals.
Example tasks include:
• convert between numbers and words, e.g.
six billion is 6000000000
10007 is ten thousand and seven
• express 72 as a product of its prime factors
• find the highest common factor (HCF) of two
numbers
• find the lowest common multiple (LCM) of two
numbers.
1 Number (continued)
C1.2 Sets Notes and examples
Understand and use set language, notation and
Venn diagrams to describe sets.
Venn diagrams are limited to two sets.
The following set notation will be used:
• n(A) Number of elements in set A
• A′ Complement of set A
• Universal set
• A ∪ B Union of A and B
• A ∩ B Intersection of A and B.
Example definition of sets:
A = {x: x is a natural number}
B = {a, b, c, …}
C = {x: a ⩽ x ⩽ b}.
C1.3 Powers and roots Notes and examples
Calculate with the following:
• squares
• square roots
• cubes
• cube roots
• other powers and roots of numbers.
Includes recall of squares and their corresponding
roots from 1 to 15, and recall of cubes and their
corresponding roots of 1, 2, 3, 4, 5 and 10, e.g.:
• Write down the value of 169 .
• Work out 5 8 2 3 # .
C1.4 Fractions, decimals and percentages Notes and examples
1  Use the language and notation of the following in
appropriate contexts:
• proper fractions
• improper fractions
• mixed numbers
• decimals
• percentages.
2  Recognise equivalence and convert between
these forms.
Candidates are expected to be able to write
fractions in their simplest form.
Candidates are not expected to use recurring
decimal notation.
Candidates are not expected to demonstrate the
conversion of a recurring decimal to a fraction and
vice versa.
C1.5 Ordering Notes and examples
Order quantities by magnitude and demonstrate
familiarity with the symbols =, ≠, >, < , ⩾ and ⩽ .
1 Number (continued)
C1.6 The four operations Notes and examples
Use the four operations for calculations with
integers, fractions and decimals, including correct
ordering of operations and use of brackets.
Includes:
• negative numbers
• improper fractions
• mixed numbers
• practical situations, e.g. temperature changes.
C1.7 Indices I Notes and examples
1  Understand and use indices (positive, zero and
negative integers).
2  Understand and use the rules of indices.
e.g. find the value of 7 –2.
e.g. find the value of 2–3 × 24
, (23
)
2
, 23
÷ 24
.
C1.8 Standard form Notes and examples
1  Use the standard form A × 10n
where n is a
positive or negative integer and 1 ⩽ A < 10.
2  Convert numbers into and out of standard form.
3  Calculate with values in standard form. Core candidates are expected to calculate with
standard form only on Paper 3.
C1.9 Estimation Notes and examples
1  Round values to a specified degree of accuracy.
2  Make estimates for calculations involving
numbers, quantities and measurements.
3  Round answers to a reasonable degree of
accuracy in the context of a given problem.
Includes decimal places and significant figures.
e.g. write 5764 correct to the nearest thousand.
e.g. by writing each number correct to 1 significant
figure, estimate the value of . .
.
9 79 0 765
41 3
# .
C1.10 Limits of accuracy Notes and examples
Give upper and lower bounds for data rounded to a
specified accuracy.
e.g. write down the upper bound of a length
measured correct to the nearest metre.
Candidates are not expected to find the bounds
of the results of calculations which have used data
rounded to a specified accuracy.
1 Number (continued)
C1.11 Ratio and proportion Notes and examples
Understand and use ratio and proportion to:
• give ratios in their simplest form
• divide a quantity in a given ratio
• use proportional reasoning and ratios in
context.
e.g. 20:30:40 in its simplest form is 2:3:4.
e.g. adapt recipes; use map scales; determine best
value.
C1.12 Rates Notes and examples
1 Use common measures of rate.
2 Apply other measures of rate.
3 Solve problems involving average speed.
e.g. calculate with:
• hourly rates of pay
• exchange rates between currencies
• flow rates
• fuel consumption.
e.g. calculate with:
• pressure
• density
• population density.
Required formulas will be given in the question.
Knowledge of speed/distance/time formula is
required.
e.g. A cyclist travels 45km in 3 hours 45 minutes.
What is their average speed?
Notation used will be, e.g. m/s (metres per second),
g/cm3
(grams per cubic centimetre).
C1.13 Percentages Notes and examples
1 Calculate a given percentage of a quantity.
2 Express one quantity as a percentage of another.
3 Calculate percentage increase or decrease.
4 Calculate with simple and compound interest. Formulas are not given.
Percentage calculations may include:
• deposit
• discount
• profit and loss (as an amount or a percentage)
• earnings
• percentages over 100%.
1 Number (continued)
C1.14 Using a calculator Notes and examples
1 Use a calculator efficiently.
2 Enter values appropriately on a calculator.
3 Interpret the calculator display appropriately.
e.g. know not to round values within a calculation
and to only round the final answer.
e.g. enter 2 hours 30 minutes as 2.5 hours or
2° 30’ 0’’.
e.g. in money 4.8 means $4.80; in time 3.25 means
3 hours 15 minutes.
C1.15 Time Notes and examples
1  Calculate with time: seconds (s), minutes (min),
hours (h), days, weeks, months, years, including
the relationship between units.
2  Calculate times in terms of the 24-hour and
12-hour clock.
3 Read clocks and timetables.
1 year = 365 days.
In the 24-hour clock, for example, 3.15 a.m. will be
denoted by 0315 and 3.15 p.m. by 1515.
Includes problems involving time zones, local times
and time differences.
C1.16 Money Notes and examples
1 Calculate with money.
2 Convert from one currency to another.
1 Number
E1.1 Types of number Notes and examples
Identify and use:
• natural numbers
• integers (positive, zero and negative)
• prime numbers
• square numbers
• cube numbers
• common factors
• common multiples
• rational and irrational numbers
• reciprocals.
Example tasks include:
• convert between numbers and words, e.g.
six billion is 6000000000
10007 is ten thousand and seven
• express 72 as a product of its prime factors
• find the highest common factor (HCF) of two
numbers
• find the lowest common multiple (LCM) of two
numbers.
E1.2 Sets Notes and examples
Understand and use set language, notation and
Venn diagrams to describe sets and represent
relationships between sets.
Venn diagrams are limited to two or three sets.
The following set notation will be used:
• n(A) Number of elements in set A
• ∈ “… is an element of …”
• ∉ “… is not an element of …”
• A′ Complement of set A
• ∅ The empty set
• Universal set
• A ⊆ B A is a subset of B
• A ⊈ B A is not a subset of B
• A ∪ B Union of A and B
• A ∩ B Intersection of A and B.
Example definition of sets:
A = {x: x is a natural number}
B = {(x, y): y = mx + c}
C = {x: a ⩽ x ⩽ b}
D = {a, b, c, …}.
E1.3 Powers and roots Notes and examples
Calculate with the following:
• squares
• square roots
• cubes
• cube roots
• other powers and roots of numbers.
Includes recall of squares and their corresponding
roots from 1 to 15, and recall of cubes and their
corresponding roots of 1, 2, 3, 4, 5 and 10, e.g.:
• Write down the value of 169 .
• Work out 5 8 2 3 # .
1 Number (continued)
E1.4 Fractions, decimals and percentages Notes and examples
1  Use the language and notation of the following in
appropriate contexts:
• proper fractions
• improper fractions
• mixed numbers
• decimals
• percentages.
2  Recognise equivalence and convert between
these forms.
Candidates are expected to be able to write
fractions in their simplest form.
Recurring decimal notation is required, e.g.
• 0 1. . 7 0 o = 1777f
0. . 123o o =0 1232323f
• 0. . 123 =0 123123f
Includes converting between recurring decimals
and fractions and vice versa,
e.g. write 0 1. 7
o as a fraction.
E1.5 Ordering Notes and examples
Order quantities by magnitude and demonstrate
familiarity with the symbols =, ≠, >, < , ⩾ and ⩽.
E1.6 The four operations Notes and examples
Use the four operations for calculations with
integers, fractions and decimals, including correct
ordering of operations and use of brackets.
Includes:
• negative numbers
• improper fractions
• mixed numbers
• practical situations, e.g. temperature changes.
E1.7 Indices I Notes and examples
1  Understand and use indices (positive, zero,
negative, and fractional).
2 Understand and use the rules of indices.
Examples include:
• 6 6 2
1
=
• 16 16 4 4
1
=
• find the value of 7 –2, 812
1
, 8 3
2 - .
e.g. find the value of 2–3 × 24
, (23
)
2
, 23 ÷ 24
.
E1.8 Standard form Notes and examples
1  Use the standard form A × 10n
where n is a
positive or negative integer and 1 ⩽ A < 10.
2 Convert numbers into and out of standard form.
3 Calculate with values in standard form.
1 Number (continued)
E1.9 Estimation Notes and examples
1 Round values to a specified degree of accuracy.
2  Make estimates for calculations involving
numbers, quantities and measurements.
3  Round answers to a reasonable degree of
accuracy in the context of a given problem.
Includes decimal places and significant figures.
e.g. write 5764 correct to the nearest thousand.
e.g. by writing each number correct to 1 significant
figure, estimate the value of
. .
.
9 79 0 765
41 3
# .
E1.10 Limits of accuracy Notes and examples
1  Give upper and lower bounds for data rounded
to a specified accuracy.
2  Find upper and lower bounds of the results of
calculations which have used data rounded to a
specified accuracy.
e.g. write down the upper bound of a length
measured correct to the nearest metre.
Example calculations include:
• calculate the upper bound of the perimeter
or the area of a rectangle given dimensions
measured to the nearest centimetre
• find the lower bound of the speed given
rounded values of distance and time.
E1.11 Ratio and proportion Notes and examples
Understand and use ratio and proportion to:
• give ratios in their simplest form
• divide a quantity in a given ratio
• use proportional reasoning and ratios in
context.
e.g. 20:30:40 in its simplest form is 2:3:4.
e.g. adapt recipes; use map scales; determine best
value.
1 Number (continued)
E1.12 Rates Notes and examples
1 Use common measures of rate.
2 Apply other measures of rate.
3 Solve problems involving average speed.
e.g. calculate with:
• hourly rates of pay
• exchange rates between currencies
• flow rates
• fuel consumption.
e.g. calculate with:
• pressure
• density
• population density.
Required formulas will be given in the question.
Knowledge of speed/distance/time formula is
required.
e.g. A cyclist travels 45km in 3 hours 45 minutes.
What is their average speed?
Notation used will be, e.g. m/s (metres per second),
g/cm3
(grams per cubic centimetre).
E1.13 Percentages Notes and examples
1 Calculate a given percentage of a quantity.
2 Express one quantity as a percentage of another.
3 Calculate percentage increase or decrease.
4 Calculate with simple and compound interest.
5 Calculate using reverse percentages.
Problems may include repeated percentage
change.
Formulas are not given.
e.g. find the cost price given the selling price and
the percentage profit.
Percentage calculations may include:
• deposit
• discount
• profit and loss (as an amount or a percentage)
• earnings
• percentages over 100%.
E1.14 Using a calculator Notes and examples
1 Use a calculator efficiently.
2 Enter values appropriately on a calculator.
3 Interpret the calculator display appropriately.
e.g. know not to round values within a calculation
and to only round the final answer.
e.g. enter 2 hours 30 minutes as 2.5 hours or
2° 30’ 0’’.
e.g. in money 4.8 means $4.80; in time 3.25 means
3 hours 15 minutes.
1 Number (continued)
E1.15 Time Notes and examples
1  Calculate with time: seconds (s), minutes (min),
hours (h), days, weeks, months, years, including
the relationship between units.
2  Calculate times in terms of the 24-hour and
12-hour clock.
3 Read clocks and timetables.
1 year = 365 days.
In the 24-hour clock, for example, 3.15 a.m. will be
denoted by 0315 and 3.15 p.m. by 1515.
Includes problems involving time zones, local times
and time differences.
E1.16 Money Notes and examples
1 Calculate with money.
2 Convert from one currency to another.
E1.17 Exponential growth and decay Notes and examples
Use exponential growth and decay. e.g. depreciation, population change.
Knowledge of e is not required.
E1.18 Surds Notes and examples
1  Understand and use surds, including simplifying
expressions.
2 Rationalise the denominator.
Examples include:
• 20 = 2 5
200 − 32 = 6 2 .
Examples include:
• 5
10 = 2 5
1 3
1
2
1 3
− + = + .
"""

text2 = """
2 Algebra and graphs
C2.1 Introduction to algebra Notes and examples
1  Know that letters can be used to represent
generalised numbers.
2  Substitute numbers into expressions and
formulas.
C2.2 Algebraic manipulation Notes and examples
1 Simplify expressions by collecting like terms.
2 Expand products of algebraic expressions.
3 Factorise by extracting common factors.
Simplify means give the answer in its simplest form,
e.g. 2a + 3b + 5a – 9b = 7a – 6b.
e.g. expand 3x(2x – 4y).
Includes products of two brackets involving one
variable, e.g. expand (2x + 1)(x – 4).
Factorise means factorise fully,
e.g. 9x
2
+ 15xy = 3x(3x + 5y).
C2.4 Indices II Notes and examples
1  Understand and use indices (positive, zero and
negative).
2 Understand and use the rules of indices.
e.g. 2x
= 32. Find the value of x.
e.g. simplify:
• (5x 3
)
2
• 12a 5 ÷ 3a
–2
• 6x 7
y
4 × 5x –5
y.
Knowledge of logarithms is not required.
C2.5 Equations Notes and examples
1  Construct simple expressions, equations and
formulas.
2 Solve linear equations in one unknown.
3  Solve simultaneous linear equations in two
unknowns.
4 Change the subject of simple formulas.
e.g. write an expression for a number that is 2 more
than n.
Includes constructing linear simultaneous
equations.
Examples include:
• 3x + 4 = 10
• 5 – 2x = 3(x + 7).
e.g. change the subject of formulas where:
• the subject only appears once
• there is not a power or root of the subject.
2 Algebra and graphs (continued)
C2.6 Inequalities Notes and examples
Represent and interpret inequalities, including on a
number line.
When representing and interpreting inequalities on
a number line:
• open circles should be used to represent strict
inequalities (<, >)
• closed circles should be used to represent
inclusive inequalities (⩽, ⩾)
e.g. – 3 ⩽ x < 1
–3 –2 –1 0 1
x
C2.7 Sequences Notes and examples
1 Continue a given number sequence or pattern.
2  Recognise patterns in sequences, including the
term-to-term rule, and relationships between
different sequences.
3  Find and use the nth term of the following
sequences:
(a) linear
(b) simple quadratic
(c) simple cubic.
e.g. write the next two terms in this sequence:
1, 3, 6, 10, 15, … , …
e.g. find the nth term of 2, 5, 10, 17
C2.9 Graphs in practical situations Notes and examples
1  Use and interpret graphs in practical situations
including travel graphs and conversion graphs.
2 Draw graphs from given data.
e.g. interpret the gradient of a straight-line graph as
a rate of change.
e.g. draw a distance–time graph to represent a
journey.
2 Algebra and graphs (continued)
C2.10 Graphs of functions Notes and examples
1  Construct tables of values, and draw, recognise
and interpret graphs for functions of the following
forms:
• ax + b
• ± x
2
+ ax + b
• x
a (x ≠ 0)
where a and b are integer constants.
2  Solve associated equations graphically, including
finding and interpreting roots by graphical
methods.
e.g. find the intersection of a line and a curve.
C2.11 Sketching curves Notes and examples
Recognise, sketch and interpret graphs of the
following functions:
(a) linear
(b) quadratic. Knowledge of symmetry and roots is required.
Knowledge of turning points is not required.
2 Algebra and graphs
E2.1 Introduction to algebra Notes and examples
1  Know that letters can be used to represent
generalised numbers.
2  Substitute numbers into expressions and
formulas.
E2.2 Algebraic manipulation Notes and examples
1 Simplify expressions by collecting like terms.
2 Expand products of algebraic expressions.
3 Factorise by extracting common factors.
4 Factorise expressions of the form:
• ax + bx + kay + kby
• a
2
x
2
− b2
y
2
• a
2
+ 2ab + b2
• ax
2
+ bx + c
• ax
3
+ bx2
+ cx.
5  Complete the square for expressions in the form
ax
2
+ bx + c.
Simplify means give the answer in its simplest form,
e.g. 2a
2
+ 3ab – 1 + 5a
2
– 9ab + 4 = 7a
2
– 6ab + 3.
e.g. expand 3x(2x – 4y), (3x + y)(x – 4y).
Includes products of more than two brackets,
e.g. expand (x – 2)(x + 3)(2x + 1).
Factorise means factorise fully,
e.g. 9x
2
+ 15xy = 3x(3x + 5y).
E2.3 Algebraic fractions Notes and examples
1 Manipulate algebraic fractions.
2 Factorise and simplify rational expressions.
Examples include:
• x
3
+ x – 4
2
• 2x
3 – 3(x –5)
2
• 3a
4 × 9a
10
• 3a
4 ÷ 9a
10
• 1
x – 2
+ x + 1
x – 3
.
e.g. x
2
– 2x
x
2
– 5x + 6 .
2 Algebra and graphs (continued)
E2.4 Indices II Notes and examples
1  Understand and use indices (positive, zero,
negative and fractional).
2  Understand and use the rules of indices.
e.g. solve:
• 32x = 2
• 5x + 1 = 25x
.
e.g. simplify:
• 3x x 3
4 2 2
1
# −
x x 5
2 2 2 2
1
' −
• x
3
2 5 J 3
L
K
K
N
P
O
O .
Knowledge of logarithms is not required.
E2.5 Equations Notes and examples
1 Construct expressions, equations and formulas.
2  Solve linear equations in one unknown.
3  Solve fractional equations with numerical and
linear algebraic denominators.
4  Solve simultaneous linear equations in two
unknowns.
5  Solve simultaneous equations, involving one
linear and one non-linear.
6  Solve quadratic equations by factorisation,
completing the square and by use of the
quadratic formula.
7  Change the subject of formulas.
e.g. write an expression for the product of two
consecutive even numbers.
Includes constructing simultaneous equations.
Examples include:
• 3x + 4 = 10
• 5 – 2x = 3(x + 7).
Examples include:
• x
2x + 1
= 4
• 2
x + 2 + 3
2x – 1 = 1
• x
x + 2 = 3
x – 6 .
With powers no higher than two.
Includes writing a quadratic expression in
completed square form.
Candidates may be expected to give solutions in
surd form.
The quadratic formula is given in the List of
formulas.
e.g. change the subject of a formula where:
• the subject appears twice
• there is a power or root of the subject.
2 Algebra and graphs (continued)
E2.6 Inequalities Notes and examples
1  Represent and interpret inequalities, including on
a number line.
2 Construct, solve and interpret linear inequalities.
3  Represent and interpret linear inequalities in two
variables graphically.
4 List inequalities that define a given region.
When representing and interpreting inequalities on
a number line:
• open circles should be used to represent strict
inequalities (<, >)
• closed circles should be used to represent
inclusive inequalities (⩽, ⩾).
e.g. – 3 ⩽ x < 1
–3 –2 –1 0 1
x
Examples include:
• 3x < 2x + 4
• –3 ⩽ 3x – 2 < 7 .
The following conventions should be used:
• broken lines should be used to represent strict
inequalities (<, >)
• solid lines should be used to represent inclusive
inequalities (⩽, ⩾)
• shading should be used to represent unwanted
regions (unless otherwise directed in the
question).
e.g.
0 1 2 0 1 2
x x
y y
1
2
1
2
x < 1
y ⩾ 1
Linear programming problems are not included.
E2.7 Sequences Notes and examples
1 Continue a given number sequence or pattern.
2  Recognise patterns in sequences, including the
term-to-term rule, and relationships between
different sequences.
3 Find and use the nth term of sequences.
Subscript notation may be used, e.g. Tn is the nth
term of sequence T.
Includes linear, quadratic, cubic and exponential
sequences and simple combinations of these.
2 Algebra and graphs (continued)
E2.8 Proportion Notes and examples
Express direct and inverse proportion in algebraic
terms and use this form of expression to find
unknown quantities.
Includes linear, square, square root, cube and cube
root proportion.
Knowledge of proportional symbol (∝) is required.
E2.9 Graphs in practical situations Notes and examples
1  Use and interpret graphs in practical situations
including travel graphs and conversion graphs.
2  Draw graphs from given data.
3  Apply the idea of rate of change to simple
kinematics involving distance–time and
speed–time graphs, acceleration and
deceleration.
4  Calculate distance travelled as area under a
speed–time graph.
Includes estimation and interpretation of the
gradient of a tangent at a point.
Areas will involve linear sections of the graph only.
E2.10 Graphs of functions Notes and examples
1  Construct tables of values, and draw, recognise
and interpret graphs for functions of the following
forms:
• axn
(includes sums of no more than three of
these)
• abx
+ c
where n = –2, –1, 2
1 − , 0, 2
1 , 1, 2, 3; a and c are
rational numbers; and b is a positive integer.
2  Solve associated equations graphically, including
finding and interpreting roots by graphical
methods.
3  Draw and interpret graphs representing
exponential growth and decay problems.
Examples include:
• y = x
3
+ x – 4
• y = 2x + 3
x
2
• y = 4
1
× 2x
.
e.g. finding the intersection of a line and a curve.
2 Algebra and graphs (continued)
E2.11 Sketching curves Notes and examples
Recognise, sketch and interpret graphs of the
following functions:
(a) linear
(b) quadratic
(c) cubic
(d) reciprocal
(e) exponential.
Functions will be equivalent to:
• ax + by = c
• y = ax
2
+ bx + c
• y = ax
3
+ b
• y = ax
3
+ bx2
+ cx
• y x
a = +b
y = arx
+ b
where a, b and c are rational numbers and r is a
rational, positive number.
Knowledge of turning points, roots and symmetry is
required.
Knowledge of vertical and horizontal asymptotes is
required.
Finding turning points of quadratics by completing
the square is required.
E2.12 Differentiation Notes and examples
1  Estimate gradients of curves by drawing
tangents.
2  Use the derivatives of functions of the form axn
,
where a is a rational constant and n is a positive
integer or zero, and simple sums of not more
than three of these.
3  Apply differentiation to gradients and stationary
points (turning points).
4  Discriminate between maxima and minima by
any method.
d
d
x
y notation will be expected.
Maximum and minimum points may be identified by:
• an accurate sketch
• use of the second differential
• inspecting the gradient either side of a turning
point.
Candidates are not expected to identify points of
inflection.
2 Algebra and graphs (continued)
E2.13 Functions Notes and examples
1  Understand functions, domain and range and
use function notation.
2  Understand and find inverse functions f –1(x).
3  Form composite functions as defined by
gf(x) = g(f(x)).
Examples include:
• f(x) = 3x – 5
• g(x) = 3(x + 4)
5
• h(x) = 2x
2
+ 3.
e.g. f(x) = 3
x + 2 and g(x) = (3x + 5)2
. Find fg(x).
Give your answer as a fraction in its simplest form.
Candidates are not expected to find the domains
and ranges of composite functions.
This topic may include mapping diagrams.
"""

text3 = """
3 Coordinate geometry
C3.1 Coordinates Notes and examples
Use and interpret Cartesian coordinates in
two dimensions.
C3.2 Drawing linear graphs Notes and examples
Draw straight-line graphs for linear equations. Equations will be given in the form y = mx + c
(e.g. y = –2x + 5), unless a table of values is given.
C3.3 Gradient of linear graphs Notes and examples
Find the gradient of a straight line. From a grid only.
C3.5 Equations of linear graphs Notes and examples
Interpret and obtain the equation of a straight-line
graph in the form y = mx + c.
Questions may:
• use and request lines in the forms
y = mx + c
x = k
• involve finding the equation when the graph is
given
• ask for the gradient or y-intercept of a graph
from an equation, e.g. find the gradient and
y-intercept of the graph with the equation
y = 6x + 3.
Candidates are expected to give equations of a line
in a fully simplified form.
C3.6 Parallel lines Notes and examples
Find the gradient and equation of a straight line
parallel to a given line.
e.g. find the equation of the line parallel to
y = 4x – 1 that passes through (1, –3).
3 Coordinate geometry
E3.1 Coordinates Notes and examples
Use and interpret Cartesian coordinates in two
dimensions.
E3.2 Drawing linear graphs Notes and examples
Draw straight-line graphs for linear equations. Examples include:
• y = –2x + 5
• y = 7 – 4x
• 3x + 2y = 5.
E3.3 Gradient of linear graphs Notes and examples
1 Find the gradient of a straight line.
2  Calculate the gradient of a straight line from the
coordinates of two points on it.
E3.4 Length and midpoint Notes and examples
1 Calculate the length of a line segment.
2  Find the coordinates of the midpoint of a line
segment.
E3.5 Equations of linear graphs Notes and examples
Interpret and obtain the equation of a straight-line
graph.
Questions may:
• use and request lines in different forms, e.g.
ax + by = c
y = mx + c
x = k
• involve finding the equation when the graph is
given
• ask for the gradient or y-intercept of a graph
from an equation, e.g. find the gradient and
y-intercept of the graph with equation
5x + 4y = 8.
Candidates are expected to give equations of a line
in a fully simplified form.
3 Coordinate geometry (continued)
E3.6 Parallel lines Notes and examples
Find the gradient and equation of a straight line
parallel to a given line.
e.g. find the equation of the line parallel to
y = 4x – 1 that passes through (1, –3).
E3.7 Perpendicular lines Notes and examples
Find the gradient and equation of a straight line
perpendicular to a given line.
Examples include:
• find the gradient of a line perpendicular to
2y = 3x + 1
• find the equation of the perpendicular bisector
of the line joining the points (–3, 8) and (9, –2).
"""

text4 = """
4 Geometry
C4.1 Geometrical terms Notes and examples
1  Use and interpret the following geometrical
terms:
• point
• vertex
• line
• parallel
• perpendicular
• bearing
• right angle
• acute, obtuse and reflex angles
• interior and exterior angles
• similar
• congruent
• scale factor.
2  Use and interpret the vocabulary of:
• triangles
• special quadrilaterals
• polygons
• nets
• simple solids.
Candidates are not expected to show that two
shapes are congruent.
Includes the following terms:
Triangles:
• equilateral
• isosceles
• scalene
• right-angled.
Quadrilaterals:
• square
• rectangle
• kite
• rhombus
• parallelogram
• trapezium.
Polygons:
• regular and irregular polygons
• pentagon
• hexagon
• octagon
• decagon.
continued
4 Geometry (continued)
C4.1 Geometrical terms (continued) Notes and examples
3 Use and interpret the vocabulary of a circle.
Simple solids:
• cube
• cuboid
• prism
• cylinder
• pyramid
• cone
• sphere (term ‘hemisphere’ not required)
• face
• surface
• edge.
Includes the following terms:
• centre
• radius (plural radii)
• diameter
• circumference
• semicircle
• chord
• tangent
• arc
• sector
• segment.
C4.2 Geometrical constructions Notes and examples
1 Measure and draw lines and angles.
2  Construct a triangle, given the lengths of all
sides, using a ruler and pair of compasses only.
3 Draw, use and interpret nets.
A ruler should be used for all straight edges.
Constructions of perpendicular bisectors and angle
bisectors are not required.
e.g. construct a rhombus by drawing two triangles.
Construction arcs must be shown.
Examples include:
• draw nets of cubes, cuboids, prisms and
pyramids
• use measurements from nets to calculate
volumes and surface areas.
4 Geometry (continued)
C4.3 Scale drawings Notes and examples
1 Draw and interpret scale drawings.
2 Use and interpret three-figure bearings.
A ruler must be used for all straight edges.
Bearings are measured clockwise from north
(000° to 360°).
e.g. find the bearing of A from B if the bearing of B
from A is 025°.
Includes an understanding of the terms north, east,
south and west.
e.g. point D is due east of point C.
C4.4 Similarity Notes and examples
Calculate lengths of similar shapes.
C4.5 Symmetry Notes and examples
Recognise line symmetry and order of rotational
symmetry in two dimensions.
Includes properties of triangles, quadrilaterals and
polygons directly related to their symmetries.
C4.6 Angles Notes and examples
1  Calculate unknown angles and give simple
explanations using the following geometrical
properties:
• sum of angles at a point = 360°
• sum of angles at a point on a straight line = 180°
• vertically opposite angles are equal
• angle sum of a triangle = 180° and angle sum
of a quadrilateral = 360°.
2  Calculate unknown angles and give geometric
explanations for angles formed within parallel lines:
• corresponding angles are equal
• alternate angles are equal
• co-interior angles sum to 180° (supplementary).
3  Know and use angle properties of regular
polygons.
Knowledge of three-letter notation for angles is
required, e.g. angle ABC. Candidates are expected
to use the correct geometrical terminology when
giving reasons for answers.
Includes exterior and interior angles, and angle
sum.
4 Geometry (continued)
C4.7 Circle theorems Notes and examples
Calculate unknown angles and give explanations
using the following geometrical properties of circles:
• angle in a semicircle = 90°
• angle between tangent and radius = 90°.
Candidates will be expected to use the geometrical
properties listed in the syllabus when giving
reasons for answers.
4 Geometry
E4.1 Geometrical terms Notes and examples
1  Use and interpret the following geometrical
terms:
• point
• vertex
• line
• plane
• parallel
• perpendicular
• perpendicular bisector
• bearing
• right angle
• acute, obtuse and reflex angles
• interior and exterior angles
• similar
• congruent
• scale factor.
2 Use and interpret the vocabulary of:
• triangles
• special quadrilaterals
• polygons
• nets
• solids.
Candidates are not expected to show that two
shapes are congruent.
Includes the following terms.
Triangles:
• equilateral
• isosceles
• scalene
• right-angled.
Quadrilaterals:
• square
• rectangle
• kite
• rhombus
• parallelogram
• trapezium.
continued
4 Geometry (continued)
E4.1 Geometrical terms (continued) Notes and examples
3 Use and interpret the vocabulary of a circle.
Polygons:
• regular and irregular polygons
• pentagon
• hexagon
• octagon
• decagon.
Solids:
• cube
• cuboid
• prism
• cylinder
• pyramid
• cone
• sphere
• hemisphere
• frustum
• face
• surface
• edge.
Includes the following terms:
• centre
• radius (plural radii)
• diameter
• circumference
• semicircle
• chord
• tangent
• major and minor arc
• sector
• segment.
4 Geometry (continued)
E4.2 Geometrical constructions Notes and examples
1 Measure and draw lines and angles.
2  Construct a triangle, given the lengths of all
sides, using a ruler and pair of compasses only.
3 Draw, use and interpret nets.
A ruler should be used for all straight edges.
Constructions of perpendicular bisectors and angle
bisectors are not required.
e.g. construct a rhombus by drawing two triangles.
Construction arcs must be shown.
Examples include:
• draw nets of cubes, cuboids, prisms and
pyramids
• use measurements from nets to calculate
volumes and surface areas.
E4.3 Scale drawings Notes and examples
1 Draw and interpret scale drawings.
2 Use and interpret three-figure bearings.
A ruler must be used for all straight edges.
Bearings are measured clockwise from north
(000° to 360°).
e.g. find the bearing of A from B if the bearing of B
from A is 025°.
Includes an understanding of the terms north, east,
south and west.
e.g. point D is due east of point C.
E4.4 Similarity Notes and examples
1 Calculate lengths of similar shapes.
2  Use the relationships between lengths and areas
of similar shapes and lengths, surface areas and
volumes of similar solids.
3  Solve problems and give simple explanations
involving similarity.
Includes use of scale factor, e.g.
B
A
B
A
Volume of
Volume of
Length of
Length of
3
3
= `
` j
j
.
Includes showing that two triangles are similar
using geometric reasons.
E4.5 Symmetry Notes and examples
1  Recognise line symmetry and order of rotational
symmetry in two dimensions.
2  Recognise symmetry properties of prisms,
cylinders, pyramids and cones.
Includes properties of triangles, quadrilaterals and
polygons directly related to their symmetries.
e.g. identify planes and axes of symmetry.
4 Geometry (continued)
E4.6 Angles Notes and examples
1  Calculate unknown angles and give simple
explanations using the following geometrical
properties:
• sum of angles at a point = 360°
• sum of angles at a point on a straight line = 180°
• vertically opposite angles are equal
• angle sum of a triangle = 180° and angle sum
of a quadrilateral = 360°.
2  Calculate unknown angles and give geometric
explanations for angles formed within parallel lines:
• corresponding angles are equal
• alternate angles are equal
• co-interior angles sum to 180° (supplementary).
3  Know and use angle properties of regular and
irregular polygons.
Knowledge of 3-letter notation for angles is
required, e.g. angle ABC. Candidates are expected
to use the correct geometrical terminology when
giving reasons for answers.
Includes exterior and interior angles, and angle
sum.
E4.7 Circle theorems I Notes and examples
Calculate unknown angles and give explanations
using the following geometrical properties of circles:
• angle in a semicircle = 90°
• angle between tangent and radius = 90°
• angle at the centre is twice the angle at the
circumference
• angles in the same segment are equal
• opposite angles of a cyclic quadrilateral sum to
180° (supplementary)
• alternate segment theorem.
Candidates are expected to use the geometrical
properties listed in the syllabus when giving
reasons for answers.
E4.8 Circle theorems II Notes and examples
Use the following symmetry properties of circles:
• equal chords are equidistant from the centre
• the perpendicular bisector of a chord passes
through the centre
• tangents from an external point are equal in
length.
Candidates are expected to use the geometrical
properties listed in the syllabus when giving
reasons for answers.
"""

text5 = """
5 Mensuration
C5.1 Units of measure Notes and examples
Use metric units of mass, length, area, volume
and capacity in practical situations and convert
quantities into larger or smaller units.
Units include:
• mm, cm, m, km
• mm2
, cm2
, m2
, km2
• mm3
, cm3
, m3
• ml, l
• g, kg.
Conversion between units includes:
• between different units of area, e.g. cm2 ↔ m2
• between units of volume and capacity,
e.g. m3 ↔ litres.
C5.2 Area and perimeter Notes and examples
Carry out calculations involving the perimeter and
area of a rectangle, triangle, parallelogram and
trapezium.
Except for area of a triangle, formulas are not
given.
C5.3 Circles, arcs and sectors Notes and examples
1  Carry out calculations involving the
circumference and area of a circle.
2  Carry out calculations involving arc length and
sector area as fractions of the circumference and
area of a circle, where the sector angle is a factor
of 360°.
Answers may be asked for in terms of π.
Formulas are given in the List of formulas.
C5.4 Surface area and volume Notes and examples
Carry out calculations and solve problems involving
the surface area and volume of a:
• cuboid
• prism
• cylinder
• sphere
• pyramid
• cone.
Answers may be asked for in terms of π.
The following formulas are given in the List of
formulas:
• curved surface area of a cylinder
• curved surface area of a cone
• surface area of a sphere
• volume of a prism
• volume of a pyramid
• volume of a cylinder
• volume of a cone
• volume of a sphere.
The term prism refers to any solid with a uniform
cross-section, e.g. a cylindrical sector.
5 Mensuration (continued)
C5.5 Compound shapes and parts of shapes Notes and examples
1  Carry out calculations and solve problems
involving perimeters and areas of:
• compound shapes
• parts of shapes.
2  Carry out calculations and solve problems
involving surface areas and volumes of:
• compound solids
• parts of solids.
Answers may be asked for in terms of π.
e.g. find the volume of half of a sphere.
5 Mensuration
E5.1 Units of measure Notes and examples
Use metric units of mass, length, area, volume
and capacity in practical situations and convert
quantities into larger or smaller units.
Units include:
• mm, cm, m, km
• mm2
, cm2
, m2
, km2
• mm3
, cm3
, m3
• ml, l
• g, kg.
Conversion between units includes:
• between different units of area, e.g. cm2 ↔ m2
• between units of volume and capacity,
e.g. m3 ↔ litres.
E5.2 Area and perimeter Notes and examples
Carry out calculations involving the perimeter and
area of a rectangle, triangle, parallelogram and
trapezium.
Except for the area of a triangle, formulas are not
given.
E5.3 Circles, arcs and sectors Notes and examples
1  Carry out calculations involving the
circumference and area of a circle.
2  Carry out calculations involving arc length and
sector area as fractions of the circumference and
area of a circle.
Answers may be asked for in terms of π.
Formulas are given in the List of formulas.
Includes minor and major sectors.
E5.4 Surface area and volume Notes and examples
Carry out calculations and solve problems involving
the surface area and volume of a:
• cuboid
• prism
• cylinder
• sphere
• pyramid
• cone.
Answers may be asked for in terms of π.
The following formulas are given in the List of
formulas:
• curved surface area of a cylinder
• curved surface area of a cone
• surface area of a sphere
• volume of a prism
• volume of a pyramid
• volume of a cylinder
• volume of a cone
• volume of a sphere.
The term prism refers to any solid with a uniform
cross-section, e.g. a cylindrical sector.
5 Mensuration (continued)
E5.5 Compound shapes and parts of shapes Notes and examples
1  Carry out calculations and solve problems
involving perimeters and areas of:
• compound shapes
• parts of shapes.
2  Carry out calculations and solve problems
involving surface areas and volumes of:
• compound solids
• parts of solids.
Answers may be asked for in terms of π.
e.g. find the surface area and volume of a frustum.
"""

text6 = """
6 Trigonometry
C6.1 Pythagoras’ theorem Notes and examples
Know and use Pythagoras’ theorem.
C6.2 Right-angled triangles
1  Know and use the sine, cosine and tangent
ratios for acute angles in calculations involving
sides and angles of a right-angled triangle.
2  Solve problems in two dimensions using
Pythagoras’ theorem and trigonometry.
Angles will be given in degrees and answers should
be written in degrees, with decimals correct to one
decimal place.
Knowledge of bearings may be required.
6 Trigonometry
E6.1 Pythagoras’ theorem Notes and examples
Know and use Pythagoras’ theorem.
E6.2 Right-angled triangles Notes and examples
1  Know and use the sine, cosine and tangent
ratios for acute angles in calculations involving
sides and angles of a right-angled triangle.
2  Solve problems in two dimensions using
Pythagoras’ theorem and trigonometry.
3  Know that the perpendicular distance from a
point to a line is the shortest distance to the line.
4  Carry out calculations involving angles of
elevation and depression.
Angles will be given in degrees and answers should
be written in degrees, with decimals correct to one
decimal place.
Knowledge of bearings may be required.
E6.3 Exact trigonometric values Notes and examples
Know the exact values of:
1 sin x and cos x for x = 0°, 30°, 45°, 60° and 90°.
2 tan x for x = 0°, 30°, 45° and 60°.
E6.4 Trigonometric functions Notes and examples
1  Recognise, sketch and interpret the following
graphs for 0° ⩽ x ⩽ 360°:
• y = sinx
• y = cos x
• y = tanx.
2  Solve trigonometric equations involving sin x,
cos x or tan x, for 0° ⩽ x ⩽ 360°.
e.g. solve:
• sin x = 2
3
for 0° ⩽ x ⩽ 360°
• 2 cos x + 1 = 0 for 0° ⩽ x ⩽ 360°.
6 Trigonometry (continued)
E6.5 Non-right-angled triangles Notes and examples
1  Use the sine and cosine rules in calculations
involving lengths and angles for any triangle.
2  Use the formula
area of triangle = 2
1 absin C.
Includes problems involving obtuse angles and the
ambiguous case.
The sine and cosine rules and the formula for area
of a triangle are given in the List of formulas.
E6.6 Pythagoras’ theorem and trigonometry Notes and examples
in 3D
Carry out calculations and solve problems in
three dimensions using Pythagoras’ theorem
and trigonometry, including calculating the angle
between a line and a plane.
"""

text7 = """
7 Transformations and vectors
C7.1 Transformations Notes and examples
Recognise, describe and draw the following
transformations:
1  Reflection of a shape in a vertical or horizontal
line.
2  Rotation of a shape about the origin, vertices
or midpoints of edges of the shape, through
multiples of 90°.
3  Enlargement of a shape from a centre by a scale
factor.
4 Translation of a shape by a vector
x
y
J
L
K
K
N
P
O
O.
Questions will not involve combinations of
transformations. A ruler must be used for all straight
edges.
Positive and fractional scale factors only.
7 Transformations and vectors
E7.1 Transformations Notes and examples
Recognise, describe and draw the following
transformations:
1 Reflection of a shape in a straight line.
2  Rotation of a shape about a centre through
multiples of 90°.
3  Enlargement of a shape from a centre by a scale
factor.
4 Translation of a shape by a vector
x
y
J
L
K
K
N
P
O
O.
Questions may involve combinations of
transformations. A ruler must be used for all straight
edges.
Positive, fractional and negative scale factors may
be used.
E7.2 Vectors in two dimensions Notes and examples
1  Describe a translation using a vector represented
by
x
y
J
L
K
K
N
P
O
O, AB or a.
2 Add and subtract vectors.
3 Multiply a vector by a scalar.
Vectors will be printed as AB or a.
E7.3 Magnitude of a vector Notes and examples
Calculate the magnitude of a vector
x
y
J
L
K
K
N
P
O
O as
x y
2 2 + .
The magnitudes of vectors will be denoted by
modulus signs, e.g.
• a is the magnitude of a
• AB is the magnitude of AB.
E7.4 Vector geometry Notes and examples
1 Represent vectors by directed line segments.
2 Use position vectors.
3  Use the sum and difference of two or more
vectors to express given vectors in terms of two
coplanar vectors.
4  Use vectors to reason and to solve geometric
problems.
Examples include:
• show that vectors are parallel
• show that 3 points are collinear
• solve vector problems involving ratio and
similarity.
"""

text8 = """
8 Probability
C8.1 Introduction to probability Notes and examples
1  Understand and use the probability scale from
0 to 1.
2  Calculate the probability of a single event.
3  Understand that the probability of an event
not occurring = 1 – the probability of the event
occurring.
Probability notation is not required.
Probabilities should be given as a fraction, decimal
or percentage. Problems may require using
information from tables, graphs or Venn diagrams
(limited to two sets).
e.g. The probability that a counter is blue is 0.8.
What is the probability that it is not blue?
C8.2 Relative and expected frequencies Notes and examples
1  Understand relative frequency as an estimate of
probability.
2 Calculate expected frequencies.
e.g. use results of experiments with a spinner to
estimate the probability of a given outcome.
e.g. use probability to estimate an expected value
from a population.
Includes understanding what is meant by fair, bias
and random.
C8.3 Probability of combined events Notes and examples
Calculate the probability of combined events using,
where appropriate:
• sample space diagrams
• Venn diagrams
• tree diagrams.
Combined events will only be with replacement.
Venn diagrams will be limited to two sets.
In tree diagrams, outcomes will be written at the
end of the branches and probabilities by the side of
the branches.
8 Probability
E8.1 Introduction to probability Notes and examples
1  Understand and use the probability scale from
0 to 1.
2 Understand and use probability notation.
3 Calculate the probability of a single event.
4  Understand that the probability of an event
not occurring = 1 – the probability of the event
occurring.
P(A) is the probability of A
P(A′) is the probability of not A
Probabilities should be given as a fraction, decimal
or percentage.
Problems may require using information from
tables, graphs or Venn diagrams.
e.g. P(B) = 0.8, find P(B′)
E8.2 Relative and expected frequencies Notes and examples
1  Understand relative frequency as an estimate of
probability.
2 Calculate expected frequencies.
e.g. use results of experiments with a spinner to
estimate the probability of a given outcome.
e.g. use probability to estimate an expected value
from a population.
Includes understanding what is meant by fair, bias
and random.
E8.3 Probability of combined events Notes and examples
Calculate the probability of combined events using,
where appropriate:
• sample space diagrams
• Venn diagrams
• tree diagrams.
Combined events could be with or without
replacement.
The notation P(A ∩ B) and P(A ∪ B) may be used
in the context of Venn diagrams.
On tree diagrams outcomes will be written at the
end of branches and probabilities by the side of the
branches.
E8.4 Conditional probability Notes and examples
Calculate conditional probability using Venn
diagrams, tree diagrams and tables.
Knowledge of notation, P(A|B), and formulas
relating to conditional probability is not required.
"""

text9 = """
9 Statistics
C9.1 Classifying statistical data Notes and examples
Classify and tabulate statistical data. e.g. tally tables, two-way tables.
C9.2 Interpreting statistical data Notes and examples
1  Read, interpret and draw inferences from tables
and statistical diagrams.
2  Compare sets of data using tables, graphs and
statistical measures.
3  Appreciate restrictions on drawing conclusions
from given data.
e.g. compare averages and ranges between two
data sets.
C9.3 Averages and range Notes and examples
Calculate the mean, median, mode and range
for individual data and distinguish between the
purposes for which these are used.
Data may be in a list or frequency table, but will not
be grouped.
C9.4 Statistical charts and diagrams Notes and examples
Draw and interpret:
(a) bar charts
(b) pie charts
(c) pictograms
(d) stem-and-leaf diagrams
(e) simple frequency distributions.
Includes composite (stacked) and dual (side-by￾side) bar charts.
Stem-and-leaf diagrams should have ordered data
with a key.
9 Statistics (continued)
C9.5 Scatter diagrams Notes and examples
1 Draw and interpret scatter diagrams.
2  Understand what is meant by positive, negative
and zero correlation.
3  Draw by eye, interpret and use a straight line of
best fit.
Plotted points should be clearly marked, for
example as small crosses (×).
A line of best fit:
• should be a single ruled line drawn by
inspection
• should extend across the full data set
• does not need to coincide exactly with any of
the points but there should be a roughly even
distribution of points either side of the line over
its entire length.
Extended subject content
9 Statistics
E9.1 Classifying statistical data Notes and examples
Classify and tabulate statistical data. e.g. tally tables, two-way tables.
E9.2 Interpreting statistical data Notes and examples
1  Read, interpret and draw inferences from tables
and statistical diagrams.
2  Compare sets of data using tables, graphs and
statistical measures.
3  Appreciate restrictions on drawing conclusions
from given data.
e.g. compare averages and measures of spread
between two data sets.
E9.3 Averages and measures of spread Notes and examples
1  Calculate the mean, median, mode, quartiles,
range and interquartile range for individual data
and distinguish between the purposes for which
these are used.
2  Calculate an estimate of the mean for grouped
discrete or grouped continuous data.
3  Identify the modal class from a grouped
frequency distribution.
E9.4 Statistical charts and diagrams Notes and examples
Draw and interpret:
(a) bar charts
(b) pie charts
(c) pictograms
(d) stem-and-leaf diagrams
(e) simple frequency distributions.
Includes composite (stacked) and dual (side-by￾side) bar charts.
Stem-and-leaf diagrams should have ordered data
with a key.
9 Statistics (continued)
E9.5 Scatter diagrams Notes and examples
1 Draw and interpret scatter diagrams.
2  Understand what is meant by positive, negative
and zero correlation.
3  Draw by eye, interpret and use a straight line of
best fit.
Plotted points should be clearly marked, for
example as small crosses (×).
A line of best fit:
• should be a single ruled line drawn by
inspection
• should extend across the full data set
• does not need to coincide exactly with any of
the points but there should be a roughly even
distribution of points either side of the line over
its entire length.
E9.6 Cumulative frequency diagrams Notes and examples
1  Draw and interpret cumulative frequency tables
and diagrams.
2  Estimate and interpret the median, percentiles,
quartiles and interquartile range from cumulative
frequency diagrams.
Plotted points on a cumulative frequency diagram
should be clearly marked, for example as small
crosses (×), and be joined with a smooth curve.
E9.7 Histograms Notes and examples
1 Draw and interpret histograms.
2 Calculate with frequency density.
On histograms, the vertical axis is labelled
‘Frequency density’.
Frequency density is defined as
frequency density = frequency ÷ class width.
"""

textarr = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
data, labels = [], []
for label, chapter_text in zip(allLabels, textarr):
    for chunk in trainModels.chunk_lines(chapter_text):
        data.append(formatText(chunk))
        labels.append(label)

trainModels.train(data, labels, f"{BASE_PATH}/resources/sci-kit/igmath.joblib")
