import trainModels
import getFormattedTextfromPdf


allLabels = ['Characteristics and classification of living organisms', 'Organisation of the organism', 
             'Movement into and out of cells', 'Biological molecules', 'Enzymes', 'Plant nutrition', 'Human nutrition',
               'Transport in plants', 'Transport in animals', 'Diseases and immunity', 'Gas exchange in humans','Respiration',
               'Excretion in humans','Coordination and response','Drugs','Reproduction','Inheritance','Variation and selection',
               'Organisms and their environment','Human influences on ecosystems','Biotechnology and genetic modification']


text = """
1 Characteristics and classification of living organisms
1.1 Characteristics of living organisms
Core
1 Describe the characteristics of living organisms
by describing:
(a) movement as an action by an organism or
part of an organism causing a change of
position or place
(b) respiration as the chemical reactions in cells
that break down nutrient molecules and
release energy for metabolism
(c) sensitivity as the ability to detect and
respond to changes in the internal or external
environment
(d) growth as a permanent increase in size and
dry mass
(e) reproduction as the processes that make
more of the same kind of organism
(f) excretion as the removal of the waste
products of metabolism and substances in
excess of requirements
(g) nutrition as the taking in of materials for
energy, growth and development
Supplement
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 11
1.2 Concept and uses of classification systems
Core
1 State that organisms can be classified into groups
by the features that they share
2 Describe a species as a group of organisms that
can reproduce to produce fertile offspring
3 Describe the binomial system of naming species
as an internationally agreed system in which the
scientific name of an organism is made up of two
parts showing the genus and species
4 Construct and use dichotomous keys based on
identifiable features
Supplement
5 Explain that classification systems aim to reflect
evolutionary relationships
6 Explain that the sequences of bases in DNA are
used as a means of classification
7 Explain that groups of organisms which share a
more recent ancestor (are more closely related)
have base sequences in DNA that are more
similar than those that share only a distant
ancestor
1.3 Features of organisms
Core
1 State the main features used to place animals
and plants into the appropriate kingdoms
2 State the main features used to place organisms
into groups within the animal kingdom, limited
to:
(a) the main groups of vertebrates: mammals,
birds, reptiles, amphibians, fish
(b) the main groups of arthropods: myriapods,
insects, arachnids, crustaceans
3 Classify organisms using the features identified in
1.3.1 and 1.3.2
Supplement
4 State the main features used to place all
organisms into one of the five kingdoms: animal,
plant, fungus, prokaryote, protoctist
5 State the main features used to place organisms
into groups within the plant kingdom, limited
to ferns and flowering plants (dicotyledons and
monocotyledons)
6 Classify organisms using the features identified in
1.3.4 and 1.3.5
7 State the features of viruses, limited to a protein
coat and genetic material
"""

text2 = """
2 Organisation of the organism
2.1 Cell structure
Core
1 Describe and compare the structure of a plant
cell with an animal cell, limited to: cell wall, cell
membrane, nucleus, cytoplasm, chloroplasts,
ribosomes, mitochondria, vacuoles
2 Describe the structure of a bacterial cell,
limited to: cell wall, cell membrane, cytoplasm,
ribosomes, circular DNA, plasmids
3 Identify the cell structures listed in 2.1.1 and 2.1.2
in diagrams and images of plant, animal and
bacterial cells
4 Describe the functions of the structures listed in
2.1.1 and 2.1.2 in plant, animal and bacterial cells
5 State that new cells are produced by division of
existing cells
6 State that specialised cells have specific
functions, limited to:
(a) ciliated cells – movement of mucus in the
trachea and bronchi
(b) root hair cells – absorption
(c) palisade mesophyll cells – photosynthesis
(d) neurones – conduction of electrical impulses
(e) red blood cells – transport of oxygen
(f) sperm and egg cells (gametes) – reproduction
7 Describe the meaning of the terms: cell, tissue,
organ, organ system and organism as illustrated
by examples given in the syllabus
Supplement
2.2 Size of specimens
Core
1 State and use the formula:
magnification = image size ÷ actual size
2 Calculate magnification and size of biological
specimens using millimetres as units
Supplement
3 Convert measurements between millimetres (mm)
and micrometres (μm)
"""

text3 = """
3 Movement into and out of cells
3.1 Diffusion
Core
1 Describe diffusion as the net movement
of particles from a region of their higher
concentration to a region of their lower
concentration (i.e. down a concentration
gradient), as a result of their random movement
2 State that the energy for diffusion comes from
the kinetic energy of random movement of
molecules and ions
3 State that some substances move into and out of
cells by diffusion through the cell membrane
4 Describe the importance of diffusion of gases and
solutes in living organisms
5 Investigate the factors that influence diffusion,
limited to: surface area, temperature,
concentration gradient and distance
Supplement
3.2 Osmosis
Core
1 Describe the role of water as a solvent in
organisms with reference to digestion, excretion
and transport
2 State that water diffuses through partially
permeable membranes by osmosis
3 State that water moves into and out of cells by
osmosis through the cell membrane
4 Investigate osmosis using materials such as
dialysis tubing
5 Investigate and describe the effects on plant
tissues of immersing them in solutions of
different concentrations
6 State that plants are supported by the pressure
of water inside the cells pressing outwards on the
cell wall
Supplement
7 Describe osmosis as the net movement of
water molecules from a region of higher water
potential (dilute solution) to a region of lower
water potential (concentrated solution), through
a partially permeable membrane
8 Explain the effects on plant cells of immersing
them in solutions of different concentrations
by using the terms: turgid, turgor pressure,
plasmolysis, flaccid
9 Explain the importance of water potential and
osmosis in the uptake and loss of water by
organisms
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
14 www.cambridgeinternational.org/igcse Back to contents page
3.3 Active transport
Core
1 Describe active transport as the movement of
particles through a cell membrane from a region
of lower concentration to a region of higher
concentration (i.e. against a concentration
gradient), using energy from respiration
Supplement
2 Explain the importance of active transport as
a process for movement of molecules or ions
across membranes, including ion uptake by root
hairs
3 State that protein carriers move molecules or
ions across a membrane during active transport
"""

