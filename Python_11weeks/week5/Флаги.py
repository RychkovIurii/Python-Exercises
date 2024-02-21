n = int(input())
print("+___ " * n)
for x in range(n):
    print("|", x + 1, " / ", sep="", end="")
print()
print("|__\\ " * n)
print("|    " * n)
