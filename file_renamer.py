## file_renamer.py
# a simple python script which renames files within a directory
# based on names listed in a text file.
#
## requires:
# names.txt which contains name list
#
import os

name_list=[x.strip() for x in open("names.txt",'r')]
dir_name = "" #place directory containing files to be renamed here
file_format = "" #place file extension here
for filename in os.listdir(dir_name):
    name = name_list[0]
    os.rename(dir_name+'/'+filename, dir_name+'/'+name+file_format)
    name_list.remove(name)

