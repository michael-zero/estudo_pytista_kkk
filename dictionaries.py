##(key, value) pairs
person = {
    "name": "zero",
     "studying": "Python"
}

print(person) #show people
print(f"key value 'name' = {person['name']}")

#percorrendo as chaves 
for k in person:
    print(f'key {k}')


#ckecking if the key is in the dictionary
print('age' in person)

#showing the keys in my dictionary
print(person.keys()) 

#convert for list
print(list(person.keys())) #list(people.keys())[0] return value in index 0

#values 
values = list(person.values())
print(values)
print(values.count('zero')) #there is one element with value equal 0 

# nome = input('digite seu nome: ')

# for k in range(0,7,1):
#     print(k)

# pi = 3.1415

# print(f'{pi:.2f}')