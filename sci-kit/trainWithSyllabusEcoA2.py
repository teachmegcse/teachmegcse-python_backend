import trainModels
import getFormattedTextfromPdf


allLabels = ['Utility', 'Indifference curves and budget lines', 
             'Efficiency and market failure', 'Private costs and benefits, externalities and social costs and benefits ',
               'Types of cost, revenue and profit, short-run and long-run production',
               'market structures', 'Growth and survival of firms',
               'objectives and policies of firms', 'Government policies to achieve efficient resource allocation',
                'Equity and redistribution of income and wealth', 'Labour market forces and government intervention', 'The circular flow of income',
               'Economic growth and sustainability', 'Employment/unemployment', 'Money and banking', 'Government macroeconomic policy objectives',
               'balance of payments', 'Economic development', 'levels of development']


text = """
7.1 Utility
7.1.1 definition and calculation of total utility and marginal utility
7.1.2 diminishing marginal utility
7.1.3 equi-marginal principle
7.1.4 derivation of an individual demand curve
7.1.5 limitations of marginal utility theory and its assumptions of rational behaviour
"""

text2 = """
7.2 Indifference curves and budget lines
7.2.1 meaning of an indifference curve and a budget line
7.2.2 causes of a shift in the budget line
7.2.3 income, substitution and price effects for normal, inferior and Giffen goods
7.2.4 limitations of the model of indifference curves
"""

text3 = """
7.3 Efficiency and market failure
7.3.1 definitions of productive efficiency and allocative efficiency
7.3.2 conditions for productive efficiency and allocative efficiency
7.3.3 Pareto optimality
7.3.4 definition of dynamic efficiency
7.3.5 definition of market failure
7.3.6 reasons for market failure
"""

text4 = """
7.4 Private costs and benefits, externalities and social costs and benefits
7.4.1 definition and calculation of social costs (SC) as the sum of private costs (PC) and external costs (EC),
including marginal social costs (MSC), marginal private costs (MPC) and marginal external costs (MEC)
7.4.2 definition and calculation of social benefits (SB) as the sum of private benefits (PB) and external benefits
(EB), including marginal social benefits (MSB), marginal private benefits (MPB) and marginal external
benefits (MEB)
7.4.3 definition of positive externality and negative externality
7.4.4 positive and negative externalities of both consumption and production
7.4.5 deadweight welfare losses arising from positive and negative externalities
7.4.6 asymmetric information and moral hazard
7.4.7 use of costs and benefits in analysing decisions (knowledge of net present value is not required)
"""

text5 = """
7.5 Types of cost, revenue and profit, short-run and long-run production
7.5.1 short-run production function:
• fixed and variable factors of production
• definition and calculation of total product, average product and marginal product
• law of diminishing returns (law of variable proportions)
7.5.2 short-run cost function:
• definition and calculation of fixed costs (FC) and variable costs (VC)
• definition and calculation of total, average and marginal costs (TC, AC, MC), including average total
cost (ATC), total and average fixed costs (TFC, AFC) and total and average variable costs (TVC, AVC)
• explanation of shape of short-run average cost and marginal cost curves
7.5.3 long-run production function:
• no fixed factors of production
• returns to scale
7.5.4 long-run cost function:
• explanation of shape of long-run average cost curve
• concept of minimum efficient scale
7.5.5 relationship between economies of scale and decreasing average costs
7.5.6 internal and external economies of scale
7.5.7 internal and external diseconomies of scale
7.5.8 definition and calculation of revenue: total, average and marginal revenue (TR, AR, MR)
7.5.9 definition of normal, subnormal and supernormal profit
7.5.10 calculation of supernormal and subnormal profit
"""

text6 = """
7.6 Different market structures
7.6.1 perfect competition and imperfect competition: monopoly, monopolistic competition, oligopoly, natural
monopoly
7.6.2 structure of the listed markets as explained by number of buyers and sellers, product differentiation,
degree of freedom of entry and availability of information
7.6.3 barriers to entry and exit:
• legal barriers
• market barriers
• cost barriers
• physical barriers
7.6 Different market structures continued
7.6.4 performance of firms in different market structures:
• revenues and revenue curves
• output in the short run and the long run
• profits in the short run and the long run
• shutdown price in the short run and the long run
• derivation of a firm’s supply curve in a perfectly competitive market
• efficiency and X-inefficiency in the short run and the long run
• contestable markets: features and implications
• price competition and non-price competition
• collusion and the Prisoner’s Dilemma in oligopolistic markets, including a two-player pay-off matrix
7.6.5 definition and calculation of the concentration ratio
"""

text7 = """
7.7 Growth and survival of firms
7.7.1 reasons for different sizes of firms
7.7.2 internal growth of firms: organic growth and diversification
7.7.3 external growth of firms – integration (mergers and takeovers):
• methods of integration:
– horizontal
– vertical (forwards and backwards)
– conglomerate
• reasons for integration
• consequences of integration
7.7.4 cartels:
• conditions for an effective cartel
• consequences of a cartel
7.7.5 principal–agent problem arising from differing objectives of shareholders/owners and managers
"""

