import pandas as pd
import matplotlib.pyplot as plt

mydata = {
	'cats':["BMW","VOLVO","FORD"],
	'passing':[3,7,2]}
myvar = pd.DataFrame(mydata,index=["ONE","TWO","THREE"])
#print(myvar)

excel = pd.read_csv('fie.csv')
#myx = pd.DataFrame(excel)
#print(excel.tail()) #Lấy 5 mảng sau cùng
#print(excel.head()) #Mặc định lấy 5 mảng đầu
#new_ = excel.dropna() ## Xóa row mà có ô không có giá trị hoặc bằng null
#excel.fillna(130,inplace=True) ## Điều vào ô không có giá trị bằng giá trị cần move
#excel['DATE'] = pd.to_datetime(['DATE'])  convert to datetime
#excel.dropna(subset=['DATE'],inplace=True) #Xóa row không có giá trị
#excel.loc[7,'STT'] = 45 # Gán giá trị mưới vào sô trong row số 7 ô STT
#for x in excel.index:
#	if excel.loc[x,'STT']>9:
#		excel.drop(x,inplace=True) #Xóa row mong muốn
#excel.drop(7,inplace=True)
#excel.drop_duplicates(inplace = True) #Xóa 2 row trung nhau
excel.plot()
plt.show()
print(excel.to_string())