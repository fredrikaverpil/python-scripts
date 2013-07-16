'''
This commandline Python script renames all files of specified type (png, jpg and jpeg)
based on a search and replace formula in the textfile fileRenameMatrix.txt.

Example contents of fileRenameMatrix.txt:
hello=hi
version=v

Would rename the following files accordingly:
hello.jpeg -> hi.jpeg
image_version_001.png -> image_v_001.png
'''

import os

# Open text file and read contents into list
with open('fileRenameMatrix.txt', 'r') as textFile:
	myList = [line.strip() for line in textFile]


# Open current directory and read contents (jpegs) into list
files = [file for file in os.listdir('.') if os.path.isfile(file)]

# Parse list of files...
for file in files:
	if ('.png' in file) or ('.jpg' in file) or ('.jpeg' in file):
		print 'Processing ' + file
		for item in myList:
			delimiter = '='
			oldString = item[:item.rfind(delimiter)]
			newString = item[item.rfind(delimiter)+1:]
			if oldString in file:
				print 'Found match of ' + oldString
				print 'Renaming ' + file + ' to ' + file.replace(oldString, newString)
				try:
					os.rename(file, file.replace(oldString, newString))
					print 'Rename successful.'
				except:
					print 'Error: unable to rename ' + file
				print '\n'

	else:
		print 'Skipped ' + file
