import trainModels
import getFormattedTextfromPdf


allLabels = ['Cell structure', 'Biological molecules', 
             'Enzymes', 'Cell membranes and transport', 'The mitotic cell cycle', 'Nucleic acids and protein synthesis', 'Transport in plants',
               'Transport in mammals', 'Gas exchange', 'Infectious diseases', 'Immunity']


text = """
1 Cell structure
All organisms are composed of cells. Knowledge of the structure and function of cells underpins much of biology.
The fundamental differences between eukaryotic and prokaryotic cells are explored and provide useful biological
background for the topic on Infectious diseases (Topic 10). Viruses are introduced as non-cellular structures,
which gives candidates the opportunity to consider whether cells are the basic unit of life.
The use of light microscopes is a fundamental skill that is developed in this topic and applied throughout several
other topics of the syllabus.
1.1 The microscope in cell studies Learning outcomes
Candidates should be able to:
1 make temporary preparations of cellular material suitable for
viewing with a light microscope
2 draw cells from microscope slides and photomicrographs
3 calculate magnifications of images and actual sizes of
specimens from drawings, photomicrographs and electron
micrographs (scanning and transmission)
4 use an eyepiece graticule and stage micrometer scale to make
measurements and use the appropriate units, millimetre (mm),
micrometre (µm) and nanometre (nm)
5 define resolution and magnification and explain the differences
between these terms, with reference to light microscopy and
electron microscopy
1.2 Cells as the basic units of living
organisms
Learning outcomes
Candidates should be able to:
1 recognise organelles and other cell structures found in
eukaryotic cells and outline their structures and functions,
limited to:
• cell surface membrane
• nucleus, nuclear envelope and nucleolus
• rough endoplasmic reticulum
• smooth endoplasmic reticulum
• Golgi body (Golgi apparatus or Golgi complex)
• mitochondria (including the presence of small circular DNA)
• ribosomes (80S in the cytoplasm and 70S in chloroplasts
and mitochondria)
• lysosomes
• centrioles and microtubules
• cilia
• microvilli
• chloroplasts (including the presence of small circular DNA)
• cell wall
• plasmodesmata
• large permanent vacuole and tonoplast of plant cells
2 describe and interpret photomicrographs, electron micrographs
and drawings of typical plant and animal cells
3 compare the structure of typical plant and animal cells
4 state that cells use ATP from respiration for energy-requiring
processes
5 outline key structural features of a prokaryotic cell as found in a
typical bacterium, including:
• unicellular
• generally 1–5 µm diameter
• peptidoglycan cell walls
• circular DNA
• 70S ribosomes
• absence of organelles surrounded by double membranes
6 compare the structure of a prokaryotic cell as found in a typical
bacterium with the structures of typical eukaryotic cells in
plants and animals
7 state that all viruses are non-cellular structures with a nucleic
acid core (either DNA or RNA) and a capsid made of protein,
and that some viruses have an outer envelope made of
phospholipids
"""

