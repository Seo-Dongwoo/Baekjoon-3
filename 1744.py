import sys
N = int(sys.stdin.readline())
positiveList = []
nagativeList = []
oneList = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 1:
        positiveList.append(num)
    elif num <= 0:
        nagativeList.append(num)
    else:
        oneList.append(num)

positiveList.sort(reverse=True)
nagativeList.sort()
result = 0

if len(positiveList) % 2 == 0:
    for i in range(0, len(positiveList),2):
        result += positiveList[i]*positiveList[i+1]
else:
    for i in range(0, len(positiveList)-1, 2):
        result += positiveList[i]*positiveList[i+1]
    result += positiveList[len(positiveList)-1]

if len(nagativeList) % 2 == 0:
    for i in range(0, len(nagativeList), 2):
        result += nagativeList[i]*nagativeList[i+1]
else:
    for i in range(0, len(nagativeList)-1, 2):
        result += nagativeList[i]*nagativeList[i+1]
    result+= nagativeList[len(nagativeList)-1]
result += sum(oneList)

print(result)