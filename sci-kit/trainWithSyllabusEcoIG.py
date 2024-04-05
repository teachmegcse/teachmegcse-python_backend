import trainModels
import getFormattedTextfromPdf


allLabels = ['The basic economic problem', 'The allocation of resources', 
             'Microeconomic decision makers', 'Government and the macroeconomy', 'Economic development', 'International trade and globalisation']


text = """
1 The basic economic problem
1.1 The nature of the economic problem
Topic
1.1.1 finite resources and unlimited wants
1.1.2 economic and free goods
Guidance
Definition and examples of the economic problem in
the contexts of: consumers; workers; producers; and
governments.
The difference between economic goods and free
goods.
1.2 The factors of production
Topic
1.2.1 definitions of the factors of production and
their rewards
1.2.2 mobility of the factors of production
1.2.3 quantity and quality of the factors of
production
Guidance
Definitions and examples of land, labour, capital and
enterprise. Examples of the nature of each factor of
production.
The influences on the mobility of the various factors.
The causes of changes in the quantity and quality of
the various factors.
1.3 Opportunity cost
Topic
1.3.1 definition of opportunity cost
1.3.2 the influence of opportunity cost on decision
making
Guidance
Definition and examples of opportunity cost in
different contexts.
Decisions made by consumers, workers, producers
and governments when allocating their resources.
Cambridge IGCSE Economics 0455 syllabus for 2023, 2024 and 2025. Subject content
10 www.cambridgeinternational.org/igcse Back to contents page
1.4 Production possibility curve (PPC) diagrams
Topic
1.4.1 definition of PPC
1.4.2 points under, on and beyond a PPC
1.4.3 movements along a PPC
1.4.4 shifts in a PPC
Guidance
Definition, drawing and interpretation of appropriate
diagrams.
The significance of the location of production points.
Movements along a PPC and opportunity cost.
The causes and consequences of shifts in a PPC in
terms of an economy’s growth.
"""

