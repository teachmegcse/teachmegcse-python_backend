import trainModels
import getFormattedTextfromPdf


allLabels = ['Atomic structure', 'Atoms, molecules and stoichiometry', 
             'Chemical bonding', 'States of matter', 'Chemical energetics', 'Electrochemistry', 'Equilibria',
               'Reaction kinetics', 'The Periodic Table: chemical periodicity', 'Group 2', 'Group 17', 'Nitrogen and sulfur', 'introduction to AS Level organic chemistry', 
               'Hydrocarbons', 'Halogen compounds', 'Hydroxy compounds', 'Carbonyl compounds', 'Carboxylic acids and derivatives', 'Nitrogen compounds', 'Polymerisation',
                 'Organic synthesis', 'Analytical techniques']


text1 = """
1 Atomic structure
1.1 Particles in the atom and atomic radius
Learning outcomes
Candidates should be able to:
1 understand that atoms are mostly empty space surrounding a very small, dense nucleus that contains
protons and neutrons; electrons are found in shells in the empty space around the nucleus
2 identify and describe protons, neutrons and electrons in terms of their relative charges and relative masses
3 understand the terms atomic and proton number; mass and nucleon number
4 describe the distribution of mass and charge within an atom
5 describe the behaviour of beams of protons, neutrons and electrons moving at the same velocity in an
electric field
6 determine the numbers of protons, neutrons and electrons present in both atoms and ions given atomic or
proton number, mass or nucleon number and charge
7 state and explain qualitatively the variations in atomic radius and ionic radius across a period and down a
group
1.2 Isotopes
Learning outcomes
Candidates should be able to:
1 define the term isotope in terms of numbers of protons and neutrons
2 understand the notation x
yA for isotopes, where x
 is the mass or nucleon number and y is the atomic or
proton number
3 state that and explain why isotopes of the same element have the same chemical properties
4 state that and explain why isotopes of the same element have different physical properties, limited to mass
and density
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content
Back to contents page www.cambridgeinternational.org/alevel 15
1.3 Electrons, energy levels and atomic orbitals
In 1.3 each atom or ion described will be in the ground state. Only the elements hydrogen to krypton will be
assessed.
Learning outcomes
Candidates should be able to:
1 understand the terms:
• shells, sub-shells and orbitals
• principal quantum number (n)
• ground state, limited to electronic configuration
2 describe the number of orbitals making up s, p and d sub-shells, and the number of electrons that can fill s, p
and d sub-shells
3 describe the order of increasing energy of the sub-shells within the first three shells and the 4s and 4p
sub-shells
4 describe the electronic configurations to include the number of electrons in each shell, sub-shell and orbital
5 explain the electronic configurations in terms of energy of the electrons and inter-electron repulsion
6 determine the electronic configuration of atoms and ions given the atomic or proton number and charge,
using either of the following conventions:
e.g. for Fe: 1s2
2s2
2p6
3s2
3p6
3d6
4s2
 (full electronic configuration)
or [Ar] 3d6
 4s2
 (shorthand electronic configuration)
7 understand and use the electrons in boxes notation
e.g. for Fe: [Ar]
8 describe and sketch the shapes of s and p orbitals
9 describe a free radical as a species with one or more unpaired electrons
1.4 Ionisation energy
In 1.4 each atom or ion described will be in the ground state. Only the elements hydrogen to krypton will be
assessed.
Learning outcomes
Candidates should be able to:
1 define and use the term first ionisation energy, IE
2 construct equations to represent first, second and subsequent ionisation energies
3 identify and explain the trends in ionisation energies across a period and down a group of the Periodic Table
4 identify and explain the variation in successive ionisation energies of an element
5 understand that ionisation energies are due to the attraction between the nucleus and the outer electron
6 explain the factors influencing the ionisation energies of elements in terms of nuclear charge, atomic/ionic
radius, shielding by inner shells and sub-shells and spin-pair repulsion
7 deduce the electronic configurations of elements using successive ionisation energy data
8 deduce the position of an element in the Periodic Table using successive ionisation energy data
"""

