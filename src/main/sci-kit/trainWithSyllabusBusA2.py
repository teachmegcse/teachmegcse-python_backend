import trainModels
import os
import sys

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)

from main.utils import formatText


allLabels = ['Business and its environment',
             'Human resource management',
             'Marketing',
             'Operations management',
             'Finance and accounting']


text1 = """
6 Business and its environment (A Level)
This A Level topic builds on the learning acquired in topic 1, enabling candidates to further understand the
environment in which a business operates. All businesses operate in a constantly changing environment.
Candidates will develop an understanding that although some aspects of the environment are fixed, businesses
operate in a context in which things change. The way in which the topic is taught should reflect the changing
needs of the environment in which a business operates.
The study of business strategy will enable candidates to develop their skills to produce a basic business strategy.
Candidates will develop an understanding of the tools a business uses to analyse the internal and external
environment to ensure the success of the business.
6.1 External influences on business activity
6.1.1 Political and legal
• the advantages and disadvantages of privatisation in a given situation
• the advantages and disadvantages of nationalisation in a given situation
• how a government might use the law to seek to control: employment practices, conditions of work
(including health and safety), wage levels, marketing behaviour, competition, location decisions, particular
goods and services
• the impact of changes in political and legal factors on business and business decisions
6.1 External influences on business activity continued
6.1.2 Economic
• how government might intervene to help businesses and encourage enterprise
• how government might intervene to constrain business activity
• how government might deal with market failure
• the key macroeconomic objectives of governments: low unemployment, low inflation, economic growth
• how macroeconomic objectives and performance of an economy can have an impact on business activity
• government policies used to achieve macroeconomic objectives: monetary, fiscal, supply-side and exchange
rate policies
• the impact of changes in these government policies on business and business decisions
6.1.3 Social and demographic
• the impact of and issues associated with corporate social responsibility (CSR), e.g. accounting practices,
paying incentives for the award of contracts, social auditing
• why businesses need to consider the needs of the community including pressure groups
• demographic changes at a local, national and global level
• the impact of social and demographic change on business and business decisions
6.1.4 Technological
• the impact of technological change on business and business decisions
6.1.5 Competitors and suppliers
• the impact of competitors and suppliers on business and business decisions
6.1.6 International
• the importance of international trading links and their impact on business and business decisions
• how international trade agreements might have an impact on businesses
• the role of technology in international trade
• the advantages and disadvantages that a multinational might bring to a country
• relationships between multinationals and governments
6.1.7 Environmental
• how physical environmental issues might influence business behaviour
• how a business and its stakeholders may use an environmental audit
• the impact of the growing importance of sustainability on business and business decisions
6.2 Business strategy
6.2.1 Developing business strategy
• the meaning and purpose of business strategy
• the meaning and purpose of strategic management: analysis, choice and implementation
• approaches to develop business strategy, including:
– blue ocean strategy
– scenario planning
– SWOT analysis
– PEST analysis
– Porter’s five forces
– core competence framework
– Ansoff matrix
– force field analysis
– decision trees
6.2.2 Corporate planning and implementation
• the meaning and importance of corporate planning
• the meaning of corporate culture and its impact on business decision-making
• the meaning and importance of transformational leadership
• the management and control of strategic change
• the meaning and importance of contingency planning and crisis management
"""

