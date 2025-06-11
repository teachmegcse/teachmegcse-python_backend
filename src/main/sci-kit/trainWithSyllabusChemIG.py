import trainModels
import getFormattedTextfromPdf


allLabels = ['States of matter', 'Atoms, elements and compounds', 
             'Stoichiometry', 'Electrochemistry', 'Chemical energetics', 'Chemical reactions', 'Acids, bases and salts',
               'The Periodic Table', 'Metals', 'Chemistry of the environment', 'Organic chemistry', 'Experimental techniques and chemical analysis']


text1 = """
1 States of matter
1.1 Solids, liquids and gases
Core
1 State the distinguishing properties of solids,
liquids and gases
2 Describe the structures of solids, liquids
and gases in terms of particle separation,
arrangement and motion
3 Describe changes of state in terms of melting,
boiling, evaporating, freezing and condensing
4 Describe the effects of temperature and pressure
on the volume of a gas
Supplement
5 Explain changes of state in terms of kinetic
particle theory, including the interpretation of
heating and cooling curves
6 Explain, in terms of kinetic particle theory, the
effects of temperature and pressure on the
volume of a gas
1.2 Diffusion
Core
1 Describe and explain diffusion in terms of kinetic
particle theory
Supplement
2 Describe and explain the effect of relative
molecular mass on the rate of diffusion of gases"""

text2 = """
2 Atoms, elements and compounds
2.1 Elements, compounds and mixtures
Core
1 Describe the differences between elements,
compounds and mixtures
Supplement
2.2 Atomic structure and the Periodic Table
Core
1 Describe the structure of the atom as a central
nucleus containing neutrons and protons
surrounded by electrons in shells
2 State the relative charges and relative masses of
a proton, a neutron and an electron
3 Define proton number/ atomic number as the
number of protons in the nucleus of an atom
4 Define mass number/nucleon number as the
total number of protons and neutrons in the
nucleus of an atom
5 Determine the electronic configuration of
elements and their ions with proton number 1 to
20, e.g. 2,8,3
6 State that:
(a) Group VIII noble gases have a full outer shell
(b) the number of outer shell electrons is equal
to the group number in Groups I to VII
(c) the number of occupied electron shells is
equal to the period number
Supplement
2.3 Isotopes
Core
1 Define isotopes as different atoms of the same
element that have the same number of protons
but different numbers of neutrons
2 Interpret and use symbols for atoms, e.g. 12
6C, and
ions, e.g. 35
17Cl –
Supplement
3 State that isotopes of the same element have
the same chemical properties because they have
the same number of electrons and therefore the
same electronic configuration
4 Calculate the relative atomic mass of an element
from the relative masses and abundances of its
isotopes
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
12 www.cambridgeinternational.org/igcse Back to contents page
2.4 Ions and ionic bonds
Core
1 Describe the formation of positive ions, known as
cations, and negative ions, known as anions
2 State that an ionic bond is a strong electrostatic
attraction between oppositely charged ions
3 Describe the formation of ionic bonds between
elements from Group I and Group VII, including
the use of dot-and-cross diagrams
4 Describe the properties of ionic compounds:
(a) high melting points and boiling points
(b) good electrical conductivity when aqueous or
molten and poor when solid
Supplement
5 Describe the giant lattice structure of ionic
compounds as a regular arrangement of
alternating positive and negative ions
6 Describe the formation of ionic bonds between
ions of metallic and non-metallic elements,
including the use of dot-and-cross diagrams
7 Explain in terms of structure and bonding the
properties of ionic compounds:
(a) high melting points and boiling points
(b) good electrical conductivity when aqueous or
molten and poor when solid
2.5 Simple molecules and covalent bonds
Core
1 State that a covalent bond is formed when a pair
of electrons is shared between two atoms leading
to noble gas electronic configurations
2 Describe the formation of covalent bonds in
simple molecules, including H2, Cl 2, H2O, CH4,
NH3 and HCl. Use dot-and-cross diagrams to
show the electronic configurations in these and
similar molecules
3 Describe in terms of structure and bonding the
properties of simple molecular compounds:
(a) low melting points and boiling points
(b) poor electrical conductivity
Supplement
4 Describe the formation of covalent bonds in
simple molecules, including CH3OH, C2H4, O2,
CO2 and N2. Use dot-and-cross diagrams to show
the electronic configurations in these and similar
molecules
5 Explain in terms of structure and bonding the
properties of simple molecular compounds:
(a) low melting points and boiling points in
terms of weak intermolecular forces (specific
types of intermolecular forces are not
required)
(b) poor electrical conductivity
2.6 Giant covalent structures
Core
1 Describe the giant covalent structures of graphite
and diamond
2 Relate the structures and bonding of graphite and
diamond to their uses, limited to:
(a) graphite as a lubricant and as an electrode
(b) diamond in cutting tools
Supplement
3 Describe the giant covalent structure of
silicon(IV) oxide, SiO2
4 Describe the similarity in properties between
diamond and silicon(IV) oxide, related to their
structures
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 13
2.7 Metallic bonding
Core Supplement
1 Describe metallic bonding as the electrostatic
attraction between the positive ions in a giant
metallic lattice and a ‘sea’ of delocalised
electrons
2 Explain in terms of structure and bonding the
properties of metals:
(a) good electrical conductivity
(b) malleability and ductility"""

