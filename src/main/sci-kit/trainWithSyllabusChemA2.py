import trainModels
import getFormattedTextfromPdf


allLabels = ['Chemical energetics', 'Electrochemistry', 
             'Equilibria', 'Reaction kinetics', 'Group 2', 'Chemistry of transition elements', 'An introduction to A Level organic chemistry',
               'Hydrocarbons', 'Halogen compounds', 'Hydroxy compounds', 'Carboxylic acids and derivatives','Nitrogen compounds',
               'Polymerisation','Organic synthesis','Analytical techniques']


text = """
 23 Chemical energetics
 23.1  Lattice energy and Born-Haber cycles
 Learning outcomes
 Candidates should be able to:
 1  define and use the terms: 
(a) enthalpy change of atomisation, ΔHat
 (b) lattice energy, ΔHlatt
 (the change from gas phase ions to solid lattice)
 2 (a) define and use the term first electron affinity, EA
 (b) explain the factors affecting the electron affinities of elements
 (c) describe and explain the trends in the electron affinities of the Group 16 and Group 17 elements 
3 construct and use Born–Haber cycles for ionic solids 
 (limited to +1 and +2 cations, –1 and –2 anions) 
4 carry out calculations involving Born–Haber cycles
 5 explain, in qualitative terms, the effect of ionic charge and of ionic radius on the numerical magnitude of a 
lattice energy 
23.2 Enthalpies of solution and hydration 
Learning outcomes
 Candidates should be able to:
 1  define and use the term enthalpy change with reference to hydration, ΔHhyd
 , and solution, ΔHsol
 
2 construct and use an energy cycle involving enthalpy change of solution, lattice energy and enthalpy change 
of hydration
 3 carry out calculations involving the energy cycles in 23.2.2
 4 explain, in qualitative terms, the effect of ionic charge and of ionic radius on the numerical magnitude of an 
enthalpy change of hydration  
23.3  Entropy change, ΔS
 Learning outcomes
 Candidates should be able to:
 1 define the term entropy, S, as the number of possible arrangements of the particles and their energy in a 
given system 
2 predict and explain the sign of the entropy changes that occur: 
(a) during a change in state, e.g. melting, boiling and dissolving (and their reverse)
 (b) during a temperature change 
(c) during a reaction in which there is a change in the number of gaseous molecules
 3 calculate the entropy change for a reaction, ΔS, given the standard entropies, S⦵, of the reactants and 
products, ΔS⦵ = ΣS⦵ (products) – ΣS⦵ (reactants)
 (use of ΔS⦵ = ΔSsurr⦵ + ΔSsys⦵ is not required)
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content  
36 www.cambridgeinternational.org/alevel Back to contents page
 23.4  Gibbs free energy change, ΔG 
Learning outcomes
 Candidates should be able to:
 1 state and use the Gibbs equation ΔG⦵ = ΔH⦵ – TΔS⦵
 2 perform calculations using the equation ΔG⦵ = ΔH⦵ – TΔS⦵
 3 state whether a reaction or process will be feasible by using the sign of ΔG
 4 predict the effect of temperature change on the feasibility of a reaction, given standard enthalpy and 
entropy changes
"""

text2 = """
 24 Electrochemistry
 24.1  Electrolysis
 Learning outcomes
 Candidates should be able to:
 1 predict the identities of substances liberated during electrolysis from the state of electrolyte (molten or 
aqueous), position in the redox series (electrode potential) and concentration 
2 state and apply the relationship F = Le between the Faraday constant, F, the Avogadro constant, L, and the 
charge on the electron, e
 3 calculate:
 (a) the quantity of charge passed during electrolysis, using Q = It
 (b) the mass and/or volume of substance liberated during electrolysis
 4 describe the determination of a value of the Avogadro constant by an electrolytic method
 24.2  Standard electrode potentials E⦵; standard cell potentials E⦵
 cell
 and the Nernst equation
 Learning outcomes
 Candidates should be able to:
 1 define the terms:
 (a) standard electrode (reduction) potential
 (b) standard cell potential
 2 describe the standard hydrogen electrode
 3 describe methods used to measure the standard electrode potentials of:
 (a) metals or non-metals in contact with their ions in aqueous solution
 (b) ions of the same element in different oxidation states
 4 calculate a standard cell potential by combining two standard electrode potentials 
5 use standard cell potentials to:
 (a)  deduce the polarity of each electrode and hence explain/deduce the direction of electron flow in the 
external circuit of a simple cell
 (b) predict the feasibility of a reaction
 6 deduce from E⦵ values the relative reactivity of elements, compounds and ions as oxidising agents or as 
reducing agents 
7 construct redox equations using the relevant half-equations 
(continued)
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content  
24.2   Standard electrode potentials E⦵; standard cell potentials E⦵
 cell
 and the Nernst equation (continued)
 Learning outcomes
 Candidates should be able to:
 8 predict qualitatively how the value of an electrode potential, E, varies with the concentrations of the 
aqueous ions
 9 use the Nernst equation, e.g. E = E⦵ + (0.059/z) log [oxidised species]
 [reduced species]
 to predict quantitatively how the value of an electrode potential varies with the concentrations of the 
aqueous ions; examples include Cu2+(aq) + 2e–⇌ Cu(s), Fe3+(aq) + e– ⇌ Fe2+(aq)
 10 understand and use the equation ΔG⦵ = –nE⦵
 cell
 F
"""