text2 = """
7 Human resource management (A Level)
This A Level topic builds on the learning acquired in topic 2, enabling candidates to build the bigger picture of
managing a workforce. Candidates will develop an understanding of the different ways in which a business can
structure its workforce to reach its goals. Candidates will learn about business leadership and the ability to make
decisions. Candidates will develop an understanding that there are different ways to lead. The most suitable
method will depend on the business, and its context.
The study of strategic elements of human resource management will require candidates to bring together the
content learnt in topic 2 and in this topic 7 to think about how a business can manage its people from a business￾wide perspective.
7.1 Organisational structure
7.1.1 The relationship between business objectives and organisational structure
• the purpose and attributes of an organisational structure such as flexibility, meeting the needs of the
business, allowing for growth and development and encouraging intrapreneurship
7.1 Organisational structure continued
7.1.2 Types of structure: functional, hierarchical (flat and narrow), matrix
• the advantages and disadvantages of the different types of structure
• why some organisations are structured by product and others by function or geographical area
• the reasons and ways structures change e.g. due to growth or delayering
• the features of a formal structure: levels of hierarchy, chain of command, span of control, responsibility,
authority, delegation, accountability, centralised, decentralised
7.1.3 Delegation and accountability
• the relationship between delegation and accountability
• the processes of accountability in a business
• the impact of delegation on a business
7.1.4 Control, authority and trust
• the relationship between span of control and levels of hierarchy
• the difference between authority and responsibility
• the conflicts between control and trust that might arise when delegating
7.1.5 Centralisation and decentralisation
• the impact of centralisation and decentralisation on a business
7.1.6 Line and staff
• examples of and distinctions between line and staff functions and the conflicts between them
7.2 Business communication
7.2.1 Purposes of communication
• situations in which communication is essential
7.2.2 Methods of communication
• the standard methods of communication used in business: spoken, written, electronic, visual
• the strengths and weaknesses of the different methods of communication
7.2 Business communication continued
7.2.3 Channels of communication
• how communication works within a business
• the difference between one- and two-way communication; the difference between vertical and horizontal
communication
• problems associated with different channels of communication
7.2.4 Barriers to communication
• barriers to communication and how to overcome them
7.2.5 The role of management in facilitating communication
• the role of informal communications within a business
• ways in which communication can influence the efficiency of a business
• ways of improving communication in a given situation
7.3 Leadership
7.3.1 Leadership
• the purpose of leadership
• leadership roles in business (directors, managers, supervisors, worker representatives)
• the qualities of a good leader
7.3.2 Theories of leadership
• key leadership theories: trait, behavioural, contingency, power and influence and transformational
7.3.3 Emotional intelligence/emotional quotient (EQ)
• Goleman’s four competencies of emotional intelligence: self-awareness, social awareness, self-management
and social skills
7.4 Human resource management (HRM) strategy
7.4.1 Approaches to human resource management (HRM)
• the difference between ‘hard’ and ‘soft’ HRM
• flexible working contracts: advantages and disadvantages of temporary contracts or flexible contracts
including zero hours contracts, part-time, full-time, annualised hours, flexi-time, home working, shift
working, job sharing, compressed working hours, the gig economy
• the measurement, causes and consequences of poor employee performance
• strategies for improving employee performance
• Management by Objectives (MBO) – implementation and usefulness
• the changing role of Information Technology (IT) and Artificial Intelligence (AI) in HRM
"""

text3 = """
8 Marketing (A Level)
The focus of this A Level topic is on how a business can plan and strategise for the future. Candidates will build
from their learning in topic 3 to plan for the future marketing needs of the business.
The study of the strategic elements of marketing, include learning about the marketing plan which includes the
whole process of marketing, not just the marketing mix. Candidates will look at how a business can adapt and
change their marketing to focus on international markets.
8.1 Marketing analysis
8.1.1 Elasticity
• the concept of elasticity of demand: price, income and promotional
• calculation of price, income and promotional elasticity of demand
• interpretation of elasticity results
• the impact of elasticity measures on business decisions
• the limitations of the concept of elasticity in its various forms
8.1.2 Product development
• the process of product development
• sources of new ideas for product development
• the importance of Research and Development (R&D)
8.1.3 Sales forecasting
• the need to forecast sales
• time series analysis: calculation and use of four period centred moving average method to forecast sales
• qualitative sales forecasting
• the impact of sales forecasting on business decisions
8.2 Marketing strategy
8.2.1 Planning the marketing strategy
• the contents of a marketing plan: objectives, resources, research, marketing mix
• the benefits and limitations of marketing planning
8.2.2 Approaches to marketing strategy
• the need for the marketing strategy to be consistent with the business, the product and the market
• the need for and development of a coordinated marketing strategy
• the development of marketing strategies that are focused towards achieving specific marketing objectives
• the changing role of Information Technology (IT) and Artificial Intelligence (AI) in marketing
8.2.3 Strategies for international marketing
• the implications for marketing of increased globalisation and economic collaboration
• the importance of international marketing for a business
• international markets – identification, selection and entry
• whether a business in a given situation should develop an international market through pan-global
marketing or maintain local differences
• choosing a strategy, in a given situation, to develop a global market
• the factors influencing the method of entry into international markets
"""

