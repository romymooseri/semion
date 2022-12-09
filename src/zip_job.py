from zipfile import ZipFile
import shutil
import os
import os.path
import sys

VERSION=os.environ["VERSION"]
WD=os.getcwd()

array = ["a", "b", "c", "d"]
data_file="devops is the best hi hi hi"*10000
for x in array:
	with open("src/"+ x + ".txt",'w+') as file:
		file.write(data_file)
		file.close()

for x in array:
# Specify path
	print(f'romi {WD}/src/{x}.txt')
	path = f'{WD}/src/{x}.txt'
	   
	# Check whether the specified path exists or not	
	if os.path.exists(path):
		pass
	else:
		print ("ERROR: not all txt files have been created. the scrips fails")
		sys.exit()
		
for x in array:
	z= f'{x}{VERSION}'
	fzip = ZipFile(z + '.zip' ,'w')
	fzip.close()

	

for x in array:
	original = f'{WD}/src/{x}.txt'
	target = f'{WD}/src/{x}{VERSION}.zip'

	shutil.copyfile(original, target)

for x in array:
# Specify path
	path = f'{WD}/src/{x}{VERSION}.zip'
   
# Check whether the specified path exists or not	
	if os.path.exists(path):
		pass

	else:
		print ("ERROR: not all zip files have been created. the script fails")
		sys.exit()
		