text4 = """
4 Biological molecules
4.1 Biological molecules
Core
1 List the chemical elements that make up:
carbohydrates, fats and proteins
2 State that large molecules are made from smaller
molecules, limited to:
(a) starch, glycogen and cellulose from glucose
(b) proteins from amino acids
(c) fats and oils from fatty acids and glycerol
3 Describe the use of:
(a) iodine solution test for starch
(b) Benedict’s solution test for reducing sugars
(c) biuret test for proteins
(d) ethanol emulsion test for fats and oils
(e) DCPIP test for vitamin C
Supplement
4 Describe the structure of a DNA molecule:
(a) two strands coiled together to form a double
helix
(b) each strand contains chemicals called bases
(c) bonds between pairs of bases hold the
strands together
(d) the bases always pair up in the same way:
A with T, and C with G (full names are not
required)
"""

text5 = """
5 Enzymes
5.1 Enzymes
Core
1 Describe a catalyst as a substance that increases
the rate of a chemical reaction and is not
changed by the reaction
2 Describe enzymes as proteins that are involved
in all metabolic reactions, where they function as
biological catalysts
3 Describe why enzymes are important in all living
organisms in terms of a reaction rate necessary
to sustain life
4 Describe enzyme action with reference to
the shape of the active site of an enzyme
being complementary to its substrate and the
formation of products
5 Investigate and describe the effect of changes
in temperature and pH on enzyme activity
with reference to optimum temperature and
denaturation
Supplement
6 Explain enzyme action with reference to: active
site, enzyme-substrate complex, substrate and
product
7 Explain the specificity of enzymes in terms of the
complementary shape and fit of the active site
with the substrate
8 Explain the effect of changes in temperature on
enzyme activity in terms of kinetic energy, shape
and fit, frequency of effective collisions and
denaturation
9 Explain the effect of changes in pH on
enzyme activity in terms of shape and fit and
denaturation
"""

text6 = """
6 Plant nutrition
6.1 Photosynthesis
Core
1 Describe photosynthesis as the process by
which plants synthesise carbohydrates from raw
materials using energy from light
2 State the word equation for photosynthesis as:
carbon dioxide + water → glucose + oxygen
in the presence of light and chlorophyll
3 State that chlorophyll is a green pigment that is
found in chloroplasts
4 State that chlorophyll transfers energy from light
into energy in chemicals, for the synthesis of
carbohydrates
Supplement
10 State the balanced chemical equation for
photosynthesis as:
6CO2 + 6H2O → C6H12O6 + 6O2
continued
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
16 www.cambridgeinternational.org/igcse Back to contents page
6.1 Photosynthesis continued
Core
5 Outline the subsequent use and storage of the
carbohydrates made in photosynthesis, limited
to:
(a) starch as an energy store
(b) cellulose to build cell walls
(c) glucose used in respiration to provide energy
(d) sucrose for transport in the phloem
(e) nectar to attract insects for pollination
6 Explain the importance of:
(a) nitrate ions for making amino acids
(b) magnesium ions for making chlorophyll
7 Investigate the need for chlorophyll, light
and carbon dioxide for photosynthesis, using
appropriate controls
8 Investigate and describe the effects of varying
light intensity, carbon dioxide concentration and
temperature on the rate of photosynthesis
9 Investigate and describe the effect of light and
dark conditions on gas exchange in an aquatic
plant using hydrogencarbonate indicator solution
Supplement
11 Identify and explain the limiting factors of
photosynthesis in different environmental
conditions
6.2 Leaf structure
Core
1 State that most leaves have a large surface area
and are thin, and explain how these features are
adaptations for photosynthesis
2 Identify in diagrams and images the following
structures in the leaf of a dicotyledonous plant:
chloroplasts, cuticle, guard cells and stomata,
upper and lower epidermis, palisade mesophyll,
spongy mesophyll, air spaces, vascular bundles,
xylem and phloem
3 Explain how the structures listed in 6.2.2 adapt
leaves for photosynthesis
"""

text7 = """
7 Human nutrition
7.1 Diet
Core
1 Describe what is meant by a balanced diet
2 State the principal dietary sources and describe
the importance of:
(a) carbohydrates
(b) fats and oils
(c) proteins
(d) vitamins, limited to C and D
(e) mineral ions, limited to calcium and iron
(f) fibre (roughage)
(g) water
3 State the causes of scurvy and rickets
Supplement
7.2 Digestive system
Core
1 Identify in diagrams and images the main organs
of the digestive system, limited to:
(a) alimentary canal: mouth, oesophagus,
stomach, small intestine (duodenum and
ileum) and large intestine (colon, rectum,
anus)
(b) associated organs: salivary glands, pancreas,
liver and gall bladder
2 Describe the functions of the organs of the
digestive system listed in 7.2.1, in relation to:
(a) ingestion – the taking of substances, e.g. food
and drink, into the body
(b) digestion – the breakdown of food
(c) absorption – the movement of nutrients from
the intestines into the blood
(d) assimilation – uptake and use of nutrients by
cells
(e) egestion – the removal of undigested food
from the body as faeces
Supplement
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
18 www.cambridgeinternational.org/igcse Back to contents page
7.3 Physical digestion
Core
1 Describe physical digestion as the breakdown of
food into smaller pieces without chemical change
to the food molecules
2 State that physical digestion increases the
surface area of food for the action of enzymes in
chemical digestion
3 Identify in diagrams and images the types of
human teeth: incisors, canines, premolars and
molars
4 Describe the structure of human teeth, limited
to: enamel, dentine, pulp, nerves, blood vessels
and cement, and understand that teeth are
embedded in bone and the gums
5 Describe the functions of the types of human
teeth in physical digestion of food
6 Describe the function of the stomach in physical
digestion
Supplement
7 Outline the role of bile in emulsifying fats and
oils to increase the surface area for chemical
digestion
7.4 Chemical digestion
Core
1 Describe chemical digestion as the break down
of large insoluble molecules into small soluble
molecules
2 State the role of chemical digestion in producing
small soluble molecules that can be absorbed
3 Describe the functions of enzymes as follows:
(a) amylase breaks down starch to simple
reducing sugars
(b) proteases break down protein to amino acids
(c) lipase breaks down fats and oils to fatty acids
and glycerol
4 State where, in the digestive system, amylase,
protease and lipase are secreted and where they
act
5 Describe the functions of hydrochloric acid
in gastric juice, limited to killing harmful
microorganisms in food and providing an acidic
pH for optimum enzyme activity
Supplement
6 Describe the digestion of starch in the digestive
system:
(a) amylase breaks down starch to maltose
(b) maltase breaks down maltose to glucose on
the membranes of the epithelium lining the
small intestine
7 Describe the digestion of protein by proteases in
the digestive system:
(a) pepsin breaks down protein in the acidic
conditions of the stomach
(b) trypsin breaks down protein in the alkaline
conditions of the small intestine
8 Explain that bile is an alkaline mixture that
neutralises the acidic mixture of food and gastric
juices entering the duodenum from the stomach,
to provide a suitable pH for enzyme action
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 19
7.5 Absorption
Core
1 State that the small intestine is the region where
nutrients are absorbed
2 State that most water is absorbed from the small
intestine but that some is also absorbed from the
colon
Supplement
3 Explain the significance of villi and microvilli in
increasing the internal surface area of the small
intestine
4 Describe the structure of a villus
5 Describe the roles of capillaries and lacteals in
villi
"""