text2 = """
2.1 Relative masses of atoms and molecules
Learning outcomes
Candidates should be able to:
1 define the unified atomic mass unit as one twelfth of the mass of a carbon-12 atom
2 define relative atomic mass, Ar
, relative isotopic mass, relative molecular mass, Mr
, and relative formula mass
in terms of the unified atomic mass unit
2.2 The mole and the Avogadro constant
Learning outcomes
Candidates should be able to:
1 define and use the term mole in terms of the Avogadro constant
2.3 Formulae
Learning outcomes
Candidates should be able to:
1 write formulae of ionic compounds from ionic charges and oxidation numbers (shown by a Roman numeral),
including:
(a) the prediction of ionic charge from the position of an element in the Periodic Table
(b) recall of the names and formulae for the following ions: NO3
–
, CO3
2–, SO4
2–, OH–
, NH4
+
, Zn2+, Ag+
,
HCO3
–
, PO4
3–
2 (a) write and construct equations (which should be balanced), including ionic equations (which should not
include spectator ions)
(b) use appropriate state symbols in equations
3 define and use the terms empirical and molecular formula
4 understand and use the terms anhydrous, hydrated and water of crystallisation
5 calculate empirical and molecular formulae, using given data
2.4 Reacting masses and volumes (of solutions and gases)
Learning outcomes
Candidates should be able to:
1 perform calculations including use of the mole concept, involving:
(a) reacting masses (from formulae and equations) including percentage yield calculations
(b) volumes of gases (e.g. in the burning of hydrocarbons)
(c) volumes and concentrations of solutions
(d) limiting reagent and excess reagent
(When performing calculations, candidates’ answers should reflect the number of significant figures given or
asked for in the question. When rounding up or down, candidates should ensure that significant figures are
neither lost unnecessarily nor used beyond what is justified (see also Mathematical requirements section).)
(e) deduce stoichiometric relationships from calculations such as those in 2.4.1 (a)–(d)
"""

text3 = """
3 Chemical bonding
3.1 Electronegativity and bonding
Learning outcomes
Candidates should be able to:
1 define electronegativity as the power of an atom to attract electrons to itself
2 explain the factors influencing the electronegativities of the elements in terms of nuclear charge, atomic
radius and shielding by inner shells and sub-shells
3 state and explain the trends in electronegativity across a period and down a group of the Periodic Table
4 use the differences in Pauling electronegativity values to predict the formation of ionic and covalent bonds
(the presence of covalent character in some ionic compounds will not be assessed) (Pauling electronegativity
values will be given where necessary)
3.2 Ionic bonding
Learning outcomes
Candidates should be able to:
1 define ionic bonding as the electrostatic attraction between oppositely charged ions (positively charged
cations and negatively charged anions)
2 describe ionic bonding including the examples of sodium chloride, magnesium oxide and calcium fluoride
3.3 Metallic bonding
Learning outcomes
Candidates should be able to:
1 define metallic bonding as the electrostatic attraction between positive metal ions and delocalised electrons
3.4 Covalent bonding and coordinate (dative covalent) bonding
Learning outcomes
Candidates should be able to:
1 define covalent bonding as electrostatic attraction between the nuclei of two atoms and a shared pair of
electrons
(a) describe covalent bonding in molecules including:
• hydrogen, H2
• oxygen, O2
• nitrogen, N2
• chlorine, Cl 2
• hydrogen chloride, HCl
• carbon dioxide, CO2
• ammonia, NH3
• methane, CH4
• ethane, C2H6
• ethene, C2H4
(continued)
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content
18 www.cambridgeinternational.org/alevel Back to contents page
3.4 Covalent bonding and coordinate (dative covalent) bonding (continued)
Learning outcomes
Candidates should be able to:
(b) understand that elements in period 3 can expand their octet including in the compounds sulfur dioxide,
SO2, phosphorus pentachloride, PCl 5 , and sulfur hexafluoride, SF6
(c) describe coordinate (dative covalent) bonding, including in the reaction between ammonia and hydrogen
chloride gases to form the ammonium ion, NH4
+ , and in the Al 2Cl 6 molecule
2 (a) describe covalent bonds in terms of orbital overlap giving σ and π bonds:
• σ bonds are formed by direct overlap of orbitals between the bonding atoms
• π bonds are formed by the sideways overlap of adjacent p orbitals above and below the σ bond
(b) describe how the σ and π bonds form in molecules including H2, C2H6, C2H4, HCN and N2
(c) use the concept of hybridisation to describe sp, sp2
 and sp3
 orbitals
3 (a) define the terms:
• bond energy as the energy required to break one mole of a particular covalent bond in the gaseous
state
• bond length as the internuclear distance of two covalently bonded atoms
(b) use bond energy values and the concept of bond length to compare the reactivity of covalent molecules
3.5 Shapes of molecules
Learning outcomes
Candidates should be able to:
1 state and explain the shapes of, and bond angles in, molecules by using VSEPR theory, including as simple
examples:
• BF3 (trigonal planar, 120°)
• CO2 (linear, 180°)
• CH4 (tetrahedral, 109.5°)
• NH3 (pyramidal, 107°)
• H2O (non-linear, 104.5°)
• SF6 (octahedral, 90°)
• PF5 (trigonal bipyramidal, 120° and 90°)
2 predict the shapes of, and bond angles in, molecules and ions analogous to those specified in 3.5.1
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content
Back to contents page www.cambridgeinternational.org/alevel 19
3.6 Intermolecular forces, electronegativity and bond properties
Learning outcomes
Candidates should be able to:
1 (a) describe hydrogen bonding, limited to molecules containing N–H and O–H groups, including ammonia
and water as simple examples
(b) use the concept of hydrogen bonding to explain the anomalous properties of H2O (ice and water):
• its relatively high melting and boiling points
• its relatively high surface tension
• the density of the solid ice compared with the liquid water
2 use the concept of electronegativity to explain bond polarity and dipole moments of molecules
3 (a) describe van der Waals’ forces as the intermolecular forces between molecular entities other than
those due to bond formation, and use the term van der Waals’ forces as a generic term to describe all
intermolecular forces
(b) describe the types of van der Waals’ force:
• instantaneous dipole – induced dipole (id-id) force, also called London dispersion forces
• permanent dipole – permanent dipole (pd-pd) force, including hydrogen bonding
(c) describe hydrogen bonding and understand that hydrogen bonding is a special case of
permanent dipole – permanent dipole force between molecules where hydrogen is bonded to a highly
electronegative atom
4 state that, in general, ionic, covalent and metallic bonding are stronger than intermolecular forces
3.7 Dot-and-cross diagrams
Learning outcomes
Candidates should be able to:
1 use dot-and-cross diagrams to illustrate ionic, covalent and coordinate bonding including the representation
of any compounds stated in 3.4 and 3.5 (dot-and-cross diagrams may include species with atoms which
have an expanded octet or species with an odd number of electrons)
"""

