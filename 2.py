numbers = list(map(int,input("Enter numbers : ").split()))
import numpy 
import statistics

def Average(lst):
    return sum(lst) / len(lst)

print("Minimum : " + str(min(numbers)))

print("Maximum : " + str(max(numbers)))
print("Average : " + str(Average(numbers)))

print("Standard Deviation : " + str(statistics.stdev(numbers)))

print("Vartiance : " + str(numpy.var(numbers)))