text2 = """
2 The allocation of resources
2.1 Microeconomics and macroeconomics
Topic
2.1.1 microeconomics
2.1.2 macroeconomics
Guidance
The difference between microeconomics and
macroeconomics and the decision makers involved
in each.
2.2 The role of markets in allocating resources
Topic
2.2.1 the market system
2.2.2 key resources allocation decisions
2.2.3 introduction to the price mechanism
Guidance
How a market system works; including buyers, sellers,
allocation of scarce resources, market equilibrium,
and market disequilibrium.
Establishing that the economic problem creates three
key questions about determining resource allocation
– what to produce, how, and for whom.
How the price mechanism provides answers to these
key allocation questions.
2.3 Demand
Topic
2.3.1 definition of demand
2.3.2 price, demand and quantity
2.3.3 individual and market demand
2.3.4 conditions of demand
Guidance
Definition, drawing and interpretation of appropriate
diagrams.
A demand curve to be drawn and used to illustrate
movements along a demand curve with appropriate
terminology, for example extensions and
contractions in demand.
The link between individual and market demand in
terms of aggregation.
The causes of shifts in a demand curve with
appropriate terminology, for example increase and
decrease in demand.
Cambridge IGCSE Economics 0455 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 11
2.4 Supply
Topic
2.4.1 definition of supply
2.4.2 price, supply and quantity
2.4.3 individual and market supply
2.4.4 conditions of supply
Guidance
Definition, drawing and interpretation of appropriate
diagrams.
A supply curve to be drawn and used to illustrate
movements along a supply curve with appropriate
terminology, for example extensions and
contractions in supply.
The link between individual and market supply in
terms of aggregation.
The causes of shifts in a supply curve with
appropriate terminology, for example increase and
decrease in supply.
2.5 Price determination
Topic
2.5.1 market equilibrium
2.5.2 market disequilibrium
Guidance
Definition, drawing and interpretation of demand
and supply schedules and curves used to establish
equilibrium price and sales in a market.
Definition, drawing and interpretation of demand
and supply schedules and curves used to identify
disequilibrium prices and shortages (demand
exceeding supply) and surpluses (supply exceeding
demand).
2.6 Price changes
Topic
2.6.1 causes of price changes
2.6.2 consequences of price changes
Guidance
Changing market conditions as causes of price
changes.
Demand and supply diagrams to be used to illustrate
these changes in market conditions and their
consequences for equilibrium price and sales.
Cambridge IGCSE Economics 0455 syllabus for 2023, 2024 and 2025. Subject content
12 www.cambridgeinternational.org/igcse Back to contents page
2.7 Price elasticity of demand (PED)
Topic
2.7.1 definition of PED
2.7.2 calculation of PED
2.7.3 determinants of PED
2.7.4 PED and total spending on a product/revenue
2.7.5 significance of PED
Guidance
Calculation of PED using the formula and interpreting
the significance of the result.
Drawing and interpretation of demand curve
diagrams to show different PED.
The key influences on whether demand is elastic or
inelastic.
The relationship between PED and total spending
on a product/revenue, both in a diagram and as a
calculation.
The implications for decision making by consumers,
producers and government.
2.8 Price elasticity of supply (PES)
Topic
2.8.1 definition of PES
2.8.2 calculation of PES
2.8.3 determinants of PES
2.8.4 significance of PES
Guidance
Calculation of PES using the formula and interpreting
the significance of the result.
Drawing and interpretation of supply curve diagrams
to show different PES.
The key influences on whether supply is elastic or
inelastic.
The implications for decision making by consumers,
producers and government.
2.9 Market economic system
Topic
2.9.1 definition of market economic system
2.9.2 advantages and disadvantages of the market
economic system
Guidance
Including examples of how it works in a variety of
different countries.
Cambridge IGCSE Economics 0455 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 13
2.10 Market failure
Topic
2.10.1 definition of market failure
2.10.2 causes of market failure
2.10.3 consequences of market failure
Guidance
The key terms associated with market failure: public
good, merit good, demerit good, social benefits,
external benefits, private benefits, social costs,
external costs, private costs.
With respect to public goods, merit and demerit
goods, external costs and external benefits, abuse of
monopoly power and factor immobility.
Examples of market failure with respect to these
areas only.
The implications of misallocation of resources in
respect of the over consumption of demerit goods
and goods with external costs, and the under
consumption of merit goods and goods with external
benefits.
Note: demand and supply diagrams relating to
market failure are not required.
2.11 Mixed economic system
Topic
2.11.1 definition of the mixed economic system
2.11.2 government intervention to address market
failure
Guidance
Definitions, drawing and interpretation of appropriate
diagrams showing the effects of three government
microeconomic policy measures: maximum and
minimum prices in product, labour and foreign
exchange markets; indirect taxation; and subsidies.
The implications of other government
microeconomic policy measures: regulation;
privatisation and nationalisation; and direct provision
of goods.
The effectiveness of government intervention in
overcoming the drawbacks of a market economic
system. 
"""