text8 = """
8 Transport in plants
8.1 Xylem and phloem
Core
1 State the functions of xylem and phloem:
(a) xylem – transport of water and mineral ions,
and support
(b) phloem – transport of sucrose and amino
acids
2 Identify in diagrams and images the position of
xylem and phloem as seen in sections of roots,
stems and leaves of non-woody dicotyledonous
plants
Supplement
3 Relate the structure of xylem vessels to their
function, limited to:
(a) thick walls with lignin (details of lignification
are not required)
(b) no cell contents
(c) cells joined end to end with no cross walls to
form a long continuous tube
8.2 Water uptake
Core
1 Identify in diagrams and images root hair cells
and state their functions
2 State that the large surface area of root hairs
increases the uptake of water and mineral ions
3 Outline the pathway taken by water through the
root, stem and leaf as: root hair cells, root cortex
cells, xylem, mesophyll cells
4 Investigate, using a suitable stain, the pathway of
water through the above-ground parts of a plant
Supplement
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
20 www.cambridgeinternational.org/igcse Back to contents page
8.3 Transpiration
Core
1 Describe transpiration as the loss of water vapour
from leaves
2 State that water evaporates from the surfaces of
the mesophyll cells into the air spaces and then
diffuses out of the leaves through the stomata as
water vapour
3 Investigate and describe the effects of variation
of temperature and wind speed on transpiration
rate
Supplement
4 Explain how water vapour loss is related to:
the large internal surface area provided by the
interconnecting air spaces between mesophyll
cells and the size and number of stomata
5 Explain the mechanism by which water moves
upwards in the xylem in terms of a transpiration
pull that draws up a column of water molecules,
held together by forces of attraction between
water molecules
6 Explain the effects on the rate of transpiration of
varying the following factors: temperature, wind
speed and humidity
7 Explain how and why wilting occurs
8.4 Translocation
Core Supplement
1 Describe translocation as the movement of
sucrose and amino acids in phloem from sources
to sinks
2 Describe:
(a) sources as the parts of plants that release
sucrose or amino acids
(b) sinks as the parts of plants that use or store
sucrose or amino acids
3 Explain why some parts of a plant may act as a
source and a sink at different times
"""

text9 = """
9 Transport in animals
9.1 Circulatory systems
Core
1 Describe the circulatory system as a system of
blood vessels with a pump and valves to ensure
one-way flow of blood
Supplement
2 Describe the single circulation of a fish
3 Describe the double circulation of a mammal
4 Explain the advantages of a double circulation
9.2 Heart
Core
1 Identify in diagrams and images the structures of
the mammalian heart, limited to: muscular wall,
septum, left and right ventricles, left and right
atria, one-way valves and coronary arteries
2 State that blood is pumped away from the heart
in arteries and returns to the heart in veins
3 State that the activity of the heart may be
monitored by: ECG, pulse rate and listening to
sounds of valves closing
4 Investigate and describe the effect of physical
activity on the heart rate
5 Describe coronary heart disease in terms of
the blockage of coronary arteries and state
the possible risk factors including: diet, lack of
exercise, stress, smoking, genetic predisposition,
age and sex
6 Discuss the roles of diet and exercise in reducing
the risk of coronary heart disease
Supplement
7 Identify in diagrams and images the
atrioventricular and semilunar valves in the
mammalian heart
8 Explain the relative thickness of:
(a) the muscle walls of the left and right
ventricles
(b) the muscle walls of the atria compared to
those of the ventricles
9 Explain the importance of the septum in
separating oxygenated and deoxygenated blood
10 Describe the functioning of the heart in terms
of the contraction of muscles of the atria and
ventricles and the action of the valves
11 Explain the effect of physical activity on the heart
rate
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
22 www.cambridgeinternational.org/igcse Back to contents page
9.3 Blood vessels
Core
1 Describe the structure of arteries, veins and
capillaries, limited to: relative thickness of wall,
diameter of the lumen and the presence of valves
in veins
2 State the functions of capillaries
3 Identify in diagrams and images the main blood
vessels to and from the:
(a) heart, limited to: vena cava, aorta, pulmonary
artery and pulmonary vein
(b) lungs, limited to: pulmonary artery and
pulmonary vein
(c) kidney, limited to: renal artery and renal vein
Supplement
4 Explain how the structure of arteries and veins
is related to the pressure of the blood that they
transport
5 Explain how the structure of capillaries is related
to their functions
6 Identify, in diagrams and images, the main blood
vessels to and from the liver as: hepatic artery,
hepatic veins and hepatic portal vein
9.4 Blood
Core
1 List the components of blood as: red blood cells,
white blood cells, platelets and plasma
2 Identify red and white blood cells in
photomicrographs and diagrams
3 State the functions of the following components
of blood:
(a) red blood cells in transporting oxygen,
including the role of haemoglobin
(b) white blood cells in phagocytosis and
antibody production
(c) platelets in clotting (details are not required)
(d) plasma in the transport of blood cells, ions,
nutrients, urea, hormones and carbon dioxide
4 State the roles of blood clotting as preventing
blood loss and the entry of pathogens
Supplement
5 Identify lymphocytes and phagocytes in
photomicrographs and diagrams
6 State the functions of:
(a) lymphocytes – antibody production
(b) phagocytes – engulfing pathogens by
phagocytosis
7 Describe the process of clotting as the conversion
of fibrinogen to fibrin to form a mesh
"""