text2 = """
2 Biological molecules
This topic introduces carbohydrates, lipids and proteins: organic molecules that are important in cells. Nucleic
acids, another class of biological molecule, are covered in Topic 6. All of these molecules are based on the
versatile element carbon. This topic explains how carbohydrates, lipids and proteins, which have a great diversity
of function in organisms, are assembled from smaller organic molecules such as glucose, amino acids, glycerol
and fatty acids.
The emphasis in this topic is on the relationship between molecular structures and their functions. Some of these
ideas are continued in other topics, for example, the functions of haemoglobin in gas transport in Transport in
mammals (Topic 8), phospholipids in membranes in Cell membranes and transport (Topic 4) and antibodies in
Immunity (Topic 11).
Life as we know it would not be possible without water. Understanding the properties of this extraordinary
molecule is an essential part of any study of biological molecules. Some of the roles of water are in this topic,
others are in Topics 4, 7, 8, 12, 13 and 14.
2.1 Testing for biological molecules Learning outcomes
Candidates should be able to:
1 describe and carry out the Benedict’s test for reducing sugars,
the iodine test for starch, the emulsion test for lipids and the
biuret test for proteins
2 describe and carry out a semi-quantitative Benedict’s test on
a reducing sugar solution by standardising the test and using
the results (time to first colour change or comparison to colour
standards) to estimate the concentration
3 describe and carry out a test to identify the presence of
non-reducing sugars, using acid hydrolysis and Benedict’s
solution
2.2 Carbohydrates and lipids Learning outcomes
Candidates should be able to:
1 describe and draw the ring forms of α-glucose and β-glucose
2 define the terms monomer, polymer, macromolecule,
monosaccharide, disaccharide and polysaccharide
3 state the role of covalent bonds in joining smaller molecules
together to form polymers
4 state that glucose, fructose and maltose are reducing sugars and
that sucrose is a non-reducing sugar
5 describe the formation of a glycosidic bond by condensation,
with reference to disaccharides, including sucrose, and
polysaccharides
continued
2.2 Carbohydrates and lipids
continued
Learning outcomes
Candidates should be able to:
6 describe the breakage of a glycosidic bond in polysaccharides
and disaccharides by hydrolysis, with reference to the
non-reducing sugar test
7 describe the molecular structure of the polysaccharides starch
(amylose and amylopectin) and glycogen and relate their
structures to their functions in living organisms
8 describe the molecular structure of the polysaccharide cellulose
and outline how the arrangement of cellulose molecules
contributes to the function of plant cell walls
9 state that triglycerides are non-polar hydrophobic molecules
and describe the molecular structure of triglycerides with
reference to fatty acids (saturated and unsaturated), glycerol
and the formation of ester bonds
10 relate the molecular structure of triglycerides to their functions
in living organisms
11 describe the molecular structure of phospholipids with reference
to their hydrophilic (polar) phosphate heads and hydrophobic
(non-polar) fatty acid tails
2.3 Proteins Learning outcomes
Candidates should be able to:
1 describe and draw the general structure of an amino acid and
the formation and breakage of a peptide bond
2 explain the meaning of the terms primary structure, secondary
structure, tertiary structure and quaternary structure of proteins
3 describe the types of interaction that hold protein molecules in
shape:
• hydrophobic interactions
• hydrogen bonding
• ionic bonding
• covalent bonding, including disulfide bonds
4 state that globular proteins are generally soluble and have
physiological roles and fibrous proteins are generally insoluble
and have structural roles
5 describe the structure of a molecule of haemoglobin as an
example of a globular protein, including the formation of its
quaternary structure from two alpha (α) chains (α–globin), two
beta (β) chains (β–globin) and a haem group
6 relate the structure of haemoglobin to its function, including
the importance of iron in the haem group
7 describe the structure of a molecule of collagen as an example
of a fibrous protein, and the arrangement of collagen molecules
to form collagen fibres
8 relate the structures of collagen molecules and collagen fibres
to their function
2.4 Water Learning outcomes
Candidates should be able to:
1 explain how hydrogen bonding occurs between water molecules
and relate the properties of water to its roles in living organisms,
limited to solvent action, high specific heat capacity and latent
heat of vaporisation
"""

text3 = """
3 Enzymes
Enzymes are essential for life to exist. The mode of action of enzymes and the factors that affect their activity
are explored in this topic. Prior knowledge for this topic is an understanding that an enzyme is a biological
catalyst that increases the rate of a reaction and remains unchanged when the reaction is complete.
There are many opportunities in this topic for candidates to gain experience of carrying out practical
investigations and analysing, interpreting and evaluating their results.
3.1 Mode of action of enzymes Learning outcomes
Candidates should be able to:
1 state that enzymes are globular proteins that catalyse reactions
inside cells (intracellular enzymes) or are secreted to catalyse
reactions outside cells (extracellular enzymes)
2 explain the mode of action of enzymes in terms of an active site,
enzyme–substrate complex, lowering of activation energy and
enzyme specificity, including the lock-and-key hypothesis and
the induced-fit hypothesis
3 investigate the progress of enzyme-catalysed reactions by
measuring rates of formation of products using catalase and
rates of disappearance of substrate using amylase
4 outline the use of a colorimeter for measuring the progress of
enzyme-catalysed reactions that involve colour changes
3.2 Factors that affect enzyme
action
Learning outcomes
Candidates should be able to:
1 investigate and explain the effects of the following factors on
the rate of enzyme-catalysed reactions:
• temperature
• pH (using buffer solutions)
• enzyme concentration
• substrate concentration
• inhibitor concentration
2 explain that the maximum rate of reaction (Vmax) is used to
derive the Michaelis–Menten constant (Km), which is used to
compare the affinity of different enzymes for their substrates
3 explain the effects of reversible inhibitors, both competitive and
non-competitive, on enzyme activity
4 investigate the difference in activity between an enzyme
immobilised in alginate and the same enzyme free in solution,
and state the advantages of using immobilised enzymes
"""

