# size of array
n = int(input("Enter Array Size: "))


#  adding element to array 
arr = []
for i in range(n):
    arr.append(input(f"Enter array's {i+1} element: "))
    
    
# setting max val to first number
max = arr[0]

for i in range(n):
    # setting max element
    if arr[i]>max:
        max = arr[i];
    
    
print(f"Max number is {max}")