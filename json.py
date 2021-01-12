try:
	f=open("text.txt", "r")
	print(f.read())
	f=open("text.txt", "a")
	f.write("HIHI")
	#f.close()
except:
	print("Something wet wrong when writing to the file")
#finally:
	#f.close()