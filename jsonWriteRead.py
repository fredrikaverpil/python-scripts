# -*- coding: utf-8 -*-

import os, sys, json, pprint

def writeJson(filename, data):
		with open(filename, 'w') as x:
				json.dump(data, x, sort_keys=True, indent=4, separators=(',', ': '))
				#json.dump(data, x, sort_keys=True)

def readJson(filename):
				with open(filename, 'r') as x:
						data = json.load(x)
				return data


scriptDir = os.path.dirname( __file__ )
filename = os.path.join( scriptDir, 'jsonFile.json' )
data = {'Name': 'Bårk Bärk Börk'}

# Write data
#writeJson( filename, data )

# Read data back into 'dataFromFile'
dataFromFile = readJson( filename )

for item in dataFromFile.keys():
	print dataFromFile[item].encode('utf-8')