text3 = """
3 Stoichiometry
3.1 Formulae
Core
1 State the formulae of the elements and
compounds named in the subject content
2 Define the molecular formula of a compound as
the number and type of different atoms in one
molecule
3 Deduce the formula of a simple compound from
the relative numbers of atoms present in a model
or a diagrammatic representation
4 Construct word equations and symbol equations
to show how reactants form products, including
state symbols
Supplement
5 Define the empirical formula of a compound as
the simplest whole number ratio of the different
atoms or ions in a compound
6 Deduce the formula of an ionic compound from
the relative numbers of the ions present in a
model or a diagrammatic representation or from
the charges on the ions
7 Construct symbol equations with state symbols,
including ionic equations
8 Deduce the symbol equation with state
symbols for a chemical reaction, given relevant
information
3.2 Relative masses of atoms and molecules
Core
1 Describe relative atomic mass, Ar
, as the average
mass of the isotopes of an element compared to
1/12th of the mass of an atom of 12C
2 Define relative molecular mass, Mr
, as the sum
of the relative atomic masses. Relative formula
mass, Mr
, will be used for ionic compounds
3 Calculate reacting masses in simple proportions.
Calculations will not involve the mole concept
Supplement
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
14 www.cambridgeinternational.org/igcse Back to contents page
3.3 The mole and the Avogadro constant
Core
1 State that concentration can be measured in
g /dm3
 or mol/dm3
Supplement
2 State that the mole, mol, is the unit of amount of
substance and that one mole contains
6.02 × 1023 particles, e.g. atoms, ions, molecules;
this number is the Avogadro constant
3 Use the relationship
amount of substance (mol) = mass (g)
molar mass (g /mol)
to calculate:
(a) amount of substance
(b) mass
(c) molar mass
(d) relative atomic mass or relative
molecular/formula mass
(e) number of particles, using the value of the
Avogadro constant
4 Use the molar gas volume, taken as 24dm3
at room temperature and pressure, r.t.p., in
calculations involving gases
5 Calculate stoichiometric reacting masses, limiting
reactants, volumes of gases at r.t.p., volumes
of solutions and concentrations of solutions
expressed in g /dm3
 and mol/dm3
, including
conversion between cm3
 and dm3
6 Use experimental data from a titration
to calculate the moles of solute, or the
concentration or volume of a solution
7 Calculate empirical formulae and molecular
formulae, given appropriate data
8 Calculate percentage yield, percentage
composition by mass and percentage purity,
given appropriate data"""

text4 = """
4 Electrochemistry
4.1 Electrolysis
Core
1 Define electrolysis as the decomposition of an
ionic compound, when molten or in aqueous
solution, by the passage of an electric current
2 Identify in simple electrolytic cells:
(a) the anode as the positive electrode
(b) the cathode as the negative electrode
(c) the electrolyte as the molten or aqueous
substance that undergoes electrolysis
Supplement
8 Describe the transfer of charge during electrolysis
to include:
(a) the movement of electrons in the external
circuit
(b) the loss or gain of electrons at the electrodes
(c) the movement of ions in the electrolyte
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 15
4.1 Electrolysis continued
Core
3 Identify the products formed at the electrodes
and describe the observations made during the
electrolysis of:
(a) molten lead(II) bromide
(b) concentrated aqueous sodium chloride
(c) dilute sulfuric acid
using inert electrodes made of platinum or
carbon/ graphite
4 State that metals or hydrogen are formed at
the cathode and that non-metals (other than
hydrogen) are formed at the anode
5 Predict the identity of the products at each
electrode for the electrolysis of a binary
compound in the molten state
6 State that metal objects are electroplated to
improve their appearance and resistance to
corrosion
7 Describe how metals are electroplated
Supplement
9 Identify the products formed at the electrodes
and describe the observations made during the
electrolysis of aqueous copper(II) sulfate using
inert carbon/ graphite electrodes and when using
copper electrodes
10 Predict the identity of the products at each
electrode for the electrolysis of a halide
compound in dilute or concentrated aqueous
solution
11 Construct ionic half-equations for reactions
at the anode (to show oxidation) and at the
cathode (to show reduction)
4.2 Hydrogen–oxygen fuel cells
Core
1 State that a hydrogen–oxygen fuel cell uses
hydrogen and oxygen to produce electricity with
water as the only chemical product
Supplement
2 Describe the advantages and disadvantages of
using hydrogen–oxygen fuel cells in comparison
with gasoline /petrol engines in vehicles"""

