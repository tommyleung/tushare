import tushare as ts
group = ['1', '2',  '3',  '4',  '5',  '6']
Years = [2006, 2007, 2008,2009,2010,2011,2012,2013,2014,2015,2016]
season = ['1', '2',  '3',  '4']
for g in group:
   for m in Years:
      for index in range(len(season)):
         if g == '1':
         	df = ts.get_report_data(m, index + 1)
         	path = "/Users/binhaizhu/Desktop/AllData/report_data/%d-%d.xlsx" % (m,index+1)
         	df.to_excel(path)
         elif g == '2':
         	df = ts.get_profit_data(m, index + 1)
         	path = "/Users/binhaizhu/Desktop/AllData/profit_data/%d-%d.xlsx" % (m, index+1)
         	df.to_excel(path)
         elif g == '3':
         	df = ts.get_operation_data(m, index + 1)
         	path = "/Users/binhaizhu/Desktop/AllData/operation_data/%d-%d.xlsx" % (m, index+1)
         	df.to_excel(path)
         elif g == '4':
         	df = ts.get_growth_data(m, index + 1)
         	path = "/Users/binhaizhu/Desktop/AllData/growth_data/%d-%d.xlsx" % (m, index+1)
         	df.to_excel(path)
         elif g == '5':
         	df = ts.get_debtpaying_data(m, index + 1)
         	path = "/Users/binhaizhu/Desktop/AllData/debtpaying_data/%d-%d.xlsx" % (m, index+1)
         	df.to_excel(path)
         elif g == '6':
         	df = ts.get_cashflow_data(m, index + 1)
         	path = "/Users/binhaizhu/Desktop/AllData/cashflow_data/%d-%d.xlsx" % (m, index + 1)
         	df.to_excel(path)