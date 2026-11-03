import trainModels
import os
import sys

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)

from main.utils import formatText


allLabels = ['Understanding business activity',
             'People in business',
             'Marketing',
             'Operations management',
             'Financial information and decisions',
             'External influences on business activity']


text1 = """
1 Understanding business activity
1.1 Business activity
1.1.1 The purpose and nature of business activity: • Concepts of needs, wants, scarcity and
opportunity cost
• Importance of specialisation
• Purpose of business activity
• The concept of adding value and how added
value can be increased
1.2 Classification of businesses
1.2.1 Economic sectors in terms of primary,
secondary and tertiary sectors:
• Basis of business classification, using examples to
illustrate the classification
• Reasons for the changing importance of business
classification, e.g. in developed and developing
economies
1.2.2 Classify business enterprises between private
sector and public sector in a mixed economy
1.3 Enterprise, business growth and size
1.3.1 Enterprise and entrepreneurship: • Characteristics of successful entrepreneurs
• Contents of a business plan and how business
plans assist entrepreneurs
• Why and how governments support business
start-ups, e.g. grants, training schemes
1.3.2 The methods and problems of measuring
business size:
• Methods of measuring business size, e.g. number
of people employed, value of output, capital
employed (profit is not a method of measuring
business size)
• Limitations of methods of measuring business
size
1.3 Enterprise, business growth and size continued
1.3.3 Why some businesses grow and others remain
small:
• Why the owners of a business may want to
expand the business
• Different ways in which businesses can grow,
e.g. internal/external
• Problems linked to business growth and how
these might be overcome
• Why some businesses remain small
1.3.4 Why some (new or established) businesses fail: • Causes of business failure, e.g. lack of
management skills, changes in the business
environment, liquidity problems
• Why new businesses are at a greater risk of failing
1.4 Types of business organisation
1.4.1 The main features of different forms of
business organisation:
• Sole traders, partnerships, private and public
limited companies, franchises and joint ventures
• Differences between unincorporated businesses
and limited companies
• Concepts of risk, ownership and limited liability
• Recommend and justify a suitable form of
business organisation to owners/management in
a given situation
• Business organisations in the public sector,
e.g. public corporations
1.5 Business objectives and stakeholder objectives
1.5.1 Businesses can have several objectives and the
importance of them can change:
• Need for business objectives and the importance
of them
• Different business objectives, e.g. survival,
growth, profit and market share
• Objectives of social enterprises
1.5.2 The role of stakeholder groups involved in
business activity:
• Main internal and external stakeholder groups
• Objectives of different stakeholder groups
• How these objectives might conflict with each
other, use examples
1.5.3 Differences in the objectives of private sector
and public sector enterprises
"""

