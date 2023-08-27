# size of array
n = int(input("Enter Array Size: "))


#  adding element to array 
arr = []
for i in range(n):
    arr.append(input(f"Enter array's {i+1} element: "))
    


for i in range(n-1):
    
    for j in range(n-1-i):
        t = arr[j]
        if arr[j] > arr[j+1]:
            arr[j] = arr[j+1]
            arr[j+1] = t
            

for i in range(n):
    print(arr[i])