text4 = """
4 States of matter
4.1 The gaseous state: ideal and real gases and pV = nRT
Learning outcomes
Candidates should be able to:
1 explain the origin of pressure in a gas in terms of collisions between gas molecules and the wall of the
container
2 understand that ideal gases have zero particle volume and no intermolecular forces of attraction
3 state and use the ideal gas equation pV = nRT in calculations, including in the determination of Mr
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content
20 www.cambridgeinternational.org/alevel Back to contents page
4.2 Bonding and structure
Learning outcomes
Candidates should be able to:
1 describe, in simple terms, the lattice structure of a crystalline solid which is:
(a) giant ionic, including sodium chloride and magnesium oxide
(b) simple molecular, including iodine, buckminsterfullerene C60 and ice
(c) giant molecular, including silicon(IV) oxide, graphite and diamond
(d) giant metallic, including copper
2 describe, interpret and predict the effect of different types of structure and bonding on the physical
properties of substances, including melting point, boiling point, electrical conductivity and solubility
3 deduce the type of structure and bonding present in a substance from given information
"""

text5 = """
5 Chemical energetics
5.1 Enthalpy change, ΔH
Learning outcomes
Candidates should be able to:
1 understand that chemical reactions are accompanied by enthalpy changes and these changes can be
exothermic (ΔH is negative) or endothermic (ΔH is positive)
2 construct and interpret a reaction pathway diagram, in terms of the enthalpy change of the reaction and of
the activation energy
3 define and use the terms:
(a) standard conditions (this syllabus assumes that these are 298K and 101 kPa) shown by ⦵.
(b) enthalpy change with particular reference to: reaction, ΔHr
, formation, ΔHf
, combustion, ΔHc ,
neutralisation, ΔHneut
4 understand that energy transfers occur during chemical reactions because of the breaking and making of
chemical bonds
5 use bond energies (ΔH positive, i.e. bond breaking) to calculate enthalpy change of reaction, ΔHr
6 understand that some bond energies are exact and some bond energies are averages
7 calculate enthalpy changes from appropriate experimental results, including the use of the relationships
q = mcΔT and ΔH = –mcΔT/n
5.2 Hess’s Law
Learning outcomes
Candidates should be able to:
1 apply Hess’s Law to construct simple energy cycles
2 carry out calculations using cycles and relevant energy terms, including:
(a) determining enthalpy changes that cannot be found by direct experiment
(b) use of bond energy data
"""

text6 = """
6 Electrochemistry
6.1 Redox processes: electron transfer and changes in oxidation number (oxidation state)
Learning outcomes
Candidates should be able to:
1 calculate oxidation numbers of elements in compounds and ions
2 use changes in oxidation numbers to help balance chemical equations
3 explain and use the terms redox, oxidation, reduction and disproportionation in terms of electron transfer
and changes in oxidation number
4 explain and use the terms oxidising agent and reducing agent
5 use a Roman numeral to indicate the magnitude of the oxidation number of an element
"""