text3 = """
3 Microeconomic decision makers
3.1 Money and banking
Topic
3.1.1 money
3.1.2 banking
Guidance
The forms, functions and characteristics of money.
The role and importance of central banks and
commercial banks for government, producers and
consumers.
3.2 Households
Topic
3.2.1 the influences on spending, saving and
borrowing
Guidance
Including income, the rate of interest and confidence
– between different households and over time.
3.3 Workers
Topic
3.3.1 factors affecting an individual’s choice of
occupation
3.3.2 wage determination
3.3.3 reasons for differences in earnings
3.3.4 division of labour/specialisation
Guidance
Wage and non-wage factors.
The influences of demand and supply, relative
bargaining power and government policy, including
minimum wage.
How changes in demand and supply, relative
bargaining strengths, discrimination and government
policy can all influence differences in earnings
between workers whether they are: skilled/unskilled;
primary/secondary/tertiary; male/female; private
sector/public sector. Definition, drawing and
interpretation of diagrams that illustrate the effects
of changes in demand and supply in the labour
market.
Advantages and disadvantages for workers, firms and
the economy.
3.4 Trade unions
Topic
3.4.1 definition of a trade union
3.4.2 the role of trade unions in the economy
3.4.3 the advantages and disadvantages of trade
union activity
Guidance
Including engaging in collective bargaining on wages,
working hours and working conditions; protecting
employment; and influencing government policy.
Factors influencing the strength of trade unions.
From the viewpoint of workers, firms and the
government.
Cambridge IGCSE Economics 0455 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 15
3.5 Firms
Topic
3.5.1 classification of firms
3.5.2 small firms
3.5.3 causes and forms of the growth of firms
3.5.4 mergers
3.5.5 economies and diseconomies of scale
Guidance
In terms of primary/secondary/tertiary sectors and
private/public sector, and the relative size of firms.
Note: detailed knowledge of different types of
structure of a firm is not required.
The advantages and disadvantages of small firms, the
challenges facing small firms and reasons for their
existence.
Internal growth, for example increased market share.
External growth, for example mergers.
Examples, advantages and disadvantages of
different types of mergers: horizontal, vertical, and
conglomerate.
How internal and external economies and
diseconomies of scale can affect a firm/industry as
the scale of production changes.
3.6 Firms and production
Topic
3.6.1 demand for factors of production
3.6.2 labour-intensive and capital-intensive
production
3.6.3 production and productivity
Guidance
Influences to include demand for the product,
the price of different factors of production, their
availability and their productivity.
The reasons for adopting the different forms of
production and their advantages and disadvantages.
The difference between, and influences on,
production and productivity.
3.7 Firms’ costs, revenue and objectives
Topic
3.7.1 definition of costs of production
3.7.2 calculation of costs of production
3.7.3 definition of revenue
3.7.4 calculation of revenue
3.7.5 objectives of firms
Guidance
Total cost (TC), average total cost (ATC), fixed cost
(FC), variable cost (VC), average fixed cost (AFC),
average variable cost (AVC).
Note: marginal cost is not required.
Calculation of TC, ATC, FC, VC, AFC and AVC.
Definition, drawing and interpretation of diagrams
that show how changes in output affect costs of
production.
Total revenue (TR) and average revenue (AR).
Note: marginal revenue is not required.
Calculation of TR and AR.
The influence of sales on revenue.
Survival, social welfare, profit maximisation and
growth.
Cambridge IGCSE Economics 0455 syllabus for 2023, 2024 and 2025. Subject content
16 www.cambridgeinternational.org/igcse Back to contents page
3.8 Market structure
Topic
3.8.1 competitive markets
3.8.2 monopoly markets
Guidance
The effect of having a high number of firms on price,
quality, choice, profit.
Note: the theory of perfect and imperfect
competition and diagrams are not required.
Characteristics, advantages and disadvantages of
monopoly.
Note: diagrams are not required. """

