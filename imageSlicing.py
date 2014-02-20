import math


slices = 11
imageWidth = 1024
imageHeight = 576
totalPixels = imageWidth * imageHeight
print 'Slices: ' + str(slices)

slices = int(slices/2)*2
print 'Re-calculated slices: ' + str(slices)

print 'Total pixels in image: ' + str(totalPixels)
print 'Maximum slices allowed: ' + str(totalPixels/4)

factor = math.sqrt( slices )
print 'Factor: ' + str(factor)

if slices < 4:
	print 'You cannot use less than 4 slices!'
if (slices > totalPixels/4):
	print 'You cannot use more than ' + int(totalPixels/4) + ' slices!'
else:

	regionWidth = int(math.ceil(imageWidth / factor))
	regionHeight = int(math.ceil(imageHeight / factor))
	print 'Region size: ' + str(int(regionWidth)) + 'x' + str(int(regionHeight))

	print 'Regions total pixels: ' + str(regionWidth*regionHeight*slices)

	print 'Region width: '  + str(regionWidth)
	print 'Region height: ' + str(regionHeight)

	imageWidthRounded = int( math.ceil(factor) * math.ceil( imageWidth / factor ) )
	restWidth = imageWidthRounded - imageWidth
	imageHeightRounded = int( math.ceil(factor) * math.ceil( imageHeight / factor ) )
	restHeight = imageHeightRounded - imageHeight
	print 'Rest width: ' + str(restWidth)
	print 'Rest height: ' + str(restHeight)

	factorRounded = int(math.ceil(factor))
	print 'Factor rounded: ' + str(factorRounded)


	xMin = 0
	xMax = 0
	yMin = 0
	yMax = 0


	rows = factorRounded
	columns = factorRounded
	print 'Total rows: ' + str(rows)
	print 'Total columns: ' + str(columns)


	for column in range(1, columns+1):
		xMin = 0
		xMax = 0
		if column == columns:
			print 'Col '+ str(column) + ' (last column) '
			yMin = (column*regionHeight + 1) - regionHeight
			yMax += (regionHeight - restHeight)

		else:
			print 'Col '+ str(column)
			yMin = (column*regionHeight + 1) - regionHeight
			yMax += regionHeight


		for row in range(1, rows+1):
			if row == rows:
				xMin = (row*regionWidth + 1) - regionWidth
				xMax += (regionWidth-restWidth)
				
				print 'Row ' + str(row) + ':  xMin=' +str(xMin) + '\t xMax=' + str(xMax) + '\t yMin=' + str(yMin) + '\t yMax=' + str(yMax) + ' (last row)'
			else:
				xMin = (row*regionWidth + 1) - regionWidth
				xMax += regionWidth
			
				print 'Row ' + str(row) + ':  xMin=' +str(xMin) + '\t xMax=' + str(xMax) + '\t yMin=' + str(yMin) + '\t yMax=' + str(yMax)