text3 = """
 25 
Equilibria
 25.1  Acids and bases
 Learning outcomes
 Candidates should be able to:
 1 understand and use the terms conjugate acid and conjugate base
 2 define conjugate acid–base pairs, identifying such pairs in reactions  
3 define mathematically the terms pH, Ka
 , pKa
 and Kw
 and use them in calculations (Kb
 and the equation  
Kw
 = Ka
 × Kb
 will not be tested)
 4 calculate [H+(aq)] and pH values for:
 (a) strong acids 
(b) strong alkalis
 (c) weak acids 
5 (a) define a buffer solution 
(b) explain how a buffer solution can be made
 (c) explain how buffer solutions control pH; use chemical equations in these explanations
 (d) describe and explain the uses of buffer solutions, including the role of HCO3– in controlling pH in blood  
6 calculate the pH of buffer solutions, given appropriate data
 7 understand and use the term solubility product, Ksp
 8 write an expression for Ksp
 9 calculate Ksp
 from concentrations and vice versa
 10 (a)  understand and use the common ion effect to explain the different solubility of a compound in a 
solution containing a common ion
 (b) perform calculations using Ksp
 values and concentration of a common ion 
25.2  Partition coefficients
 Learning outcomes
 Candidates should be able to:
 1 state what is meant by the term partition coefficient, Kpc
 2 calculate and use a partition coefficient for a system in which the solute is in the same physical state in the 
two solvents
 3 understand the factors affecting the numerical value of a partition coefficient in terms of the polarities of 
the solute and the solvents used  
"""

text4 = """
26 Reaction kinetics
 26.1  Simple rate equations, orders of reaction and rate constants
 Learning outcomes
 Candidates should be able to:
 1 explain and use the terms rate equation, order of reaction, overall order of reaction, rate constant, half-life, 
rate-determining step and intermediate
 2 (a) understand and use rate equations of the form rate = k [A]m[B]n (for which m and n are 0, 1 or 2)
 (b)  deduce the order of a reaction from concentration-time graphs or from experimental data relating to 
the initial rates method and half-life method
 (c)  interpret experimental data in graphical form, including concentration-time and rate-concentration 
graphs
 (d) calculate an initial rate using concentration data 
(e) construct a rate equation 
3 (a) show understanding that the half-life of a first-order reaction is independent of concentration
 (b) use the half-life of a first-order reaction in calculations
 4 calculate the numerical value of a rate constant, for example by:
 (a) using the initial rates and the rate equation 
(b) using the half-life, t1/2
 , and the equation k = 0.693/t1/2
 5 for a multi-step reaction:
 (a)  suggest a reaction mechanism that is consistent with the rate equation and the equation for the overall 
reaction
 (b) predict the order that would result from a given reaction mechanism and rate-determining step
 (c) deduce a rate equation using a given reaction mechanism and rate-determining step for a given reaction 
(d) identify an intermediate or catalyst from a given reaction mechanism 
(e) identify the rate determining step from a rate equation and a given reaction mechanism  
6 describe qualitatively the effect of temperature change on the rate constant and hence the rate of a reaction
 26.2  Homogeneous and heterogeneous catalysts 
Learning outcomes
 Candidates should be able to:
 1 explain that catalysts can be homogeneous or heterogeneous 
2 describe the mode of action of a heterogeneous catalyst to include adsorption of reactants, bond weakening 
and desorption of products, for example:
 (a) iron in the Haber process
 (b)  palladium, platinum and rhodium in the catalytic removal of oxides of nitrogen from the exhaust gases 
of car engines 
3  describe the mode of action of a homogeneous catalyst by being used in one step and reformed in a later 
step, for example:
 (a) atmospheric oxides of nitrogen in the oxidation of atmospheric sulfur dioxide 
(b) Fe2+ or Fe3+ in the I–/S2
 O8
 2– reaction
"""