text4 = """
4 Government and the macroeconomy
4.1 The role of government
Topic
4.1.1 the role of government
Guidance
Locally, nationally and internationally.
4.2 The macroeconomic aims of government
Topic
4.2.1 the macroeconomic aims of government
4.2.2 possible conflicts between macroeconomic
aims
Guidance
Economic growth, full employment/low
unemployment, stable prices/low inflation, balance
of payments stability, redistribution of income.
Reasons behind the choice of aims and the criteria
that governments set for each aim.
Possible conflicts between aims: full employment
versus stable prices; economic growth versus balance
of payments stability; and full employment versus
balance of payments stability.
4.3 Fiscal policy
Topic
4.3.1 definition of the government budget
4.3.2 reasons for government spending
4.3.3 reasons for taxation
4.3.4 classification of taxes
4.3.5 principles of taxation
4.3.6 impact of taxation
Guidance
The main areas of government spending and the
reasons for and effects of spending in these areas.
Taxation as the main source of government revenue
and the reasons for levying taxation.
Examples of the different classifications of tax;
progressive, regressive, proportional; and direct,
indirect.
The qualities of a good tax.
The impact of taxation on consumers, producers,
government and economy as a whole.
Continued
Cambridge IGCSE Economics 0455 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 17
4.3 Fiscal policy continued
Topic
4.3.7 definition of fiscal policy
4.3.8 fiscal policy measures
4.3.9 effects of fiscal policy on government
macroeconomic aims
Guidance
The tax and spending changes, in the form of fiscal
policy, that cause budget balance or imbalance.
Including calculations of the size of a budget deficit
or surplus.
How fiscal policy measures may enable the
government to achieve its macroeconomic aims.
Note: aggregate demand and aggregate supply are
not required.
4.4 Monetary policy
Topic
4.4.1 definition of money supply and monetary
policy
4.4.2 monetary policy measures
4.4.3 effects of monetary policy on government
macroeconomic aims
Guidance
Changes in interest rates, money supply and foreign
exchange rates.
How monetary policy measures may enable the
government to achieve its macroeconomic aims.
4.5 Supply-side policy
Topic
4.5.1 definition of supply-side policy
4.5.2 supply-side policy measures
4.5.3 effects of supply-side policy measures on
government macroeconomic aims
Guidance
Possible supply-side policy measures include
education and training, labour market reforms, lower
direct taxes, deregulation, improving incentives to
work and invest, and privatisation.
How supply-side policy measures may enable the
government to achieve its macroeconomic aims.
Cambridge IGCSE Economics 0455 syllabus for 2023, 2024 and 2025. Subject content
18 www.cambridgeinternational.org/igcse Back to contents page
4.6 Economic growth
Topic
4.6.1 definition of economic growth
4.6.2 measurement of economic growth
4.6.3 causes and consequences of recession
4.6.4 causes of economic growth
4.6.5 consequences of economic growth
4.6.6 policies to promote economic growth
Guidance
Real Gross Domestic Product (GDP) and how it can
be used to measure economic growth. GDP per head
(capita).
Meaning of recession and how a recession moves the
economy within its PPC.
How changes in total demand may increase the
utilisation of resources and GDP – resulting in a
movement from inside toward the PPC.
How economic growth shifts the economy’s PPC to
the right and is caused by changes in investment,
technology, and the quantity and quality of the
factors of production.
The costs and benefits of economic growth in the
context of different economies.
The range of policies available to promote economic
growth and how effective they might be.
4.7 Employment and unemployment
Topic
4.7.1 definition of employment, unemployment and
full employment
4.7.2 changing patterns and level of employment
4.7.3 measurement of unemployment
4.7.4 causes/types of unemployment
4.7.5 consequences of unemployment
4.7.6 policies to reduce unemployment
Guidance
The nature and causes of changes in the pattern of
employment, for example increase in proportion
of workers employed in the tertiary sector and
formal economy as an economy develops; a greater
proportion of women in the labour force due to
changes in social attitudes; decline in the proportion
employed in the public sector as a country moves
towards a market economy.
How unemployment is measured – claimant count
and labour force survey – and the formula for the
unemployment rate.
Frictional, structural and cyclical unemployment.
The consequences of unemployment for the
individual, firms and the economy as a whole.
The range of policies available to reduce
unemployment and how effective they might be.
Cambridge IGCSE Economics 0455 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 19
4.8 Inflation and deflation
Topic
4.8.1 definition of inflation and deflation
4.8.2 measurement of inflation and deflation
4.8.3 causes of inflation and deflation
4.8.4 consequences of inflation and deflation
4.8.5 policies to control inflation and deflation
Guidance
Measurement of inflation and deflation using the
Consumer Prices Index (CPI).
Causes of inflation: demand-pull and cost-push.
Causes of deflation: demand-side and supply-side.
The consequences of inflation and deflation for
consumers, workers, savers, lenders, firms and the
economy as a whole.
The range of policies available to control inflation and
deflation and how effective they might be."""