text2 = """
2 People in business
2.1 Motivating employees
2.1.1 The importance of a well-motivated workforce: • Why people work and what motivation means
• The benefits of a well-motivated workforce:
labour productivity, reduced absenteeism and
labour turnover
• The concept of human needs, e.g. Maslow’s
hierarchy
• Key motivational theories: Taylor and Herzberg
2.1.2 Methods of motivation: • Financial rewards, e.g. wage, salary, bonus,
commission and profit sharing
• Non-financial methods, e.g. job enrichment, job
rotation, teamworking, training, opportunities for
promotion
• Recommend and justify appropriate method(s) of
motivation in given circumstances
2.2 Organisation and management
2.2.1 Draw, interpret and understand simple
organisational charts:
• Simple hierarchical structures: levels of hierarchy,
span of control, chain of command e.g. tall/short
• Roles and responsibilities of directors, managers,
supervisors, other employees in an organisation
and inter-relationships between them
2.2.2 The role of management: • Functions of management, e.g. planning,
organising, coordinating, commanding and
controlling
• Importance of delegation; trust versus control
2.2.3 Leadership styles: • Features of the main leadership styles,
e.g. autocratic, democratic and laissez-faire
• Recommend and justify an appropriate leadership
style in given circumstances
2.2.4 Trade unions: • What a trade union is and the effects of
employees being union members
2.3 Recruitment, selection and training of employees
2.3.1 Recruitment and selecting employees: • Recruitment and selection methods
• Difference between internal recruitment and
external recruitment
• Main stages in recruitment and selection of
employees
• Recommend and justify who to employ in given
circumstances
• Benefits and limitations of part-time employees
and full-time employees
2.3.2 The importance of training and the methods of
training:
• Importance of training to a business and to
employees
• Benefits and limitations of induction training,
on-the-job training and off-the-job training
2.3.3 Why reducing the size of the workforce might
be necessary:
• Difference between dismissal and redundancy
with examples
• Understand situations in which downsizing the
workforce might be necessary, e.g. automation or
reduced demand for products
• Recommend and justify which employees to
make redundant in given circumstances
2.3.4 Legal controls over employment issues and
their impact on employers and employees:
• Legal controls over employment contracts, unfair
dismissal, discrimination, health and safety, legal
minimum wage
2.4 Internal and external communication
2.4.1 Why effective communication is important and
the methods used to achieve it:
• Effective communication and its importance to
business
• Benefits and limitations of different
communication methods including those based
on information technology (IT)
• Recommend and justify which communication
method to use in given circumstances
2.4.2 Demonstrate an awareness of communication
barriers:
• How communication barriers arise and
problems of ineffective communication; how
communication barriers can be reduced or
removed
"""

text3 = """
3 Marketing
3.1 Marketing, competition and the customer
3.1.1 The role of marketing: • Identifying customer needs
• Satisfying customer needs
• Maintaining customer loyalty
• Building customer relationships
3.1.2 Market changes: • Why customer/consumer spending patterns may
change
• The importance of changing customer needs
• Why some markets have become more
competitive
• How businesses can respond to changing
spending patterns and increased competition
3.1.3 Concepts of niche marketing and mass
marketing:
• Benefits and limitations of both approaches to
marketing
3.1.4 How and why market segmentation is
undertaken:
• How markets can be segmented, e.g. according to
age, socio-economic grouping, location, gender
• Potential benefits of segmentation to business
• Recommend and justify an appropriate method
of segmentation in given circumstances
3.2 Market research
3.2.1 The role of market research and methods used: • Market-orientated businesses (uses of market
research information to a business)
• Primary research and secondary research
(benefits and limitations of each)
• Methods of primary research, e.g. postal
questionnaire, online survey, interviews, focus
groups
• The need for sampling
• Methods of secondary research, e.g. online,
accessing government sources, paying for
commercial market research reports
• Factors influencing the accuracy of market
research data
3.2.2 Presentation and use of market research
results:
• Analyse market research data shown in the form
of graphs, charts and diagrams; draw simple
conclusions from such data
3.3 Marketing mix
3.3.1 Product: • The limitations and benefits of developing new
products
• Brand image; impact on sales and customer
loyalty
• The role of packaging
• The product life cycle: main stages and extension
strategies; draw and interpret a product life cycle
diagram
• How stages of the product life cycle can influence
marketing decisions, e.g. promotion and pricing
decisions
3.3.2 Price: • Pricing methods (benefits and limitations of
different methods), e.g. cost plus, competitive,
penetration, skimming, and promotional
• Recommend and justify an appropriate pricing
method in given circumstances
• Understand the significance of price elasticity:
difference between price elastic demand and
price inelastic demand; importance of the
concept in pricing decisions (knowledge of
the formula and calculations of PED will not be
assessed)
3.3.3 Place – distribution channels: • Advantages and disadvantages of different
channels, e.g. use of wholesalers, retailers or
direct to consumers
• Recommend and justify an appropriate
distribution channel in given circumstances
3.3.4 Promotion: • The aims of promotion
• Different forms of promotion and how they
influence sales, e.g. advertising, sales promotion
• The need for cost-effectiveness in spending the
marketing budget on promotion
3.3.5 Technology and the marketing mix: • Define and explain the concept of e-commerce
• The opportunities and threats of e-commerce to
business and consumers
• Use of the internet and social media networks for
promotion
3.4 Marketing strategy
3.4.1 Justify marketing strategies appropriate to a
given situation:
• Importance of different elements of the
marketing mix in influencing consumer decisions
in given circumstances
• Recommend and justify an appropriate marketing
strategy in given circumstances
3.4.2 The nature and impact of legal controls related
to marketing:
• Impact of legal controls on marketing strategy,
e.g. misleading promotion, faulty and dangerous
goods
3.4.3 The opportunities and problems of entering
new foreign markets:
• Growth potential of new markets in other
countries
• Problems of entering foreign markets,
e.g. cultural differences and lack of knowledge
• Benefits and limitations of methods to overcome
such problems, e.g. joint ventures, licensing
"""