text7 = """
7 Equilibria
7.1 Chemical equilibria: reversible reactions, dynamic equilibrium
Learning outcomes
Candidates should be able to:
1 (a) understand what is meant by a reversible reaction
(b) understand what is meant by dynamic equilibrium in terms of the rate of forward and reverse reactions
being equal and the concentration of reactants and products remaining constant
(c) understand the need for a closed system in order to establish dynamic equilibrium
2 define Le Chatelier’s principle as: if a change is made to a system at dynamic equilibrium, the position of
equilibrium moves to minimise this change
3 use Le Chatelier’s principle to deduce qualitatively (from appropriate information) the effects of changes in
temperature, concentration, pressure or presence of a catalyst on a system at equilibrium
4 deduce expressions for equilibrium constants in terms of concentrations, Kc
5 use the terms mole fraction and partial pressure
6 deduce expressions for equilibrium constants in terms of partial pressures, K
p
(use of the relationship between K
p
 and Kc
 is not required)
7 use the Kc
 and K
p
 expressions to carry out calculations (such calculations will not require the solving of
quadratic equations)
8 calculate the quantities present at equilibrium, given appropriate data
9 state whether changes in temperature, concentration or pressure or the presence of a catalyst affect the
value of the equilibrium constant for a reaction
10 describe and explain the conditions used in the Haber process and the Contact process, as examples of the
importance of an understanding of dynamic equilibrium in the chemical industry and the application of Le
Chatelier’s principle
7.2 Brønsted–Lowry theory of acids and bases
Learning outcomes
Candidates should be able to:
1 state the names and formulae of the common acids, limited to hydrochloric acid, HCl, sulfuric acid, H2SO4,
nitric acid, HNO3, ethanoic acid, CH3COOH
2 state the names and formulae of the common alkalis, limited to sodium hydroxide, NaOH, potassium
hydroxide, KOH, ammonia, NH3
(continued)
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content
22 www.cambridgeinternational.org/alevel Back to contents page
7.2 Brønsted–Lowry theory of acids and bases (continued)
Learning outcomes
Candidates should be able to:
3 describe the Brønsted–Lowry theory of acids and bases
4 describe strong acids and strong bases as fully dissociated in aqueous solution and weak acids and weak
bases as partially dissociated in aqueous solution
5 appreciate that water has pH of 7, acid solutions pH of below 7 and alkaline solutions pH of above 7
6 explain qualitatively the differences in behaviour between strong and weak acids including the reaction with
a reactive metal and difference in pH values by use of a pH meter, universal indicator or conductivity
7 understand that neutralisation reactions occur when H+
(aq) and OH–
(aq) form H2O(l)
8 understand that salts are formed in neutralisation reactions
9 sketch the pH titration curves of titrations using combinations of strong and weak acids with strong and
weak alkalis
10 select suitable indicators for acid-alkali titrations, given appropriate data (pKa
 values will not be used)
"""

text8 = """
8 Reaction kinetics
8.1 Rate of reaction
Learning outcomes
Candidates should be able to:
1 explain and use the term rate of reaction, frequency of collisions, effective collisions and non-effective
collisions
2 explain qualitatively, in terms of frequency of effective collisions, the effect of concentration and pressure
changes on the rate of a reaction
3 use experimental data to calculate the rate of a reaction
8.2 Effect of temperature on reaction rates and the concept of activation energy
Learning outcomes
Candidates should be able to:
1 define activation energy, EA, as the minimum energy required for a collision to be effective
2 sketch and use the Boltzmann distribution to explain the significance of activation energy
3 explain qualitatively, in terms both of the Boltzmann distribution and of frequency of effective collisions, the
effect of temperature change on the rate of a reaction
8.3 Homogeneous and heterogeneous catalysts
Learning outcomes
Candidates should be able to:
1 explain and use the terms catalyst and catalysis
(a) explain that, in the presence of a catalyst, a reaction has a different mechanism, i.e. one of lower
activation energy
(b) explain this catalytic effect in terms of the Boltzmann distribution
(c) construct and interpret a reaction pathway diagram, for a reaction in the presence and absence of an
effective catalyst 
"""

text9 = """
9 The Periodic Table: chemical periodicity
9.1 Periodicity of physical properties of the elements in Period 3
Learning outcomes
Candidates should be able to:
1 describe qualitatively (and indicate the periodicity in) the variations in atomic radius, ionic radius, melting
point and electrical conductivity of the elements
2 explain the variation in melting point and electrical conductivity in terms of the structure and bonding of the
elements
9.2 Periodicity of chemical properties of the elements in Period 3
Learning outcomes
Candidates should be able to:
1 describe, and write equations for, the reactions of the elements with oxygen (to give Na2O, MgO, Al 2O3,
P4O10, SO2), chlorine (to give NaCl, MgCl 2, Al Cl 3, SiCl 4, PCl 5) and water (Na and Mg only)
2 state and explain the variation in the oxidation number of the oxides (Na2O, MgO, Al 2O3, P4O10, SO2 and
SO3 only) and chlorides (NaCl, MgCl 2, Al Cl 3, SiCl 4, PCl 5 only) in terms of their outer shell (valence shell)
electrons
3 describe, and write equations for, the reactions, if any, of the oxides Na2O, MgO, Al 2O3, SiO2, P4O10, SO2
and SO3 with water including the likely pHs of the solutions obtained
4 describe, explain, and write equations for, the acid/base behaviour of the oxides Na2O, MgO, Al 2O3, P4O10,
SO2 and SO3and the hydroxides NaOH, Mg(OH)2, Al(OH)3 including, where relevant, amphoteric behaviour
in reactions with acids and bases (sodium hydroxide only)
5 describe, explain, and write equations for, the reactions of the chlorides NaCl, MgCl 2, Al Cl 3, SiCl 4, PCl 5
with water including the likely pHs of the solutions obtained
6 explain the variations and trends in 9.2.2, 9.2.3, 9.2.4 and 9.2.5 in terms of bonding and electronegativity
7 suggest the types of chemical bonding present in the chlorides and oxides from observations of their
chemical and physical properties
9.3 Chemical periodicity of other elements
Learning outcomes
Candidates should be able to:
1 predict the characteristic properties of an element in a given group by using knowledge of chemical
periodicity
2 deduce the nature, possible position in the Periodic Table and identity of unknown elements from given
information about physical and chemical properties
"""

