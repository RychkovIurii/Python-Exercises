n = int(input())
students = []
for _ in range(n):
    tempList = input().split()
    tempList[1] = int(tempList[1])
    tempList[0], tempList[1] = tempList[1], tempList[0]
    students.append(tempList)
students.sort(reverse=True)
for student in students:
    print(student[1])
