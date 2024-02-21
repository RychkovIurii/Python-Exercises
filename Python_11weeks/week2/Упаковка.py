l1, w1, h1 = int(input()), int(input()), int(input())
l2, w2, h2 = int(input()), int(input()), int(input())
lc, wc, hc = int(input()), int(input()), int(input())
if hc >= h1 + h2 and w1 <= wc >= w2 and l1 <= lc >= l2:
    print('YES')
elif hc >= h1 + h2 and l1 <= wc >= w2 and w1 <= lc >= l2:
    print('YES')
elif hc >= h1 + h2 and l2 <= wc >= w1 and w2 <= lc >= l1:
    print('YES')
elif hc >= h1 + h2 and l1 <= wc >= l2 and w2 <= lc >= w1:
    print('YES')
elif h1 <= hc >= h2 and lc >= l1 + l2 and w1 <= wc >= w2:
    print('YES')
elif h1 <= hc >= h2 and lc >= w1 + w2 and l1 <= wc >= l2:
    print('YES')
elif h1 <= hc >= h2 and lc >= l1 + w2 and l2 <= wc >= w1:
    print('YES')
elif h1 <= hc >= h2 and lc >= l2 + w1 and l1 <= wc >= w2:
    print('YES')
elif h1 <= hc >= h2 and wc >= l1 + l2 and w1 <= lc >= w2:
    print('YES')
elif h1 <= hc >= h2 and wc >= w1 + w2 and l1 <= lc >= l2:
    print('YES')
elif h1 <= hc >= h2 and wc >= l1 + w2 and l2 <= lc >= w1:
    print('YES')
elif h1 <= hc >= h2 and wc >= l2 + w1 and l1 <= lc >= w2:
    print('YES')
else:
    print('No')
