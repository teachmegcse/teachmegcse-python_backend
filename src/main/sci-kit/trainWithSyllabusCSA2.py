import trainModels
import getFormattedTextfromPdf


allLabels = ['Data Representation', 'Communication and internet technologies', 
             'Hardware and Virtual Machines', 'System Software', 'Security',
               'Artificial Intelligence (AI)', 'Computational thinking and Problem-solving',
               'Further Programming']

text = """
13 Data Representation
13.1 User-defined data types
Candidates should be able to:
Show understanding of why user-defined types are
necessary
Notes and guidance
Define and use non-composite types Including enumerated, pointer
Define and use composite data types Including set, record and class/object
Choose and design an appropriate user-defined
data type for a given problem
13.2 File organisation and access
Candidates should be able to:
Show understanding of the methods of file
organisation and select an appropriate method of
file organisation and file access for a given problem
Notes and guidance
Including serial, sequential (using a key field),
random (using a record key)
Show understanding of methods of file access Including
Sequential access for serial and sequential files
Direct access for sequential and random files
Show understanding of hashing algorithms Describe and use different hashing algorithms to
read from and write data to a random/ sequential file
13.3 Floating-point numbers, representation and manipulation
Candidates should be able to:
Describe the format of binary floating-point real
numbers
Notes and guidance
Use two’s complement form
Understand of the effects of changing the allocation
of bits to mantissa and exponent in a floating-point
representation
Convert binary floating-point real numbers into
denary and vice versa
Normalise floating-point numbers Understand the reasons for normalisation
Show understanding of the consequences of a
binary representation only being an approximation
to the real number it represents (in certain cases)
Understand how underflow and overflow can occur
Show understanding that binary representations
can give rise to rounding errors
"""

text2 = """
14 Communication and internet technologies
14.1 Protocols
Candidates should be able to:
Show understanding of why a protocol is essential
for communication between computers
Notes and guidance
Show understanding of how protocol
implementation can be viewed as a stack, where
each layer has its own functionality
Show understanding of the TCP/IP protocol suite Four Layers (Application, Transport, Internet, Link)
Purpose and function of each layer
Application when a message is sent from one host
to another on the internet
Show understanding of protocols (HTTP, FTP,
POP3, IMAP, SMTP, BitTorrent) and their purposes
BitTorrent protocol provides peer-to-peer file sharing
14.2 Circuit switching, packet switching
Candidates should be able to:
Show understanding of circuit switching
Notes and guidance
Benefits, drawbacks and where it is applicable
Show understanding of packet switching Benefits, drawbacks and where it is applicable
Show understanding of the function of a router in
packet switching
Explain how packet switching is used to pass
messages across a network, including the internet
"""

text3 = """
15 Hardware and Virtual Machines
15.1 Processors, Parallel Processing and Virtual Machines
Candidates should be able to:
Show understanding of Reduced Instruction Set
Computers (RISC) and Complex Instruction Set
Computers (CISC) processors
Notes and guidance
Differences between RISC and CISC
Understand interrupt handling on CISC and RISC
processors
Show understanding of the importance/use of
pipelining and registers in RISC processors
Show understanding of the four basic computer
architectures
SISD, SIMD, MISD, MIMD
Show understanding of the characteristics of
massively parallel computers
Show understanding of the concept of a virtual
machine
Give examples of the role of virtual machines
Understand the benefits and limitations of virtual
machines
15.2 Boolean Algebra and Logic Circuits
Candidates should be able to:
Produce truth tables for logic circuits including half
adders and full adders
Notes and guidance
May include logic gates with more than two inputs
Show understanding of a flip-flop (SR, JK) Draw a logic circuit and derive a truth table for a
flip-flop
Understand of the role of flip-flops as data storage
elements
Show understanding of Boolean algebra Understand De Morgan’s laws
Perform Boolean algebra using De Morgan’s laws
Simplify a logic circuit/expression using Boolean
algebra
Show understanding of Karnaugh maps (K-map) Understand of the benefits of using Karnaugh maps
Solve logic problems using Karnaugh maps
"""

text4 = """
16 System Software
16.1 Purposes of an Operating System (OS)
Candidates should be able to:
Show understanding of how an OS can maximise
the use of resources
Notes and guidance
Describe the ways in which the user interface hides
the complexities of the hardware from the user
Show understanding of process management The concept of multi-tasking and a process
The process states: running, ready and blocked
The need for scheduling and the function and
benefits of different scheduling routines (including
round robin, shortest job first, first come first served,
shortest remaining time)
How the kernel of the OS acts as an interrupt
handler and how interrupt handling is used to
manage low-level scheduling
Show understanding of virtual memory, paging and
segmentation for memory management
The concepts of paging, virtual memory and
segmentation
The difference between paging and segmentation
How pages can be replaced
How disk thrashing can occur
16.2 Translation Software
Candidates should be able to:
Show understanding of how an interpreter can
execute programs without producing a translated
version
Notes and guidance
Show understanding of the various stages in the
compilation of a program
Including lexical analysis, syntax analysis, code
generation and optimisation
Show understanding of how the grammar of a
language can be expressed using syntax diagrams
or Backus-Naur Form (BNF) notation
Show understanding of how Reverse Polish
Notation (RPN) can be used to carry out the
evaluation of expressions
"""