text5 = """
5 Chemical energetics
5.1 Exothermic and endothermic reactions
Core
1 State that an exothermic reaction transfers
thermal energy to the surroundings leading to an
increase in the temperature of the surroundings
2 State that an endothermic reaction takes in
thermal energy from the surroundings leading
to a decrease in the temperature of the
surroundings
3 Interpret reaction pathway diagrams showing
exothermic and endothermic reactions
Supplement
4 State that the transfer of thermal energy during a
reaction is called the enthalpy change, ∆H, of the
reaction. ∆H is negative for exothermic reactions
and positive for endothermic reactions
5 Define activation energy, Ea
, as the minimum
energy that colliding particles must have to react
6 Draw and label reaction pathway diagrams for
exothermic and endothermic reactions using
information provided, to include:
(a) reactants
(b) products
(c) enthalpy change of the reaction, ∆H
(d) activation energy, Ea
7 State that bond breaking is an endothermic
process and bond making is an exothermic
process and explain the enthalpy change of a
reaction in terms of bond breaking and bond
making
8 Calculate the enthalpy change of a reaction using
bond energies"""

text6 = """
6 Chemical reactions
6.1 Physical and chemical changes
Core
1 Identify physical and chemical changes, and
describe the differences between them
Supplement
6.2 Rate of reaction
Core
1 Describe the effect on the rate of reaction of:
(a) changing the concentration of solutions
(b) changing the pressure of gases
(c) changing the surface area of solids
(d) changing the temperature
(e) adding or removing a catalyst, including
enzymes
2 State that a catalyst increases the rate of a
reaction and is unchanged at the end of a
reaction
3 Describe practical methods for investigating the
rate of a reaction including change in mass of a
reactant or a product and the formation of a gas
4 Interpret data, including graphs, from rate of
reaction experiments
Supplement
5 Describe collision theory in terms of:
(a) number of particles per unit volume
(b) frequency of collisions between particles
(c) kinetic energy of particles
(d) activation energy, Ea
6 Describe and explain the effect on the rate of
reaction of:
(a) changing the concentration of solutions
(b) changing the pressure of gases
(c) changing the surface area of solids
(d) changing the temperature
(e) adding or removing a catalyst, including
enzymes
using collision theory
7 State that a catalyst decreases the activation
energy, Ea
, of a reaction
8 Evaluate practical methods for investigating the
rate of a reaction including change in mass of a
reactant or a product and the formation of a gas
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
18 www.cambridgeinternational.org/igcse Back to contents page
6.3 Reversible reactions and equilibrium
Core
1 State that some chemical reactions are reversible
as shown by the symbol ⇌
2 Describe how changing the conditions can
change the direction of a reversible reaction for:
(a) the effect of heat on hydrated compounds
(b) the addition of water to anhydrous
compounds
limited to copper(II) sulfate and
cobalt(II) chloride
Supplement
3 State that a reversible reaction in a closed system
is at equilibrium when:
(a) the rate of the forward reaction is equal to
the rate of the reverse reaction
(b) the concentrations of reactants and products
are no longer changing
4 Predict and explain, for a reversible reaction, how
the position of equilibrium is affected by:
(a) changing temperature
(b) changing pressure
(c) changing concentration
(d) using a catalyst
using information provided
5 State the symbol equation for the production of
ammonia in the Haber process,
N2(g) + 3H2(g) ⇌ 2NH3(g)
6 State the sources of the hydrogen (methane) and
nitrogen (air) in the Haber process
7 State the typical conditions in the Haber process
as 450°C, 20000kPa /200atm and an iron
catalyst
8 State the symbol equation for the conversion of
sulfur dioxide to sulfur trioxide in the Contact
process, 2SO2(g) + O2(g) ⇌ 2SO3(g)
9 State the sources of the sulfur dioxide (burning
sulfur or roasting sulfide ores) and oxygen (air) in
the Contact process
10 State the typical conditions for the conversion
of sulfur dioxide to sulfur trioxide in the Contact
process as 450°C, 200kPa /2atm and a
vanadium(V) oxide catalyst
11 Explain, in terms of rate of reaction and position
of equilibrium, why the typical conditions stated
are used in the Haber process and in the Contact
process, including safety considerations and
economics
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 19
6.4 Redox
Core
1 Use a Roman numeral to indicate the oxidation
number of an element in a compound
2 Define redox reactions as involving simultaneous
oxidation and reduction
3 Define oxidation as gain of oxygen and reduction
as loss of oxygen
4 Identify redox reactions as reactions involving
gain and loss of oxygen
5 Identify oxidation and reduction in redox
reactions
Supplement
6 Define oxidation in terms of:
(a) loss of electrons
(b) an increase in oxidation number
7 Define reduction in terms of:
(a) gain of electrons
(b) a decrease in oxidation number
8 Identify redox reactions as reactions involving
gain and loss of electrons
9 Identify redox reactions by changes in oxidation
number using:
(a) the oxidation number of elements in their
uncombined state is zero
(b) the oxidation number of a monatomic ion is
the same as the charge on the ion
(c) the sum of the oxidation numbers in a
compound is zero
(d) the sum of the oxidation numbers in an ion is
equal to the charge on the ion
10 Identify redox reactions by the colour changes
involved when using acidified aqueous potassium
manganate(VII) or aqueous potassium iodide
11 Define an oxidising agent as a substance that
oxidises another substance and is itself reduced
12 Define a reducing agent as a substance that
reduces another substance and is itself oxidised
13 Identify oxidising agents and reducing agents in
redox reactions"""

