import trainModels
import getFormattedTextfromPdf


allLabels = ['Physical quantities and units', 'Kinematics', 
             'Dynamics', 'Forces, density and pressure', 'Work, energy and power', 'Deformation of solids', 'Waves',
               'Superposition', 'Electricity', 'D.C. circuits', 'Particle physics']


text = """
1 Physical quantities and units
1.1 Physical quantities
Candidates should be able to:
1 understand that all physical quantities consist of a numerical magnitude and a unit
2 make reasonable estimates of physical quantities included within the syllabus
1.2 SI units
Candidates should be able to:
1 recall the following SI base quantities and their units: mass (kg), length (m), time (s), current (A),
temperature (K)
2 express derived units as products or quotients of the SI base units and use the derived units for
quantities listed in this syllabus as appropriate
3 use SI base units to check the homogeneity of physical equations
4 recall and use the following prefixes and their symbols to indicate decimal submultiples or multiples of
both base and derived units: pico (p), nano (n), micro (μ), milli (m), centi (c), deci (d), kilo (k), mega (M),
giga (G), tera (T)
1.3 Errors and uncertainties
Candidates should be able to:
1 understand and explain the effects of systematic errors (including zero errors) and random errors in
measurements
2 understand the distinction between precision and accuracy
3 assess the uncertainty in a derived quantity by simple addition of absolute or percentage uncertainties
1.4 Scalars and vectors
Candidates should be able to:
1 understand the difference between scalar and vector quantities and give examples of scalar and vector
quantities included in the syllabus
2 add and subtract coplanar vectors
3 represent a vector as two perpendicular components
"""

text2 = """
2 Kinematics
2.1 Equations of motion
Candidates should be able to:
1 define and use distance, displacement, speed, velocity and acceleration
2 use graphical methods to represent distance, displacement, speed, velocity and acceleration
3 determine displacement from the area under a velocity–time graph
4 determine velocity using the gradient of a displacement–time graph
5 determine acceleration using the gradient of a velocity–time graph
6 derive, from the definitions of velocity and acceleration, equations that represent uniformly accelerated
motion in a straight line
7 solve problems using equations that represent uniformly accelerated motion in a straight line, including
the motion of bodies falling in a uniform gravitational field without air resistance
8 describe an experiment to determine the acceleration of free fall using a falling object
9 describe and explain motion due to a uniform velocity in one direction and a uniform acceleration in a
perpendicular direction
"""

text3 = """
3 Dynamics
An understanding of forces from Cambridge IGCSE/O Level Physics or equivalent is assumed.
3.1 Momentum and Newton’s laws of motion
Candidates should be able to:
1 understand that mass is the property of an object that resists change in motion
2 recall F = ma and solve problems using it, understanding that acceleration and resultant force are always
in the same direction
3 define and use linear momentum as the product of mass and velocity
4 define and use force as rate of change of momentum
5 state and apply each of Newton’s laws of motion
6 describe and use the concept of weight as the effect of a gravitational field on a mass and recall that the
weight of an object is equal to the product of its mass and the acceleration of free fall
3.2 Non-uniform motion
Candidates should be able to:
1 show a qualitative understanding of frictional forces and viscous/drag forces including air resistance
(no treatment of the coefficients of friction and viscosity is required, and a simple model of drag force
increasing as speed increases is sufficient)
2 describe and explain qualitatively the motion of objects in a uniform gravitational field with air
resistance
3 understand that objects moving against a resistive force may reach a terminal (constant) velocity
3.3 Linear momentum and its conservation
Candidates should be able to:
1 state the principle of conservation of momentum
2 apply the principle of conservation of momentum to solve simple problems, including elastic and
inelastic interactions between objects in both one and two dimensions (knowledge of the concept of
coefficient of restitution is not required)
3 recall that, for a perfectly elastic collision, the relative speed of approach is equal to the relative speed of
separation
4 understand that, while momentum of a system is always conserved in interactions between objects,
some change in kinetic energy may take place
"""

text4 = """
4 Forces, density and pressure
4.1 Turning effects of forces
Candidates should be able to:
1 understand that the weight of an object may be taken as acting at a single point known as its centre of
gravity
2 define and apply the moment of a force
3 understand that a couple is a pair of forces that acts to produce rotation only
4 define and apply the torque of a couple
4.2 Equilibrium of forces
Candidates should be able to:
1 state and apply the principle of moments
2 understand that, when there is no resultant force and no resultant torque, a system is in equilibrium
3 use a vector triangle to represent coplanar forces in equilibrium
4.3 Density and pressure
Candidates should be able to:
1 define and use density
2 define and use pressure
3 derive, from the definitions of pressure and density, the equation for hydrostatic pressure ∆p = ρg∆h
4 use the equation ∆p = ρg∆h
5 understand that the upthrust acting on an object in a fluid is due to a difference in hydrostatic pressure
6 calculate the upthrust acting on an object in a fluid using the equation F = ρgV (Archimedes’ principle)
"""

