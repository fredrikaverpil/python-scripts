def sliceCalculator(slices, x, y):
	# Feed this function the amount of slices you would like and the resolution of the image
	
	import math

	imageWidth = x
	imageHeight = y
	totalPixels = imageWidth * imageHeight

	# Re-calculate slices
	slices = int(slices/2)*2
	if slices < 4:
		# Too few slices, set to minimum amount
		slices = 4
	elif (slices > totalPixels/4):
		# Too many slices, set to maximum amount
		slices = int(totalPixels/4)
	
	print 'Re-calculated slices: ' + str(slices)

	# Factor
	factor = math.sqrt( slices )

	# Calculations
	regionWidth = int(math.ceil(imageWidth / factor))
	regionHeight = int(math.ceil(imageHeight / factor))
	imageWidthRounded = int( math.ceil(factor) * math.ceil( imageWidth / factor ) )
	restWidth = imageWidthRounded - imageWidth
	imageHeightRounded = int( math.ceil(factor) * math.ceil( imageHeight / factor ) )
	restHeight = imageHeightRounded - imageHeight
	factorRounded = int(math.ceil(factor))

	# Start position
	xMin = 0
	xMax = 0
	yMin = 0
	yMax = 0

	rows = factorRounded
	columns = factorRounded

	regionList = []

	for column in range(1, columns+1):
		xMin = 0
		xMax = 0
		if column == columns:
			#print 'Col '+ str(column) + ' (last column) '
			yMin = (column*regionHeight + 1) - regionHeight
			yMax += (regionHeight - restHeight)

		else:
			#print 'Col '+ str(column)
			yMin = (column*regionHeight + 1) - regionHeight
			yMax += regionHeight


		for row in range(1, rows+1):
			if row == rows:
				xMin = (row*regionWidth + 1) - regionWidth
				xMax += (regionWidth-restWidth)
				#print 'Row ' + str(row) + ':  xMin=' +str(xMin) + '\t xMax=' + str(xMax) + '\t yMin=' + str(yMin) + '\t yMax=' + str(yMax) + ' (last row)'
				regionList.append( [xMin-1, xMax-1, yMin-1, yMax-1] )

			else:
				xMin = (row*regionWidth + 1) - regionWidth
				xMax += regionWidth
				#print 'Row ' + str(row) + ':  xMin=' +str(xMin) + '\t xMax=' + str(xMax) + '\t yMin=' + str(yMin) + '\t yMax=' + str(yMax)
				regionList.append( [xMin-1, xMax-1, yMin-1, yMax-1] )

	return regionList