text10 = """
10 Diseases and immunity
10.1 Diseases and immunity
Core
1 Describe a pathogen as a disease-causing
organism
2 Describe a transmissible disease as a disease in
which the pathogen can be passed from one host
to another
3 State that a pathogen is transmitted:
(a) by direct contact, including through blood
and other body fluids
(b) indirectly, including from contaminated
surfaces, food, animals and air
4 Describe the body defences, limited to: skin,
hairs in the nose, mucus, stomach acid and white
blood cells
5 Explain the importance of the following in
controlling the spread of disease:
(a) a clean water supply
(b) hygienic food preparation
(c) good personal hygiene
(d) waste disposal
(e) sewage treatment (details of the stages of
sewage treatment are not required)
Supplement
6 Describe active immunity as defence against a
pathogen by antibody production in the body
7 State that each pathogen has its own antigens,
which have specific shapes
8 Describe antibodies as proteins that bind
to antigens leading to direct destruction
of pathogens or marking of pathogens for
destruction by phagocytes
9 State that specific antibodies have
complementary shapes which fit specific antigens
10 Explain that active immunity is gained after an
infection by a pathogen or by vaccination
11 Outline the process of vaccination:
(a) weakened pathogens or their antigens are
put into the body
(b) the antigens stimulate an immune response
by lymphocytes which produce antibodies
(c) memory cells are produced that give
long-term immunity
12 Explain the role of vaccination in controlling the
spread of diseases
13 Explain that passive immunity is a short-term
defence against a pathogen by antibodies
acquired from another individual, including
across the placenta and in breast milk
14 Explain the importance of breast-feeding for the
development of passive immunity in infants
15 State that memory cells are not produced in
passive immunity
continued
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
24 www.cambridgeinternational.org/igcse Back to contents page
10.1 Diseases and immunity continued
Core Supplement
16 Describe cholera as a disease caused by a
bacterium which is transmitted in contaminated
water
17 Explain that the cholera bacterium produces a
toxin that causes secretion of chloride ions into
the small intestine, causing osmotic movement
of water into the gut, causing diarrhoea,
dehydration and loss of ions from the blood
"""
text11 = """
11 Gas exchange in humans
11.1 Gas exchange in humans
Core
1 Describe the features of gas exchange surfaces
in humans, limited to: large surface area, thin
surface, good blood supply and good ventilation
with air
2 Identify in diagrams and images the following
parts of the breathing system: lungs, diaphragm,
ribs, intercostal muscles, larynx, trachea, bronchi,
bronchioles, alveoli and associated capillaries
3 Investigate the differences in composition
between inspired and expired air using limewater
as a test for carbon dioxide
4 Describe the differences in composition between
inspired and expired air, limited to: oxygen,
carbon dioxide and water vapour
5 Investigate and describe the effects of physical
activity on the rate and depth of breathing
Supplement
6 Identify in diagrams and images the internal and
external intercostal muscles
7 State the function of cartilage in the trachea
8 Explain the role of the ribs, the internal and
external intercostal muscles and the diaphragm
in producing volume and pressure changes in the
thorax leading to the ventilation of the lungs
9 Explain the differences in composition between
inspired and expired air
10 Explain the link between physical activity and
the rate and depth of breathing in terms of: an
increased carbon dioxide concentration in the
blood, which is detected by the brain, leading to
an increased rate and greater depth of breathing
11 Explain the role of goblet cells, mucus and
ciliated cells in protecting the breathing system
from pathogens and particles
"""

text12 = """
12 Respiration
12.1 Respiration
Core
1 State the uses of energy in living organisms,
including: muscle contraction, protein synthesis,
cell division, active transport, growth, the
passage of nerve impulses and the maintenance
of a constant body temperature
2 Investigate and describe the effect of
temperature on respiration in yeast
Supplement
12.2 Aerobic respiration
Core
1 Describe aerobic respiration as the chemical
reactions in cells that use oxygen to break down
nutrient molecules to release energy
2 State the word equation for aerobic respiration as:
glucose + oxygen → carbon dioxide + water
Supplement
3 State the balanced chemical equation for aerobic
respiration as:
C6H12O6 + 6O2 → 6CO2 + 6H2O
12.3 Anaerobic respiration
Core
1 Describe anaerobic respiration as the chemical
reactions in cells that break down nutrient
molecules to release energy without using
oxygen
2 State that anaerobic respiration releases much
less energy per glucose molecule than aerobic
respiration
3 State the word equation for anaerobic respiration
in yeast as:
glucose → alcohol + carbon dioxide
4 State the word equation for anaerobic respiration
in muscles during vigorous exercise as:
glucose → lactic acid
Supplement
5 State the balanced chemical equation for
anaerobic respiration in yeast as:
C6H12O6 → 2C2H5OH + 2CO2
6 State that lactic acid builds up in muscles and
blood during vigorous exercise causing an oxygen
debt
continued
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
26 www.cambridgeinternational.org/igcse Back to contents page
12.3 Anaerobic respiration continued
Core Supplement
7 Outline how the oxygen debt is removed after
exercise, limited to:
(a) continuation of fast heart rate to transport
lactic acid in the blood from the muscles to
the liver
(b) continuation of deeper and faster breathing
to supply oxygen for aerobic respiration of
lactic acid
(c) aerobic respiration of lactic acid in the liver
"""

text13 = """
13 Excretion in humans
13.1 Excretion in humans
Core
1 State that carbon dioxide is excreted through the
lungs
2 State that the kidneys excrete urea and excess
water and ions
3 Identify in diagrams and images the kidneys,
ureters, bladder and urethra
Supplement
4 Identify in diagrams and images the structure of
the kidney, limited to the cortex and medulla
5 Outline the structure and function of a nephron
and its associated blood vessels, limited to:
(a) the role of the glomerulus in the filtration
from the blood of water, glucose, urea and
ions
(b) the role of the nephron in the reabsorption of
all of the glucose, some of the ions and most
of the water back into the blood
(c) the formation of urine containing urea,
excess water and excess ions
(details of these processes are not required)
6 Describe the role of the liver in the assimilation
of amino acids by converting them to proteins
7 State that urea is formed in the liver from excess
amino acids
8 Describe deamination as the removal of the
nitrogen-containing part of amino acids to form
urea
9 Explain the importance of excretion, limited to
toxicity of urea
"""

