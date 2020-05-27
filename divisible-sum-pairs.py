def divisibleSumPairs(n, k, ar):
	c = 0
	for i in range(0, len(ar)):
		for j in range(i + 1, len(ar)):
			if (ar[i] + ar[j]) % k == 0:
				c += 1
	return c