text10 = """
10 Group 2
10.1 Similarities and trends in the properties of the Group 2 metals, magnesium to barium, and their
compounds
Learning outcomes
Candidates should be able to:
1 describe, and write equations for, the reactions of the elements with oxygen, water and dilute hydrochloric
and sulfuric acids
2 describe, and write equations for, the reactions of the oxides, hydroxides and carbonates with water and
dilute hydrochloric and sulfuric acids
3 describe, and write equations for, the thermal decomposition of the nitrates and carbonates, to include the
trend in thermal stabilities
4 describe, and make predictions from, the trends in physical and chemical properties of the elements involved
in the reactions in 10.1.1 and the compounds involved in 10.1.2, 10.1.3 and 10.1.5
5 state the variation in the solubilities of the hydroxides and sulfates
"""
text11 = """
11 Group 17
11.1 Physical properties of the Group 17 elements
Learning outcomes
Candidates should be able to:
1 describe the colours and the trend in volatility of chlorine, bromine and iodine
2 describe and explain the trend in the bond strength of the halogen molecules
3 interpret the volatility of the elements in terms of instantaneous dipole–induced dipole forces
11.2 The chemical properties of the halogen elements and the hydrogen halides
Learning outcomes
Candidates should be able to:
1 describe the relative reactivity of the elements as oxidising agents
2 describe the reactions of the elements with hydrogen and explain their relative reactivity in these reactions
3 describe the relative thermal stabilities of the hydrogen halides and explain these in terms of bond strengths
11.3 Some reactions of the halide ions
Learning outcomes
Candidates should be able to:
1 describe the relative reactivity of halide ions as reducing agents
2 describe and explain the reactions of halide ions with:
(a) aqueous silver ions followed by aqueous ammonia (the formation and formula of the [Ag(NH3)
2]
+
complex is not required)
(b) concentrated sulfuric acid, to include balanced chemical equations
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content
Back to contents page www.cambridgeinternational.org/alevel 25
11.4 The reactions of chlorine
Learning outcomes
Candidates should be able to:
1 describe and interpret, in terms of changes in oxidation number, the reaction of chlorine with cold and with
hot aqueous sodium hydroxide and recognise these as disproportionation reactions
2 explain, including by use of an equation, the use of chlorine in water purification to include the production of
the active species HOCl and ClO–
 which kill bacteria.
"""

text12 = """
12 Nitrogen and sulfur
12.1 Nitrogen and sulfur
Learning outcomes
Candidates should be able to:
1 explain the lack of reactivity of nitrogen, with reference to triple bond strength and lack of polarity
2 describe and explain:
(a) the basicity of ammonia, using the Brønsted–Lowry theory
(b) the structure of the ammonium ion and its formation by an acid–base reaction
(c) the displacement of ammonia from ammonium salts by an acid–base reaction
3 state and explain the natural and man-made occurrences of oxides of nitrogen and their catalytic removal
from the exhaust gases of internal combustion engines
4 understand that atmospheric oxides of nitrogen (NO and NO2) can react with unburned hydrocarbons to
form peroxyacetyl nitrate, PAN, which is a component of photochemical smog
5 describe the role of NO and NO2 in the formation of acid rain both directly and in their catalytic role in the
oxidation of atmospheric sulfur dioxide 
"""