text5 = """
5 Work, energy and power
 An understanding of the forms of energy and energy transfers from Cambridge IGCSE/O Level Physics or
equivalent is assumed.
5.1 Energy conservation
Candidates should be able to:
1 understand the concept of work, and recall and use work done = force × displacement in the direction of
the force
2 recall and apply the principle of conservation of energy
3 recall and understand that the efficiency of a system is the ratio of useful energy output from the
system to the total energy input
4 use the concept of efficiency to solve problems
5 define power as work done per unit time
6 solve problems using P = W/t
7 derive P = Fv and use it to solve problems
5.2 Gravitational potential energy and kinetic energy
Candidates should be able to:
1 derive, using W = Fs, the formula ∆EP = mg∆h for gravitational potential energy changes in a uniform
gravitational field
2 recall and use the formula ∆EP = mg∆h for gravitational potential energy changes in a uniform
gravitational field
3 derive, using the equations of motion, the formula for kinetic energy EK = 1/2mv2
4 recall and use EK = 1/2mv2
"""

text6 = """
6 Deformation of solids
6.1 Stress and strain
Candidates should be able to:
1 understand that deformation is caused by tensile or compressive forces (forces and deformations will be
assumed to be in one dimension only)
2 understand and use the terms load, extension, compression and limit of proportionality
3 recall and use Hooke’s law
4 recall and use the formula for the spring constant k = F / x
5 define and use the terms stress, strain and the Young modulus
6 describe an experiment to determine the Young modulus of a metal in the form of a wire
Cambridge International AS & A Level Physics 9702 syllabus for 2022, 2023 and 2024. Subject content
18 www.cambridgeinternational.org/alevel Back to contents page
6.2 Elastic and plastic behaviour
Candidates should be able to:
1 understand and use the terms elastic deformation, plastic deformation and elastic limit
2 understand that the area under the force–extension graph represents the work done
3 determine the elastic potential energy of a material deformed within its limit of proportionality from the
area under the force–extension graph
4 recall and use EP = 1/2 Fx = 1/2 kx2
 for a material deformed within its limit of proportionality
"""

text7 = """
7 Waves
An understanding of colour from Cambridge IGCSE/O Level Physics or equivalent is assumed.
7.1 Progressive waves
Candidates should be able to:
1 describe what is meant by wave motion as illustrated by vibration in ropes, springs and ripple tanks
2 understand and use the terms displacement, amplitude, phase difference, period, frequency, wavelength
and speed
3 understand the use of the time-base and y-gain of a cathode-ray oscilloscope (CRO) to determine
frequency and amplitude
4 derive, using the definitions of speed, frequency and wavelength, the wave equation v = f λ
5 recall and use v = f λ
6 understand that energy is transferred by a progressive wave
7 recall and use intensity = power/area and intensity ∝ (amplitude)
2
 for a progressive wave
7.2 Transverse and longitudinal waves
Candidates should be able to:
1 compare transverse and longitudinal waves
2 analyse and interpret graphical representations of transverse and longitudinal waves
7.3 Doppler effect for sound waves
Candidates should be able to:
1 understand that when a source of sound waves moves relative to a stationary observer, the observed
frequency is different from the source frequency (understanding of the Doppler effect for a stationary
source and a moving observer is not required)
2 use the expression f
ο = fs
v /(v ± vs) for the observed frequency when a source of sound waves moves
relative to a stationary observer
7.4 Electromagnetic spectrum
Candidates should be able to:
1 state that all electromagnetic waves are transverse waves that travel with the same speed c in free space
2 recall the approximate range of wavelengths in free space of the principal regions of the electromagnetic
spectrum from radio waves to γ-rays
3 recall that wavelengths in the range 400–700nm in free space are visible to the human eye
7.5 Polarisation
Candidates should be able to:
1 understand that polarisation is a phenomenon associated with transverse waves
2 recall and use Malus’s law (I = I0 cos2
θ ) to calculate the intensity of a plane polarised electromagnetic
wave after transmission through a polarising filter or a series of polarising filters
"""

text8 = """
8 Superposition
8.1 Stationary waves
Candidates should be able to:
1 explain and use the principle of superposition
2 show an understanding of experiments that demonstrate stationary waves using microwaves, stretched
strings and air columns (it will be assumed that end corrections are negligible; knowledge of the concept
of end corrections is not required)
3 explain the formation of a stationary wave using a graphical method, and identify nodes and antinodes
4 understand how wavelength may be determined from the positions of nodes or antinodes of a stationary
wave
8.2 Diffraction
Candidates should be able to:
1 explain the meaning of the term diffraction
2 show an understanding of experiments that demonstrate diffraction including the qualitative effect of
the gap width relative to the wavelength of the wave; for example diffraction of water waves in a ripple
tank
8.3 Interference
Candidates should be able to:
1 understand the terms interference and coherence
2 show an understanding of experiments that demonstrate two-source interference using water waves in a
ripple tank, sound, light and microwaves
3 understand the conditions required if two-source interference fringes are to be observed
4 recall and use λ = ax /D for double-slit interference using light
8.4 The diffraction grating
Candidates should be able to:
1 recall and use d sin θ = nλ
2 describe the use of a diffraction grating to determine the wavelength of light (the structure and use of
the spectrometer are not included)
"""