text7 = """
7 Acids, bases and salts
7.1 The characteristic properties of acids and bases
Core
1 Describe the characteristic properties of acids in
terms of their reactions with:
(a) metals
(b) bases
(c) carbonates
2 Describe acids in terms of their effect on:
(a) litmus
(b) thymolphthalein
(c) methyl orange
3 State that bases are oxides or hydroxides of
metals and that alkalis are soluble bases
4 Describe the characteristic properties of bases in
terms of their reactions with:
(a) acids
(b) ammonium salts
5 Describe alkalis in terms of their effect on:
(a) litmus
(b) thymolphthalein
(c) methyl orange
6 State that aqueous solutions of acids contain H+
ions and aqueous solutions of alkalis contain OH–
ions
7 Describe how to compare hydrogen ion
concentration, neutrality, relative acidity and
relative alkalinity in terms of colour and pH using
universal indicator paper
8 Describe the neutralisation reaction between an
acid and an alkali to produce water,
H+ (aq) + OH–
(aq) → H2O(l)
Supplement
9 Define acids as proton donors and bases as
proton acceptors
10 Define a strong acid as an acid that is completely
dissociated in aqueous solution and a weak acid
as an acid that is partially dissociated in aqueous
solution
11 State that hydrochloric acid is a strong acid,
as shown by the symbol equation,
HCl(aq) → H+
(aq) + Cl
–
(aq)
12 State that ethanoic acid is a weak acid,
as shown by the symbol equation,
CH3COOH(aq) ⇌ H+
(aq) + CH3COO–
(aq)
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 21
7.2 Oxides
Core
1 Classify oxides as acidic, including SO2 and CO2,
or basic, including CuO and CaO, related to
metallic and non-metallic character
Supplement
2 Describe amphoteric oxides as oxides that react
with acids and with bases to produce a salt and
water
3 Classify Al 2O3 and ZnO as amphoteric oxides
7.3 Preparation of salts
Core
1 Describe the preparation, separation and
purification of soluble salts by reaction of an acid
with:
(a) an alkali by titration
(b) excess metal
(c) excess insoluble base
(d) excess insoluble carbonate
2 Describe the general solubility rules for salts:
(a) sodium, potassium and ammonium salts are
soluble
(b) nitrates are soluble
(c) chlorides are soluble, except lead and silver
(d) sulfates are soluble, except barium, calcium
and lead
(e) carbonates are insoluble, except sodium,
potassium and ammonium
(f) hydroxides are insoluble, except sodium,
potassium, ammonium and
calcium (partially)
3 Define a hydrated substance as a substance
that is chemically combined with water and an
anhydrous substance as a substance containing
no water
Supplement
4 Describe the preparation of insoluble salts by
precipitation
5 Define the term water of crystallisation as the
water molecules present in hydrated crystals,
including CuSO4•5H2O and CoCl 2•6H2O
"""

text8 = """
ge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
22 www.cambridgeinternational.org/igcse Back to contents page
8 The Periodic Table
8.1 Arrangement of elements
Core
1 Describe the Periodic Table as an arrangement of
elements in periods and groups and in order of
increasing proton number/ atomic number
2 Describe the change from metallic to
non-metallic character across a period
3 Describe the relationship between group number
and the charge of the ions formed from elements
in that group
4 Explain similarities in the chemical properties of
elements in the same group of the Periodic Table
in terms of their electronic configuration
5 Explain how the position of an element in
the Periodic Table can be used to predict its
properties
Supplement
6 Identify trends in groups, given information
about the elements
8.2 Group I properties
Core
1 Describe the Group I alkali metals, lithium,
sodium and potassium, as relatively soft metals
with general trends down the group, limited to:
(a) decreasing melting point
(b) increasing density
(c) increasing reactivity
2 Predict the properties of other elements in
Group I, given information about the elements
Supplement
8.3 Group VII properties
Core
1 Describe the Group VII halogens, chlorine,
bromine and iodine, as diatomic non-metals with
general trends down the group, limited to:
(a) increasing density
(b) decreasing reactivity
2 State the appearance of the halogens at r.t.p. as:
(a) chlorine, a pale yellow-green gas
(b) bromine, a red-brown liquid
(c) iodine, a grey-black solid
3 Describe and explain the displacement reactions
of halogens with other halide ions
4 Predict the properties of other elements in
Group VII, given information about the elements
Supplement
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 23
8.4 Transition elements
Core
1 Describe the transition elements as metals that:
(a) have high densities
(b) have high melting points
(c) form coloured compounds
(d) often act as catalysts as elements and in
compounds
Supplement
2 Describe transition elements as having ions with
variable oxidation numbers, including iron(II) and
iron(III)
8.5 Noble gases
Core
1 Describe the Group VIII noble gases as
unreactive, monatomic gases and explain this in
terms of electronic configuration"""

