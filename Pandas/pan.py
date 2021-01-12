import pandas as pd

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
excel.fillna(130,inplace=True) ## Điều vào ô không có giá trị bằng giá trị cần move

print(excel.to_string())