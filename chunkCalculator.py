def chunkCalculator(self, startframe, endframe, chunksize):
	import math

	# User input values
	#startframe = 1   # Start frame
	#endframe = 10    # End frame
	#chunksize = 3    # Size of each frame chunk

	startframe = int(startframe)
	endframe = int(endframe)
	chunksize = int(chunksize)

	totalFrames = endframe-startframe+1
	totalChunks = math.ceil( float(totalFrames)/float(chunksize) )
	totalChunks = int(totalChunks)

	chunkDict = {}
	for chunk in range(1,totalChunks+1):
		if chunk == 1:
			# First chunk
			sf = startframe
			ef = sf + chunksize - 1
		else:
			# Middle chunk
			sf = ef + 1
			ef = sf + chunksize - 1
		
		# Last chunk
		if ef > endframe:
			ef = endframe

		# Summary
		#print 'Chunk: ' + str(chunk) + ', Render ' + str(sf) + '-' + str(ef) + ' scenefile'

		# Prepare for next chunk
		chunkDict[chunk] = [str(sf), str(ef)]


	return chunkDict