text13 = """
13.1 Formulae, functional groups and the naming of organic compounds
Learning outcomes
Candidates should be able to:
1 define the term hydrocarbon as a compound made up of C and H atoms only
2 understand that alkanes are simple hydrocarbons with no functional group
3 understand that the compounds in the table on page 26 and 27 contain a functional group which dictates
their physical and chemical properties
4 interpret and use the general, structural, displayed and skeletal formulae of the classes of compound stated
in the table on page 26 and 27
5 understand and use systematic nomenclature of simple aliphatic organic molecules with functional groups
detailed in the table on page 26 and 27, up to six carbon atoms (six plus six for esters, straight chains only
for esters and nitriles)
6 deduce the molecular and/or empirical formula of a compound, given its structural, displayed or skeletal
formula
13.2 Characteristic organic reactions
Learning outcomes
Candidates should be able to:
1 interpret and use the following terminology associated with types of organic compounds and reactions:
(a) homologous series
(b) saturated and unsaturated
(c) homolytic and heterolytic fission
(d) free radical, initiation, propagation, termination (the use of arrows to show movement of single
electrons is not required)
(e) nucleophile, electrophile, nucleophilic, electrophilic
(f) addition, substitution, elimination, hydrolysis, condensation
(g) oxidation and reduction
(in equations for organic redox reactions, the symbol [O] can be used to represent one atom of oxygen from
an oxidising agent and the symbol [H] one atom of hydrogen from a reducing agent)
2 understand and use the following terminology associated with types of organic mechanisms:
(a) free-radical substitution
(b) electrophilic addition
(c) nucleophilic substitution
(d) nucleophilic addition
(in organic reaction mechanisms, the use of curly arrows to represent movement of electron pairs is
expected; the arrow should begin at a bond or a lone pair of electrons)
13.3 Shapes of organic molecules; σ and π bonds
Learning outcomes
Candidates should be able to:
1 describe organic molecules as either straight-chained, branched or cyclic
2 describe and explain the shape of, and bond angles in, molecules containing sp, sp2
 and sp3
 hybridised atoms
3 describe the arrangement of σ and π bonds in molecules containing sp, sp2
 and sp3
 hybridised atoms
4 understand and use the term planar when describing the arrangement of atoms in organic molecules, for
example ethene
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content
Back to contents page www.cambridgeinternational.org/alevel 29
13.4 Isomerism: structural and stereoisomerism
Learning outcomes
Candidates should be able to:
1 describe structural isomerism and its division into chain, positional and functional group isomerism
2 describe stereoisomerism and its division into geometrical (cis/trans) and optical isomerism (use of E, Z
nomenclature is acceptable but is not required)
3 describe geometrical (cis/trans) isomerism in alkenes, and explain its origin in terms of restricted rotation
due to the presence of π bonds
4 explain what is meant by a chiral centre and that such a centre gives rise to two optical isomers
(enantiomers)
(Candidates should appreciate that compounds can contain more than one chiral centre, but knowledge of
meso compounds, or nomenclature such as diastereoisomers is not required)
5 identify chiral centres and geometrical (cis/trans) isomerism in a molecule of given structural formula
including cyclic compounds
6 deduce the possible isomers for an organic molecule of known molecular formula
"""

text14 = """
14 Hydrocarbons
14.1 Alkanes
Learning outcomes
Candidates should be able to:
1 recall the reactions (reagents and conditions) by which alkanes can be produced:
(a) addition of hydrogen to an alkene in a hydrogenation reaction, H2(g) and Pt/Ni catalyst and heat
(b) cracking of a longer chain alkane, heat with Al 2O3
2 describe:
(a) the complete and incomplete combustion of alkanes
(b) the free-radical substitution of alkanes by Cl 2 or Br2 in the presence of ultraviolet light, as exemplified by
the reactions of ethane
3 describe the mechanism of free-radical substitution with reference to the initiation, propagation and
termination steps
4 suggest how cracking can be used to obtain more useful alkanes and alkenes of lower Mr
 from heavier crude
oil fractions
5 understand the general unreactivity of alkanes, including towards polar reagents in terms of the strength of
the C–H bonds and their relative lack of polarity
6 recognise the environmental consequences of carbon monoxide, oxides of nitrogen and unburnt
hydrocarbons arising from the combustion of alkanes in the internal combustion engine and of their catalytic
removal
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content
30 www.cambridgeinternational.org/alevel Back to contents page
14.2 Alkenes
Learning outcomes
Candidates should be able to:
1 recall the reactions (including reagents and conditions) by which alkenes can be produced:
(a) elimination of HX from a halogenoalkane by ethanolic NaOH and heat
(b) dehydration of an alcohol, by using a heated catalyst (e.g. Al 2O3) or a concentrated acid
(c) cracking of a longer chain alkane
2 describe the following reactions of alkenes:
(a) the electrophilic addition of
(i) hydrogen in a hydrogenation reaction, H2(g) and Pt/Ni catalyst and heat
(ii) steam, H2O(g) and H3PO4 catalyst
(iii) a hydrogen halide, HX(g) at room temperature
(iv) a halogen, X2
(b) the oxidation by cold dilute acidified KMnO4 to form the diol
(c) the oxidation by hot concentrated acidified KMnO4 leading to the rupture of the carbon–carbon double
bond and the identities of the subsequent products to determine the position of alkene linkages in larger
molecules
(d) addition polymerisation exemplified by the reactions of ethene and propene
3 describe the use of aqueous bromine to show the presence of a C=C bond
4 describe the mechanism of electrophilic addition in alkenes, using bromine / ethene and hydrogen
bromide /propene as examples
5 describe and explain the inductive effects of alkyl groups on the stability of primary, secondary and tertiary
cations formed during electrophilic addition (this should be used to explain Markovnikov addition) 
"""

