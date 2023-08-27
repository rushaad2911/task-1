# size of array
n = int(input("Enter Array Size: "))


#  adding element to array 
arr = []
for i in range(n):
    arr.append(input(f"Enter array's {i+1} element: "))
    
    
#  checking for prime

def prime(num) :
    
    
    if(num == 1 or num == 0): 
        
        return False 
    for i in range(2, num//2) : 
        
        if(num % i == 0) : 
            return False
    return True


for i in range(n):
    
    if prime(arr[i]):
        print(f"{arr[i]} is prime")
        
        