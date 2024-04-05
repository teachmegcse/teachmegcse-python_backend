import trainModels
import getFormattedTextfromPdf


allLabels = ['Motion in a circle', 'Gravitational fields', 
             'Temperature', 'Ideal gases', 'Thermodynamics', 'Oscillations', 'Electric fields',
               'Capacitance', 'Magnetic fields', 'Alternating currents', 'Quantum physics', 'Nuclear physics',
               'Medical physics', 'Astronomy and cosmology']


text = """
12 Motion in a circle
12.1 Kinematics of uniform circular motion
1 define the radian and express angular displacement in radians
2 understand and use the concept of angular speed
3 recall and use ω = 2π/ T and v = rω
12.2 Centripetal acceleration
1 understand that a force of constant magnitude that is always perpendicular to the direction of motion
causes centripetal acceleration
2 understand that centripetal acceleration causes circular motion with a constant angular speed
3 recall and use a = rω2
 and a = v
2 /r
4 recall and use F = mrω2
 and F = mv2 /r
"""

text2 = """
13 Gravitational fields
13.1 Gravitational field
1 understand that a gravitational field is an example of a field of force and define gravitational field as force
per unit mass
2 represent a gravitational field by means of field lines
13.2 Gravitational force between point masses
1 understand that, for a point outside a uniform sphere, the mass of the sphere may be considered to be a
point mass at its centre
2 recall and use Newton’s law of gravitation F = Gm1
m2/r
2
 for the force between two point masses
3 analyse circular orbits in gravitational fields by relating the gravitational force to the centripetal
acceleration it causes
4 understand that a satellite in a geostationary orbit remains at the same point above the Earth’s surface,
with an orbital period of 24 hours, orbiting from west to east, directly above the Equator
13.3 Gravitational field of a point mass
1 derive, from Newton’s law of gravitation and the definition of gravitational field, the equation
g = GM/r
2
 for the gravitational field strength due to a point mass
2 recall and use g = GM/r
2
3 understand why g is approximately constant for small changes in height near the Earth’s surface
13.4 Gravitational potential
1 define gravitational potential at a point as the work done per unit mass in bringing a small test mass from
infinity to the point
2 use ϕ = –GM/r for the gravitational potential in the field due to a point mass
3 understand how the concept of gravitational potential leads to the gravitational potential energy of two
point masses and use EP = –GMm/r
"""

text3 = """
14 Temperature
14.1 Thermal equilibrium
1 understand that (thermal) energy is transferred from a region of higher temperature to a region of lower
temperature
2 understand that regions of equal temperature are in thermal equilibrium
14.2 Temperature scales
1 understand that a physical property that varies with temperature may be used for the measurement of
temperature and state examples of such properties, including the density of a liquid, volume of a gas at
constant pressure, resistance of a metal, e.m.f. of a thermocouple
2 understand that the scale of thermodynamic temperature does not depend on the property of any
particular substance
3 convert temperatures between kelvin and degrees Celsius and recall that T /K = θ/°C + 273.15
4 understand that the lowest possible temperature is zero kelvin on the thermodynamic temperature scale
and that this is known as absolute zero
14.3 Specific heat capacity and specific latent heat
1 define and use specific heat capacity
2 define and use specific latent heat and distinguish between specific latent heat of fusion and specific
latent heat of vaporisation
"""

text4 = """
15 Ideal gases
15.1 The mole
1 understand that amount of substance is an SI base quantity with the base unit mol
2 use molar quantities where one mole of any substance is the amount containing a number of particles of
that substance equal to the Avogadro constant NA
Cambridge International AS & A Level Physics 9702 syllabus for 2022, 2023 and 2024. Subject content
Back to contents page www.cambridgeinternational.org/alevel 25
15.2 Equation of state
1 understand that a gas obeying pV ∝ T, where T is the thermodynamic temperature, is known as an ideal
gas
2 recall and use the equation of state for an ideal gas expressed as pV = nRT, where n = amount of
substance (number of moles) and as pV = NkT, where N = number of molecules
3 recall that the Boltzmann constant k is given by k = R/NA
15.3 Kinetic theory of gases
1 state the basic assumptions of the kinetic theory of gases
2 explain how molecular movement causes the pressure exerted by a gas and derive and use the
relationship pV = 1/3Nm<c
2
>, where <c
2
> is the mean-square speed (a simple model considering onedimensional collisions and then extending to three dimensions using 1/3<c
2
> = <cx
2
> is sufficient)
3 understand that the root-mean-square speed cr.m.s. is given by < > c
2
4 compare pV = 1/3Nm<c
2
> with pV = NkT to deduce that the average translational kinetic energy of a
molecule is 3
–
2 kT
"""