text4 = """
4 Cell membranes and transport
The fluid mosaic model, introduced in 1972, describes the way in which biological molecules are arranged to
form cell membranes. The model continues to be modified as understanding improves of the ways in which
substances cross membranes, how cells interact and how cells respond to signals. The model also provides the
basis for our understanding of passive and active movement of molecules and ions between cells and their
surroundings, cell-to-cell interactions and long-distance cell signalling.
Investigating the effects of different factors on diffusion, osmosis and membrane permeability involves an
understanding of the properties of phospholipids and proteins covered in Biological molecules (Topic 2).
4.1 Fluid mosaic membranes Learning outcomes
Candidates should be able to:
1 describe the fluid mosaic model of membrane structure with
reference to the hydrophobic and hydrophilic interactions that
account for the formation of the phospholipid bilayer and the
arrangement of proteins
2 describe the arrangement of cholesterol, glycolipids and
glycoproteins in cell surface membranes
3 describe the roles of phospholipids, cholesterol, glycolipids,
proteins and glycoproteins in cell surface membranes, with
reference to stability, fluidity, permeability, transport (carrier
proteins and channel proteins), cell signalling (cell surface
receptors) and cell recognition (cell surface antigens – see
11.1.2)
4 outline the main stages in the process of cell signalling leading
to specific responses:
• secretion of specific chemicals (ligands) from cells
• transport of ligands to target cells
• binding of ligands to cell surface receptors on target cells
4.2 Movement into and out of cells Learning outcomes
Candidates should be able to:
1 describe and explain the processes of simple diffusion,
facilitated diffusion, osmosis, active transport, endocytosis and
exocytosis
2 investigate simple diffusion and osmosis using plant tissue and
non-living materials, including dialysis (Visking) tubing and agar
3 illustrate the principle that surface area to volume ratios
decrease with increasing size by calculating surface areas and
volumes of simple 3-D shapes (as shown in the Mathematical
requirements)
4 investigate the effect of changing surface area to volume ratio
on diffusion using agar blocks of different sizes
continued
4.2 Movement into and out of cells
continued
Learning outcomes
Candidates should be able to:
5 investigate the effects of immersing plant tissues in solutions
of different water potentials, using the results to estimate the
water potential of the tissues
6 explain the movement of water between cells and solutions in
terms of water potential and explain the different effects of the
movement of water on plant cells and animal cells (knowledge
of solute potential and pressure potential is not expected)
"""

text5 = """
 The mitotic cell cycle
When body cells reach a certain size they divide into two cells. Nuclear division occurs first, followed by division
of the cytoplasm. The mitotic cell cycle of eukaryotes involves DNA replication followed by nuclear division. This
ensures the genetic uniformity of all daughter cells.
5.1 Replication and division of nuclei
and cells
Learning outcomes
Candidates should be able to:
1 describe the structure of a chromosome, limited to:
• DNA
• histone proteins
• sister chromatids
• centromere
• telomeres
2 explain the importance of mitosis in the production of
genetically identical daughter cells during:
• growth of multicellular organisms
• replacement of damaged or dead cells
• repair of tissues by cell replacement
• asexual reproduction
3 outline the mitotic cell cycle, including:
• interphase (growth in G1
 and G2 phases and DNA replication
in S phase)
• mitosis
• cytokinesis
4 outline the role of telomeres in preventing the loss of genes
from the ends of chromosomes during DNA replication
5 outline the role of stem cells in cell replacement and tissue
repair by mitosis
6 explain how uncontrolled cell division can result in the
formation of a tumour
5.2 Chromosome behaviour in
mitosis
Learning outcomes
Candidates should be able to:
1 describe the behaviour of chromosomes in plant and animal
cells during the mitotic cell cycle and the associated behaviour
of the nuclear envelope, the cell surface membrane and the
spindle (names of the main stages of mitosis are expected:
prophase, metaphase, anaphase and telophase)
2 interpret photomicrographs, diagrams and microscope slides of
cells in different stages of the mitotic cell cycle and identify the
main stages of mitosis
"""

