import trainModels
import getFormattedTextfromPdf


allLabels = ['Energy and respiration', 'Photosynthesis', 
             'Homeostasis', 'Control and coordination', 'Inheritance', 'Selection and evolution', 'Classification, biodiversity and conservation',
               'Genetic technology']


text = """
Energy is a fundamental concept in biology. All living organisms require a source of cellular energy to drive their 
various activities. All organisms respire by using enzyme-catalysed reactions to release energy from energy-rich 
molecules such as glucose and fatty acids and transfer that energy to ATP. ATP is the universal energy currency 
of cells. In eukaryotes, aerobic respiration occurs in mitochondria.
 The practical activities in this topic give opportunities for candidates to plan investigations, analyse and interpret 
data and evaluate experimental procedures and the quality of the data collected.
 12.1 Energy 
Learning outcomes 
Candidates should be able to:
 1 outline the need for energy in living organisms, as illustrated 
by active transport, movement and anabolic reactions, such as 
those occurring in DNA replication and protein synthesis
 2 describe the features of ATP that make it suitable as the 
universal energy currency
 3 state that ATP is synthesised by:
 • transfer of phosphate in substrate-linked reactions 
• chemiosmosis in membranes of mitochondria and 
chloroplasts
 4 explain the relative energy values of carbohydrates, lipids and 
proteins as respiratory substrates 
5 state that the respiratory quotient (RQ) is the ratio of the 
number of molecules of carbon dioxide produced to the number 
of molecules of oxygen taken in, as a result of respiration
 6 calculate RQ values of different respiratory substrates from 
equations for respiration
 7 describe and carry out investigations, using simple 
respirometers, to determine the RQ of germinating seeds or 
small invertebrates (e.g. blowfly larvae)
 12.2 Respiration
 Learning outcomes 
Candidates should be able to:
 1 State where each of the four stages in aerobic respiration occurs 
in eukaryotic cells: 
• glycolysis in the cytoplasm 
• link reaction in the mitochondrial matrix 
• Krebs cycle in the mitochondrial matrix  
• oxidative phosphorylation on the inner membrane of 
mitochondria  
2 outline glycolysis as phosphorylation of glucose and the 
subsequent splitting of fructose 1,6-bisphosphate (6C) into 
two triose phosphate molecules (3C), which are then further 
oxidised to pyruvate (3C), with the production of ATP and 
reduced NAD
 3 explain that, when oxygen is available, pyruvate enters 
mitochondria to take part in the link reaction
 Back to contents page
 continued
 29
 www.cambridgeinternational.org/alevel
Cambridge International AS & A Level Biology 9700 syllabus for 2022, 2023 and 2024. Subject content  
12.2 Respiration continued
 Learning outcomes 
Candidates should be able to:
 4 describe the link reaction, including the role of coenzyme A in 
the transfer of acetyl (2C) groups
 5 outline the Krebs cycle, explaining that oxaloacetate (4C) acts 
as an acceptor of the 2C fragment from acetyl coenzyme A to 
form citrate (6C), which is converted back to oxaloacetate in a 
series of small steps
 6 explain that reactions in the Krebs cycle involve decarboxylation 
and dehydrogenation and the reduction of the coenzymes NAD 
and FAD
 7 describe the role of NAD and FAD in transferring hydrogen to 
carriers in the inner mitochondrial membrane 
8 explain that during oxidative phosphorylation:
 • hydrogen atoms split into protons and energetic electrons 
• energetic electrons release energy as they pass through 
the electron transport chain (details of carriers are not 
expected) 
• the released energy is used to transfer protons across the 
inner mitochondrial membrane
 • protons return to the mitochondrial matrix by facilitated 
diffusion through ATP synthase, providing energy for ATP 
synthesis (details of ATP synthase are not expected)
 • oxygen acts as the final electron acceptor to form water 
9 describe the relationship between the structure and function of 
mitochondria using diagrams and electron micrographs
 10 outline respiration in anaerobic conditions in mammals (lactate 
fermentation) and in yeast cells (ethanol fermentation)
 11 explain why the energy yield from respiration in aerobic 
conditions is much greater than the energy yield from 
respiration in anaerobic conditions (a detailed account of the 
total yield of ATP from the aerobic respiration of glucose is not 
expected)
 12 explain how rice is adapted to grow with its roots submerged 
in water, limited to the development of aerenchyma in roots, 
ethanol fermentation in roots and faster growth of stems
 13 describe and carry out investigations using redox indicators, 
including DCPIP and methylene blue, to determine the effects 
of temperature and substrate concentration on the rate of 
respiration of yeast 
14 describe and carry out investigations using simple respirometers 
to determine the effect of temperature on the rate of 
respiration
"""

