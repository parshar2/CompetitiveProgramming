A = map(int, raw_input().strip().split(','))
p = int(raw_input())
n = len(A)
l, e, g = 0, 0, n -1

def swap(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

while e <= g:
	if A[e] == p:
		e += 1
	elif A[e] < p:
		swap(A, l, e)
		l += 1
		e += 1
	else:
		swap(A, e, g)
		g -= 1
print A

 