text6 = """
6 Nucleic acids and protein synthesis
Nucleic acids have roles in the storage and retrieval of genetic information and in the use of this information
to synthesise polypeptides. DNA is the molecule of heredity and is an extremely stable molecule that cells
replicate with great accuracy. The genetic code explains how the sequence of nucleotides in DNA and
messenger RNA (mRNA) determines the sequence of amino acids that make up a polypeptide. In eukaryotes
this involves the processes of transcription in the nucleus to produce mRNA, followed by translation in the
cytoplasm to produce polypeptides.
6.1 Structure of nucleic acids and
replication of DNA
Learning outcomes
Candidates should be able to:
1 describe the structure of nucleotides, including the
phosphorylated nucleotide ATP (structural formulae are not
expected)
2 state that the bases adenine and guanine are purines with a
double ring structure, and that the bases cytosine, thymine and
uracil are pyrimidines with a single ring structure (structural
formulae for bases are not expected)
3 describe the structure of a DNA molecule as a double helix,
including:
• the importance of complementary base pairing between the
5′ to 3′ strand and the 3′ to 5′ strand (antiparallel strands)
• differences in hydrogen bonding between C–G and A–T base
pairs
• linking of nucleotides by phosphodiester bonds
4 describe the semi-conservative replication of DNA during the
S phase of the cell cycle, including:
• the roles of DNA polymerase and DNA ligase (knowledge
of other enzymes in DNA replication in cells and different
types of DNA polymerase is not expected)
• the differences between leading strand and lagging strand
replication as a consequence of DNA polymerase adding
nucleotides only in a 5′ to 3′ direction
5 describe the structure of an RNA molecule, using the example
of messenger RNA (mRNA)
6.2 Protein synthesis Learning outcomes
Candidates should be able to:
1 state that a polypeptide is coded for by a gene and that a gene
is a sequence of nucleotides that forms part of a DNA molecule
2 describe the principle of the universal genetic code in which
different triplets of DNA bases either code for specific amino
acids or correspond to start and stop codons
6.2 Protein synthesis continued Learning outcomes
Candidates should be able to:
3 describe how the information in DNA is used during
transcription and translation to construct polypeptides,
including the roles of:
• RNA polymerase
• messenger RNA (mRNA)
• codons
• transfer RNA (tRNA)
• anticodons
• ribosomes
4 state that the strand of a DNA molecule that is used in
transcription is called the transcribed or template strand and
that the other strand is called the non-transcribed strand
5 explain that, in eukaryotes, the RNA molecule formed following
transcription (primary transcript) is modified by the removal
of non-coding sequences (introns) and the joining together of
coding sequences (exons) to form mRNA
6 state that a gene mutation is a change in the sequence of
base pairs in a DNA molecule that may result in an altered
polypeptide
7 explain that a gene mutation is a result of substitution or
deletion or insertion of nucleotides in DNA and outline how
each of these types of mutation may affect the polypeptide
produced 
"""