text2 = """
 Photosynthesis is the energy transfer process that is the basis of nearly all life on Earth. It provides energy 
directly or indirectly to all the organisms in most food chains. In eukaryotes, the process occurs within 
chloroplasts. Candidates should apply their knowledge of plant cells from Cell structure (Topic 1) and leaf 
structure from Transport in plants (Topic 7) while studying photosynthesis. Various environmental factors 
influence the rate at which photosynthesis occurs.
 The practical activities in this topic give opportunities for candidates to plan investigations, analyse and interpret 
data and evaluate experimental procedures and the quality of the data that they collect.
 13.1 Photosynthesis as an energy  
transfer process 
Learning outcomes 
Candidates should be able to:
 1 describe the relationship between the structure of chloroplasts, 
as shown in diagrams and electron micrographs, and their 
function
 2 explain that energy transferred as ATP and reduced NADP from 
the light-dependent stage is used during the light-independent 
stage (Calvin cycle) of photosynthesis to produce complex 
organic molecules
 3 state that within a chloroplast, the thylakoids (thylakoid 
membranes and thylakoid spaces), which occur in stacks called 
grana, are the site of the light-dependent stage and the stroma 
is the site of the light-independent stage
 4 describe the role of chloroplast pigments (chlorophyll a, 
chlorophyll b, carotene and xanthophyll) in light absorption in 
thylakoids
 5 interpret absorption spectra of chloroplast pigments and action 
spectra for photosynthesis 
6 describe and use chromatography to separate and identify 
chloroplast pigments (reference should be made to Rf
 values in 
identification of chloroplast pigments)
 7 state that cyclic photophosphorylation and non-cyclic 
photophosphorylation occur during the light-dependent stage 
of photosynthesis
 8 explain that in cyclic photophosphorylation:
 • only photosystem I (PSI) is involved 
• photoactivation of chlorophyll occurs
 • ATP is synthesised 
9 explain that in non-cyclic photophosphorylation:
 • photosystem I (PSI) and photosystem II (PSII) are both 
involved 
• photoactivation of chlorophyll occurs
 • the oxygen-evolving complex catalyses the photolysis of 
water
 • ATP and reduced NADP are synthesised 
continued
 Back to contents page
 31
 www.cambridgeinternational.org/alevel
Cambridge International AS & A Level Biology 9700 syllabus for 2022, 2023 and 2024. Subject content  
13.1 Photosynthesis as an energy  
transfer process continued
 Learning outcomes 
Candidates should be able to:
 10 explain that during photophosphorylation:
 • energetic electrons release energy as they pass through 
the electron transport chain (details of carriers are not 
expected) 
• the released energy is used to transfer protons across the 
thylakoid membrane
 • protons return to the stroma from the thylakoid space by 
facilitated diffusion through ATP synthase, providing energy 
for ATP synthesis (details of ATP synthase are not expected)
 11 outline the three main stages of the Calvin cycle:
 • rubisco catalyses the fixation of carbon dioxide  
by combination with a molecule of  
ribulose bisphosphate (RuBP), a 5C compound, to yield two 
molecules of glycerate 3-phosphate (GP), a 3C compound
 • GP is reduced to triose phosphate (TP) in reactions involving 
reduced NADP and ATP
 • RuBP is regenerated from TP in reactions that use ATP
 12 state that Calvin cycle intermediates are used to produce other 
molecules, limited to GP to produce some amino acids and TP 
to produce carbohydrates, lipids and amino acids  
13.2 Investigation of limiting  
factors
 Learning outcomes 
Candidates should be able to:
 1 state that light intensity, carbon dioxide concentration and 
temperature are examples of limiting factors of photosynthesis
 2 explain the effects of changes in light intensity, carbon dioxide 
concentration and temperature on the rate of photosynthesis
 3 describe and carry out investigations using redox indicators, 
including DCPIP and methylene blue, and a suspension of 
chloroplasts to determine the effects of light intensity and light 
wavelength on the rate of photosynthesis 
4 describe and carry out investigations using whole plants, 
including aquatic plants, to determine the effects of light 
intensity, carbon dioxide concentration and temperature on the 
rate of photosynthesis 
"""