text14 = """
14 Coordination and response
14.1 Coordination and response
Core
1 State that electrical impulses travel along
neurones
2 Describe the mammalian nervous system in
terms of:
(a) the central nervous system (CNS) consisting
of the brain and the spinal cord
(b) the peripheral nervous system (PNS)
consisting of the nerves outside of the brain
and spinal cord
3 Describe the role of the nervous system as
coordination and regulation of body functions
4 Identify in diagrams and images sensory, relay
and motor neurones
5 Describe a simple reflex arc in terms of: receptor,
sensory neurone, relay neurone, motor neurone
and effector
6 Describe a reflex action as a means of
automatically and rapidly integrating and
coordinating stimuli with the responses of
effectors (muscles and glands)
7 Describe a synapse as a junction between two
neurones
Supplement
8 Describe the structure of a synapse, including the
presence of vesicles containing neurotransmitter
molecules, the synaptic gap and receptor
proteins
9 Describe the events at a synapse as:
(a) an impulse stimulates the release of
neurotransmitter molecules from vesicles
into the synaptic gap
(b) the neurotransmitter molecules diffuse
across the gap
(c) neurotransmitter molecules bind with
receptor proteins on the next neurone
(d) an impulse is then stimulated in the next
neurone
10 State that synapses ensure that impulses travel in
one direction only
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
28 www.cambridgeinternational.org/igcse Back to contents page
14.2 Sense organs
Core
1 Describe sense organs as groups of receptor cells
responding to specific stimuli: light, sound, touch,
temperature and chemicals
2 Identify in diagrams and images the structures of
the eye, limited to: cornea, iris, pupil, lens, retina,
optic nerve and blind spot
3 Describe the function of each part of the eye,
limited to:
(a) cornea – refracts light
(b) iris – controls how much light enters the
pupil
(c) lens – focuses light on to the retina
(d) retina – contains light receptors, some
sensitive to light of different colours
(e) optic nerve – carries impulses to the brain
4 Explain the pupil reflex, limited to changes in
light intensity and pupil diameter
Supplement
5 Explain the pupil reflex in terms of the
antagonistic action of circular and radial muscles
in the iris
6 Explain accommodation to view near and distant
objects in terms of the contraction and relaxation
of the ciliary muscles, tension in the suspensory
ligaments, shape of the lens and refraction of
light
7 Describe the distribution of rods and cones in the
retina of a human
8 Outline the function of rods and cones, limited
to:
(a) greater sensitivity of rods for night vision
(b) three different kinds of cones, absorbing light
of different colours, for colour vision
9 Identify in diagrams and images the position of
the fovea and state its function
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 29
14.3 Hormones
Core
1 Describe a hormone as a chemical substance,
produced by a gland and carried by the blood,
which alters the activity of one or more specific
target organs
2 Identify in diagrams and images specific
endocrine glands and state the hormones they
secrete, limited to:
(a) adrenal glands and adrenaline
(b) pancreas and insulin
(c) testes and testosterone
(d) ovaries and oestrogen
3 Describe adrenaline as the hormone secreted in
‘fight or flight’ situations and its effects, limited
to:
(a) increased breathing rate
(b) increased heart rate
(c) increased pupil diameter
4 Compare nervous and hormonal control, limited
to speed of action and duration of effect
Supplement
5 State that glucagon is secreted by the pancreas
6 Describe the role of adrenaline in the control of
metabolic activity, limited to:
(a) increasing the blood glucose concentration
(b) increasing heart rate
14.4 Homeostasis
Core
1 Describe homeostasis as the maintenance of a
constant internal environment
2 State that insulin decreases blood glucose
concentration
Supplement
3 Explain the concept of homeostatic control by
negative feedback with reference to a set point
4 Describe the control of blood glucose
concentration by the liver and the roles of insulin
and glucagon
5 Outline the treatment of Type 1 diabetes
6 Identify in diagrams and images of the skin: hairs,
hair erector muscles, sweat glands, receptors,
sensory neurones, blood vessels and fatty tissue
7 Describe the maintenance of a constant internal
body temperature in mammals in terms of:
insulation, sweating, shivering and the role of the
brain
8 Describe the maintenance of a constant internal
body temperature in mammals in terms of
vasodilation and vasoconstriction of arterioles
supplying skin surface capillaries
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
30 www.cambridgeinternational.org/igcse Back to contents page
14.5 Tropic responses
Core
1 Describe gravitropism as a response in which
parts of a plant grow towards or away from
gravity
2 Describe phototropism as a response in which
parts of a plant grow towards or away from the
direction of the light source
3 Investigate and describe gravitropism and
phototropism in shoots and roots
Supplement
4 Explain phototropism and gravitropism of a shoot
as examples of the chemical control of plant
growth
5 Explain the role of auxin in controlling shoot
growth, limited to:
(a) auxin is made in the shoot tip
(b) auxin diffuses through the plant from the
shoot tip
(c) auxin is unequally distributed in response to
light and gravity
(d) auxin stimulates cell elongation
"""

text15 = """
15 Drugs
15.1 Drugs
Core
1 Describe a drug as any substance taken into the
body that modifies or affects chemical reactions
in the body
2 Describe the use of antibiotics for the treatment
of bacterial infections
3 State that some bacteria are resistant to
antibiotics which reduces the effectiveness of
antibiotics
4 State that antibiotics kill bacteria but do not
affect viruses
Supplement
5 Explain how using antibiotics only when essential
can limit the development of resistant bacteria
such as MRSA
"""

