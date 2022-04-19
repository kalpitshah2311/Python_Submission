heights = list(map(int,input("Enter numbers : ").split()))

maxh = 0

for i in heights:
    if i > maxh:
        maxh=i


maxh2 = 0
heights.pop(heights.index(maxh))
for i in heights:
    if i > maxh2:
        maxh2=i

print(maxh2*maxh2)