text4 = """
4 Operations management
4.1 Production of goods and services
4.1.1 The meaning of production: • Managing resources effectively to produce goods
and services
• Difference between production and productivity
• Benefits of increasing efficiency and how to
increase it, e.g. increasing productivity by
automation and technology, improved labour
skills
• Why businesses hold inventories
• The concept of lean production: how to achieve
it, e.g. just-in-time inventory control and Kaizen;
benefits of lean production
4.1.2 The main methods of production: • Features, benefits and limitations of job, batch
and flow production
• Recommend and justify an appropriate
production method for a given situation
4.1.3 How technology has changed and is changing
production methods, e.g. using computers in
design and manufacturing
4.2 Costs, scale of production and break-even analysis
4.2.1 Identify and classify costs: • Classifying costs using examples, e.g. fixed,
variable, average, total
• Use cost data to help make simple cost-based
decisions, e.g. to stop production or continue
4.2.2 Economies and diseconomies of scale: • The concept of economies of scale with
examples, e.g. purchasing, marketing, financial,
managerial, technical
• The concept of diseconomies of scale with
examples, e.g. poor communication, lack of
commitment from employees, weak coordination
4.2.3 Break-even analysis: • The concept of break-even
• Construct, complete or amend a simple
break-even chart
• Interpret a given chart and use it to analyse a
situation
• Calculate break-even output from given data
• Define, calculate and interpret the margin of
safety
• Use break-even analysis to help make simple
decisions, e.g. impact of higher price
• Understand the limitations of break-even analysis
4.3 Achieving quality production
4.3.1 Why quality is important and how quality
production might be achieved:
• What quality means and why it is important for
all businesses
• The concept of quality control and how
businesses implement quality control
• The concept of quality assurance and how this
can be implemented
4.4 Location decisions
4.4.1 The main factors influencing the location and
relocation decisions of a business:
• Factors relevant to the location decision of
manufacturing businesses and service businesses
• Factors that a business could consider when
deciding which country to locate operations in
• The role of legal controls on location decisions
• Recommend and justify an appropriate location
for a business in given circumstances
"""

