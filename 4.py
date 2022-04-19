from itertools import combinations

values =[int(i) for i in input('Enter space-separated integers: ').split()]
values.sort()

K = int(input('Enter K: '))
counterUniqueCombinations=0
print("The unique combinations with the sum equal to "+str(K)+" are:")
for i in range(1, len(values)+1):
    com =list(set(combinations(values, i)))
    for combination in com:
        if sum(combination) == K:
            print(combination)
            counterUniqueCombinations += 1
print("The count of all unique combinations is: "+str(counterUniqueCombinations))
