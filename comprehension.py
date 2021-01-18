prizes = [3,50,30,500]
db_prizes = []

for prize in prizes:
    db_prizes.append(prize * 2)

print(db_prizes) 

db_prizes = [prize-1 for prize in prizes]

print(db_prizes)

nums = [1,2,3,4,5,6,7,8,9,10]

squared_even_nums = []

for num in nums:
    if(num**2) % 2 == 0:
        squared_even_nums.append(num**2)
print(squared_even_nums) 

squared_even_nums = [ num ** 2 for num in nums if (num**2) % 2 == 0]
print(squared_even_nums)