text3 = """
Cells function most efficiently if they are kept in near optimum conditions. Cells in multicellular animals are 
surrounded by tissue fluid. The composition of tissue fluid is kept constant by exchanges with the blood as 
discussed in the topic on Transport in mammals (Topic 8). In mammals, core temperature, blood glucose 
concentration and blood water potential are maintained within narrow limits to ensure the efficient operation of 
cells. Prior knowledge for this topic includes an understanding that waste products are excreted from the body 
and an outline of the structure and function of the nervous and endocrine systems. In plants, guard cells respond 
to fluctuations in environmental conditions and open and close stomata as appropriate for photosynthesis and 
conserving water.
 14.1 Homeostasis in mammals 
Learning outcomes 
Candidates should be able to:
 1 explain what is meant by homeostasis and the importance of 
homeostasis in mammals 
2 explain the principles of homeostasis in terms of internal and 
external stimuli, receptors, coordination systems (nervous 
system and endocrine system), effectors (muscles and glands) 
and negative feedback
 3 state that urea is produced in the liver from the deamination of 
excess amino acids 
4 describe the structure of the human kidney, limited to:
 • fibrous capsule
 • cortex
 • medulla
 • renal pelvis
 • ureter 
• branches of the renal artery and renal vein
 5 Identify, in diagrams, photomicrographs and electron 
micrographs, the parts of a nephron and its associated blood 
vessels and structures, limited to: 
• glomerulus
 • Bowman’s capsule
 • proximal convoluted tubule
 • loop of Henle
 • distal convoluted tubule 
• collecting duct
 6 describe and explain the formation of urine in the nephron, 
limited to:
 • the formation of glomerular filtrate by ultrafiltration in the 
Bowman’s capsule
 • selective reabsorption in the proximal convoluted tubule
 7 relate the detailed structure of the Bowman’s capsule and 
proximal convoluted tubule to their functions in the formation 
of urine
 8 describe the roles of the hypothalamus, posterior pituitary 
gland, antidiuretic hormone (ADH), aquaporins and collecting 
ducts in osmoregulation 
continued
 Back to contents page
 33
 www.cambridgeinternational.org/alevel
Cambridge International AS & A Level Biology 9700 syllabus for 2022, 2023 and 2024. Subject content  
14.1 Homeostasis in mammals  
continued
 Learning outcomes 
Candidates should be able to:
 9 describe the principles of cell signalling using the example of the 
control of blood glucose concentration by glucagon, limited to:
 • binding of hormone to cell surface receptor causing 
conformational change
 • activation of G-protein leading to stimulation of adenylyl 
cyclase
 • formation of the second messenger, cyclic AMP (cAMP)
 • activation of protein kinase A by cAMP leading to initiation 
of an enzyme cascade
 • amplification of the signal through the enzyme cascade 
as a result of activation of more and more enzymes by 
phosphorylation
 • cellular response in which the final enzyme in the pathway 
is activated, catalysing the breakdown of glycogen
 10 explain how negative feedback control mechanisms regulate 
blood glucose concentration, with reference to the effects of 
insulin on muscle cells and liver cells and the effect of glucagon 
on liver cells 
11 explain the principles of operation of test strips and biosensors 
for measuring the concentration of glucose in blood and urine, 
with reference to glucose oxidase and peroxidase enzymes
 14.2 Homeostasis in plants
 Learning outcomes 
Candidates should be able to:
 1 explain that stomata respond to changes in environmental 
conditions by opening and closing and that regulation of 
stomatal aperture balances the need for carbon dioxide 
uptake by diffusion with the need to minimise water loss by 
transpiration
 2 explain that stomata have daily rhythms of opening and closing
 3 describe the structure and function of guard cells and explain 
the mechanism by which they open and close stomata
 4 describe the role of abscisic acid in the closure of stomata 
during times of water stress, including the role of calcium ions 
as a second messenger 
"""