text5 = """
27 
Group 2
 27.1   Similarities and trends in the properties of the Group 2 metals, magnesium to barium, and their 
compounds
 Learning outcomes
 Candidates should be able to:
 1 describe and explain qualitatively the trend in the thermal stability of the nitrates and carbonates including 
the effect of ionic radius on the polarisation of the large anion 
2 describe and explain qualitatively the variation in solubility and of enthalpy change of solution, ΔH⦵
 sol
 , of the 
hydroxides and sulfates in terms of relative magnitudes of the enthalpy change of hydration and the lattice 
energy
"""

text6 = """
 28 Chemistry of transition elements
 28.1  General physical and chemical properties of the first row of transition elements, titanium to copper
 Learning outcomes
 Candidates should be able to:
 1 define a transition element as a d-block element which forms one or more stable ions with incomplete d 
orbitals
 2 sketch the shape of a 3dxy
 orbital and 3dz2
 orbital 
3 understand that transition elements have the following properties:
 (a) they have variable oxidation states 
(b) they behave as catalysts
 (c) they form complex ions
 (d) they form coloured compounds 
4 explain why transition elements have variable oxidation states in terms of the similarity in energy of the 3d 
and the 4s sub-shells 
5  
explain why transition elements behave as catalysts in terms of having more than one stable oxidation state, 
and vacant d orbitals that are energetically accessible and can form dative bonds with ligands
 6 explain why transition elements form complex ions in terms of vacant d orbitals that are energetically 
accessible 
Back to contents page
 39
 www.cambridgeinternational.org/alevel
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content  
40 www.cambridgeinternational.org/alevel Back to contents page
 28.2  General characteristic chemical properties of the first set of transition elements, titanium to copper 
Learning outcomes
 Candidates should be able to:
 1 describe and explain the reactions of transition elements with ligands to form complexes, including the 
complexes of copper(II) and cobalt(II) ions with water and ammonia molecules and hydroxide and chloride 
ions 
2 define the term ligand as a species that contains a lone pair of electrons that forms a dative covalent bond to 
a central metal atom / ion 
3 understand and use the terms 
(a) monodentate ligand including as examples H2
 O, NH3
 , Cl – and CN– 
(b)  bidentate ligand including as examples 1,2-diaminoethane, en, H2
 NCH2
 CH2
 NH2
 and the ethanedioate 
ion, C2
 O4
 2– 
(c) polydentate ligand including as an example EDTA4
4 define the term complex as a molecule or ion formed by a central metal atom / ion surrounded by one or 
more ligands 
5 describe the geometry (shape and bond angles) of transition element complexes which are linear, square 
planar, tetrahedral or octahedral 
6 (a) state what is meant by coordination number 
(b)  predict the formula and charge of a complex ion, given the metal ion, its charge or oxidation state, the 
ligand and its coordination number or geometry 
7 explain qualitatively that ligand exchange can occur, including the complexes of copper(II) ions and  
cobalt(II) ions with water and ammonia molecules and hydroxide and chloride ions
 8 predict, using E⦵ values, the feasibility of redox reactions involving transition elements and their ions 
9 describe the reactions of, and perform calculations involving: 
(a) MnO4– / C2
 O4
 2– in acid solution given suitable data  
(b) MnO4– / Fe2+ in acid solution given suitable data  
(c) Cu2+ / I– given suitable data
 10  perform calculations involving other redox systems given suitable data  
28.3  Colour of complexes 
Learning outcomes
 Candidates should be able to:
 1  define and use the terms degenerate and non-degenerate d orbitals 
2 describe the splitting of degenerate d orbitals into two non-degenerate sets of d orbitals of higher energy, 
and use of Δ E in:
 (a) octahedral complexes, two higher and three lower d orbitals
 (b) tetrahedral complexes, three higher and two lower d orbitals 
3  explain why transition elements form coloured compounds in terms of the frequency of light absorbed as an 
electron is promoted between two non-degenerate d orbitals
 4 describe, in qualitative terms, the effects of different ligands on Δ E, frequency of light absorbed, and hence 
the complementary colour that is observed
 5 use the complexes of copper(II) ions and cobalt(II) ions with water and ammonia molecules and hydroxide 
and chloride ions as examples of ligand exchange affecting the colour observed
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content  
28.4  Stereoisomerism in transition element complexes
 Learning outcomes
 Candidates should be able to:
 1 describe the types of stereoisomerism shown by complexes, including those associated with bidentate 
ligands: 
(a)  geometrical (cis-trans) isomerism, e.g. square planar such as [Pt(NH3
 )2
 Cl 2
 ] and octahedral such as 
[Co(NH3
 )4
 (H2
 O)2
 ]2+ and [Ni(H2
 NCH2
 CH2
 NH2
 )2
 (H2
 O)2
 ]2+
 (b) optical isomerism, e.g. [Ni(H2
 NCH2
 CH2
 NH2
 )3
 ]2+ and [Ni(H2
 NCH2
 CH2
 NH2
 )2
 (H2
 O)2
 ]2+
 2 deduce the overall polarity of complexes such as those described in 28.4.1(a) and 28.4.1(b)
 28.5  Stability constants, Kstab
 
Learning outcomes
 Candidates should be able to:
 1 define the stability constant, Kstab
 , of a complex as the equilibrium constant for the formation of the 
complex ion in a solvent (from its constituent ions or molecules)
 2 write an expression for a Kstab
 of a complex ([H2
 O] should not be included)
 3  
use Kstab
 expressions to perform calculations 
4 describe and explain ligand exchanges in terms of Kstab
 values and understand that a large Kstab
 is due to the 
formation of a stable complex ion
"""

