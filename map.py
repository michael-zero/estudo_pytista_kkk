from random import shuffle

def jumble(word): #embaralhar
    anagram = list(word) #c,a,r,r,o,t,s
    shuffle(anagram) #c,r,a,r,s,t,o
    return ''.join(anagram) #crarsto

words = ['beetroot', 'potatoes','carrots']
anagrams = []

# for word in words:
#     anagrams.append(jumble(word))

#map
print(list(map(jumble,words))) #cast for list

list((map(print, (1,2,3,4))))

def squad(x):
    return x**2

print(list(map(squad,(3,9,27))))

#comprehension
print([jumble(word) for word in words])


