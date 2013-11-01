import math

# User input values
startframe = 1   # Start frame
endframe = 10    # End frame
chunksize = 3    # Size of each frame chunk


totalFrames = endframe-startframe+1
totalChunks = math.ceil( float(totalFrames)/float(chunksize) )
totalChunks = int(totalChunks)

chunkCount = 0
for chunk in range(1,totalChunks+1):
	sf = startframe+chunkCount
	ef = chunkCount+chunksize
	if ef > endframe:
		ef = endframe
	print 'Chunk: ' + str(chunk) + ', Render ' + str(sf) + '-' + str(ef) + ' scenefile'
	chunkCount += chunksize
