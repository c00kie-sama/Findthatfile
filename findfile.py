from os import listdir
from os import getlogin

path_to_folder = "C:\\Users\\"+getlogin()+"\\AppData\\Local\\Temp"
#print(path_to_folder)


def check(filed,path_to_folder):
	file_location =  path_to_folder+"\\"+filed
	file = open(file_location,"r")
	fr = file.read(42)
	#print(fr)
	if fr == "==========================================":
		print("Found file:",file_location)
		if input("show contents of file? [Y/N]  ").lower() == "y":
			print("\n\n\n==========================================",file.read())




files_in_tmp = listdir(path_to_folder)
potential_files = []
for x in files_in_tmp:
	#print (x[-3:])
	if x[-4:] == ".txt":
		potential_files.append(x)




for x in potential_files:
	check(x,path_to_folder)