text4 = """
 All the activities of multicellular organisms require coordinating, some very rapidly and some more slowly. The 
nervous system and the endocrine system provide coordination in mammals. Coordination systems also exist in 
plants.
 15.1 Control and coordination in  
mammals 
Learning outcomes 
Candidates should be able to:
 1 describe the features of the endocrine system with reference to 
the hormones ADH, glucagon and insulin (see 14.1.8, 14.1.9 and 
14.1.10)
 2 compare the features of the nervous system and the endocrine 
system 
3 describe the structure and function of a sensory neurone and a 
motor neurone and state that intermediate neurones connect 
sensory neurones and motor neurones
 4 outline the role of sensory receptor cells in detecting stimuli and 
stimulating the transmission of impulses in sensory neurones 
5 describe the sequence of events that results in an action 
potential in a sensory neurone, using a chemoreceptor cell in a 
human taste bud as an example 
6 describe and explain changes to the membrane potential of 
neurones, including:
 • how the resting potential is maintained  
• the events that occur during an action potential
 • how the resting potential is restored during the refractory 
period 
7 describe and explain the rapid transmission of an impulse in a 
myelinated neurone with reference to saltatory conduction
 8 explain the importance of the refractory period in determining 
the frequency of impulses 
9 describe the structure of a cholinergic synapse and explain how 
it functions, including the role of calcium ions
 10 describe the roles of neuromuscular junctions, the T-tubule 
system and sarcoplasmic reticulum in stimulating contraction in 
striated muscle
 11 describe the ultrastructure of striated muscle with reference to 
sarcomere structure using electron micrographs and diagrams 
12 explain the sliding filament model of muscular contraction 
including the roles of troponin, tropomyosin, calcium ions and 
ATP
 15.2 Control and coordination in  
plants
 Learning outcomes 
Candidates should be able to:
 1 describe the rapid response of the Venus fly trap to stimulation 
of hairs on the lobes of modified leaves and explain how the 
closure of the trap is achieved
 2 explain the role of auxin in elongation growth by stimulating 
proton pumping to acidify cell walls
 3 describe the role of gibberellin in the germination of barley (see 
16.3.4)
"""