text16 = """
16 Reproduction
16.1 Asexual reproduction
Core
1 Describe asexual reproduction as a process
resulting in the production of genetically
identical offspring from one parent
2 Identify examples of asexual reproduction in
diagrams, images and information provided
Supplement
3 Discuss the advantages and disadvantages of
asexual reproduction:
(a) to a population of a species in the wild
(b) to crop production
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 31
16.2 Sexual reproduction
Core
1 Describe sexual reproduction as a process
involving the fusion of the nuclei of two gametes
to form a zygote and the production of offspring
that are genetically different from each other
2 Describe fertilisation as the fusion of the nuclei of
gametes
Supplement
3 State that nuclei of gametes are haploid and that
the nucleus of a zygote is diploid
4 Discuss the advantages and disadvantages of
sexual reproduction:
(a) to a population of a species in the wild
(b) to crop production
16.3 Sexual reproduction in plants
Core
1 Identify in diagrams and images and draw the
following parts of an insect-pollinated flower:
sepals, petals, stamens, filaments, anthers,
carpels, style, stigma, ovary and ovules
2 State the functions of the structures listed in
16.3.1
3 Identify in diagrams and images and describe the
anthers and stigmas of a wind-pollinated flower
4 Distinguish between the pollen grains of
insect-pollinated and wind-pollinated flowers
5 Describe pollination as the transfer of pollen
grains from an anther to a stigma
Supplement
9 Describe self-pollination as the transfer of pollen
grains from the anther of a flower to the stigma
of the same flower or a different flower on the
same plant
10 Describe cross-pollination as the transfer of
pollen grains from the anther of a flower to the
stigma of a flower on a different plant of the
same species
11 Discuss the potential effects of self-pollination
and cross-pollination on a population, in terms of
variation, capacity to respond to changes in the
environment and reliance on pollinators
continued
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
32 www.cambridgeinternational.org/igcse Back to contents page
16.3 Sexual reproduction in plants continued
Core
6 State that fertilisation occurs when a pollen
nucleus fuses with a nucleus in an ovule
7 Describe the structural adaptations of
insect-pollinated and wind-pollinated flowers
8 Investigate and describe the environmental
conditions that affect germination of seeds,
limited to the requirement for: water, oxygen and
a suitable temperature
Supplement
12 Describe the growth of the pollen tube and its
entry into the ovule followed by fertilisation
(details of production of endosperm and
development are not required)
16.4 Sexual reproduction in humans
Core
1 Identify on diagrams and state the functions
of the following parts of the male reproductive
system: testes, scrotum, sperm ducts, prostate
gland, urethra and penis
2 Identify on diagrams and state the functions of
the following parts of the female reproductive
system: ovaries, oviducts, uterus, cervix and
vagina
3 Describe fertilisation as the fusion of the nuclei
from a male gamete (sperm) and a female
gamete (egg cell)
4 Explain the adaptive features of sperm, limited
to: flagellum, mitochondria and enzymes in the
acrosome
5 Explain the adaptive features of egg cells, limited
to: energy stores and the jelly coat that changes
at fertilisation
6 Compare male and female gametes in terms of:
size, structure, motility and numbers
7 State that in early development, the zygote
forms an embryo which is a ball of cells that
implants into the lining of the uterus
8 Identify on diagrams and state the functions of
the following in the development of the fetus:
umbilical cord, placenta, amniotic sac and
amniotic fluid
Supplement
9 Describe the function of the placenta and
umbilical cord in relation to the exchange of
dissolved nutrients, gases and excretory products
between the blood of the mother and the blood
of the fetus
10 State that some pathogens and toxins can pass
across the placenta and affect the fetus
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 33
16.5 Sexual hormones in humans
Core
1 Describe the roles of testosterone and oestrogen
in the development and regulation of secondary
sexual characteristics during puberty
2 Describe the menstrual cycle in terms of changes
in the ovaries and in the lining of the uterus
Supplement
3 Describe the sites of production of oestrogen
and progesterone in the menstrual cycle and in
pregnancy
4 Explain the role of hormones in controlling the
menstrual cycle and pregnancy, limited to FSH,
LH, progesterone and oestrogen
16.6 Sexually transmitted infections
Core
1 Describe a sexually transmitted infection (STI) as
an infection that is transmitted through sexual
contact
2 State that human immunodeficiency virus (HIV)
is a pathogen that causes an STI
3 State that HIV infection may lead to AIDS
4 Describe the methods of transmission of HIV
5 Explain how the spread of STIs is controlled
"""

text17 = """
17 Inheritance
17.1 Chromosomes, genes and proteins
Core
1 State that chromosomes are made of DNA,
which contains genetic information in the form
of genes
2 Define a gene as a length of DNA that codes for a
protein
3 Define an allele as an alternative form of a gene
4 Describe the inheritance of sex in humans with
reference to X and Y chromosomes
Supplement
5 State that the sequence of bases in a gene
determines the sequence of amino acids used to
make a specific protein (knowledge of the details
of nucleotide structure is not required)
6 Explain that different sequences of amino acids
give different shapes to protein molecules
continued
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
34 www.cambridgeinternational.org/igcse Back to contents page
17.1 Chromosomes, genes and proteins continued
Core Supplement
7 Explain that DNA controls cell function by
controlling the production of proteins, including
enzymes, membrane carriers and receptors for
neurotransmitters
8 Explain how a protein is made, limited to:
• the gene coding for the protein remains in
the nucleus
• messenger RNA (mRNA) is a copy of a gene
• mRNA molecules are made in the nucleus
and move to the cytoplasm
• the mRNA passes through ribosomes
• the ribosome assembles amino acids into
protein molecules
• the specific sequence of amino acids is
determined by the sequence of bases in the
mRNA
 (knowledge of the details of transcription or
translation is not required)
9 Explain that most body cells in an organism
contain the same genes, but many genes in a
particular cell are not expressed because the cell
only makes the specific proteins it needs
10 Describe a haploid nucleus as a nucleus
containing a single set of chromosomes
11 Describe a diploid nucleus as a nucleus containing
two sets of chromosomes
12 State that in a diploid cell, there is a pair of each
type of chromosome and in a human diploid cell
there are 23 pairs
17.2 Mitosis
Core Supplement
1 Describe mitosis as nuclear division giving rise to
genetically identical cells (details of the stages of
mitosis are not required)
2 State the role of mitosis in growth, repair of
damaged tissues, replacement of cells and
asexual reproduction
3 State that the exact replication of chromosomes
occurs before mitosis
4 State that during mitosis, the copies of
chromosomes separate, maintaining the
chromosome number in each daughter cell
5 Describe stem cells as unspecialised cells that
divide by mitosis to produce daughter cells that
can become specialised for specific functions
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 35
17.3 Meiosis
Core Supplement
1 State that meiosis is involved in the production
of gametes
2 Describe meiosis as a reduction division in which
the chromosome number is halved from diploid
to haploid resulting in genetically different cells
(details of the stages of meiosis are not required)
17.4 Monohybrid inheritance
Core
1 Describe inheritance as the transmission
of genetic information from generation to
generation
2 Describe genotype as the genetic make-up of an
organism and in terms of the alleles present
3 Describe phenotype as the observable features of
an organism
4 Describe homozygous as having two identical
alleles of a particular gene
5 State that two identical homozygous individuals
that breed together will be pure-breeding
6 Describe heterozygous as having two different
alleles of a particular gene
7 State that a heterozygous individual will not be
pure-breeding
8 Describe a dominant allele as an allele that is
expressed if it is present in the genotype
9 Describe a recessive allele as an allele that is only
expressed when there is no dominant allele of
the gene present in the genotype
10 Interpret pedigree diagrams for the inheritance of
a given characteristic
11 Use genetic diagrams to predict the results of
monohybrid crosses and calculate phenotypic
ratios, limited to 1 : 1 and 3: 1 ratios
12 Use Punnett squares in crosses which result in
more than one genotype to work out and show
the possible different genotypes
Supplement
13 Explain how to use a test cross to identify an
unknown genotype
continued
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
36 www.cambridgeinternational.org/igcse Back to contents page
17.4 Monohybrid inheritance continued
Core Supplement
14 Describe codominance as a situation in
which both alleles in heterozygous organisms
contribute to the phenotype
15 Explain the inheritance of ABO blood groups:
phenotypes are A, B, AB and O blood groups and
alleles are IA
, IB
 and Io
16 Describe a sex-linked characteristic as a feature
in which the gene responsible is located on
a sex chromosome and that this makes the
characteristic more common in one sex than in
the other
17 Describe red-green colour blindness as an
example of sex linkage
18 Use genetic diagrams to predict the results of
monohybrid crosses involving codominance or
sex linkage and calculate phenotypic ratios
"""