text7 = """
benzene
 halogenoarene halogen
 chlorobenzene
 (when X = Cl )
 phenol phenol
 acyl chloride acyl chloride
 propanoyl chloride
 amines (secondary 
and tertiary) amine
 (naming of secondary 
and tertiary amines is 
not required)
 amide (primary, 
secondary and tertiary) amide R C NH2
 2-aminoethanoic acid
 *where a benzene ring is part of the molecule, a displayed formula would not be expected to be drawn.
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content  
43 www.cambridgeinternational.org/alevel Back to contents page
 29.1  Formulae, functional groups and the naming of organic compounds 
Learning outcomes
 Candidates should be able to:
 1 understand that the compounds in the table on page 42 contain a functional group which dictates their 
physical and chemical properties 
2 interpret and use the general, structural, displayed and skeletal formulae of the classes of compound stated 
in the table on page 42
 3 understand and use systematic nomenclature of simple aliphatic organic molecules (including cyclic 
compounds containing a single ring of up to six carbon atoms) with functional groups detailed in the table 
on page 42, up to six carbon atoms (six plus six for esters and amides, straight chains only for esters and 
nitriles)  
4 understand and use systematic nomenclature of simple aromatic molecules with one benzene ring and one 
or more simple substituents, for example 3-nitrobenzoic acid or 2,4,6-tribromophenol
 29.2  Characteristic organic reactions
 Learning outcomes
 Candidates should be able to:
 1 understand and use the following terminology associated with types of organic mechanisms:
 (a) electrophilic substitution 
(b) addition-elimination 
29.3  Shapes of aromatic organic molecules; σ and π bonds
 Learning outcomes
 Candidates should be able to:
 1 describe and explain the shape of benzene and other aromatic molecules, including sp2 hybridisation, in 
terms of σ bonds and a delocalised π system 
29.4  Isomerism: optical
 Learning outcomes
 Candidates should be able to:
 1  understand that enantiomers have identical physical and chemical properties apart from their ability to 
rotate plane polarised light and their potential biological activity 
2 understand and use the terms optically active and racemic mixture 
3 describe the effect on plane polarised light of the two optical isomers of a single substance 
4 explain the relevance of chirality to the synthetic preparation of drug molecules including:
 (a) the potential different biological activity of the two enantiomers 
(b) the need to separate a racemic mixture into two pure enantiomers 
(c) the use of chiral catalysts to produce a single pure optical isomer 
(Candidates should appreciate that compounds can contain more than one chiral centre, but knowledge of 
meso compounds and nomenclature such as diastereoisomers is not required.)
"""

