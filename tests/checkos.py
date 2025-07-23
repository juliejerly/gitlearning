import os
import string
import sys

# in windows we dont have / root directory, so we first need to find out all the valid drives and then perform the file search

# possible_drives = string.ascii_uppercase
# valid_drives = []
# for each_drive in possible_drives:
#     if os.path.exists(each_drive+":\\"):
#         print(each_drive+":\\")
#         valid_drives.append(each_drive+":\\")
#         print(valid_drives)

# path = input("Enter the path: ")
# # os.listdir(path)
# print(os.listdir(path))
# for dir in os.listdir(path):
#     print(os.path.join(path,dir))

# # print string with index values
# txt = input("Enter the text: ")
# index = 0
# for i in txt:
#     print(i, "-->", index)
#     index = index + 1
#
# #Find all files in a directory with required extension - .py/.sh/.log/.txt etc
# dir_path = input("Enter the required directory path: ")
# if os.path.isfile(dir_path):
#     print(f"InValid {dir_path}, pls pass only directory path")
# else:
#        all_dir_files = os.listdir(dir_path)
#        if len(all_dir_files) == 0:
#            print("No files in the directory")
#        else:
#            dir_file_extn = input("Enter the file extension: ")
#            file_list = []
#            for each in all_dir_files:
#                if each.endswith(dir_file_extn):
#                    file_list.append(each)
#            if len(file_list) ==0:
#                print(f"No files with {dir_file_extn} found")
#            else:
#                 print(file_list)




# C:\Users\julie.g.DC\Downloads\ML forms\seafarer page


'''
req_filename = input("Enter the required file name: ")
for r,d,f in os.walk("C:\\Users\\julie.g.DC"):
	if req_filename in f:		
		print(os.path.join(r, req_filename))
'''

# # Generating index values using range
# my_list = [1, 4, 6, "Julie", 10, 11]
# for each in range(len(my_list)):
#     print(my_list[each])

# # print chars one by one
# my_string = "Working with for loop"
# print(my_string)
# print("\n".join(my_string))

# # working witth tuples
# tup_list = [(1,2),(3,4),(5,6)]
# for a,b in tup_list:
#     print(b) #returns 2,4,6

# #working with dictionary
# my_dict = {'a':1, 'b':2, 'c':3}
# for each in my_dict:
#     print(each) #returns key values only
#
# #working with dictionary
# my_dict = {'a':1, 'b':2, 'c':3}
# for each in my_dict.keys():
#     print(each) #returns key values only

# #working with dictionary
# my_dict = {'a':1, 'b':2, 'c':3}
# for each in my_dict.values():
#     print(each) #returns values only

# working with dictionary
# my_dict = {'a':1, 'b':2, 'c':3}
# for each in my_dict.items(): #returns key,values in tuple form
#     print(each) #returns key,values in tuple form

# #working with dictionary once in tuple format
# my_dict = {'a':1, 'b':2, 'c':3}
# for key,value in my_dict.items():
#     print(key,value) #returns key,values in tuple form

# working with datetime module
# import datetime
# import pytz
#
# print(datetime.datetime.now())
# utctime = datetime.datetime.now(pytz.UTC)
# print(utctime)
# dt = pytz.timezone('Asia/Kolkata').localize(datetime(2025, 7, 14, 12, 0, 0))
# print(dt)

# # delete files older than x days
# import datetime
# req_path = input("Enter your required path: ")
# age = 14
# if not os.path.exists(req_path):
#     print("Pls provide valid path")
#     sys.exit()
# if os.path.isfile(req_path):
#     print("Provide valid directory")
#     sys.exit()
# today_date = datetime.datetime.now()
# for each_file in os.listdir(req_path):
#     each_file_path = os.path.join(req_path, each_file)
#     if os.path.isfile(each_file_path):
#         file_create_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
#         file_days = (today_date-file_create_date).days
#         if file_days>age:
#             print(each_file_path, file_days)
#             # to remove the files > age, we have os.remove

# # working with text files - one approach
# fo = open("testjg", "w")
# print(fo.mode, fo.writable(), fo.readable())
# fo.write("Hi I am learning python\n")
# fo.write("Hi This is second line\n")
# fo.write("Hi This is third line\n")
# fo.close()

# # working with text files - second approach
# my_lines = ["This is my 1st line\n", "This is my 2nd line \n", "This is my 3rd line"]
# fo = open("testjg", "w")
# print(fo.mode, fo.writable(), fo.readable())
# fo.writelines(my_lines)
#
# fo.close()

# # working with text files - third approach
# my_lines = ["This is my 1st Loop line", "This is my 2nd loop line", "This is my 3rd loop line"]
# fo = open("testjg", "w")
# for each_line in my_lines:
#     fo.write(each_line+"\n")
# fo.close()

# "w", "a" mode creates a new file if the file is not existing

# # working with text files - append data to a file
# my_lines = ["This is my 1st Loop line", "This is my 2nd loop line", "This is my 3rd loop line"]
# fo = open("testjg", "a")
# for each_line in my_lines:
#     fo.write(each_line+"\n")
# fo.close()

# # working with text files - read data from a file - different ways
# fo = open("testjg", "w")
# my_lines = ["This is my 1st Loop line\n", "This is my 2nd loop line\n", "This is my 3rd loop line"]
# for each in my_lines:
#     fo.write(each)
# # fo.close()
# fo = open("testjg", "r")
# print(fo.readline()) #reads line by line
# print(fo.readline())
# print(fo.readline())
# data = (fo.read())
# print(data)

# fo.close()

# # working with text files - read data from a file - different ways
# fo = open("testjg", "r")
# data = fo.readlines()
# print(data)
# for each in range(len(data)):
#     print(data[each])
# fo.close()

#copy the contents of the file from source file to dest file.  read mode to write mode
# sfile = "testjg"
# destfile = "random.txt"
sfile = input("Enter your source file path: ")
destfile = input("Enter your destination file path:")
fo = open(sfile, "r") # we mode is not mentioned, be default it will be read mode.
content = fo.read()
print(content)

fo = open(destfile,"w")
fo.write(content)
fo.close()

# C:\\Users\\julie.g.DC\\Downloads\\ML forms\\Generate ML forms docs
# C:\\Users\\julie.g.DC\\Downloads\\ML forms\\seafarer page