text15 = """
15 Halogen compounds
15.1 Halogenoalkanes
Learning outcomes
Candidates should be able to:
1 recall the reactions (reagents and conditions) by which halogenoalkanes can be produced:
(a) the free-radical substitution of alkanes by Cl 2 or Br2 in the presence of ultraviolet light, as exemplified by
the reactions of ethane
(b) electrophilic addition of an alkene with a halogen, X2, or hydrogen halide, HX(g), at room temperature
(c) substitution of an alcohol, e.g. by reaction with HX or KBr with H2SO4 or H3PO4; or with PCl 3 and heat;
or with PCl 5; or with SOCl 2
2 classify halogenoalkanes into primary, secondary and tertiary
3 describe the following nucleophilic substitution reactions:
(a) the reaction with NaOH(aq) and heat to produce an alcohol
(b) the reaction with KCN in ethanol and heat to produce a nitrile
(c) the reaction with NH3 in ethanol heated under pressure to produce an amine
(d) the reaction with aqueous silver nitrate in ethanol as a method of identifying the halogen present as
exemplified by bromoethane
(continued)
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content
Back to contents page www.cambridgeinternational.org/alevel 31
15.1 Halogenoalkanes (continued)
4 describe the elimination reaction with NaOH in ethanol and heat to produce an alkene as exemplified by
bromoethane
5 describe the SN1 and SN2 mechanisms of nucleophilic substitution in halogenoalkanes including the inductive
effects of alkyl groups
6 recall that primary halogenoalkanes tend to react via the SN2 mechanism; tertiary halogenoalkanes via the
SN1 mechanism; and secondary halogenoalkanes by a mixture of the two, depending on structure
7 describe and explain the different reactivities of halogenoalkanes (with particular reference to the relative
strengths of the C–X bonds as exemplified by the reactions of halogenoalkanes with aqueous silver nitrates)
"""

text16 = """
16 Hydroxy compounds
16.1 Alcohols
Learning outcomes
Candidates should be able to:
1 recall the reactions (reagents and conditions) by which alcohols can be produced:
(a) electrophilic addition of steam to an alkene, H2O(g) and H3PO4 catalyst
(b) reaction of alkenes with cold dilute acidified potassium manganate(VII) to form a diol
(c) substitution of a halogenoalkane using NaOH(aq) and heat
(d) reduction of an aldehyde or ketone using NaBH4 or LiAlH4
(e) reduction of a carboxylic acid using LiAlH4
(f) hydrolysis of an ester using dilute acid or dilute alkali and heat
2 describe:
(a) the reaction with oxygen (combustion)
(b) substitution to halogenoalkanes, e.g. by reaction with HX or KBr with H2SO4 or H3PO4; or with PCl 3 and
heat; or with PCl 5; or with SOCl 2
(c) the reaction with Na(s)
(d) oxidation with acidified K2Cr2O7
 or acidified KMnO4 to:
(i) carbonyl compounds by distillation
(ii) carboxylic acids by refluxing
(primary alcohols give aldehydes which can be further oxidised to carboxylic acids, secondary alcohols
give ketones, tertiary alcohols cannot be oxidised)
(e) dehydration to an alkene, by using a heated catalyst, e.g. Al 2O3 or a concentrated acid
(f) formation of esters by reaction with carboxylic acids and concentrated H2SO4 or H3PO4 as catalyst as
exemplified by ethanol
3 (a) classify alcohols as primary, secondary and tertiary alcohols, to include examples with more than one
alcohol group
(b) state characteristic distinguishing reactions, e.g. mild oxidation with acidified K2Cr2O7
, colour change
from orange to green
4 deduce the presence of a CH3CH(OH)– group in an alcohol, CH3CH(OH)–R, from its reaction with alkaline
I2(aq) to form a yellow precipitate of tri-iodomethane and an ion, RCO2
–
5 explain the acidity of alcohols compared with water
"""