text4 = """
9 Operations management (A Level)
This A Level topic builds on the learning acquired in topic 4, enabling candidates to study the wider aspects of
production. Candidates will develop an understanding of the importance of the location of a business and the
effect that the location has on other aspects of the operations of the business. Candidates will learn about the
importance of quality and the effect that quality has on the other functional areas of business. Candidates will
develop an awareness of quality in terms of operations management (i.e. being ‘fit for purpose’) as opposed to a
customer’s perception of quality of a product.
Candidates will learn about various aspects of operations strategy, including the longer-term planning needed
to improve the operations of a business, innovations such as enterprise resource planning (ERP) and lean
production, and tools such as critical path analysis.
9.1 Location and scale
9.1.1 Location
• the factors that determine location and relocation
• the differences between local, national and international location decisions
• the reasons for and impact of offshoring and reshoring
• the impact of globalisation on location and relocation decisions
9.1 Location and scale continued
9.1.2 Scale of operations
• the factors that influence the scale of a business
• causes and examples of internal and external economies and diseconomies of scale
• the links between economies and diseconomies of scale and unit costs
9.2 Quality management
9.2.1 Quality control and quality assurance
• quality in terms of meeting customer expectations
• the importance of quality
• the impact of methods of quality control on a business
• the impact of methods of quality assurance on a business
• the impact of Total Quality Management (TQM) on a business
9.2.2 Benchmarking
• the importance of benchmarking in quality management
9.3 Operations strategy
9.3.1 Operational decisions
• the influence of human, marketing and finance resource availability on operations decisions
• the changing role of Information Technology (IT) and Artificial Intelligence (AI) in operations management
9.3.2 Flexibility and innovation
• the need for flexibility with regard to volume, delivery time and specification
• process innovation: changing current processes or adopting new ways of producing products or delivering
services
9.3.3 Enterprise resource planning (ERP)
• the main features of an ERP programme
• how ERP can improve a business’ efficiency in relation to: inventory control, costing and pricing, capacity
utilisation, responses to change, workforce flexibility, management information
9.3 Operations strategy continued
9.3.4 Lean production
• the aims and purposes of lean production
• Kaizen, quality circles, simultaneous engineering, cell production, JIT manufacturing and waste management
as operational strategies to achieve lean production
• the limitations of operational strategies to achieve lean production
• the links between lean production and inventory control, quality, employees roles, capacity management
and efficiency
9.3.5 Operations planning
• the need for planning operations
• network diagrams as tools to plan operations
• the main elements of a network diagram: activities, dummy activities, nodes
• network diagrams as means of performing Critical Path Analysis (CPA), including identification of the
minimum project duration and the critical path, calculation of total and free float, interpretation of the
results of the analysis of a network, how minimum duration and floats might be used in project management
• the benefits and limitations of CPA as a management tool
"""