text8 = """
7.8 Differing objectives and policies of firms
7.8.1 traditional profit-maximising objective of firms
7.8.2 an understanding of other objectives of firms:
• survival
• profit satisficing
• sales maximisation
• revenue maximisation
7.8.3 price discrimination – first, second and third degree:
• conditions for effective price discrimination
• consequences of price discrimination
7.8.4 other pricing policies:
• limit pricing
• predatory pricing
• price leadership
7.8.5 relationship between price elasticity of demand and a firm’s revenue:
• in a normal downward sloping demand curve
• in a kinked demand curve
"""

text9 = """
8.1 Government policies to achieve efficient resource allocation and correct market failure
8.1.1 application and effectiveness of measures to tackle different forms of market failure:
• specific and ad valorem indirect taxes
• subsidies
• price controls
• production quotas
• prohibitions and licences
• regulation and deregulation
• direct provision
• pollution permits
• property rights
• nationalisation and privatisation
• provision of information
• behavioural insights and ‘nudge’ theory
8.1 Government policies to achieve efficient resource allocation and correct market failure continued
8.1.2 government failure in microeconomic intervention:
• definition of government failure
• causes of government failure
• consequences of government failure
"""

text10 = """
8.2 Equity and redistribution of income and wealth
8.2.1 difference between equity and equality
8.2.2 difference between equity and efficiency
8.2.3 distinction between absolute poverty and relative poverty
8.2.4 the poverty trap
8.2.5 policies towards equity and equality, for example:
• negative income tax
• universal benefits and means-tested benefits
• universal basic income
"""

text11 = """
8.3 Labour market forces and government intervention
8.3.1 demand for labour as a derived demand
8.3.2 factors affecting demand for labour in a firm or an occupation
8.3.3 causes of shifts in and movement along the demand curve for labour in a firm or an occupation
8.3.4 marginal revenue product (MRP) theory:
• definition and calculation of marginal revenue product
• derivation of an individual firm’s demand for labour using marginal revenue product
8.3.5 factors affecting the supply of labour to a firm or to an occupation:
• wage and non-wage factors
8.3.6 causes of shifts in and movement along the supply curve of labour to a firm or an occupation
8.3.7 wage determination in perfect markets:
• equilibrium wage rate and employment in a labour market
8.3.8 wage determination in imperfect markets:
• influence of trade unions on wage determination and employment in a labour market
• influence of government on wage determination and employment in a labour market using a national
minimum wage
• influence of monopsony employers on wage determination and employment in a labour market
8.3.9 determination of wage differentials by labour market forces
8.3.10 transfer earnings and economic rent:
• definition of transfer earnings
• definition of economic rent
• factors affecting transfer earnings and economic rent in an occupation
"""

text12 = """
9.1 The circular flow of income
9.1.1 the multiplier process:
• definition of the multiplier
• formulae for and calculation of multiplier in a closed and open economy, with and without a
government sector
• calculation of:
– average and marginal propensities to save (aps and mps)
– average and marginal propensities to consume (apc and mpc)
– average and marginal propensities to import (apm and mpm)
– average and marginal rates of tax (art and mrt)
• national income determination using AD and income approach with the multiplier process
• calculation of effect of changing AD on national income using the multiplier
9.1.2 components of Aggregate Demand (AD) and their determinants:
• consumption function: autonomous and induced consumer expenditure
• savings function: autonomous and induced savings
• autonomous and induced investment; the accelerator
• government spending
• net exports (exports minus imports)
9.1.3 full employment level of national income and equilibrium level of national income:
• inflationary and deflationary gaps 
"""

text13 = """
9.2 Economic growth and sustainability
9.2.1 actual growth versus potential growth in national output
9.2.2 positive and negative output gaps
9.2.3 business (trade) cycle:
• phases of the cycle
• causes of the cycle
• role of automatic stabilisers
9.2.4 policies to promote economic growth and their effectiveness
9.2 Economic growth and sustainability continued
9.2.5 inclusive economic growth:
• definition of inclusive economic growth
• impact of economic growth on equity and equality
• policies to promote inclusive growth
9.2.6 sustainable economic growth:
• definition of sustainable economic growth
• using and conserving resources
• impact of economic growth on the environment and climate change
• policies to mitigate the impact of economic growth on the environment and climate change
"""

text14 = """
9.3 Employment/unemployment
9.3.1 definition of full employment
9.3.2 equilibrium and disequilibrium unemployment (including hysteresis)
9.3.3 voluntary and involuntary unemployment
9.3.4 natural rate of unemployment:
• definition
• determinants
• policy implications
9.3.5 patterns and trends in (un)employment
9.3.6 mobility of labour:
• forms of labour mobility: geographical and occupational
• factors affecting labour mobility
9.3.7 policies to reduce unemployment and their effectiveness
"""