text17 = """
17 Carbonyl compounds
17.1 Aldehydes and ketones
Learning outcomes
Candidates should be able to:
1 recall the reactions (reagents and conditions) by which aldehydes and ketones can be produced:
(a) the oxidation of primary alcohols using acidified K2Cr2O7
 or acidified KMnO4 and distillation to produce
aldehydes
(b) the oxidation of secondary alcohols using acidified K2Cr2O7
 or acidified KMnO4 and distillation to
produce ketones
2 describe:
(a) the reduction of aldehydes and ketones, using NaBH4 or LiAlH4 to produce alcohols
(b) the reaction of aldehydes and ketones with HCN, KCN as catalyst, and heat to produce hydroxynitriles
exemplified by ethanal and propanone
3 describe the mechanism of the nucleophilic addition reactions of hydrogen cyanide with aldehydes and
ketones in 17.1.2(b)
4 describe the use of 2,4-dinitrophenylhydrazine (2,4-DNPH reagent) to detect the presence of carbonyl
compounds
5 deduce the nature (aldehyde or ketone) of an unknown carbonyl compound from the results of simple tests
(Fehling’s and Tollens’ reagents; ease of oxidation)
6 deduce the presence of a CH3CO– group in an aldehyde or ketone, CH3CO–R, from its reaction with alkaline
I2(aq) to form a yellow precipitate of tri-iodomethane and an ion, RCO2
–
"""

text18 = """
18 Carboxylic acids and derivatives
18.1 Carboxylic acids
Learning outcomes
Candidates should be able to:
1 recall the reactions by which carboxylic acids can be produced:
(a) oxidation of primary alcohols and aldehydes with acidified K2Cr2O7
 or acidified KMnO4 and refluxing
(b) hydrolysis of nitriles with dilute acid or dilute alkali followed by acidification
(c) hydrolysis of esters with dilute acid or dilute alkali and heat followed by acidification
2 describe:
(a) the redox reaction with reactive metals to produce a salt and H2(g)
(b) the neutralisation reaction with alkalis to produce a salt and H2O(l)
(c) the acid–base reaction with carbonates to produce a salt and H2O(l) and CO2(g)
(d) esterification with alcohols with concentrated H2SO4 as catalyst
(e) reduction by LiAlH4 to form a primary alcohol
18.2 Esters
Learning outcomes
Candidates should be able to:
1 recall the reaction (reagents and conditions) by which esters can be produced:
(a) the condensation reaction between an alcohol and a carboxylic acid with concentrated H2
SO4 as catalyst
2 describe the hydrolysis of esters by dilute acid and by dilute alkali and heat
"""

text19 = """
19 Nitrogen compounds
19.1 Primary amines
Learning outcomes
Candidates should be able to:
1 recall the reactions by which amines can be produced:
(a) reaction of a halogenoalkane with NH3 in ethanol heated under pressure
Classification of amines will not be tested at AS Level.
19.2 Nitriles and hydroxynitriles
Learning outcomes
Candidates should be able to:
1 recall the reactions by which nitriles can be produced:
(a) reaction of a halogenoalkane with KCN in ethanol and heat
2 recall the reactions by which hydroxynitriles can be produced:
(a) the reaction of aldehydes and ketones with HCN, KCN as catalyst, and heat
3 describe the hydrolysis of nitriles with dilute acid or dilute alkali followed by acidification to produce a
carboxylic acid
"""

text20 = """
20 Polymerisation
20.1 Addition polymerisation
Learning outcomes
Candidates should be able to:
1 describe addition polymerisation as exemplified by poly(ethene) and poly(chloroethene), PVC
2 deduce the repeat unit of an addition polymer obtained from a given monomer
3 identify the monomer(s) present in a given section of an addition polymer molecule
4 recognise the difficulty of the disposal of poly(alkene)s, i.e. non-biodegradability and harmful combustion
products 

"""

text21 = """
21 Organic synthesis
21.1 Organic synthesis
Learning outcomes
Candidates should be able to:
1 for an organic molecule containing several functional groups:
(a) identify organic functional groups using the reactions in the syllabus
(b) predict properties and reactions
2 devise multi-step synthetic routes for preparing organic molecules using the reactions in the syllabus
3 analyse a given synthetic route in terms of type of reaction and reagents used for each step of it, and
possible by-products
"""

text22 = """
22 Analytical techniques
22.1 Infrared spectroscopy
Learning outcomes
Candidates should be able to:
1 analyse an infrared spectrum of a simple molecule to identify functional groups (see the Data section for the
functional groups required)
22.2 Mass spectrometry
Learning outcomes
Candidates should be able to:
1 analyse mass spectra in terms of m/e values and isotopic abundances (knowledge of the working of the mass
spectrometer is not required)
2 calculate the relative atomic mass of an element given the relative abundances of its isotopes, or its mass
spectrum
3 deduce the molecular mass of an organic molecule from the molecular ion peak in a mass spectrum
4 suggest the identity of molecules formed by simple fragmentation in a given mass spectrum
5 deduce the number of carbon atoms, n, in a compound using the M +1 peak and the formula
n =
100 × abundance of M +1 ion
1.1 × abundance of M + ion
6 deduce the presence of bromine and chlorine atoms in a compound using the M +2 peak 
"""


textarr = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14, text15, text16, text17, text18, text19, text20, text21, text22]
for i in range(len(textarr)):
    textarr[i] = getFormattedTextfromPdf.formatText(textarr[i])

trainModels.train(textarr, allLabels)
