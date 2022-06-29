T = int(input())
for i in range(T):
    num, s = input().split()
    text = ""
    for i in s:
        text += int(num)*i
    print(text)