text18 = """
18 Variation and selection
18.1 Variation
Core
1 Describe variation as differences between
individuals of the same species
2 State that continuous variation results in a range
of phenotypes between two extremes; examples
include body length and body mass
3 State that discontinuous variation results
in a limited number of phenotypes with no
intermediates; examples include ABO blood
groups, seed shape in peas and seed colour in
peas
4 State that discontinuous variation is usually
caused by genes only and continuous variation is
caused by both genes and the environment
5 Investigate and describe examples of continuous
and discontinuous variation
6 Describe mutation as genetic change
7 State that mutation is the way in which new
alleles are formed
8 State that ionising radiation and some chemicals
increase the rate of mutation
Supplement
9 Describe gene mutation as a random change in
the base sequence of DNA
10 State that mutation, meiosis, random mating
and random fertilisation are sources of genetic
variation in populations
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 37
18.2 Adaptive features
Core
1 Describe an adaptive feature as an inherited
feature that helps an organism to survive and
reproduce in its environment
2 Interpret images or other information about a
species to describe its adaptive features
Supplement
3 Explain the adaptive features of hydrophytes and
xerophytes to their environments
18.3 Selection
Core
1 Describe natural selection with reference to:
(a) genetic variation within populations
(b) production of many offspring
(c) struggle for survival, including competition
for resources
(d) a greater chance of reproduction by
individuals that are better adapted to the
environment than others
(e) these individuals pass on their alleles to the
next generation
2 Describe selective breeding with reference to:
(a) selection by humans of individuals with
desirable features
(b) crossing these individuals to produce the
next generation
(c) selection of offspring showing the desirable
features
3 Outline how selective breeding by artificial
selection is carried out over many generations to
improve crop plants and domesticated animals
and apply this to given contexts
Supplement
4 Describe adaptation as the process, resulting
from natural selection, by which populations
become more suited to their environment over
many generations
5 Describe the development of strains of antibiotic
resistant bacteria as an example of natural
selection
6 Outline the differences between natural and
artificial selection
"""

text19 = """
19 Organisms and their environment
19.1 Energy flow
Core
1 State that the Sun is the principal source of
energy input to biological systems
2 Describe the flow of energy through living
organisms, including light energy from the
Sun and chemical energy in organisms, and its
eventual transfer to the environment
Supplement
19.2 Food chains and food webs
Core
1 Describe a food chain as showing the transfer of
energy from one organism to the next, beginning
with a producer
2 Construct and interpret simple food chains
3 Describe a food web as a network of
interconnected food chains and interpret food
webs
4 Describe a producer as an organism that makes
its own organic nutrients, usually using energy
from sunlight, through photosynthesis
5 Describe a consumer as an organism that gets its
energy by feeding on other organisms
6 State that consumers may be classed as primary,
secondary, tertiary and quaternary according to
their position in a food chain
7 Describe a herbivore as an animal that gets its
energy by eating plants
8 Describe a carnivore as an animal that gets its
energy by eating other animals
9 Describe a decomposer as an organism that gets
its energy from dead or waste organic material
10 Use food chains and food webs to describe the
impact humans have through overharvesting of
food species and through introducing foreign
species to a habitat
11 Draw, describe and interpret pyramids of
numbers and pyramids of biomass
12 Discuss the advantages of using a pyramid of
biomass rather than a pyramid of numbers to
represent a food chain
13 Describe a trophic level as the position of an
organism in a food chain, food web or ecological
pyramid
Supplement
15 Draw, describe and interpret pyramids of energy
16 Discuss the advantages of using a pyramid of
energy rather than pyramids of numbers or
biomass to represent a food chain
continued
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 39
19.2 Food chains and food webs continued
Core
14 Identify the following as the trophic levels in
food webs, food chains and ecological pyramids:
producers, primary consumers, secondary
consumers, tertiary consumers and quaternary
consumers
Supplement
17 Explain why the transfer of energy from one
trophic level to another is often not efficient
18 Explain, in terms of energy loss, why food chains
usually have fewer than five trophic levels
19 Explain why it is more energy efficient for
humans to eat crop plants than to eat livestock
that have been fed on crop plants
19.3 Nutrient cycles
Core
1 Describe the carbon cycle, limited to:
photosynthesis, respiration, feeding,
decomposition, formation of fossil fuels and
combustion
Supplement
2 Describe the nitrogen cycle with reference to:
• decomposition of plant and animal protein to
ammonium ions
• nitrification
• nitrogen fixation by lightning and bacteria
• absorption of nitrate ions by plants
• production of amino acids and proteins
• feeding and digestion of proteins
• deamination
• denitrification
3 State the roles of microorganisms in the nitrogen
cycle, limited to: decomposition, nitrification,
nitrogen fixation and denitrification (generic
names of individual bacteria, e.g. Rhizobium, are
not required)
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
40 www.cambridgeinternational.org/igcse Back to contents page
19.4 Populations
Core
1 Describe a population as a group of organisms of
one species, living in the same area, at the same
time
2 Describe a community as all of the populations
of different species in an ecosystem
3 Describe an ecosystem as a unit containing the
community of organisms and their environment,
interacting together
4 Identify and state the factors affecting the rate
of population growth for a population of an
organism, limited to food supply, competition,
predation and disease
5 Identify the lag, exponential (log), stationary
and death phases in the sigmoid curve of
population growth for a population growing in an
environment with limited resources
6 Interpret graphs and diagrams of population
growth
Supplement
7 Explain the factors that lead to each phase in
the sigmoid curve of population growth, making
reference, where appropriate, to the role of
limiting factors
"""