text9 = """
9 Metals
9.1 Properties of metals
Core
1 Compare the general physical properties of
metals and non-metals, including:
(a) thermal conductivity
(b) electrical conductivity
(c) malleability and ductility
(d) melting points and boiling points
2 Describe the general chemical properties of
metals, limited to their reactions with:
(a) dilute acids
(b) cold water and steam
(c) oxygen
Supplement
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
24 www.cambridgeinternational.org/igcse Back to contents page
9.2 Uses of metals
Core
1 Describe the uses of metals in terms of their
physical properties, including:
(a) aluminium in the manufacture of aircraft
because of its low density
(b) aluminium in the manufacture of overhead
electrical cables because of its low density
and good electrical conductivity
(c) aluminium in food containers because of its
resistance to corrosion
(d) copper in electrical wiring because of its good
electrical conductivity and ductility
Supplement
9.3 Alloys and their properties
Core
1 Describe an alloy as a mixture of a metal with
other elements, including:
(a) brass as a mixture of copper and zinc
(b) stainless steel as a mixture of iron and other
elements such as chromium, nickel and
carbon
2 State that alloys can be harder and stronger than
the pure metals and are more useful
3 Describe the uses of alloys in terms of their
physical properties, including stainless steel in
cutlery because of its hardness and resistance to
rusting
4 Identify representations of alloys from diagrams
of structure
Supplement
5 Explain in terms of structure how alloys can
be harder and stronger than the pure metals
because the different sized atoms in alloys mean
the layers can no longer slide over each other
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 25
9.4 Reactivity series
Core
1 State the order of the reactivity series as:
potassium, sodium, calcium, magnesium,
aluminium, carbon, zinc, iron, hydrogen, copper,
silver, gold
2 Describe the reactions, if any, of:
(a) potassium, sodium and calcium with
cold water
(b) magnesium with steam
(c) magnesium, zinc, iron, copper, silver and gold
with dilute hydrochloric acid
and explain these reactions in terms of the
position of the metals in the reactivity series
3 Deduce an order of reactivity from a given set of
experimental results
Supplement
4 Describe the relative reactivities of metals in
terms of their tendency to form positive ions, by
displacement reactions, if any, with the aqueous
ions of magnesium, zinc, iron, copper and silver
5 Explain the apparent unreactivity of aluminium in
terms of its oxide layer
9.5 Corrosion of metals
Core
1 State the conditions required for the rusting of
iron and steel to form hydrated iron(III) oxide
2 State some common barrier methods, including
painting, greasing and coating with plastic
3 Describe how barrier methods prevent rusting by
excluding oxygen or water
Supplement
4 Describe the use of zinc in galvanising as an
example of a barrier method and sacrificial
protection
5 Explain sacrificial protection in terms of the
reactivity series and in terms of electron loss
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
26 www.cambridgeinternational.org/igcse Back to contents page
9.6 Extraction of metals
Core
1 Describe the ease in obtaining metals from their
ores, related to the position of the metal in the
reactivity series
2 Describe the extraction of iron from hematite in
the blast furnace, limited to:
(a) the burning of carbon (coke) to provide heat
and produce carbon dioxide
(b) the reduction of carbon dioxide to carbon
monoxide
(c) the reduction of iron(III) oxide by carbon
monoxide
(d) the thermal decomposition of calcium
carbonate /limestone to produce calcium
oxide
(e) the formation of slag
Symbol equations are not required
3 State that the main ore of aluminium is bauxite
and that aluminium is extracted by electrolysis
Supplement
4 State the symbol equations for the extraction of
iron from hematite
(a) C + O2 → CO2
(b) C + CO2 → 2CO
(c) Fe2O3 + 3CO → 2Fe + 3CO2
(d) CaCO3 → CaO + CO2
(e) CaO + SiO2 → CaSiO3
5 Describe the extraction of aluminium from
purified bauxite / aluminium oxide, including:
(a) the role of cryolite
(b) why the carbon anodes need to be regularly
replaced
(c) the reactions at the electrodes, including
ionic half-equations
Details of the purification of bauxite are not
required"""