text5 = """
10 Finance and accounting (A Level)
This A Level topic builds on the learning acquired in topic 5, with a focus on accounting information, including
published accounts.
Candidates will develop an understanding of what can be learnt from the accounts of a business.
Candidates are not expected to be able to draw up a set of accounts. However, candidates do need to be able to
calculate relevant ratios and use this data to inform business decisions.
10.1 Financial statements
10.1.1 Statement of profit or loss
• the meaning and purpose of the statement of profit or loss
• the contents of a statement of profit or loss: revenue, cost of sales, gross profit, expenses, profit from
operations (operating profit), taxation, profit for the year, dividends, retained earnings
• amendment of a statement of profit or loss
• the impact on the statement of profit or loss a given change
10.1.2 Statement of financial position
• the meaning and purpose of statement of financial position
• the contents of a statement of financial position including non-current assets, current assets, current
liabilities, net current assets, net assets, non-current liabilities, reserves and equity
• amendment of a statement of financial position
• the relationships between items in the statement of profit or loss and the statement of financial position
10.1 Financial statements continued
10.1.3 Inventory valuation
• the difficulties of valuing inventory
• the net realisable value method
10.1.4 Depreciation
• the role of depreciation in the accounts
• the impact of depreciation (straight-line method only) on the statement of financial position and the
statement of profit or loss
10.2 Analysis of published accounts
10.2.1 Liquidity ratios
• the meaning and importance of liquidity
• current ratio: calculation and interpretation
• acid test ratio: calculation and interpretation
• methods of improving liquidity
10.2.2 Profitability ratios
• the meaning and importance of profitability
• return on capital employed: calculation and interpretation
• gross profit margin: calculation and interpretation
• profit margin: calculation and interpretation
• methods of improving profitability
10.2.3 Financial efficiency ratios
• the meaning and importance of financial efficiency
• rate of inventory turnover: calculation and interpretation
• trade receivables turnover (days): calculation and interpretation
• trade payables turnover (days): calculation and interpretation
• methods of improving financial efficiency
10.2.4 Gearing ratio
• the meaning and importance of gearing
• gearing ratio: calculation and interpretation
• methods of improving gearing
10.2 Analysis of published accounts continued
10.2.5 Investment ratios
• the meaning and importance of return to investors
• dividend yield: calculation and interpretation
• dividend cover: calculation and interpretation
• price/earnings ratio: calculation and interpretation
• methods of improving investor return
10.3 Investment appraisal
10.3.1 The concept of investment appraisal
• the need for investment appraisal
10.3.2 Basic methods: payback, accounting rate of return (ARR)
• the meaning, calculation and interpretation of payback and ARR
(ARR = (average profit/ average investment) × 100)
10.3.3 Discounted cash flow method: net present value (NPV)
• the meaning, calculation and interpretation of NPV
10.3.4 Investment appraisal decisions
• quantitative results and their impact on investment decisions
• qualitative factors and their impact on investment decisions
• comparison of investment appraisal methods, including their limitations
10.4 Finance and accounting strategy
10.4.1 The use of accounting data to enable strategic decision making
• the use of financial statements in developing strategies
• the contents of an annual report and their usefulness to business and other stakeholders
10.4 Finance and accounting strategy continued
10.4.2 The use of accounting data and ratio analysis in strategic decision-making
• assessment of business performance over time and against competitors
• the impact of accounting data including ratio results on business strategy
• the impact of debt or equity decisions on ratio results
• the impact of changes in dividend strategy on ratio results
• the impact of business growth on ratio results
• the impact of other business strategies on ratio results
• the limitations of using published accounts and ratio analyses
Ratios to support analysis of published accounts
Liquidity ratios
Current ratio
Current assets
Current liabilities
Answer presented as a ratio
Acid test ratio
Current assets – inventory
Current liabilities
Answer presented as a ratio
Profitability ratios
Gross profit margin (%) Gross profit
Revenue × 100
Operating profit margin (%) Profit from operations
Revenue × 100
Return on capital employed (%)
Profit from operations
Capital employed × 100
Capital employed = issued shares + reserves + non-current liabilities
Financial efficiency ratios
Trade receivables turnover (days) Trade receivables
Credit sales × 365 days
Trade payables turnover (days) Trade payables
Credit purchases × 365 days
Rate of inventory turnover (times) Cost of sales
Average inventory
Gearing ratio
Gearing (%) Non-current liabilities
Capital employed × 100
Investment ratios
Price/earnings ratio Market price per share
Earnings per share
Dividend yield (%) Dividend per share
Market price per share × 100
Dividend cover Profit for the year
Annual dividend
"""

textarr = [text1, text2, text3, text4, text5]
for i in range(len(textarr)):
    textarr[i] = formatText(textarr[i])

trainModels.train(textarr, allLabels, f"{BASE_PATH}/resources/sci-kit/a2bus.joblib")