text20 = """
20 Human influences on ecosystems
20.1 Food supply
Core
1 Describe how humans have increased food
production, limited to:
(a) agricultural machinery to use larger areas of
land and improve efficiency
(b) chemical fertilisers to improve yields
(c) insecticides to improve quality and yield
(d) herbicides to reduce competition with weeds
(e) selective breeding to improve production by
crop plants and livestock
2 Describe the advantages and disadvantages of
large-scale monocultures of crop plants
3 Describe the advantages and disadvantages of
intensive livestock production
Supplement
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 41
20.2 Habitat destruction
Core
1 Describe biodiversity as the number of different
species that live in an area
2 Describe the reasons for habitat destruction,
including:
(a) increased area for housing, crop plant
production and livestock production
(b) extraction of natural resources
(c) freshwater and marine pollution
3 State that through altering food webs and food
chains, humans can have a negative impact on
habitats
4 Explain the undesirable effects of deforestation
as an example of habitat destruction, to include:
reducing biodiversity, extinction, loss of soil,
flooding and increase of carbon dioxide in the
atmosphere
Supplement
20.3 Pollution
Core
1 Describe the effects of untreated sewage and
excess fertiliser on aquatic ecosystems
2 Describe the effects of non-biodegradable
plastics, in both aquatic and terrestrial
ecosystems
3 Describe the sources and effects of pollution of
the air by methane and carbon dioxide, limited
to: the enhanced greenhouse effect and climate
change
Supplement
4 Explain the process of eutrophication of water,
limited to:
• increased availability of nitrate and other
ions
• increased growth of producers
• increased decomposition after death of
producers
• increased aerobic respiration by decomposers
• reduction in dissolved oxygen
• death of organisms requiring dissolved
oxygen in water
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
42 www.cambridgeinternational.org/igcse Back to contents page
20.4 Conservation
Core
1 Describe a sustainable resource as one which is
produced as rapidly as it is removed from the
environment so that it does not run out
2 State that some resources can be conserved and
managed sustainably, limited to forests and fish
stocks
3 Explain why organisms become endangered
or extinct, including: climate change, habitat
destruction, hunting, overharvesting, pollution
and introduced species
4 Describe how endangered species can be
conserved, limited to:
(a) monitoring and protecting species and
habitats
(b) education
(c) captive breeding programmes
(d) seed banks
Supplement
5 Explain how forests can be conserved using:
education, protected areas, quotas and replanting
6 Explain how fish stocks can be conserved using:
education, closed seasons, protected areas,
controlled net types and mesh size, quotas and
monitoring
7 Describe the reasons for conservation
programmes, limited to:
(a) maintaining or increasing biodiversity
(b) reducing extinction
(c) protecting vulnerable ecosystems
(d) maintaining ecosystem functions, limited
to nutrient cycling and resource provision,
including food, drugs, fuel and genes
8 Describe the use of artificial insemination (AI)
and in vitro fertilisation (IVF) in captive breeding
programmes
9 Explain the risks to a species if its population size
decreases, reducing genetic variation (knowledge
of genetic drift is not required) 
"""

text21 = """
21 Biotechnology and genetic modification
21.1 Biotechnology and genetic modification
Core
1 State that bacteria are useful in biotechnology
and genetic modification due to their rapid
reproduction rate and their ability to make
complex molecules
Supplement
2 Discuss why bacteria are useful in biotechnology
and genetic modification, limited to:
(a) few ethical concerns over their manipulation
and growth
(b) the presence of plasmids
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 43
21.2 Biotechnology
Core
1 Describe the role of anaerobic respiration in yeast
during the production of ethanol for biofuels
2 Describe the role of anaerobic respiration in yeast
during bread-making
3 Describe the use of pectinase in fruit juice
production
4 Investigate and describe the use of biological
washing powders that contain enzymes
Supplement
5 Explain the use of lactase to produce lactose-free
milk
6 Describe how fermenters can be used for the
large-scale production of useful products by
bacteria and fungi, including insulin, penicillin and
mycoprotein
7 Describe and explain the conditions that need to be
controlled in a fermenter, including: temperature,
pH, oxygen, nutrient supply and waste products
21.3 Genetic modification
Core
1 Describe genetic modification as changing the
genetic material of an organism by removing,
changing or inserting individual genes
Supplement
3 Outline the process of genetic modification using
bacterial production of a human protein as an
example, limited to:
(a) isolation of the DNA making up a human
gene using restriction enzymes, forming
sticky ends
(b) cutting of bacterial plasmid DNA with
the same restriction enzymes, forming
complementary sticky ends
(c) insertion of human DNA into bacterial
plasmid DNA using DNA ligase to form a
recombinant plasmid
(d) insertion of recombinant plasmids into
bacteria (specific details are not required)
(e) multiplication of bacteria containing
recombinant plasmids
(f) expression in bacteria of the human gene to
make the human protein
continued
Cambridge IGCSE Biology 0610 syllabus for 2023, 2024 and 2025. Subject content
44 www.cambridgeinternational.org/igcse Back to contents page
21.3 Genetic modification continued
Core
2 Outline examples of genetic modification:
(a) the insertion of human genes into bacteria to
produce human proteins
(b) the insertion of genes into crop plants to
confer resistance to herbicides
(c) the insertion of genes into crop plants to
confer resistance to insect pests
(d) the insertion of genes into crop plants to
improve nutritional qualities
Supplement
4 Discuss the advantages and disadvantages of
genetically modifying crops, including soya,
maize and rice
"""


textarr = [text, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11,
           text12,text13,text14,text15,text16,text17,text18,text19,text20,text21]
for i in range(len(textarr)):
    textarr[i] = getFormattedTextfromPdf.formatText(textarr[i])

trainModels.train(textarr, allLabels)