text8 = """
30 Hydrocarbons
 30.1  Arenes
 Learning outcomes
 Candidates should be able to:
 1 describe the chemistry of arenes as exemplified by the following reactions of benzene and methylbenzene:
 (a)  substitution reactions with Cl 2
 and with Br2
 in the presence of a catalyst, AlCl 3
 or Al Br3
 , to form 
halogenoarenes (aryl halides)
 (b)  nitration with a mixture of concentrated HNO3
 and concentrated H2
 SO4
 at a temperature between  
25 °C and 60 °C
 (c) Friedel–Crafts alkylation by CH3
 Cl and AlCl 3
 and heat
 (d) Friedel–Crafts acylation by CH3
 COCl and AlCl 3
 and heat
 (e)  complete oxidation of the side-chain using hot alkaline KMnO4
 and then dilute acid to give a benzoic 
acid
 (f) hydrogenation of the benzene ring using H2
 and Pt/Ni catalyst and heat to form a cyclohexane ring 
2 describe the mechanism of electrophilic substitution in arenes:
 (a) as exemplified by the formation of nitrobenzene and bromobenzene
 (b) with regards to the effect of delocalisation (aromatic stabilisation) of electrons in arenes to explain the 
predomination of substitution over addition
 3 predict whether halogenation will occur in the side-chain or in the aromatic ring in arenes depending on 
reaction conditions
 4 describe that in the electrophilic substitution of arenes, different substituents direct to different ring 
positions (limited to the directing effects of –NH2
 , –OH, –R, –NO2
 , –COOH and –COR)
"""

text9 = """
 31 Halogen compounds
 31.1  Halogen compounds
 Learning outcomes
 Candidates should be able to:
 1  recall the reactions by which halogenoarenes can be produced: substitution of an arene with Cl2
 or Br2
 
in the presence of a catalyst, Al Cl3
 or Al Br3
 to form a halogenoarene, exemplified by benzene to form 
chlorobenzene and methylbenzene to form 2-chloromethylbenzene and 4-chloromethylbenzene
 2  explain the difference in reactivity between a halogenoalkane and a halogenoarene as exemplified by 
chloroethane and chlorobenzene
"""

text10 = """
 32 Hydroxy compounds
 32.1  Alcohols
 Learning outcomes
 Candidates should be able to:
 1  describe the reaction with acyl chlorides to form esters using ethyl ethanoate 
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content  
32.2  Phenol
 Learning outcomes
 Candidates should be able to:
 1 recall the reactions (reagents and conditions) by which phenol can be produced: 
(a)  reaction of phenylamine with HNO2
 or NaNO2
 and dilute acid below 10 °C to produce the diazonium 
salt; further warming of the diazonium salt with H2
 O to give phenol
 2 recall the chemistry of phenol, as exemplified by the following reactions:
 (a) with bases, for example NaOH(aq) to produce sodium phenoxide
 (b) with Na(s) to produce sodium phenoxide and H2
 (g)
 (c) in NaOH(aq) with diazonium salts, to give azo compounds
 (d)  nitration of the aromatic ring with dilute HNO3
 (aq) at room temperature to give a mixture of 
2-nitrophenol and 4-nitrophenol
 (e) bromination of the aromatic ring with Br2
 (aq) to form 2,4,6-tribromophenol
 3 explain the acidity of phenol
 4 describe and explain the relative acidities of water, phenol and ethanol
 5  
explain why the reagents and conditions for the nitration and bromination of phenol are different from those 
for benzene
 6  
recall that the hydroxyl group of a phenol directs to the 2-, 4- and 6-positions
 7 apply knowledge of the reactions of phenol to those of other phenolic compounds, e.g. naphthol
"""
text11 = """
 33 Carboxylic acids and derivatives
 33.1  Carboxylic acids
 Learning outcomes
 Candidates should be able to:
 1 recall the reaction by which benzoic acid can be produced:
 (a)  reaction of an alkylbenzene with hot alkaline KMnO4
 and then dilute acid, exemplified by 
methylbenzene
 2 describe the reaction of carboxylic acids with PCl 3
 and heat, PCl 5
 , or SOCl 2
 to form acyl chlorides
 3 recognise that some carboxylic acids can be further oxidised:
 (a)  the oxidation of methanoic acid, HCOOH, with Fehling’s reagent or Tollens’ reagent or acidified KMnO4
 
or acidified K2
 Cr2
 O7
 to carbon dioxide and water
 (b) the oxidation of ethanedioic acid, HOOCCOOH, with warm acidified KMnO4
 to carbon dioxide
 4 describe and explain the relative acidities of carboxylic acids, phenols and alcohols
 5 describe and explain the relative acidities of chlorine-substituted carboxylic acids
 33.2  Esters
 Learning outcomes
 Candidates should be able to:
 1 recall the reaction by which esters can be produced:
 (a)  reaction of alcohols with acyl chlorides using the formation of ethyl ethanoate and phenyl benzoate as 
examples 
45
 Back to contents page
 www.cambridgeinternational.org/alevel
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content  
46 www.cambridgeinternational.org/alevel Back to contents page
 33.3  Acyl chlorides
 Learning outcomes
 Candidates should be able to:
 1  recall the reactions (reagents and conditions) by which acyl chlorides can be produced: 
(a) reaction of carboxylic acids with PCl 3
 and heat, PCl 5
 , or SOCl 2
 2 describe the following reactions of acyl chlorides:
 (a) hydrolysis on addition of water at room temperature to give the carboxylic acid and HCl 
(b) reaction with an alcohol at room temperature to produce an ester and HCl
 (c) reaction with phenol at room temperature to produce an ester and HCl
 (d) reaction with ammonia at room temperature to produce an amide and HCl
 (e) reaction with a primary or secondary amine at room temperature to produce an amide and HCl
 3 describe the addition-elimination mechanism of acyl chlorides in reactions in 33.3.2(a) – (e) 
4 explain the relative ease of hydrolysis of acyl chlorides, alkyl chlorides and halogenoarenes (aryl chlorides)
"""