text15 = """
9.4 Money and banking
9.4.1 definition, functions and characteristics of money
9.4.2 definition of money supply
9.4.3 quantity theory of money (MV = PT)
9.4.4 functions of commercial banks:
• providing deposit accounts (demand deposit account, savings account)
• lending money (overdrafts, loans)
• holding or providing cash, securities, loans, deposits, equity
• reserve ratio and capital ratio
• objectives of commercial banks: liquidity, security, profitability
9.4 Money and banking continued
9.4.5 causes of changes in the money supply in an open economy:
• commercial banks as sources of credit creation and the bank credit multiplier
• role of a central bank
• government deficit financing
• quantitative easing
• changes in the balance of payments
9.4.6 policies to reduce inflation and their effectiveness
9.4.7 demand for money: liquidity preference theory
9.4.8 interest rate determination: loanable funds theory and Keynesian theory
"""

text16 = """
10.1 Government macroeconomic policy objectives
10.1.1 objectives in terms of inflation, balance of payments, unemployment, growth, development, sustainability
and redistribution of income and wealth
10.2 Links between macroeconomic problems and their interrelatedness
10.2.1 relationship between the internal value of money and the external value of money
10.2.2 relationship between the balance of payments and inflation
10.2.3 relationship between growth and inflation
10.2.4 relationship between growth and the balance of payments
10.2.5 relationship between inflation and unemployment:
• traditional Phillips curve
• expectations-augmented Phillips curve (short- and long-run Phillips curve)
10.3 Effectiveness of policy options to meet all macroeconomic objectives
10.3.1 effectiveness of different policies in relation to different macroeconomic objectives:
• fiscal policy including Laffer curve analysis
• monetary policy
• supply-side policy including market-based and interventionist policies
• exchange rate policy
• international trade policy
10.3.2 problems and conflicts arising from the outcome of these policies
10.3.3 existence of government failure in macroeconomic policies
"""

text17 = """
11.1 Policies to correct disequilibrium in the balance of payments
11.1.1 components of the balance of payments accounts: current account, financial account and capital account
11.1.2 effect of fiscal, monetary, supply-side, protectionist and exchange rate policies on the balance of
payments
11.1.3 difference between expenditure-switching and expenditure-reducing policies
11.2 Exchange rates
11.2.1 measurement of exchange rates:
• distinction between nominal and real exchange rates
• trade-weighted exchange rates
11.2.2 determination of exchange rates under fixed and managed systems
11.2.3 distinction between revaluation and devaluation of a fixed exchange rate
11.2.4 changes in the exchange rate under different exchange rate systems
11.2.5 the effects of changing exchange rates on the external economy using Marshall-Lerner and J curve
analysis
"""

text18 = """
11.3 Economic development
11.3.1 classification of economies in terms of their level of development
11.3.2 classification of economies in terms of their level of national income
11.3.3 indicators of living standards and economic development:
• monetary indicators including real per capita national income statistics (GDP, GNI, NNI) and
purchasing power parity
• issues of comparison using monetary indicators
• non-monetary indicators
• composite indicators:
– Human Development Index (HDI)
– Measure of Economic Welfare (MEW)
– Multidimensional Poverty Index (MPI)
• the Kuznets curve
11.3.4 comparison of economic growth rates and living standards:
• over time
• between countries
11.4 Characteristics of countries at different levels of development
11.4.1 population growth and structure:
• measurement and causes of changes in birth rate, death rate, infant mortality and net migration
• optimum population
• level of urbanisation
11.4.2 income distribution:
• calculation of Gini coefficient and Lorenz curve analysis
11.4.3 economic structure:
• employment composition: primary, secondary and tertiary sectors
• pattern of trade at different levels of development
"""

text19 = """
11.5 Relationship between countries at different levels of development
11.5.1 international aid:
• forms of aid
• reasons for giving aid
• effects of aid
• importance of aid
11.5.2 trade and investment
11.5.3 role of multinational companies (MNCs):
• definition of MNC
• activities of MNCs
• consequences of MNCs
11.5.4 Foreign Direct Investment (FDI):
• definition of FDI
• consequences of FDI
11.5.5 external debt:
• causes of debt
• consequences of debt
11.5.6 role of the International Monetary Fund (IMF)
11.5.7 role of the World Bank
11.6 Globalisation
11.6.1 meaning of globalisation and its causes and consequences
11.6.2 distinction between a free trade area, a customs union, a monetary union and full economic union
11.6.3 trade creation and trade diversion
"""

textarr = [text, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14, text15, text16, text17, text18, text19]
for i in range(len(textarr)):
    textarr[i] = getFormattedTextfromPdf.formatText(textarr[i])

trainModels.train(textarr, allLabels)