text5 = """
5 Economic development
5.1 Living standards
Topic
5.1.1 indicators of living standards
5.1.2 comparing living standards and income
distribution
Guidance
Real GDP per head and the Human Development
Index (HDI).
The components of real GDP and HDI.
The advantages and disadvantages of real GDP and
HDI.
Reasons for differences in living standards and
income distribution within and between countries.
5.2 Poverty
Topic
5.2.1 definition of absolute and relative poverty
5.2.2 the causes of poverty
5.2.3 policies to alleviate poverty and redistribute
income
Guidance
The difference between the two terms.
The causes of poverty including unemployment, low
wages, illness and age.
Policies including those promoting economic growth,
improved education, more generous state benefits,
progressive taxation, and national minimum wage.
Cambridge IGCSE Economics 0455 syllabus for 2023, 2024 and 2025. Subject content
20 www.cambridgeinternational.org/igcse Back to contents page
5.3 Population
Topic
5.3.1 the factors that affect population growth
5.3.2 reasons for different rates of population
growth in different countries
5.3.3 the effects of changes in the size and structure
of population on different countries
Guidance
Birth rate, death rate, net migration, immigration and
emigration.
How and why birth rates, death rates and net
migration vary between countries.
The concept of an optimum population. The effects
of increases and decreases in population size and
changes in the age and gender distribution of
population.
Note: interpretation of a population pyramid is
required, but drawing is not.
5.4 Differences in economic development between countries
Topic
5.4.1 differences in economic development
between countries
Guidance
Causes and impacts of differences in income;
productivity; population growth; size of primary,
secondary and tertiary sectors; saving and
investment; education; and healthcare."""

text6 = """
6 International trade and globalisation
6.1 International specialisation
Topic
6.1.1 specialisation at a national level
6.1.2 advantages and disadvantages of specialisation
at a national level
Guidance
The basis for specialisation at national level in broad
terms of: superior resource allocation and/or cheaper
production methods.
For consumers, firms and the economy.
6.2 Globalisation, free trade and protection
Topic
6.2.1 definition of globalisation
6.2.2 role of multinational companies (MNCs)
6.2.3 the benefits of free trade
6.2.4 methods of protection
6.2.5 reasons for protection
6.2.6 consequences of protection
Guidance
MNCs and the costs and benefits to their host and
home countries.
The benefits for consumers, producers and the
economy in a variety of countries.
Tariffs, import quotas, subsidies and embargoes.
Including infant industry, declining industry, strategic
industry and avoidance of dumping.
Effectiveness of protection and its impact on the
home country and its trading partners.
Cambridge IGCSE Economics 0455 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/igcse 21
6.3 Foreign exchange rates
Topic
6.3.1 definition of foreign exchange rate
6.3.2 determination of foreign exchange rate in
foreign exchange market
6.3.3 causes of foreign exchange rate fluctuations
6.3.4 consequences of foreign exchange rate
fluctuations
6.3.5 floating and fixed foreign exchange rates
Guidance
Floating and fixed systems.
The demand for and supply of a currency in the
foreign exchange market and the determination of
the equilibrium foreign exchange rate.
Including changes in demand for exports and imports,
changes in the rate of interest, speculation, and the
entry or departure of MNCs.
The effects of foreign exchange rate fluctuations on
export and import prices and spending on imports
and exports via the PED.
The difference between, and the advantages and
disadvantages of, a floating foreign exchange rate
and a fixed foreign exchange rate system.
6.4 Current account of balance of payments
Topic
6.4.1 structure
6.4.2 causes of current account deficit and surplus
6.4.3 consequences of current account deficit and
surplus
6.4.4 policies to achieve balance of payments
stability
Guidance
The components of the current account of the
balance of payments – trade in goods, trade in
services, primary income and secondary income.
Calculation of deficits and surpluses on the current
account of the balance of payments and its
component sections.
Reasons for deficits and surpluses.
Impact on GDP, employment, inflation and foreign
exchange rate.
The range of policies available to achieve balance of
payments stability and how effective they might be."""

textarr = [text, text2, text3, text4, text5, text6]
for i in range(len(textarr)):
    textarr[i] = getFormattedTextfromPdf.formatText(textarr[i])

trainModels.train(textarr, allLabels)