text12 = """
34 Nitrogen compounds
 34.1  Primary and secondary amines
 Learning outcomes
 Candidates should be able to:
 1  recall the reactions (reagents and conditions) by which primary and secondary amines are produced:
 (a) reaction of halogenoalkanes with NH3
 in ethanol heated under pressure
 (b)  reaction of halogenoalkanes with primary amines in ethanol, heated in a sealed tube / under pressure
 (c) the reduction of amides with LiAl H4
 (d) the reduction of nitriles with LiAl H4
 or H2
 / Ni
 2 describe the condensation reaction of ammonia or an amine with an acyl chloride at room temperature to 
give an amide
 3 describe and explain the basicity of aqueous solutions of amines
 34.2  Phenylamine and azo compounds
 Learning outcomes
 Candidates should be able to:
 1  describe the preparation of phenylamine via the nitration of benzene to form nitrobenzene followed by 
reduction with hot Sn/concentrated HCl , followed by NaOH(aq)
 2 describe:
 (a) the reaction of phenylamine with Br2
 (aq) at room temperature
 (b)  the reaction of phenylamine with HNO2
 or NaNO2
 and dilute acid below 10 °C to produce the 
diazonium salt; further warming of the diazonium salt with H2
 O to give phenol
 3 describe and explain the relative basicities of aqueous ammonia, ethylamine and phenylamine 
4 recall the following about azo compounds:
 (a) describe the coupling of benzenediazonium chloride with phenol in NaOH(aq) to form an azo compound
 (b) identify the azo group
 (c) state that azo compounds are often used as dyes
 (d) that other azo dyes can be formed via a similar route
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content  
47 www.cambridgeinternational.org/alevel Back to contents page
 34.3  Amides
 Learning outcomes
 Candidates should be able to:
 1  recall the reactions (reagents and conditions) by which amides are produced:
 (a) the reaction between ammonia and an acyl chloride at room temperature
 (b) the reaction between a primary amine and an acyl chloride at room temperature
 2 describe the reactions of amides:
 (a) hydrolysis with aqueous alkali or aqueous acid
 (b) the reduction of the CO group in amides with LiAl H4
 to form an amine
 3 state and explain why amides are much weaker bases than amines
 34.4  Amino acids
 Learning outcomes
 Candidates should be able to:
 1 describe the acid / base properties of amino acids and the formation of zwitterions, to include the isoelectric 
point
 2 describe the formation of amide (peptide) bonds between amino acids to give di- and tripeptides
 3 interpret and predict the results of electrophoresis on mixtures of amino acids and dipeptides at varying pHs 
(the assembling of the apparatus will not be tested)
"""