text5 = """
17 Security
17.1 Encryption, Encryption Protocols and Digital certificates
Candidates should be able to:
Show understanding of how encryption works
Notes and guidance
Including the use of public key, private key, plain
text, cipher text, encryption, symmetric key
cryptography and asymmetric key cryptography
How the keys can be used to send a private
message from the public to an individual/
organisation
How the keys can be used to send a verified
message to the public
How data is encrypted and decrypted, using
symmetric and asymmetric cryptography
Purpose, benefits and drawbacks of quantum
cryptography
Show awareness of the Secure Socket Layer (SSL)/
Transport Layer Security (TLS)
Purpose of SSL/TLS
Use of SSL/TLS in client-server communication
Situations where the use of SSL/TLS would be
appropriate
Show understanding of digital certification How a digital certificate is acquired
How a digital certificate is used to produce digital
signatures
"""

text6 = """
18 Artificial Intelligence (AI)
18.1 Artificial Intelligence (AI)
Candidates should be able to:
Show understanding of how graphs can be used to
aid Artificial Intelligence (AI)
Notes and guidance
Purpose and structure of a graph
Use A* and Dijkstra’s algorithms to perform
searches on a graph
Candidates will not be required to write algorithms
to set up, access, or perform searches on graphs
Show understanding of how artificial neural
networks have helped with machine learning
Show understanding of Deep Learning, Machine
Learning and Reinforcement Learning and the
reasons for using these methods.
Understand machine learning categories, including
supervised learning, unsupervised learning
Show understanding of back propagation of errors
and regression methods in machine learning
"""

text7 = """
19 Computational thinking and Problem-solving
19.1 Algorithms
Candidates should be able to:
Show understanding of linear and binary searching
methods
Notes and guidance
Write an algorithm to implement a linear search
Write an algorithm to implement a binary search
The conditions necessary for the use of a binary
search
How the performance of a binary search varies
according to the number of data items
Show understanding of insertion sort and bubble
sort methods
Write an algorithm to implement an insertion sort
Write an algorithm to implement a bubble sort
Performance of a sorting routine may depend on
the initial order of the data and the number of data
items
Show understanding of and use Abstract Data
Types (ADT)
Write algorithms to find an item in each of the
following: linked list, binary tree
Write algorithms to insert an item into each of the
following: stack, queue, linked list, binary tree
Write algorithms to delete an item from each of the
following: stack, queue, linked list
Show understanding that a graph is an example of
an ADT. Describe the key features of a graph and
justify its use for a given situation. Candidates will
not be required to write code for a graph structure
Show how it is possible for ADTs to be implemented
from another ADT
Describe the following ADTs and demonstrate how
they can be implemented from appropriate builtin types or other ADTs: stack, queue, linked list,
dictionary, binary tree
Show understanding that different algorithms which
perform the same task can be compared by using
criteria (e.g. time taken to complete the task and
memory used)
Including use of Big O notation to specify time and
space complexity
19.2 Recursion
Candidates should be able to:
Show understanding of recursion
Notes and guidance
Essential features of recursion
How recursion is expressed in a programming
language
Write and trace recursive algorithms
When the use of recursion is beneficial
Show awareness of what a compiler has to do to
translate recursive programming code
"""

text8 = """
20 Further Programming
20.1 Programming Paradigms
Candidates should be able to:
Understanding what is meant by a programming
paradigm
Notes and guidance
Show understanding of the characteristics of a
number of programming paradigms:
• Low-level
Low-level Programming:
• understanding of and ability to write
low-level code that uses various addressing
modes: immediate, direct, indirect, indexed and
relative
• Imperative (Procedural) Imperative (Procedural) programming:
• Assumed knowledge and understanding of
Structural Programming (see details in AS
content section 11.3)
• understanding of and ability to write imperative
(procedural) programming code that uses
variables, constructs, procedures and functions.
See details in AS content
• Object Oriented Object-Oriented Programming (OOP):
• understanding of the terminology associated
with OOP (including objects, properties/
attributes, methods, classes, inheritance,
polymorphism, containment (aggregation),
encapsulation, getters, setters, instances)
• understanding of how to solve a problem by
designing appropriate classes
• understanding of and ability to write code that
demonstrates the use of OOP
• Declarative Declarative programming:
• understanding of and ability to solve a problem
by writing appropriate facts and rules based on
supplied information
• understanding of and ability to write code that
can satisfy a goal using facts and rules
Cambridge International AS & A Level Computer Science 9618 syllabus for 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/alevel 39
20.2 File Processing and Exception Handling
Candidates should be able to:
Write code to perform file-processing operations
Notes and guidance
Open (in read, write, append mode) and close a file
Read a record from a file and write a record to a file
Perform file-processing operations on serial,
sequential, random files
Show understanding of an exception and the
importance of exception handling
Know when it is appropriate to use exception
handling
Write program code to use exception handling
"""



textarr = [text, text2, text3, text4, text5, text6, text7, text8]
for i in range(len(textarr)):
    textarr[i] = getFormattedTextfromPdf.formatText(textarr[i])

trainModels.train(textarr, allLabels)
