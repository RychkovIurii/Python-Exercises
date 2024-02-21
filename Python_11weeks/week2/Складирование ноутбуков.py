a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
case1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
case2 = (a1 // b2) * (b1 // a2) * (c1 // c2)
case3 = (a1 // a2) * (b1 // c2) * (c1 // b2)
case4 = (a1 // b2) * (b1 // c2) * (c1 // a2)
case5 = (a1 // c2) * (b1 // b2) * (c1 // a2)
case6 = (a1 // c2) * (b1 // a2) * (c1 // b2)
if case1 > case2:
    case1, case2 = case2, case1
if case2 > case3:
    case2, case3 = case3, case2
if case3 > case4:
    case3, case4 = case4, case3
if case4 > case5:
    case4, case5 = case5, case4
if case5 > case6:
    case5, case6 = case6, case5
print(case6)
