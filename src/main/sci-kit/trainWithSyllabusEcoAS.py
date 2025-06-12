import trainModels
import getFormattedTextfromPdf


allLabels = ['Scarcity, choice and opportunity cost, Economic methodology, Factors of production', 'Resource allocation in different economic systems, PPC, goods and services', 
             'Demand and Supply, elasticities', 'The interaction of demand and supply, Surpluses', 'Government microeconomic intervention', 'National income, Circular Flow', 'Aggregate Demand and Aggregate Supply',
               'Economic Growth, Unemployment and Price stability', 'Government Policies', 'International trade and Protectionism', 'Balance of Payments and Exchange rates']


text = """
1.1 Scarcity, choice and opportunity cost
1.1.1 fundamental economic problem of scarcity
1.1.2 need to make choices at all levels (individuals, firms, governments)
1.1.3 nature and definition of opportunity cost, arising from choices
1.1.4 basic questions of resource allocation:
• what to produce
• how to produce
• for whom to produce
1.2 Economic methodology
1.2.1 economics as a social science
1.2.2 positive and normative statements (the distinction between facts and value judgements)
1.2.3 meaning of the term ceteris paribus
1.2.4 importance of the time period (short run, long run, very long run)
1.3 Factors of production
1.3.1 nature and definition of factors of production: land, labour, capital and enterprise
1.3.2 difference between human capital and physical capital
1.3.3 rewards to the factors of production
1.3.4 division of labour and specialisation
1.3.5 role of the entrepreneur in contemporary economies: risk and organisation of the other factors of
production
"""

text2 = """
1.4 Resource allocation in different economic systems
1.4.1 decision-making in market, planned and mixed economies
1.4.2 resource allocation in these economic systems
1.5 Production possibility curves
1.5.1 nature and meaning of a production possibility curve (PPC)
1.5.2 shape of the PPC: constant and increasing opportunity costs
1.5.3 causes and consequences of shifts in a PPC
1.5.4 significance of a position within a PPC
1.6 Classification of goods and services
1.6.1 nature and definition of free goods and private goods (economic goods)
1.6.2 nature and definition of public goods
1.6.3 nature and definition of merit goods: under-consumption as a result of imperfect information in the
market
1.6.4 nature and definition of demerit goods: over-consumption as a result of imperfect information in the
market
"""

text3 = """
2.1 Demand and supply curves
2.1.1 effective demand
2.1.2 individual and market demand and supply
2.1.3 determinants of demand
2.1.4 determinants of supply
2.1.5 causes of a shift in the demand curve (D)
2.1.6 causes of a shift in the supply curve (S)
2.1.7 distinction between the shift in the demand or supply curve and the movement along these curves
Cambridge International AS & A Level Economics 9708 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/alevel 15
2 The price system and the microeconomy (AS Level) continued
2.2 Price elasticity, income elasticity and cross elasticity of demand
2.2.1 definition of price elasticity, income elasticity and cross elasticity of demand (PED, YED, XED)
2.2.2 formulae for and calculation of price elasticity, income elasticity and cross elasticity of demand
2.2.3 significance of relative percentage changes, the size and sign of the coefficient of:
• price elasticity of demand
• income elasticity of demand
• cross elasticity of demand
2.2.4 descriptions of elasticity values: perfectly elastic, (highly) elastic, unitary elasticity, (highly) inelastic,
perfectly inelastic
2.2.5 variation in price elasticity of demand along the length of a straight-line demand curve
2.2.6 factors affecting:
• price elasticity of demand
• income elasticity of demand
• cross elasticity of demand
2.2.7 relationship between price elasticity of demand and total expenditure on a product
2.2.8 implications for decision-making of price elasticity, income elasticity and cross elasticity of demand
2.3 Price elasticity of supply
2.3.1 definition of price elasticity of supply (PES)
2.3.2 formula for and calculation of price elasticity of supply
2.3.3 significance of relative percentage changes, the size and sign of the coefficient of price elasticity of supply
2.3.4 factors affecting price elasticity of supply
2.3.5 implications for speed and ease with which firms react to changed market conditions
"""