text5 = """
16 Thermodynamics
16.1 Internal energy
1 understand that internal energy is determined by the state of the system and that it can be expressed
as the sum of a random distribution of kinetic and potential energies associated with the molecules of a
system
2 relate a rise in temperature of an object to an increase in its internal energy
16.2 The first law of thermodynamics
1 recall and use W = p∆V for the work done when the volume of a gas changes at constant pressure and
understand the difference between the work done by the gas and the work done on the gas
2 recall and use the first law of thermodynamics ∆U = q + W expressed in terms of the increase in internal
energy, the heating of the system (energy transferred to the system by heating) and the work done on
the system
"""

text6 = """
17 Oscillations
17.1 Simple harmonic oscillations
Candidates should be able to:
1 understand and use the terms displacement, amplitude, period, frequency, angular frequency and phase
difference in the context of oscillations, and express the period in terms of both frequency and angular
frequency
2 understand that simple harmonic motion occurs when acceleration is proportional to displacement from
a fixed point and in the opposite direction
3 use a = –ω2
x and recall and use, as a solution to this equation, x = x0 sin ωt
4 use the equations v = v0 cos ωt and v = ±ω ( ) x x 0
2 2 −
5 analyse and interpret graphical representations of the variations of displacement, velocity and
acceleration for simple harmonic motion
17.2 Energy in simple harmonic motion
Candidates should be able to:
1 describe the interchange between kinetic and potential energy during simple harmonic motion
2 recall and use E = 1/2mω2
x0
2
 for the total energy of a system undergoing simple harmonic motion
17.3 Damped and forced oscillations, resonance
Candidates should be able to:
1 understand that a resistive force acting on an oscillating system causes damping
2 understand and use the terms light, critical and heavy damping and sketch displacement–time graphs
illustrating these types of damping
3 understand that resonance involves a maximum amplitude of oscillations and that this occurs when an
oscillating system is forced to oscillate at its natural frequency
"""

text7 = """
18 Electric fields
18.1 Electric fields and field lines
Candidates should be able to:
1 understand that an electric field is an example of a field of force and define electric field as force per unit
positive charge
2 recall and use F = qE for the force on a charge in an electric field
3 represent an electric field by means of field lines
18.2 Uniform electric fields
Candidates should be able to:
1 recall and use E = ∆V/∆d to calculate the field strength of the uniform field between charged parallel
plates
2 describe the effect of a uniform electric field on the motion of charged particles
Cambridge International AS & A Level Physics 9702 syllabus for 2022, 2023 and 2024. Subject content
Back to contents page www.cambridgeinternational.org/alevel 27
18.3 Electric force between point charges
Candidates should be able to:
1 understand that, for a point outside a spherical conductor, the charge on the sphere may be considered
to be a point charge at its centre
2 recall and use Coulomb’s law F = Q1
Q2 /(4πε0r
2
) for the force between two point charges in free space
18.4 Electric field of a point charge
Candidates should be able to:
1 recall and use E = Q/(4πε0r
2
) for the electric field strength due to a point charge in free space
18.5 Electric potential
Candidates should be able to:
1 define electric potential at a point as the work done per unit positive charge in bringing a small test
charge from infinity to the point
2 recall and use the fact that the electric field at a point is equal to the negative of potential gradient at
that point
3 use V = Q/(4πε0r) for the electric potential in the field due to a point charge
4 understand how the concept of electric potential leads to the electric potential energy of two point
charges and use EP = Qq/(4πε0r
"""

text8 = """
19 Capacitance
19.1 Capacitors and capacitance
Candidates should be able to:
1 define capacitance, as applied to both isolated spherical conductors and to parallel plate capacitors
2 recall and use C = Q/V
3 derive, using C = Q/V, formulae for the combined capacitance of capacitors in series and in parallel
4 use the capacitance formulae for capacitors in series and in parallel
19.2 Energy stored in a capacitor
Candidates should be able to:
1 determine the electric potential energy stored in a capacitor from the area under the potential–charge
graph
2 recall and use W = 1/2QV = 1/2CV2
19.3 Discharging a capacitor
Candidates should be able to:
1 analyse graphs of the variation with time of potential difference, charge and current for a capacitor
discharging through a resistor
2 recall and use τ = RC for the time constant for a capacitor discharging through a resistor
3 use equations of the form x = x0 e–(t/RC)
 where x could represent current, charge or potential difference
for a capacitor discharging through a resistor
"""

