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

	coordinates = []
	
	grid = []

	for column in range(1, columns+1):
		xMin = 0
		xMax = 0
		cellCount = 0
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
				coordinates.append( [xMin-1, xMax-1, yMin-1, yMax-1] )
				cellCount += 1


			else:
				xMin = (row*regionWidth + 1) - regionWidth
				xMax += regionWidth
				#print 'Row ' + str(row) + ':  xMin=' +str(xMin) + '\t xMax=' + str(xMax) + '\t yMin=' + str(yMin) + '\t yMax=' + str(yMax)
				coordinates.append( [xMin-1, xMax-1, yMin-1, yMax-1] )
				cellCount += 1



		#print 'Column: ' + str(column) + ' (' + str(cellCount) + ' cells in row)'
		gridRow = []
		multiplier = ( (column-1) * cellCount)
		for cell in range(1, cellCount+1):
			#print 'Row ' + str(row) + ', cell: ' + str(cell + multiplier)
			gridRow.append( (cell + multiplier) )
		grid.append( gridRow )

	return grid, coordinates







def spiral(m):
	# Usage
	# Example output
	# >>> m = [[1, 2, 3, 4], 
	# ...      [5, 6, 7, 8], 
	# ...      [9, 10, 11, 12], 
	# ...      [13, 14, 15, 16]]
	# >>> list(spiral(m))
	# [6, 7, 11, 10, 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5]



	length = len(m[0])
	last = length - 1
	mid = length // 2
	spirals_remaining = mid

	if length % 2 == 1:
		yield m[mid][mid]
		box = [(mid-1, mid-1), (mid-1, mid+1), (mid+1, mid+1), (mid+1, mid-1)]
	else:
		box = [(mid-1, mid-1), (mid-1, mid), (mid, mid), (mid, mid-1)]

	while spirals_remaining > 0:
		# yield spiral values clockwise from top left corner
		top = m[box[0][0]][slice(box[0][1], box[1][1])]
		for x in top:
			yield x
		right = [m[i][box[1][1]] for i in range(box[1][0], box[2][0])]
		for x in right:
			yield x
		bottom = m[box[2][0]][slice(box[2][1], box[3][1], -1)]
		for x in bottom:
			yield x
		left = [m[i][box[3][1]] for i in range(box[3][0], box[0][0], -1)]
		for x in left:
			yield x

		# update bounding box for next spiral
		box[0] = box[0][0] - 1, box[0][1] - 1
		box[1] = box[1][0] - 1, box[1][1] + 1
		box[2] = box[2][0] + 1, box[2][1] + 1
		box[3] = box[3][0] + 1, box[3][1] - 1
		spirals_remaining -= 1




slices = 32				# Amount of desired slices
imageWidth = 1024		# Image width
imageHeight = 576		# Image height
grid, coordinates = sliceCalculator(slices, imageWidth, imageHeight)		# Generate grid and region coordinates
sliceorder = list(spiral(grid))												# Generate spiraling order based on grid structure


# Regular slice order
for region in coordinates:
	print region

# Spiraling slice order
for row in grid:
	for cell in row:
		print coordinates[cell]