text7 = """
7 Transport in plants
Flowering plants do not have compact bodies like those of many animals. Leaves and extensive root systems
spread out to obtain the light energy, carbon dioxide, mineral ions and water that plants gain from their
environment to make organic molecules, such as sugars and amino acids. Transport systems in plants move
substances from where they are absorbed or produced to where they are stored or used.
7.1 Structure of transport tissues Learning outcomes
Candidates should be able to:
1 draw plan diagrams of transverse sections of stems, roots and
leaves of herbaceous dicotyledonous plants from microscope
slides and photomicrographs
2 describe the distribution of xylem and phloem in transverse
sections of stems, roots and leaves of herbaceous
dicotyledonous plants
3 draw and label xylem vessel elements, phloem sieve tube
elements and companion cells from microscope slides,
photomicrographs and electron micrographs
4 relate the structure of xylem vessel elements, phloem sieve
tube elements and companion cells to their functions
7.2 Transport mechanisms Learning outcomes
Candidates should be able to:
1 state that some mineral ions and organic compounds can be
transported within plants dissolved in water
2 describe the transport of water from the soil to the xylem
through the:
• apoplast pathway, including reference to lignin and
cellulose
• symplast pathway, including reference to the endodermis,
Casparian strip and suberin
3 explain that transpiration involves the evaporation of water
from the internal surfaces of leaves followed by diffusion of
water vapour to the atmosphere
4 explain how hydrogen bonding of water molecules is involved
with movement of water in the xylem by cohesion-tension in
transpiration pull and by adhesion to cellulose in cell walls
5 make annotated drawings of transverse sections of leaves from
xerophytic plants to explain how they are adapted to reduce
water loss by transpiration
6 state that assimilates dissolved in water, such as sucrose and
amino acids, move from sources to sinks in phloem sieve tubes
7 explain how companion cells transfer assimilates to phloem
sieve tubes, with reference to proton pumps and cotransporter
proteins
8 explain mass flow in phloem sieve tubes down a hydrostatic
pressure gradient from source to sink 
"""

text8 = """
 Transport in mammals
As animals become larger, more complex and more active, transport systems become essential to supply
nutrients to, and remove waste from, individual cells. Mammals are far more active than plants and require
much greater supplies of oxygen. This is transported by haemoglobin inside red blood cells.
8.1 The circulatory system Learning outcomes
Candidates should be able to:
1 state that the mammalian circulatory system is a closed double
circulation consisting of a heart, blood and blood vessels
including arteries, arterioles, capillaries, venules and veins
2 describe the functions of the main blood vessels of the
pulmonary and systemic circulations, limited to pulmonary
artery, pulmonary vein, aorta and vena cava
3 recognise arteries, veins and capillaries from microscope
slides, photomicrographs and electron micrographs and make
plan diagrams showing the structure of arteries and veins in
transverse section (TS) and longitudinal section (LS)
4 explain how the structure of muscular arteries, elastic arteries,
veins and capillaries are each related to their functions
5 recognise and draw red blood cells, monocytes, neutrophils and
lymphocytes from microscope slides, photomicrographs and
electron micrographs
6 state that water is the main component of blood and tissue
fluid and relate the properties of water to its role in transport
in mammals, limited to solvent action and high specific heat
capacity
7 state the functions of tissue fluid and describe the formation of
tissue fluid in a capillary network
8.2 Transport of oxygen and carbon
dioxide
Learning outcomes
Candidates should be able to:
1 describe the role of red blood cells in transporting oxygen and
carbon dioxide with reference to the roles of:
• haemoglobin
• carbonic anhydrase
• the formation of haemoglobinic acid
• the formation of carbaminohaemoglobin
2 describe the chloride shift and explain the importance of the
chloride shift
3 describe the role of plasma in the transport of carbon dioxide
4 describe and explain the oxygen dissociation curve of adult
haemoglobin
5 explain the importance of the oxygen dissociation curve at
partial pressures of oxygen in the lungs and in respiring tissues
6 describe the Bohr shift and explain the importance of the Bohr
shift
Cambridge International AS & A Level Biology 9700 syllabus for 2022, 2023 and 2024. Subject content
Back to contents page www.cambridgeinternational.org/alevel 25
8.3 The heart Learning outcomes
Candidates should be able to:
1 describe the external and internal structure of the mammalian
heart
2 explain the differences in the thickness of the walls of the:
• atria and ventricles
• left ventricle and right ventricle
3 describe the cardiac cycle, with reference to the relationship
between blood pressure changes during systole and diastole and
the opening and closing of valves
4 explain the roles of the sinoatrial node, the atrioventricular
node and the Purkyne tissue in the cardiac cycle (knowledge of
nervous and hormonal control is not expected)
"""

