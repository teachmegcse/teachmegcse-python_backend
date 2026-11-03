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
1 Business and its environment (AS Level)
The foundation of Business is to understand what happens within a business. At AS Level candidates develop
an understanding of what a business is, what it wants to achieve and who is involved. Candidates develop the
vocabulary to understand how a business operates and learn how to analyse what the business does. Every
business is different, understanding its context is important to be able to understand the decisions that it makes
and the motivations of those involved.
1.1 Enterprise
1.1.1 The nature of business activity
• the purpose of business activity
• the factors of production needed for business activity: land, labour, capital and enterprise
• the concept of adding value
• the nature of economic activity, the problem of choice and opportunity cost
• the dynamic business environment
• why businesses succeed or fail
• differences between local, national, international and multinational businesses
1.1.2 The role of entrepreneurs and intrapreneurs
• the qualities entrepreneurs and intrapreneurs need for success
• the role of entrepreneurship in creating and starting up a business
• the role of intrapreneurship in the ongoing success of a business
• barriers to entrepreneurship
• business risk and uncertainty
• the role of business enterprise in the development of a country
1.1 Enterprise continued
1.1.3 Business plans
• the meaning and purpose of business plans
• the key elements of business plans
• the benefits and limitations of business plans
1.2 Business structure
1.2.1 Economic sectors
• the primary, secondary, tertiary and quaternary sectors and businesses within those sectors
• the public and private sectors and businesses within those sectors
• the reasons for and consequences of the changing relative importance of these sectors
1.2.2 Business ownership
• the main features of different types of business ownership: sole traders, partnerships, private limited
companies, public limited companies, franchises, co-operatives, joint ventures and social enterprises
• the appropriateness of different types of business ownership
• the concepts of unlimited liability and limited liability and their importance
• the advantages and disadvantages of changing from one type of business ownership to another
1.3 Size of business
1.3.1 Measurements of business size
• the appropriateness of different methods of measuring the size of a business
1.3.2 Significance of small businesses
• the advantages and disadvantages of being a small business
• the strengths and weaknesses of family businesses
• the importance of small businesses and their role in the economy
• the role of small businesses as part of the industrial structure in some industries
1.3.3 Business growth
• why and how a business might grow internally (organic growth)
• the different types of external growth through merger and takeover: horizontal, vertical (backward and
forward), conglomerate diversification, friendly merger, hostile takeover
• the impact of a merger/takeover on stakeholders
• why a merger/takeover may or may not achieve objectives
• the importance of joint ventures and strategic alliances as methods of external growth
1.4 Business objectives
1.4.1 Business objectives in the private sector and public sector
• the objectives of businesses – private sector, public sector, and social enterprises
• the importance of business objectives
• corporate social responsibility (CSR) and the triple bottom line – economic (financial), social and
environmental objectives
• the relationship between mission statement, aims, objectives, strategy and tactics
1.4.2 Objectives and business decisions
• the different stages of business decision-making and the role of objectives in the stages of business
decision-making
• how objectives might change over time
• the translation of objectives into targets and budgets
• the need for communication of objectives and their likely impact on the workforce
• SMART (specific, measurable, achievable, realistic, time-limited) objectives
• how ethics may influence business objectives and activities
1.5 Stakeholders in a business
1.5.1 Business stakeholders
• individuals or groups with an interest in the activities of a business
• internal stakeholders and external stakeholders
• the roles, rights and responsibilities of stakeholders
1.5.2 The relative importance and influence of stakeholders on business activities
• the impact of business decisions on stakeholders, and their reactions
• the impact of stakeholder aims on business decisions
• how and why a business needs to be accountable to its stakeholders
• how conflict might arise from stakeholders having different aims and objectives
• how changing business objectives might affect its stakeholders
"""

text2 = """
2 Human resource management (AS Level)
The focus of this topic is on how a business can effectively manage its workforce to achieve its objectives.
Candidates will develop an understanding of the human resource management process from planning and
recruiting workers through to their dismissal. Candidates will learn about motivation in management. They will
learn about the theory behind motivation as well as how to implement it in practice.
2.1 Human resource management (HRM)
2.1.1 Purpose and roles of HRM
• the role of HRM in meeting organisational objectives
2.1.2 Workforce planning
• the reasons for and role of a workforce plan
• measurement of labour turnover
• the implications of high and low labour turnover for a business
2.1.3 Recruitment and selection
• recruitment of employees: process (job descriptions and person specifications) and recruitment methods
(job advertisements, employment agencies, online recruitment)
• internal and external recruitment
• selection methods: curriculum vitae, résumé, application forms, interviews, references, testing, assessment
centres
• employment contracts
2.1.4 Redundancy and dismissal
• the difference between redundancy (voluntary and involuntary) and dismissal (fair, unfair)
2.1.5 Morale and welfare
• the relationship between HRM, employee morale and welfare in a business including the concept of work￾life balance
• the impact of diversity and equality in the workplace on a business
2.1.6 Training and development
• different types of training: induction, on-the-job, off-the-job
• the impact of training and development on a business
• employee development to encourage intrapreneurship
• employee development to encourage multi-skilling and flexibility
2.1 Human resource management (HRM) continued
2.1.7 Management and workforce relations
• how cooperation between management and the workforce can be of benefit to both
• the impact on employers and employees of trade union involvement in the workplace including their role in
collective bargaining
2.2 Motivation
2.2.1 Motivation as a tool of management and leadership
• the need to motivate employees to achieve the objectives of a business
2.2.2 Human needs
• a simple explanation of human need
• how human needs may or may not be satisfied at work
2.2.3 Motivation theories
• the ideas of the main content theories (Taylor, Mayo, Maslow, Herzberg and McClelland) and process theory
(Vroom)
2.2.4 Motivation methods in practice: financial motivators, non-financial motivators
• the theories in practical situations
• different payment methods: time based, salary, piece rates, commission, bonuses, profit sharing,
performance-related pay, fringe benefits
• different types of non-financial motivators: training, opportunities for promotion, development, status, job
re-design, team working, empowerment, participation, job enrichment
• ways in which employees can participate in the management and control of business activity
2.3 Management
2.3.1 Management and managers
• traditional manager functions: planning, organising, directing, controlling
• the role of managers: Fayol, Mintzberg
• the contribution of managers to business performance
• management styles: autocratic, democratic, laissez-faire, paternalistic
• McGregor’s Theory X and Theory Y managers
"""

text3 = """
3 Marketing (AS Level)
The focus of this topic is on how a business finds out the needs of potential customers, and provides for their
needs. Candidates will develop an understanding of the marketing mix. Candidates will have the opportunity to
study in further depth one or more of the elements of the marketing mix, and to develop the skills to be able to
recommend a suitable marketing mix for a business in a specific context.
3.1 The nature of marketing
3.1.1 The role of marketing and its relationship with other business activities
• marketing objectives
• the link between marketing objectives and corporate objectives
3.1.2 Demand and supply
• the factors influencing the demand for and supply of the products of a business
• interactions between demand, supply and price
3.1.3 Markets
• how markets may differ: consumer and industrial markets; local, national and international markets
• the difference between product orientation and customer (market) orientation
• measurement of market share and market growth
• the implications of changes in market share and market growth
3.1.4 Consumer and industrial marketing
• the classification of products
• how marketing might differ for consumer products (B2C – business to consumer) and industrial products
(B2B – business to business)
3.1.5 Mass marketing and niche marketing
• the features of mass and niche markets
• the advantages and disadvantages of mass marketing and niche marketing
3.1.6 Market segmentation
• methods of market segmentation: geographic, demographic and psychographic
• the advantages and disadvantages of market segmentation
3.1.7 Customer relationship marketing (CRM)
• the aims of CRM
• the costs and benefits of CRM
3.2 Market research
3.2.1 The purposes of market research
• identification of main features of a market: size, growth, competitors
• identification of customer and consumer characteristics, profiles, wants and needs
3.2.2 Primary research and secondary research
• the distinction between primary research and secondary research, and the main features of each
• usefulness of data collected using primary research methods
• usefulness of data collected from secondary research sources
3.2.3 Sampling
• the need for and limitations of sampling
3.2.4 Market research data
• the reliability of the data collected
• analysis of quantitative and qualitative data
• interpretation of information presented in tables, charts and graphs
3.3 The marketing mix
3.3.1 The elements of the marketing mix (the 4Ps)
• the 4Ps: Product, Price, Promotion, Place (distribution channels)
3.3.2 Product
• the difference between goods and services
• tangible and intangible attributes of products
• the importance of product development
• product differentiation and unique selling point (USP)
3.3.3 Product portfolio analysis
• product life cycle and decisions about extension strategies
• Boston Matrix analysis and its uses
• impact of product portfolio analysis on marketing decisions
3.3 The marketing mix continued
3.3.4 Pricing methods
• objectives and usefulness of different pricing methods: competitive, penetration, skimming, price
discrimination, dynamic, cost-based and psychological
3.3.5 Promotion methods
• the objectives and usefulness of different promotion methods
• advertising promotion
• sales promotion
• direct promotion
• developments in digital promotion
• the role of packaging in promotion
• the role of branding in promotion
3.3.6 Place (channels of distribution)
• the objectives and usefulness of different channels of distribution
• digital and physical distribution
"""

text4 = """
4 Operations management (AS Level)
The focus of this topic is on operations management from the production of physical products to managing the
process of creating services. There are different ways a business can produce a product, with a range of aspects
to consider in its production. Candidates are provided with the opportunity to apply their understanding of
production methods in a variety of business contexts.
4.1 The nature of operations
4.1.1 The transformational process
• the use of factors of production: land, labour, capital and enterprise
• the stages of the transformational process: inputs to outputs
• the contribution of operations to added value
4.1.2 Efficiency, effectiveness, productivity and sustainability
• the importance of efficiency, effectiveness, productivity and sustainability
• measurement of labour productivity
• the impact on a business of measures to improve sustainability of operations
4.1 The nature of operations continued
4.1.3 Capital intensive and labour intensive operations
• the benefits and limitations of capital intensive operations
• the benefits and limitations of labour intensive operations
4.1.4 Operations methods: job, batch, flow, mass customisation
• differences between methods – advantages and disadvantages of each method
• the problems of changing from one method to another
4.2 Inventory management
4.2.1 Managing inventory
• the purpose of inventory within a business (raw materials, work in progress, finished products)
• the costs and benefits of holding inventory
• buffer inventory, re-order level and lead time
• interpretation of simple inventory control charts
• the importance of Supply Chain Management
4.2.2 Just in Time (JIT)
• the purpose of JIT and JIC (Just in Case) inventory management
• the impact of adopting a JIT approach on a business
4.3 Capacity utilisation and outsourcing
4.3.1 Significance and measurement of capacity utilisation
• the measurement of capacity utilisation
• the impact of operating under or over maximum capacity on a business
• methods of improving capacity utilisation
4.3.2 Outsourcing
• the impact of outsourcing on a business
"""

text5 = """
5 Finance and accounting (AS Level)
The focus of this topic is on the areas more traditionally associated with finance such as how a business can
fund itself and where that money goes. Candidates will learn why a business requires finance to operate, and the
importance for businesses to successfully manage their finance.
5.1 Business finance
5.1.1 The need for business finance
• reasons why businesses need finance to start up, to grow and to survive
• the distinction between short and long term need for finance
• the difference between cash and profits
• business failure as a consequence of lack of finance: bankruptcy, liquidation and administration
5.1.2 Working capital
• the meaning and importance of working capital
• managing trade receivables and trade payables
• the distinction between capital expenditure and revenue expenditure
5.2 Sources of finance
5.2.1 Business ownership and sources of finance
• the relationship between the form of business ownership and availability of sources of finance
5.2.2 Internal and external sources of finance
• internal sources of finance: owners investment, retained earnings, sale of unwanted assets, sale and
leaseback of non-current assets, working capital
• external sources of finance: share capital, debentures, new partners, venture capital, bank overdrafts,
leasing, hire purchase, bank loans, mortgages, debt factoring, trade credit, micro-finance, crowd funding and
government grants
5.2.3 Factors affecting the sources of finance
• the factors influencing the choice of sources of finance in a given situation: cost, flexibility, need to retain
control, the use to which it is put, level of existing debt
5.2.4 Selecting the source of finance
• the appropriateness of each possible source in a given situation
5.3 Forecasting and managing cash flows
5.3.1 Cash flow forecasts
• the meaning and purpose of cash flow forecasts
• the interpretation and amendment of simple cash flow forecasts: calculating opening and closing balances
• different methods of improving cash flow
5.4 Costs
5.4.1 Cost information
• the need for accurate cost information
• different types of costs: fixed, variable, direct and indirect
5.4.2 Approaches to costing: full, contribution
• the differences between full and contribution costing
• the uses and limitations of the full costing method
• the nature of the technique of contribution costing
• the difference between contribution and profit
• the limitations of contribution costing
• situations in which contribution costing would be and would not be used
5.4.3 Uses of cost information
• cost information for decision-making purposes, e.g. average, marginal, total costs
• how costs can be used for pricing decisions
• how costs can be used to monitor and improve business performance, including using cost information to
calculate profits
• contribution costing as a means to help make special order decisions
5.4.4 Break-even analysis
• the meaning and importance of break-even analysis
• calculation and interpretation of break-even level of output, contribution, margin of safety and level of profit
(in numeric and graphic form)
• the uses and limitations of break-even analysis
5.5 Budgets
5.5.1 The meaning and purpose of budgets
• the measurement of performance
• the benefits and drawbacks from the use of budgets
• the meaning and use of incremental budgets, flexible budgets and zero budgeting
• the uses of budgets for measuring performance, allocating resources, controlling and monitoring a business
5.5.2 Variances
• the meaning of adverse variances and favourable variances
• the calculation and interpretation of variances
A Level content
The content of the AS Level is assumed knowledge for the assessment of Paper 3 and Paper 4. The A Level topics
build on the learning acquired in the AS Level topics.
"""

textarr = [text1, text2, text3, text4, text5]
for i in range(len(textarr)):
    textarr[i] = formatText(textarr[i])

trainModels.train(textarr, allLabels, f"{BASE_PATH}/resources/sci-kit/asbus.joblib")
