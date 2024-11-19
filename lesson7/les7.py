#1
def IsAscending(A):
    for i in range(1, len(A)):
        if A[i] <= A[i - 1]:
            return "NO"
    return "YES"

input_list = list(map(int, input().split()))  
print(IsAscending(input_list))

#2
def KthAppearance(A, a, k):
    count = 0  
    for i in range(len(A)):
        if A[i] == a:
            count += 1
            if count == k:
                return i
    return -1  

A = list(map(int, input().split()))  
a = int(input())  
k = int(input()) 
print(KthAppearance(A, a, k))

#block2
#1
def MaxUsers(S, sizes):
    sizes.sort()  
    count = 0  
    total_size = 0  

    for size in sizes:
        if total_size + size <= S:
            total_size += size
            count += 1
        else:
            break  

    return count

data = list(map(int, input().split()))  
S = data[0]  
N = data[1]  
sizes = data[2:]  

print(MaxUsers(S, sizes))

#2
def MinTaxiCost(distances, rates):
    distances.sort(reverse=True)  
    rates.sort()  
    
    total_cost = 0
    for i in range(len(distances)):
        total_cost += distances[i] * rates[i]
    
    return total_cost

distances = list(map(int, input().split()))  
rates = list(map(int, input().split()))  

print(MinTaxiCost(distances, rates))

#block3
#1
def CountDigits():
    counts = [0] * 9  

    while True:
        number = int(input())  
        if number == 0:  
            break
        if 1 <= number <= 9:  
            counts[number - 1] += 1

    print(" ".join(map(str, counts)))  

CountDigits()

#2
def LinearSearch(lst, target): 
    for i in range(len(lst)):
        if lst[i] == target:
            return True, i
    return False, -1

lst = [7, 9, 5, 6, -99, -32, 10, -6, 45, 14]  
print("Original list:", lst)
target = int(input("Enter a number: "))  

found, index = LinearSearch(lst, target)
print("Output:")
print("True" if found else "False")  
if found:
    print(f"Index: {index}")  
