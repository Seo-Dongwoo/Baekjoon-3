N = int(input())
s = 1
while s*(s+1)/2 <= N:
    s+=1
print(s-1)