text9 = """
20 Magnetic fields
20.1 Concept of a magnetic field
Candidates should be able to:
1 understand that a magnetic field is an example of a field of force produced either by moving charges or
by permanent magnets
2 represent a magnetic field by field lines
20.2 Force on a current-carrying conductor
Candidates should be able to:
1 understand that a force might act on a current-carrying conductor placed in a magnetic field
2 recall and use the equation F = BIL sin θ, with directions as interpreted by Fleming’s left-hand rule
3 define magnetic flux density as the force acting per unit current per unit length on a wire placed at rightangles to the magnetic field
20.3 Force on a moving charge
Candidates should be able to:
1 determine the direction of the force on a charge moving in a magnetic field
2 recall and use F = BQv sin θ
3 understand the origin of the Hall voltage and derive and use the expression VH = BI /(ntq),
where t = thickness
4 understand the use of a Hall probe to measure magnetic flux density
5 describe the motion of a charged particle moving in a uniform magnetic field perpendicular to the
direction of motion of the particle
6 explain how electric and magnetic fields can be used in velocity selection
20.4 Magnetic fields due to currents
Candidates should be able to:
1 sketch magnetic field patterns due to the currents in a long straight wire, a flat circular coil and a long
solenoid
2 understand that the magnetic field due to the current in a solenoid is increased by a ferrous core
3 explain the origin of the forces between current-carrying conductors and determine the direction of the
forces
Cambridge International AS & A Level Physics 9702 syllabus for 2022, 2023 and 2024. Subject content
Back to contents page www.cambridgeinternational.org/alevel 29
20.5 Electromagnetic induction
Candidates should be able to:
1 define magnetic flux as the product of the magnetic flux density and the cross-sectional area
perpendicular to the direction of the magnetic flux density
2 recall and use Φ = BA
3 understand and use the concept of magnetic flux linkage
4 understand and explain experiments that demonstrate:
• that a changing magnetic flux can induce an e.m.f. in a circuit
• that the induced e.m.f. is in such a direction as to oppose the change producing it
• the factors affecting the magnitude of the induced e.m.f.
5 recall and use Faraday’s and Lenz’s laws of electromagnetic induction
"""

text10 = """
21.1 Characteristics of alternating currents
Candidates should be able to:
1 understand and use the terms period, frequency and peak value as applied to an alternating current or
voltage
2 use equations of the form x = x0 sin ωt representing a sinusoidally alternating current or voltage
3 recall and use the fact that the mean power in a resistive load is half the maximum power for a sinusoidal
alternating current
4 distinguish between root-mean-square (r.m.s.) and peak values and recall and use I r.m.s. = I0 / 2 and
Vr.m.s. = V0 / 2 for a sinusoidal alternating current
21.2 Rectification and smoothing
Candidates should be able to:
1 distinguish graphically between half-wave and full-wave rectification
2 explain the use of a single diode for the half-wave rectification of an alternating current
3 explain the use of four diodes (bridge rectifier) for the full-wave rectification of an alternating current
4 analyse the effect of a single capacitor in smoothing, including the effect of the values of capacitance and
the load resistance
"""

text11 = """
22 Quantum physics
22.1 Energy and momentum of a photon
Candidates should be able to:
1 understand that electromagnetic radiation has a particulate nature
2 understand that a photon is a quantum of electromagnetic energy
3 recall and use E = hf
4 use the electronvolt (eV) as a unit of energy
5 understand that a photon has momentum and that the momentum is given by p = E / c
Cambridge International AS & A Level Physics 9702 syllabus for 2022, 2023 and 2024. Subject content
30 www.cambridgeinternational.org/alevel Back to contents page
22.2 Photoelectric effect
Candidates should be able to:
1 understand that photoelectrons may be emitted from a metal surface when it is illuminated by
electromagnetic radiation
2 understand and use the terms threshold frequency and threshold wavelength
3 explain photoelectric emission in terms of photon energy and work function energy
4 recall and use hf = Φ + 1/2mvmax
2
5 explain why the maximum kinetic energy of photoelectrons is independent of intensity, whereas the
photoelectric current is proportional to intensity
22.3 Wave-particle duality
Candidates should be able to:
1 understand that the photoelectric effect provides evidence for a particulate nature of electromagnetic
radiation while phenomena such as interference and diffraction provide evidence for a wave nature
2 describe and interpret qualitatively the evidence provided by electron diffraction for the wave nature of
particles
3 understand the de Broglie wavelength as the wavelength associated with a moving particle
4 recall and use λ = h / p
22.4 Energy levels in atoms and line spectra
Candidates should be able to:
1 understand that there are discrete electron energy levels in isolated atoms (e.g. atomic hydrogen)
2 understand the appearance and formation of emission and absorption line spectra
3 recall and use hf = E1
 – E2
"""

