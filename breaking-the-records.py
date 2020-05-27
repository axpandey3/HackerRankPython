def breakingRecords(scores):
	minc = 0
	maxc = 0
	low = scores[0]
	high = scores[0]
	for i in range(1, len(scores)):
		if scores[i] > high:
			maxc = scores[i]
			maxc += 1
		elif scores[i] < low:
			minc = scores[i]
			minc += 1
	return(maxc, minc)