text5 = """
5 Financial information and decisions
5.1 Business finance: needs and sources
5.1.1 The need for business finance: • The main reasons why businesses need finance,
e.g. start-up capital, capital for expansion and
additional working capital
• Understand the difference between short-term
and long-term finance needs
5.1.2 The main sources of finance: • Internal sources and external sources with
examples
• Short-term and long-term sources with
examples, e.g. overdraft for short-term finance
and debt or equity for long-term finance
• Importance of alternative sources of capital,
e.g. micro-finance, crowd-funding
• The main factors considered in making the
financial choice, e.g. size and legal form of
business, amount required, length of time,
existing loans
• Recommend and justify appropriate source(s) of
finance in given circumstances
5.2 Cash-flow forecasting and working capital
5.2.1 The importance of cash and of cash-flow
forecasting:
• Why cash is important to a business
• What a cash-flow forecast is, how a simple one is
constructed and the importance of it
• Amend or complete a simple cash-flow forecast
• How to interpret a simple cash-flow forecast
• How a short-term cash-flow problem might
be overcome, e.g. overdraft, delaying supplier
payments, asking debtors to pay more quickly
5.2.2 Working capital: • The concept and importance of working capital
5.3 Income statements
5.3.1 What profit is and why it is important: • How a profit is made
• Importance of profit to private sector businesses,
e.g. reward for risk-taking/enterprise, source of
finance
• Difference between profit and cash
5.3 Income statements continued
5.3.2 Income statements: • Main features of an income statement,
e.g. revenue, cost of sales, gross profit, profit and
retained profit
• Use simple income statements in decision￾making based on profit calculations (constructing
income statements will not be assessed)
5.4 Statement of financial position
5.4.1 The main elements of a statement of financial
position:
• The main classifications of assets and liabilities,
using examples
5.4.2 Interpret a simple statement of financial
position and make deductions from it,
e.g. how a business is financing its activities and
what assets it owns, sale of inventories to raise
finance (constructing statements of financial
position will not be assessed)
5.5 Analysis of accounts
5.5.1 Profitability: • The concept and importance of profitability
5.5.2 Liquidity: • The concept and importance of liquidity
5.5.3 How to interpret the financial performance
of a business by calculating and analysing
profitability ratios and liquidity ratios:
• Gross profit margin
• Profit margin
• Return on Capital Employed
• Current ratio
• Acid test ratio
5.5.4 Why and how accounts are used: • Needs of different users of accounts and ratio
analysis
• How users of accounts and ratio results might
use information to help make decisions, e.g.
whether to lend to or invest in the business
"""

text6 = """
6 External influences on business activity
6.1 Economic issues
6.1.1 Business cycle: • Main stages of the business cycle, e.g. growth,
boom, recession, slump
• Impact on businesses of changes in employment
levels, inflation and Gross Domestic Product
(GDP)
6.1.2 How government control over the economy
affects business activity and how businesses
may respond:
• Identify government economic objectives,
e.g. increasing Gross Domestic Product (GDP)
• Impact of changes in taxes and government
spending
• Impact of changes in interest rates
• How businesses might respond to these changes
6.2 Environmental and ethical issues
6.2.1 Environmental concerns and ethical issues
as both opportunities and constraints for
businesses:
• How business activity can impact on the
environment, e.g. global warming
• The concept of externalities: possible external
costs and external benefits of business decisions
• Sustainable development; how business activity
can contribute to this
• How and why business might respond to
environmental pressures and opportunities,
e.g. pressure groups
• The role of legal controls over business activity
affecting the environment, e.g. pollution controls
• Ethical issues a business might face: conflicts
between profits and ethics
• How business might react and respond to ethical
issues, e.g. child labour, paying fair prices to
suppliers
6.3 Business and the international economy
6.3.1 The importance of globalisation: • The concept of globalisation and the reasons for
it
• Opportunities and threats of globalisation for
businesses
• Why governments might introduce import tariffs
and import quotas
6.3 Business and the international economy continued
6.3.2 Reasons for the importance and growth of
multinational companies (MNCs):
• Benefits to a business of becoming a
multinational and the impact on its stakeholders
• Potential benefits to a country and/or economy
where a MNC is located, e.g. jobs, exports,
increased choice, investment
• Potential drawbacks to a country and/or
economy where a MNC is located, e.g. reduced
sales of local businesses, repatriation of profits
6.3.3 The impact of exchange rate changes: • Depreciation and appreciation of an exchange
rate
• How exchange rate changes can affect businesses
as importers and exporters of products,
e.g. prices, competitiveness, profitability
(exchange rate calculations will not be assessed)
"""

textarr = [text1, text2, text3, text4, text5, text6]
for i in range(len(textarr)):
    textarr[i] = formatText(textarr[i])

trainModels.train(textarr, allLabels, f"{BASE_PATH}/resources/sci-kit/igbus.joblib")
