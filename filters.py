numbers = [10,-9,5,-7,8,1]

def positivo(n):
    if(n > 0):
        return n

print(list(filter(lambda x: x > 0, numbers))) #arrow 

print(list(filter(positivo, numbers))) #filter

print([num for num in numbers if num > 0]) #comprehension