text4 = """
2.4 The interaction of demand and supply
2.4.1 definition of market equilibrium and disequilibrium
2.4.2 effects of shifts in demand and supply curves on equilibrium price and quantity
2.4.3 relationships between different markets:
• joint demand (complements)
• alternative demand (substitutes)
• derived demand
• joint supply
2.4.4 functions of price in resource allocation; rationing, signalling (transmission of preferences) and
incentivising
2.5 Consumer and producer surplus
2.5.1 meaning and significance of consumer surplus
2.5.2 meaning and significance of producer surplus
2.5.3 causes of changes in consumer and producer surplus
2.5.4 significance of price elasticity of demand and of supply in determining the extent of these changes 
"""

text5 = """
Candidates will explore the reasons for government intervention in individual markets, the methods of
intervention deployed, the advantages and disadvantages of the methods and their effectiveness. Candidates
will also consider why market economies create income and wealth inequality, and will evaluate the strengths
and weaknesses of policies designed to redistribute income and wealth. The key concepts that support these
topics are: the margin and decision-making; efficiency and inefficiency; the role of government and the issues of
equality and equity.
3.1 Reasons for government intervention in markets
3.1.1 addressing the non-provision of public goods
3.1.2 addressing the over-consumption of demerit goods and the under-consumption of merit goods
3.1.3 controlling prices in markets
3.2 Methods and effects of government intervention in markets
3.2.1 impact and incidence of specific indirect taxes
3.2.2 impact and incidence of subsidies
3.2.3 direct provision of goods and services
3.2.4 maximum and minimum prices
3.2.5 buffer stock schemes
3.2.6 provision of information
3.3 Addressing income and wealth inequality
3.3.1 difference between income as a flow concept and wealth as a stock concept
3.3.2 measuring income and wealth inequality:
• Gini coefficient (calculation not required)
3.3.3 economic reasons for inequality of income and wealth
3.3.4 policies to redistribute income and wealth:
• minimum wage
• transfer payments
• progressive income taxes, inheritance and capital taxes
• state provision of essential goods and services
"""

text6 = """
4.1 National income statistics
4.1.1 meaning of national income
4.1.2 measurement of national income:
• Gross Domestic Product (GDP)
• Gross National Income (GNI)
• Net National Income (NNI)
4.1.3 adjustment of measures from market prices to basic prices
4.1.4 adjustment of measures from gross values to net values
4.2 Introduction to the circular flow of income
4.2.1 circular flow of income in a closed economy and an open economy: the flow of income between
households, firms and government and the international economy
4.2.2 injections and leakages (multiplier not required)
4.2.3 equilibrium and disequilibrium (marginal and average propensities not required)
"""

text7 = """
4.3 Aggregate Demand and Aggregate Supply analysis
4.3.1 definition of Aggregate Demand (AD)
4.3.2 components of AD and their meanings: AD = C + I + G + (X – M)
4.3.3 determinants of AD (detailed knowledge of the components of AD is not required)
4.3.4 shape of the AD curve (downward sloping)
4.3.5 causes of a shift in the AD curve
4.3.6 definition of Aggregate Supply (AS)
4.3.7 determinants of AS
4.3.8 shape of the AS curve in the short run (SRAS, upward sloping line or sweeping curve) and the long run
(LRAS, either a vertical line or in three sections – highly elastic, upward sloping, vertical)
4.3.9 causes of a shift in the AS curve in the short run (SRAS) and in the long run (LRAS)
4.3.10 distinction between a movement along and a shift in AD and AS
4.3.11 establishment of equilibrium in the AD/AS model and the determination of the level of real output, the
price level and employment
4.3.12 effects of shifts in the AD curve and the AS curve on the level of real output, the price level and
employment
"""

text8 = """
4.4 Economic growth
4.4.1 meaning of economic growth
4.4.2 measurement of economic growth
4.4.3 distinction between growth in nominal GDP and real GDP
4.4.4 causes of economic growth
4.4.5 consequences of economic growth
4.5 Unemployment
4.5.1 meaning of unemployment
4.5.2 measures of unemployment, with reference to possible difficulties in measurement
4.5.3 causes and types of unemployment: frictional, structural, cyclical, seasonal and technological
4.5.4 consequences of unemployment
4.6 Price stability
4.6.1 definition of inflation, deflation and disinflation
4.6.2 measurement of changes in the price level:
• consumer price index (CPI)
• possible difficulties in measurement
4.6.3 distinction between money values (nominal) and real data
4.6.4 causes of inflation: cost-push and demand-pull inflation
4.6.5 consequences of inflation
"""