text9 = """
9 Electricity
9.1 Electric current
Candidates should be able to:
1 understand that an electric current is a flow of charge carriers
2 understand that the charge on charge carriers is quantised
3 recall and use Q = It
4 use, for a current-carrying conductor, the expression I = Anvq, where n is the number density of charge
carriers
9.2 Potential difference and power
Candidates should be able to:
1 define the potential difference across a component as the energy transferred per unit charge
2 recall and use V = W/Q
3 recall and use P = VI, P = I 2
R and P = V2 /R
9.3 Resistance and resistivity
Candidates should be able to:
1 define resistance
2 recall and use V = IR
3 sketch the I–V characteristics of a metallic conductor at constant temperature, a semiconductor diode
and a filament lamp
4 explain that the resistance of a filament lamp increases as current increases because its temperature
increases
5 state Ohm’s law
6 recall and use R = ρL /A
7 understand that the resistance of a light-dependent resistor (LDR) decreases as the light intensity
increases
8 understand that the resistance of a thermistor decreases as the temperature increases (it will be
assumed that thermistors have a negative temperature coefficient)
"""

text10 = """
10 D.C. circuits
10.1 Practical circuits
Candidates should be able to:
1 recall and use the circuit symbols shown in section 6 of this syllabus
2 draw and interpret circuit diagrams containing the circuit symbols shown in section 6 of this syllabus
3 define and use the electromotive force (e.m.f.) of a source as energy transferred per unit charge in
driving charge around a complete circuit
4 distinguish between e.m.f. and potential difference (p.d.) in terms of energy considerations
5 understand the effects of the internal resistance of a source of e.m.f. on the terminal potential difference
10.2 Kirchhoff’s laws
Candidates should be able to:
1 recall Kirchhoff’s first law and understand that it is a consequence of conservation of charge
2 recall Kirchhoff’s second law and understand that it is a consequence of conservation of energy
3 derive, using Kirchhoff’s laws, a formula for the combined resistance of two or more resistors in series
4 use the formula for the combined resistance of two or more resistors in series
5 derive, using Kirchhoff’s laws, a formula for the combined resistance of two or more resistors in parallel
6 use the formula for the combined resistance of two or more resistors in parallel
7 use Kirchhoff’s laws to solve simple circuit problems
10.3 Potential dividers
Candidates should be able to:
1 understand the principle of a potential divider circuit
2 recall and use the principle of the potentiometer as a means of comparing potential differences
3 understand the use of a galvanometer in null methods
4 explain the use of thermistors and light-dependent resistors in potential dividers to provide a potential
difference that is dependent on temperature and light intensity
"""
text11 = """
11 Particle physics
11.1 Atoms, nuclei and radiation
Candidates should be able to:
1 infer from the results of the α-particle scattering experiment the existence and small size of the nucleus
2 describe a simple model for the nuclear atom to include protons, neutrons and orbital electrons
3 distinguish between nucleon number and proton number
4 understand that isotopes are forms of the same element with different numbers of neutrons in their
nuclei
5 understand and use the notation A
ZX for the representation of nuclides
6 understand that nucleon number and charge are conserved in nuclear processes
7 describe the composition, mass and charge of α-, β- and γ-radiations (both β–
 (electrons) and β+
(positrons) are included)
8 understand that an antiparticle has the same mass but opposite charge to the corresponding particle,
and that a positron is the antiparticle of an electron
9 state that (electron) antineutrinos are produced during β–
 decay and (electron) neutrinos are produced
during β+
 decay
10 understand that α-particles have discrete energies but that β-particles have a continuous range of
energies because (anti)neutrinos are emitted in β-decay
11 represent α- and β-decay by a radioactive decay equation of the form U Th 92
238
90
234
2 " + 4α
12 use the unified atomic mass unit (u) as a unit of mass
11.2 Fundamental particles
Candidates should be able to:
1 understand that a quark is a fundamental particle and that there are six flavours (types) of quark: up,
down, strange, charm, top and bottom
2 recall and use the charge of each flavour of quark and understand that its respective antiquark has the
opposite charge (no knowledge of any other properties of quarks is required)
3 recall that protons and neutrons are not fundamental particles and describe protons and neutrons in
terms of their quark composition
4 understand that a hadron may be either a baryon (consisting of three quarks) or a meson (consisting of
one quark and one antiquark)
5 describe the changes to quark composition that take place during β–
 and β+
 decay
6 recall that electrons and neutrinos are fundamental particles called leptons
"""



textarr = [text, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11]
for i in range(len(textarr)):
    textarr[i] = getFormattedTextfromPdf.formatText(textarr[i])

trainModels.train(textarr, allLabels)
