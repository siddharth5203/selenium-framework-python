import sys
sys.path.append('../common/')
import inspect,ExcelReader
class DataProvider:
	def getData(methodName):
		print(" **************"+inspect.stack()[1][3]+"."+methodName)
		return ExcelReader.ExcelReader.readData("../test/"+inspect.stack()[1][3]+".xlsx",methodName)