text10 = """
10 Chemistry of the environment
10.1 Water
Core
1 Describe chemical tests for the presence of
water using anhydrous cobalt(II) chloride and
anhydrous copper(II) sulfate
2 Describe how to test for the purity of water using
melting point and boiling point
3 Explain that distilled water is used in practical
chemistry rather than tap water because it
contains fewer chemical impurities
4 State that water from natural sources may
contain substances, including:
(a) dissolved oxygen
(b) metal compounds
(c) plastics
(d) sewage
(e) harmful microbes
(f) nitrates from fertilisers
(g) phosphates from fertilisers and detergents
5 State that some of these substances are
beneficial, including:
(a) dissolved oxygen for aquatic life
(b) some metal compounds provide essential
minerals for life
6 State that some of these substances are
potentially harmful, including:
(a) some metal compounds are toxic
(b) some plastics harm aquatic life
(c) sewage contains harmful microbes which
cause disease
(d) nitrates and phosphates lead to
deoxygenation of water and damage to
aquatic life
Details of the eutrophication process are not
required
7 Describe the treatment of the domestic water
supply in terms of:
(a) sedimentation and filtration to remove solids
(b) use of carbon to remove tastes and odours
(c) chlorination to kill microbes
Supplement
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
28 www.cambridgeinternational.org/igcse Back to contents page
10.2 Fertilisers
Core
1 State that ammonium salts and nitrates are used
as fertilisers
2 Describe the use of NPK fertilisers to provide the
elements nitrogen, phosphorus and potassium
for improved plant growth
Supplement
10.3 Air quality and climate
Core
1 State the composition of clean, dry air as
approximately 78% nitrogen, N2
, 21% oxygen, O2
and the remainder as a mixture of noble gases
and carbon dioxide, CO2
2 State the source of each of these air pollutants,
limited to:
(a) carbon dioxide from the complete
combustion of carbon-containing fuels
(b) carbon monoxide and particulates from the
incomplete combustion of carbon-containing
fuels
(c) methane from the decomposition of
vegetation and waste gases from digestion in
animals
(d) oxides of nitrogen from car engines
(e) sulfur dioxide from the combustion of fossil
fuels which contain sulfur compounds
3 State the adverse effect of these air pollutants,
limited to:
(a) carbon dioxide: higher levels of carbon
dioxide leading to increased global warming,
which leads to climate change
(b) carbon monoxide: toxic gas
(c) particulates: increased risk of respiratory
problems and cancer
(d) methane: higher levels of methane leading
to increased global warming, which leads to
climate change
(e) oxides of nitrogen: acid rain, photochemical
smog and respiratory problems
(f) sulfur dioxide: acid rain
Supplement
7 Describe how the greenhouse gases carbon
dioxide and methane cause global warming,
limited to:
(a) the absorption, reflection and emission of
thermal energy
(b) reducing thermal energy loss to space
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 29
10.3 Air quality and climate continued
Core
4 State and explain strategies to reduce the effects
of these environmental issues, limited to:
(a) climate change: planting trees, reduction
in livestock farming, decreasing use of
fossil fuels, increasing use of hydrogen and
renewable energy, e.g. wind, solar
(b) acid rain: use of catalytic converters in
vehicles, reducing emissions of sulfur dioxide
by using low-sulfur fuels and flue gas
desulfurisation with calcium oxide
5 Describe photosynthesis as the reaction between
carbon dioxide and water to produce glucose and
oxygen in the presence of chlorophyll and using
energy from light
6 State the word equation for photosynthesis,
carbon dioxide + water → glucose + oxygen
Supplement
8 Explain how oxides of nitrogen form in car
engines and describe their removal by catalytic
converters, e.g. 2CO + 2NO → 2CO2 + N2
9 State the symbol equation for photosynthesis,
6CO2 + 6H2O → C6H12O6 + 6O2"""