text9 = """
9 Gas exchange
The gas exchange system is responsible for the uptake of oxygen into the blood and the excretion of carbon
dioxide. An understanding of this system shows how cells, tissues and organs function together to exchange
these gases between the blood and the environment.
9.1 The gas exchange system Learning outcomes
Candidates should be able to:
1 describe the structure of the human gas exchange system,
limited to:
• lungs
• trachea
• bronchi
• bronchioles
• alveoli
• capillary network
2 describe the distribution in the gas exchange system of
cartilage, ciliated epithelium, goblet cells, squamous epithelium
of alveoli, smooth muscle and capillaries
3 recognise cartilage, ciliated epithelium, goblet cells, squamous
epithelium of alveoli, smooth muscle and capillaries in
microscope slides, photomicrographs and electron micrographs
4 recognise trachea, bronchi, bronchioles and alveoli in
microscope slides, photomicrographs and electron micrographs
and make plan diagrams of transverse sections of the walls of
the trachea and bronchus
5 describe the functions of ciliated epithelial cells, goblet cells and
mucous glands in maintaining the health of the gas exchange
system
6 describe the functions in the gas exchange system of cartilage,
smooth muscle, elastic fibres and squamous epithelium
7 describe gas exchange between air in the alveoli and blood in
the capillaries 
"""

text10 = """
10 Infectious diseases
The infectious diseases studied in this topic are caused by pathogens that are transmitted from one human host
to another. Some, like Plasmodium that causes malaria, are transmitted by vectors, but there are many other
methods of transmission, such as through water and food or during sexual activity. An understanding of the
biology of the pathogen and its mode of transmission is essential if the disease is to be controlled and ultimately
prevented.
10.1 Infectious diseases Learning outcomes
Candidates should be able to:
1 state that infectious diseases are caused by pathogens and are
transmissible
2 state the name and type of pathogen that causes each of the
following diseases:
• cholera – caused by the bacterium Vibrio cholerae
• malaria – caused by the protoctists Plasmodium falciparum,
Plasmodium malariae, Plasmodium ovale and Plasmodium
vivax
• tuberculosis (TB) – caused by the bacteria Mycobacterium
tuberculosis and Mycobacterium bovis
• HIV/AIDS – caused by the human immunodeficiency virus
(HIV)
3 explain how cholera, malaria, TB and HIV are transmitted
4 discuss the biological, social and economic factors that need to
be considered in the prevention and control of cholera, malaria,
TB and HIV (details of the life cycle of the malarial parasite are
not expected)
10.2 Antibiotics Learning outcomes
Candidates should be able to:
1 outline how penicillin acts on bacteria and why antibiotics do
not affect viruses
2 discuss the consequences of antibiotic resistance and the steps
that can be taken to reduce its impact
"""
text11 = """
11 Immunity
An understanding of the immune system shows how cells and molecules function together to protect the body
against infectious diseases and how, after an initial infection, the body is protected from subsequent infections
by the same pathogen. Phagocytosis is an immediate non-specific part of the immune system, while the actions
of lymphocytes provide effective defence against specific pathogens.
11.1 The immune system Learning outcomes
Candidates should be able to:
1 describe the mode of action of phagocytes (macrophages and
neutrophils)
2 explain what is meant by an antigen (see 4.1.3) and state the
difference between self antigens and non-self antigens
3 describe the sequence of events that occurs during a primary
immune response with reference to the roles of:
• macrophages
• B-lymphocytes, including plasma cells
• T-lymphocytes, limited to T-helper cells and T-killer cells
4 explain the role of memory cells in the secondary immune
response and in long-term immunity
11.2 Antibodies and vaccination Learning outcomes
Candidates should be able to:
1 relate the molecular structure of antibodies to their functions
2 outline the hybridoma method for the production of
monoclonal antibodies
3 outline the principles of using monoclonal antibodies in the
diagnosis of disease and in the treatment of disease
4 describe the differences between active immunity and passive
immunity and between natural immunity and artificial
immunity
5 explain that vaccines contain antigens that stimulate immune
responses to provide long-term immunity
6 explain how vaccination programmes can help to control the
spread of infectious diseases
"""



textarr = [text, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11]
for i in range(len(textarr)):
    textarr[i] = getFormattedTextfromPdf.formatText(textarr[i])

trainModels.train(textarr, allLabels)