text9 = """
5 Government macroeconomic intervention (AS Level)
Candidates will investigate government macroeconomic policy objectives and the three main types of policy
available with which to meet these objectives: fiscal, monetary and supply-side policy. Candidates will consider
what constitutes expansionary policy and contractionary policy and when it is appropriate to use each policy.
They will also analyse the impact of each policy on the main macroeconomic performance indicators. The key
concepts used here will be: the margin and decision-making; time; equilibrium and disequilibrium; progress and
development.
5.1 Government macroeconomic policy objectives
5.1.1 use of government policy to achieve macroeconomic objectives: price stability, low unemployment,
economic growth (policy conflicts and trade-offs are not required)
Cambridge International AS & A Level Economics 9708 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/alevel 19
5 Government macroeconomic intervention (AS Level) continued
5.2 Fiscal policy
5.2.1 meaning of government budget
5.2.2 distinction between a government budget deficit and a government budget surplus
5.2.3 meaning and significance of the national debt
5.2.4 taxation:
• types of taxes: direct/indirect, progressive/regressive/proportional
• rates of tax: marginal and average rates of taxation (mrt, art)
• reasons for taxation
5.2.5 government spending:
• types of spending: capital (investment) and current
• reasons for government spending
5.2.6 distinction between expansionary and contractionary fiscal policy
5.2.7 AD/AS analysis of the impact of expansionary and contractionary fiscal policy on the equilibrium level of
national income and the level of real output, the price level and employment
5.3 Monetary policy
5.3.1 definition of monetary policy
5.3.2 tools of monetary policy: interest rates, money supply and credit regulations
5.3.3 distinction between expansionary and contractionary monetary policy
5.3.4 AD/AS analysis of the impact of expansionary and contractionary monetary policy on the equilibrium
national income and the level of real output, the price level and employment
5.4 Supply-side policy
5.4.1 meaning of supply-side policy, in terms of its effect on LRAS curves
5.4.2 objectives of supply-side policy: increasing productivity and productive capacity
5.4.3 tools of supply-side policy, for example training, infrastructure development, support for technological
improvement
5.4.4 AD/AS analysis of the impact of supply-side policy on the equilibrium national income and the level of
real output, the price level and employment
"""

text10 = """
6.1 The reasons for international trade
6.1.1 distinction between absolute and comparative advantage
6.1.2 benefits of specialisation and free trade (trade liberalisation), including the trading possibility curve
6.1.3 exports, imports and the terms of trade:
• measurement of the terms of trade
• causes of changes in the terms of trade
• impact of changes in the terms of trade
6.1.4 limitations of the theories of absolute and comparative advantage
6.2 Protectionism
6.2.1 meaning of protectionism in the context of international trade
6.2.2 different tools of protection and their impact:
• tariffs
• import quotas
• export subsidies
• embargoes
• excessive administrative burdens red tape
6.2.3 arguments for and against protectionism
"""

text11 = """
6.3 Current account of the balance of payments
6.3.1 components of the current account of the balance of payments:
• current account: trade in goods, trade in services, primary income and secondary income
• definition of balance and imbalances (deficit and surplus) in the current account of the balance of
payments
6.3.2 calculation of:
• balance of trade in goods
• balance of trade in services
• balance of trade in goods and services
• current account balance (CAB)
6.3.3 causes of imbalances in the current account of the balance of payments
6.3.4 consequences of imbalances in the current account of the balance of payments for the domestic and
external economy
Cambridge International AS & A Level Economics 9708 syllabus for 2023, 2024 and 2025. Subject content
Back to contents page www.cambridgeinternational.org/alevel 21
6 International economic issues (AS Level) continued
6.4 Exchange rates
6.4.1 definition of exchange rate
6.4.2 determination of a floating exchange rate
6.4.3 distinction between depreciation and appreciation of a floating exchange rate
6.4.4 causes of changes in a floating exchange rate: demand and supply of the currency
6.4.5 AD/AS analysis of the impact of exchange rate changes on the domestic economy’s equilibrium national
income and the level of real output, the price level and employment
6.5 Policies to correct imbalances in the current account of the balance of payments
6.5.1 government policy objective of stability of the current account
6.5.2 effect of fiscal, monetary, supply-side and protectionist policies on the current account
"""



textarr = [text, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11]
for i in range(len(textarr)):
    textarr[i] = getFormattedTextfromPdf.formatText(textarr[i])

trainModels.train(textarr, allLabels)
