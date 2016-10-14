n = long(raw_input().strip())
num_zeroes = 0
while n!= 0:
    if n&1 == 0:
        num_zeroes += 1
    n = n >> 1
print 2**num_zeroes