text5 = """
Genetic information is transmitted from generation to generation to maintain the continuity of life. In sexual 
reproduction, meiosis introduces genetic variation so that offspring resemble their parents but are not identical 
to them. Genetic crosses reveal how some features are inherited. The phenotype of organisms is determined 
partly by the genes that they have inherited and partly by the effect of the environment. Genes determine how 
organisms develop; gene control in bacteria gives us a glimpse of this process in action.
 16.1 Passage of information from  
parents to offspring 
Learning outcomes 
Candidates should be able to:
 1 explain the meanings of the terms haploid (n) and diploid (2n)
 2 explain what is meant by homologous pairs of chromosomes
 3 explain the need for a reduction division during meiosis in the 
production of gametes 
4 describe the behaviour of chromosomes in plant and animal 
cells during meiosis and the associated behaviour of the nuclear 
envelope, the cell surface membrane and the spindle (names 
of the main stages of meiosis, but not the sub-divisions of 
prophase I, are expected: prophase I, metaphase I,  
anaphase I, telophase I, prophase II, metaphase II, anaphase II 
and telophase II)
 5 interpret photomicrographs and diagrams of cells in different 
stages of meiosis and identify the main stages of meiosis 
6 explain that crossing over and random orientation (independent 
assortment) of pairs of homologous chromosomes and sister 
chromatids during meiosis produces genetically different 
gametes 
7 explain that the random fusion of gametes at fertilisation 
produces genetically different individuals 
16.2 The roles of genes in  
determining the phenotype
 Learning outcomes 
Candidates should be able to:
 1 explain the terms gene, locus, allele, dominant, recessive, 
codominant, linkage, test cross, F1, F2, phenotype, genotype, 
homozygous and heterozygous
 2 interpret and construct genetic diagrams, including Punnett 
squares, to explain and predict the results of monohybrid 
crosses and dihybrid crosses that involve dominance, 
codominance, multiple alleles and sex linkage
 3 interpret and construct genetic diagrams, including Punnett 
squares, to explain and predict the results of dihybrid crosses 
that involve autosomal linkage and epistasis (knowledge of the 
expected ratios for different types of epistasis is not expected)
 4 interpret and construct genetic diagrams, including Punnett 
squares, to explain and predict the results of test crosses
 5 use the chi-squared test to test the significance of differences 
between observed and expected results (the formula for the 
chi-squared test will be provided, as shown in the Mathematical 
requirements)
 continued
 36
 Back to contents page
 www.cambridgeinternational.org/alevel
Cambridge International AS & A Level Biology 9700 syllabus for 2022, 2023 and 2024. Subject content  
16.2 The roles of genes in  
determining the phenotype  
continued
 Learning outcomes 
Candidates should be able to:
 6 explain the relationship between genes, proteins and phenotype 
with respect to the: 
• TYR gene, tyrosinase and albinism 
• HBB gene, haemoglobin and sickle cell anaemia 
• F8 gene, factor VIII and haemophilia 
• HTT gene, huntingtin and Huntington’s disease 
7 explain the role of gibberellin in stem elongation including 
the role of the dominant allele, Le, that codes for a functional 
enzyme in the gibberellin synthesis pathway, and the recessive 
allele, le, that codes for a non-functional enzyme
 16.3 Gene control
 Learning outcomes 
Candidates should be able to:
 1 describe the differences between structural genes and 
regulatory genes and the differences between repressible 
enzymes and inducible enzymes
 2 explain genetic control of protein production in a prokaryote 
using the lac operon (knowledge of the role of cAMP is not 
expected) 
3 state that transcription factors are proteins that bind to DNA 
and are involved in the control of gene expression in eukaryotes 
by decreasing or increasing the rate of transcription  
4 explain how gibberellin activates genes by causing the 
breakdown of DELLA protein repressors, which normally inhibit 
factors that promote transcription
"""

text6 = """
17 Selection and evolution
 In 1858, Charles Darwin and Alfred Russel Wallace proposed a theory of natural selection to account for the 
evolution of species. A year later, Darwin published On the Origin of Species, providing evidence for the way in 
which aspects of the environment act as agents of selection and determine which phenotypic forms survive and 
which do not. The individuals best adapted to the prevailing conditions are most likely to succeed in the ‘struggle 
for existence’.
 17.1 Variation
 Learning outcomes 
Candidates should be able to:
 1 explain, with examples, that phenotypic variation is due to 
genetic factors or environmental factors or a combination of 
genetic and environmental factors 
2 explain what is meant by discontinuous variation and 
continuous variation
 3 explain the genetic basis of discontinuous variation and 
continuous variation 
4 use the t-test to compare the means of two different samples 
(the formula for the t-test will be provided, as shown in the 
Mathematical requirements)
 17.2 Natural and artificial  
selection
 Learning outcomes 
Candidates should be able to:
 1 explain that natural selection occurs because populations 
have the capacity to produce many offspring that compete for 
resources; in the ‘struggle for existence’, individuals that are 
best adapted are most likely to survive to reproduce and pass on 
their alleles to the next generation
 2 explain how environmental factors can act as stabilising, 
disruptive and directional forces of natural selection
 3 explain how selection, the founder effect and genetic drift, 
including the bottleneck effect, may affect allele frequencies in 
populations
 4 outline how bacteria become resistant to antibiotics as an 
example of natural selection 
5 use the Hardy–Weinberg principle to calculate allele and 
genotype frequencies in populations and state the conditions 
when this principle can be applied (the two equations for the 
Hardy–Weinberg principle will be provided, as shown in the 
Mathematical requirements)
 6 describe the principles of selective breeding (artificial selection) 
7 outline the following examples of selective breeding:
 • the introduction of disease resistance to varieties of wheat 
and rice
 • inbreeding and hybridisation to produce vigorous, uniform 
varieties of maize
 • improving the milk yield of dairy cattle 
38
 Back to contents page
 www.cambridgeinternational.org/alevel
Cambridge International AS & A Level Biology 9700 syllabus for 2022, 2023 and 2024. Subject content  
17.3 Evolution
 Learning outcomes 
Candidates should be able to:
 1 outline the theory of evolution as a process leading to the 
formation of new species from pre-existing species over time, as 
a result of changes to gene pools from generation to generation
 2 discuss how DNA sequence data can show evolutionary 
relationships between species 
3 explain how speciation may occur as a result of genetic isolation 
by: 
• geographical separation (allopatric speciation)
 • ecological and behavioural separation (sympatric 
speciation)
"""

