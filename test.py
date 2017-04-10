import tushare as ts

Years = [2006, 2007, 2008,2009,2010,2011,2012,2013,2014,2015,2016]
season = ['1', '2',  '3',  '4']

for m in Years:
   for index in range(len(season)):
	df = ts.get_profit_data(m,index+1)
	path = "/Users/binhaizhu/Desktop/DataAll/%d-%d.xlsx" % (m,index+1)
	df.to_excel(path)
	print  path