text11 = """
11 Organic chemistry
11.1 Formulae, functional groups and terminology
Core
1 Draw and interpret the displayed formula of a
molecule to show all the atoms and all the bonds
2 Write and interpret general formulae of
compounds in the same homologous series,
limited to:
(a) alkanes, Cn
H2n+2
(b) alkenes, Cn
H2n
(c) alcohols, Cn
H2n+1OH
(d) carboxylic acids, Cn
H2n+1COOH
3 Identify a functional group as an atom or group
of atoms that determine the chemical properties
of a homologous series
Supplement
7 State that a structural formula is an
unambiguous description of the way the atoms
in a molecule are arranged, including CH2=CH2,
CH3CH2OH, CH3COOCH3
8 Define structural isomers as compounds with the
same molecular formula, but different structural
formulae, including C4H10 as CH3CH2CH2CH3 and
CH3CH(CH3)CH3 and C4H8 as CH3CH2CH=CH2
and CH3CH=CHCH3
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
30 www.cambridgeinternational.org/igcse Back to contents page
11.1 Formulae, functional groups and terminology continued
Core
4 State that a homologous series is a family
of similar compounds with similar chemical
properties due to the presence of the same
functional group
5 State that a saturated compound has molecules
in which all carbon–carbon bonds are single
bonds
6 State that an unsaturated compound has
molecules in which one or more carbon–carbon
bonds are not single bonds
Supplement
9 Describe the general characteristics of a
homologous series as:
(a) having the same functional group
(b) having the same general formula
(c) differing from one member to the next by
a –CH2– unit
(d) displaying a trend in physical properties
(e) sharing similar chemical properties
11.2 Naming organic compounds
Core
1 Name and draw the displayed formulae of:
(a) methane and ethane
(b) ethene
(c) ethanol
(d) ethanoic acid
(e) the products of the reactions stated in
sections 11.4–11.7
2 State the type of compound present, given a
chemical name ending in -ane, -ene, -ol, or
-oic acid or from a molecular formula or
displayed formula
Supplement
3 Name and draw the structural and displayed
formulae of unbranched:
(a) alkanes
(b) alkenes, including
but-1-ene and but-2-ene
(c) alcohols, including
propan-1-ol, propan-2-ol, butan-1-ol and
butan-2-ol
(d) carboxylic acids
containing up to four carbon atoms per molecule
4 Name and draw the displayed formulae of the
unbranched esters which can be made from
unbranched alcohols and carboxylic acids, each
containing up to four carbon atoms
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 31
11.3 Fuels
Core
1 Name the fossil fuels: coal, natural gas and
petroleum
2 Name methane as the main constituent of
natural gas
3 State that hydrocarbons are compounds that
contain hydrogen and carbon only
4 State that petroleum is a mixture of
hydrocarbons
5 Describe the separation of petroleum into useful
fractions by fractional distillation
6 Describe how the properties of fractions obtained
from petroleum change from the bottom to the
top of the fractionating column, limited to:
(a) decreasing chain length
(b) higher volatility
(c) lower boiling points
(d) lower viscosity
7 Name the uses of the fractions as:
(a) refinery gas fraction for gas used in heating
and cooking
(b) gasoline /petrol fraction for fuel used in cars
(c) naphtha fraction as a chemical feedstock
(d) kerosene /paraffin fraction for jet fuel
(e) diesel oil/ gas oil fraction for fuel used in
diesel engines
(f) fuel oil fraction for fuel used in ships and
home heating systems
(g) lubricating oil fraction for lubricants, waxes
and polishes
(h) bitumen fraction for making roads
Supplement
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
32 www.cambridgeinternational.org/igcse Back to contents page
11.4 Alkanes
Core
1 State that the bonding in alkanes is single
covalent and that alkanes are saturated
hydrocarbons
2 Describe the properties of alkanes as being
generally unreactive, except in terms of
combustion and substitution by chlorine
Supplement
3 State that in a substitution reaction one atom or
group of atoms is replaced by another atom or
group of atoms
4 Describe the substitution reaction of alkanes
with chlorine as a photochemical reaction, with
ultraviolet light providing the activation energy,
Ea
, and draw the structural or displayed formulae
of the products, limited to monosubstitution
11.5 Alkenes
Core
1 State that the bonding in alkenes includes a
double carbon–carbon covalent bond and that
alkenes are unsaturated hydrocarbons
2 Describe the manufacture of alkenes and
hydrogen by the cracking of larger alkane
molecules using a high temperature and a
catalyst
3 Describe the reasons for the cracking of larger
alkane molecules
4 Describe the test to distinguish between
saturated and unsaturated hydrocarbons by their
reaction with aqueous bromine
Supplement
5 State that in an addition reaction only one
product is formed
6 Describe the properties of alkenes in terms of
addition reactions with:
(a) bromine or aqueous bromine
(b) hydrogen in the presence of a nickel catalyst
(c) steam in the presence of an acid catalyst
and draw the structural or displayed formulae of
the products
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 33
11.6 Alcohols
Core
1 Describe the manufacture of ethanol by:
(a) fermentation of aqueous glucose at 25–35°C
in the presence of yeast and in the absence of
oxygen
(b) catalytic addition of steam to ethene
at 300°C and 6000kPa /60 atm in the
presence of an acid catalyst
2 Describe the combustion of ethanol
3 State the uses of ethanol as:
(a) a solvent
(b) a fuel
Supplement
4 Describe the advantages and disadvantages of
the manufacture of ethanol by:
(a) fermentation
(b) catalytic addition of steam to ethene
11.7 Carboxylic acids
Core
1 Describe the reaction of ethanoic acid with:
(a) metals
(b) bases
(c) carbonates
including names and formulae of the salts
produced
Supplement
2 Describe the formation of ethanoic acid by the
oxidation of ethanol:
(a) with acidified aqueous potassium
manganate(VII)
(b) by bacterial oxidation during vinegar
production
3 Describe the reaction of a carboxylic acid with an
alcohol using an acid catalyst to form an ester
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
34 www.cambridgeinternational.org/igcse Back to contents page
11.8 Polymers
Core
1 Define polymers as large molecules built up from
many smaller molecules called monomers
2 Describe the formation of poly(ethene) as an
example of addition polymerisation using ethene
monomers
3 State that plastics are made from polymers
4 Describe how the properties of plastics have
implications for their disposal
5 Describe the environmental challenges caused by
plastics, limited to:
(a) disposal in land fill sites
(b) accumulation in oceans
(c) formation of toxic gases from burning
Supplement
6 Identify the repeat units and/or linkages in
addition polymers and in condensation polymers
7 Deduce the structure or repeat unit of an
addition polymer from a given alkene and vice
versa
8 Deduce the structure or repeat unit of a
condensation polymer from given monomers and
vice versa, limited to:
(a) polyamides from a dicarboxylic acid and a
diamine
(b) polyesters from a dicarboxylic acid and a diol
9 Describe the differences between addition and
condensation polymerisation
10 Describe and draw the structure of:
(a) nylon, a polyamide
The full name for PET, polyethylene
terephthalate, is not required
11 State that PET can be converted back into
monomers and re-polymerised
12 Describe proteins as natural polyamides and that
they are formed from amino acid monomers with
the general structure:
where R represents different types of side chain
13 Describe and draw the structure of proteins as:
"""