text7 = """
18 Classification, biodiversity and conservation
 Classification systems attempt to order all the organisms that exist on Earth according to their characteristics 
and evolutionary relationships with one another. There are opportunities in this topic for candidates to observe 
different species in their locality and assess species distribution and abundance. Fieldwork is an important part 
of a biological education because it provides opportunities to appreciate and analyse biodiversity, and to study 
the interactions between organisms and their environment. The biodiversity of the Earth is threatened by human 
activities and climate change. Conserving biodiversity is a difficult task; individuals, local groups, national and 
international organisations can all make significant contributions. Candidates should appreciate the threats to 
biodiversity and consider some of the steps taken in conservation, both locally and globally.
 18.1 Classification
 Learning outcomes 
Candidates should be able to:
 1 discuss the meaning of the term species, limited to the 
biological species concept, morphological species concept and 
ecological species concept
 2 describe the classification of organisms into three domains: 
Archaea, Bacteria and Eukarya
 3 state that Archaea and Bacteria are prokaryotes and that 
there are differences between them, limited to differences in 
membrane lipids, ribosomal RNA and composition of cell walls 
4 describe the classification of organisms in the Eukarya domain 
into the taxonomic hierarchy of kingdom, phylum, class, order, 
family, genus and species
 5 outline the characteristic features of the kingdoms Protoctista, 
Fungi, Plantae and Animalia
 6 outline how viruses are classified, limited to the type of nucleic 
acid (RNA or DNA) and whether this is single stranded or double 
stranded 
18.2 Biodiversity
 Learning outcomes 
Candidates should be able to:
 1 define the terms ecosystem and niche
 2 explain that biodiversity can be assessed at different levels, 
including:
 • the number and range of different ecosystems and habitats 
• the number of species and their relative abundance
 • the genetic variation within each species
 3 explain the importance of random sampling in determining the 
biodiversity of an area
 4 describe and use suitable methods to assess the distribution and 
abundance of organisms in an area, limited to frame quadrats, 
line transects, belt transects and mark-release-recapture using 
the Lincoln index (the formula for the Lincoln index will be 
provided, as shown in the Mathematical requirements) 
continued
 40
 Back to contents page
 www.cambridgeinternational.org/alevel
Cambridge International AS & A Level Biology 9700 syllabus for 2022, 2023 and 2024. Subject content  
18.2 Biodiversity continued
 Learning outcomes 
Candidates should be able to:
 5 use Spearman’s rank correlation and Pearson’s linear correlation 
to analyse the relationships between two variables, including 
how biotic and abiotic factors affect the distribution and 
abundance of species (the formulae for these correlations will 
be provided, as shown in the Mathematical requirements)
 6 use Simpson’s index of diversity (D) to calculate the biodiversity 
of an area, and state the significance of different values of D 
(the formula for Simpson’s index of diversity will be provided, as 
shown in the Mathematical requirements) 
18.3 Conservation
 Learning outcomes 
Candidates should be able to:
 1 explain why populations and species can become extinct as a 
result of:
 • climate change
 • competition
 • hunting by humans
 • degradation and loss of habitats
 2 outline reasons for the need to maintain biodiversity
 3 outline the roles of zoos, botanic gardens, conserved areas 
(including national parks and marine parks), ‘frozen zoos’ and 
seed banks, in the conservation of endangered species
 4 describe methods of assisted reproduction used in the 
conservation of endangered mammals, limited to IVF, embryo 
transfer and surrogacy
 5 explain reasons for controlling invasive alien species
 6 outline the role in conservation of the International Union for 
the Conservation of Nature (IUCN) and the Convention on 
International Trade in Endangered Species of Wild Fauna and 
Flora (CITES)
"""