text13 = """
 35 Polymerisation
 35.1  Condensation polymerisation
 Learning outcomes
 Candidates should be able to:
 1 describe the formation of polyesters: 
(a) the reaction between a diol and a dicarboxylic acid or dioyl chloride 
(b) the reaction of a hydroxycarboxylic acid 
2 describe the formation of polyamides: 
(a) the reaction between a diamine and a dicarboxylic acid or dioyl chloride 
(b) the reaction of an aminocarboxylic acid 
(c)  the reaction between amino acids
 3 deduce the repeat unit of a condensation polymer obtained from a given monomer or pair of monomers
 4 identify the monomer(s) present in a given section of a condensation polymer molecule
 35.2  Predicting the type of polymerisation
 Learning outcomes
 Candidates should be able to:
 1 predict the type of polymerisation reaction for a given monomer or pair of monomers
 2 deduce the type of polymerisation reaction which produces a given section of a polymer molecule
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content  
48 www.cambridgeinternational.org/alevel Back to contents page
 35.3  Degradable polymers
 Learning outcomes
 Candidates should be able to:
 1 recognise that poly(alkenes) are chemically inert and can therefore be difficult to biodegrade 
2 recognise that some polymers can be degraded by the action of light
 3 recognise that polyesters and polyamides are biodegradable by acidic and alkaline hydrolysis 
"""

text14 = """
36 Organic synthesis
 36.1  Organic synthesis
 Learning outcomes
 Candidates should be able to:
 1 for an organic molecule containing several functional groups:
 (a) identify organic functional groups using the reactions in the syllabus
 (b) predict properties and reactions
 2 devise multi-step synthetic routes for preparing organic molecules using the reactions in the syllabus
 3 analyse a given synthetic route in terms of type of reaction and reagents used for each step of it, and 
possible by-products
"""

text15 = """
 37 Analytical techniques
 37.1  Thin-layer chromatography
 Learning outcomes
 Candidates should be able to:
 1 describe and understand the terms 
(a) stationary phase, for example aluminium oxide (on a solid support)
 (b)  mobile phase; a polar or non-polar solvent 
(c)  Rf
 value 
(d)  solvent front and baseline 
2 interpret Rf
 values 
3 explain the differences in Rf
 values in terms of interaction with the stationary phase and of relative solubility 
in the mobile phase  
37.2  Gas / liquid chromatography 
Learning outcomes
 Candidates should be able to:
 1 describe and understand the terms 
(a) stationary phase; a high boiling point non-polar liquid (on a solid support)
 (b) mobile phase; an unreactive gas 
(c) retention time 
2 interpret gas / liquid chromatograms in terms of the percentage composition of a mixture 
3  explain retention times in terms of interaction with the stationary phase
Cambridge International AS & A Level Chemistry 9701 syllabus for 2022, 2023 and 2024. Subject content  
37.3  Carbon-13 NMR spectroscopy
 Learning outcomes
 Candidates should be able to:
 1 analyse and interpret a carbon-13 NMR spectrum of a simple molecule to deduce: 
(a) the different environments of the carbon atoms present
 (b) the possible structures for the molecule
 2 predict or explain the number of peaks in a carbon-13 NMR spectrum for a given molecule
 37.4  Proton (1H) NMR spectroscopy
 Learning outcomes
 Candidates should be able to:
 1 analyse and interpret a proton (1H) NMR spectrum of a simple molecule to deduce:
 (a) the different environments of proton present using chemical shift values
 (b) the relative numbers of each type of proton present from relative peak areas
 (c)  the number of equivalent protons on the carbon atom adjacent to the one to which the given proton is 
attached from the splitting pattern, using the n + 1 rule (limited to singlet, doublet, triplet, quartet and 
multiplet)
 (d) the possible structures for the molecule
 2 predict the chemical shifts and splitting patterns of the protons in a given molecule
 3 describe the use of tetramethylsilane, TMS, as the standard for chemical shift measurements
 4 state the need for deuterated solvents, e.g. CDCl 3
 , when obtaining a proton NMR spectrum
 5 describe the identification of O–H and N–H protons by proton exchange using D2
 O
"""

textarr = [text, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11,
           text12,text13,text14,text15]
for i in range(len(textarr)):
    textarr[i] = getFormattedTextfromPdf.formatText(textarr[i])

trainModels.train(textarr, allLabels)