text12 = """
12 Experimental techniques and chemical analysis
12.1 Experimental design
Core
1 Name appropriate apparatus for the
measurement of time, temperature, mass and
volume, including:
(a) stopwatches
(b) thermometers
(c) balances
(d) burettes
(e) volumetric pipettes
(f) measuring cylinders
(g) gas syringes
2 Suggest advantages and disadvantages of
experimental methods and apparatus
3 Describe a:
(a) solvent as a substance that dissolves a solute
(b) solute as a substance that is dissolved in a
solvent
(c) solution as a mixture of one or more solutes
dissolved in a solvent
(d) saturated solution as a solution containing
the maximum concentration of a solute
dissolved in the solvent at a specified
temperature
(e) residue as a substance that remains after
evaporation, distillation, filtration or any
similar process
(f) filtrate as a liquid or solution that has passed
through a filter
Supplement
12.2 Acid–base titrations
Core
1 Describe an acid–base titration to include the use
of a:
(a) burette
(b) volumetric pipette
(c) suitable indicator
2 Describe how to identify the end-point of a
titration using an indicator
Supplement
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
36 www.cambridgeinternational.org/igcse Back to contents page
12.3 Chromatography
Core
1 Describe how paper chromatography is used to
separate mixtures of soluble coloured substances,
using a suitable solvent
2 Interpret simple chromatograms to identify:
(a) unknown substances by comparison with
known substances
(b) pure and impure substances
Supplement
3 Describe how paper chromatography is used
to separate mixtures of soluble colourless
substances, using a suitable solvent and a
locating agent
Knowledge of specific locating agents is not
required
4 State and use the equation for Rf
:
Rf
 = distance travelled by substance
distance travelled by solvent
12.4 Separation and purification
Core
1 Describe and explain methods of separation and
purification using:
(a) a suitable solvent
(b) filtration
(c) crystallisation
(d) simple distillation
(e) fractional distillation
2 Suggest suitable separation and purification
techniques, given information about the
substances involved
3 Identify substances and assess their purity using
melting point and boiling point information
Supplement
12.5 Identification of ions and gases
Core
1 Describe tests to identify the anions:
(a) carbonate, CO3
2–, by reaction with dilute acid
and then testing for carbon dioxide gas
(b) chloride, Cl
–
, bromide, Br –
, and iodide, I –
, by
acidifying with dilute nitric acid then adding
aqueous silver nitrate
(c) nitrate, NO3
–
, reduction with aluminium foil
and aqueous sodium hydroxide and then
testing for ammonia gas
(d) sulfate, SO4
2–, by acidifying with dilute nitric
acid and then adding aqueous barium nitrate
(e) sulfite, SO3
2–, by reaction with acidified
aqueous potassium manganate(VII)
Supplement
Cambridge IGCSE Chemistry 0620 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 37
12.5 Identification of ions and gases continued
Core
2 Describe tests using aqueous sodium hydroxide
and aqueous ammonia to identify the aqueous
cations:
(a) aluminium, Al
3+
(b) ammonium, NH4
+
(c) calcium, Ca2+
(d) chromium(III), Cr3+
(e) copper(II), Cu2+
(f) iron(II), Fe2+
(g) iron(III), Fe3+
(h) zinc, Zn2+
3 Describe tests to identify the gases:
(a) ammonia, NH3, using damp red litmus paper
(b) carbon dioxide, CO2, using limewater
(c) chlorine, Cl 2, using damp litmus paper
(d) hydrogen, H2, using a lighted splint
(e) oxygen, O2, using a glowing splint
(f) sulfur dioxide, SO2, using acidified aqueous
potassium manganate(VII)
4 Describe the use of a flame test to identify the
cations:
(a) lithium, Li+
(b) sodium, Na+
(c) potassium, K+
(d) calcium, Ca2+
(e) barium, Ba2+
(f) copper(II), Cu2+"""


textarr = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12]
for i in range(len(textarr)):
    textarr[i] = getFormattedTextfromPdf.formatText(textarr[i])

trainModels.train(textarr, allLabels)