text8 = """
19 Genetic technology
 The discovery in the early 1950s of the structure of DNA by Watson and Crick, supported by the work of 
Franklin, Wilkins and Chargaff, and discoveries since, have led to many applications of genetic technology in 
areas of medicine, agriculture and forensic science. This topic relies heavily on prior knowledge of DNA and RNA 
structure and protein synthesis from the topic on Nucleic acids and protein synthesis (Topic 6). 
Candidates will benefit from carrying out practical work using electrophoresis, either with DNA or specially 
prepared dyes used to represent DNA.
 19.1 Principles of genetic  
technology
 Learning outcomes 
Candidates should be able to:
 1 define the term recombinant DNA
 2 explain that genetic engineering is the deliberate manipulation 
of genetic material to modify specific characteristics of an 
organism and that this may involve transferring a gene into an 
organism so that the gene is expressed 
3 explain that genes to be transferred into an organism may be: 
• extracted from the DNA of a donor organism 
• synthesised from the mRNA of a donor organism
 • synthesised chemically from nucleotides 
4 explain the roles of restriction endonucleases, DNA ligase, 
plasmids, DNA polymerase and reverse transcriptase in the 
transfer of a gene into an organism
 5 explain why a promoter may have to be transferred into an 
organism as well as the desired gene 
6 explain how gene expression may be confirmed by the use of 
marker genes coding for fluorescent products
 7 explain that gene editing is a form of genetic engineering 
involving the insertion, deletion or replacement of DNA at 
specific sites in the genome
 8 describe and explain the steps involved in the polymerase chain 
reaction (PCR) to clone and amplify DNA, including the role of 
Taq polymerase
 9 describe and explain how gel electrophoresis is used to separate 
DNA fragments of different lengths
 10 outline how microarrays are used in the analysis of genomes 
and in detecting mRNA in studies of gene expression
 11 outline the benefits of using databases that provide information 
about nucleotide sequences of genes and genomes, and amino 
acid sequences of proteins and protein structures  
42
 Back to contents page
 www.cambridgeinternational.org/alevel
Cambridge International AS & A Level Biology 9700 syllabus for 2022, 2023 and 2024. Subject content  
19.2 Genetic technology applied 
to medicine
 Learning outcomes 
Candidates should be able to:
 1 explain the advantages of using recombinant human proteins 
to treat disease, using the examples insulin, factor VIII and 
adenosine deaminase 
2 outline the advantages of genetic screening, using the examples 
of breast cancer (BRCA1 and BRCA2), Huntington’s disease and 
cystic fibrosis
 3 outline how genetic diseases can be treated with gene therapy, 
using the examples severe combined immunodeficiency (SCID) 
and inherited eye diseases
 4 discuss the social and ethical considerations of using genetic 
screening and gene therapy in medicine 
19.3 Genetically modified  
organisms in agriculture
 Learning outcomes 
Candidates should be able to:
 1 explain that genetic engineering may help to solve the global 
demand for food by improving the quality and productivity of 
farmed animals and crop plants, using the examples of  
GM salmon, herbicide resistance in soybean and insect 
resistance in cotton
 2 discuss the ethical and social implications of using genetically 
modified organisms (GMOs) in food production
"""

textarr = [text, text2, text3, text4, text5, text6, text7, text8]
for i in range(len(textarr)):
    textarr[i] = getFormattedTextfromPdf.formatText(textarr[i])

trainModels.train(textarr, allLabels)