text12 = """
23 Nuclear physics
23.1 Mass defect and nuclear binding energy
Candidates should be able to:
1 understand the equivalence between energy and mass as represented by E = mc2
 and recall and use this
equation
2 represent simple nuclear reactions by nuclear equations of the form 7N He O H 14
2
4
8
17
1
1 + + "
3 define and use the terms mass defect and binding energy
4 sketch the variation of binding energy per nucleon with nucleon number
5 explain what is meant by nuclear fusion and nuclear fission
6 explain the relevance of binding energy per nucleon to nuclear reactions, including nuclear fusion and
nuclear fission
7 calculate the energy released in nuclear reactions using E = c
2
∆m
Cambridge International AS & A Level Physics 9702 syllabus for 2022, 2023 and 2024. Subject content
Back to contents page www.cambridgeinternational.org/alevel 31
23.2 Radioactive decay
Candidates should be able to:
1 understand that fluctuations in count rate provide evidence for the random nature of radioactive decay
2 understand that radioactive decay is both spontaneous and random
3 define activity and decay constant, and recall and use A = λN
4 define half-life
5 use λ = 0.693/t 1
–
2
6 understand the exponential nature of radioactive decay, and sketch and use the relationship x = x0e–λt
,
where x could represent activity, number of undecayed nuclei or received count rate
"""

text13 = """
24 Medical physics
24.1 Production and use of ultrasound
Candidates should be able to:
1 understand that a piezo-electric crystal changes shape when a p.d. is applied across it and that the crystal
generates an e.m.f. when its shape changes
2 understand how ultrasound waves are generated and detected by a piezoelectric transducer
3 understand how the reflection of pulses of ultrasound at boundaries between tissues can be used to
obtain diagnostic information about internal structures
4 define the specific acoustic impedance of a medium as Z = ρc, where c is the speed of sound in the
medium
5 use IR / I0 = (Z1
 – Z2)
2 /(Z1
 + Z2)
2
 for the intensity reflection coefficient of a boundary between two media
6 recall and use I = I0e–μx for the attenuation of ultrasound in matter
24.2 Production and use of X-rays
Candidates should be able to:
1 explain that X-rays are produced by electron bombardment of a metal target and calculate the minimum
wavelength of X-rays produced from the accelerating p.d.
2 understand the use of X-rays in imaging internal body structures, including an understanding of the term
contrast in X-ray imaging
3 recall and use I = I0e–μx for the attenuation of X-rays in matter
4 understand that computed tomography (CT) scanning produces a 3D image of an internal structure by
first combining multiple X-ray images taken in the same section from different angles to obtain a 2D
image of the section, then repeating this process along an axis and combining 2D images of multiple
sections
Cambridge International AS & A Level Physics 9702 syllabus for 2022, 2023 and 2024. Subject content
32 www.cambridgeinternational.org/alevel Back to contents page
24.3 PET scanning
Candidates should be able to:
1 understand that a tracer is a substance containing radioactive nuclei that can be introduced into the body
and is then absorbed by the tissue being studied
2 recall that a tracer that decays by β+
 decay is used in positron emission tomography (PET scanning)
3 understand that annihilation occurs when a particle interacts with its antiparticle and that mass-energy
and momentum are conserved in the process
4 explain that, in PET scanning, positrons emitted by the decay of the tracer annihilate when they interact
with electrons in the tissue, producing a pair of gamma-ray photons travelling in opposite directions
5 calculate the energy of the gamma-ray photons emitted during the annihilation of an electron-positron
pair
6 understand that the gamma-ray photons from an annihilation event travel outside the body and can be
detected, and an image of the tracer concentration in the tissue can be created by processing the arrival
times of the gamma-ray photons
"""

text14 = """
25 Astronomy and cosmology
25.1 Standard candles
Candidates should be able to:
1 understand the term luminosity as the total power of radiation emitted by a star
2 recall and use the inverse square law for radiant flux intensity F in terms of the luminosity L of the source
F = L /(4πd2
)
3 understand that an object of known luminosity is called a standard candle
4 understand the use of standard candles to determine distances to galaxies
25.2 Stellar radii
Candidates should be able to:
1 recall and use Wien’s displacement law λmax ∝ 1 / T to estimate the peak surface temperature of a star
2 use the Stefan–Boltzmann law L = 4πσr
2
T4
3 use Wien’s displacement law and the Stefan–Boltzmann law to estimate the radius of a star
25.3 Hubble’s law and the Big Bang theory
Candidates should be able to:
1 understand that the lines in the emission spectra from distant objects show an increase in wavelength
from their known values
2 use ∆λ / λ . ∆f/f . v / c for the redshift of electromagnetic radiation from a source moving relative to an
observer
3 explain why redshift leads to the idea that the Universe is expanding
4 recall and use Hubble’s law v . H0d and explain how this leads to the Big Bang theory
(candidates will only be required to use SI units)
"""

textarr = [text, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14]
for i in range(len(textarr)):
    textarr[i] = getFormattedTextfromPdf.formatText(textarr[i])

trainModels.train(textarr, allLabels)
