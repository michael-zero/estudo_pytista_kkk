ipsum_file = open('files/ipsum.txt')

#list
# ipsum_file.seek(0)
# lines = ipsum_file.readlines()

# print(lines)

#read lines 
# for linha in ipsum_file:
#     print(linha.rstrip())

# another way
# ipsum_file.seek(0)
# file_text = ipsum_file.read(10)
# print(file_text)
# print(len(file_text))

# ipsum_file.close()

#open and close
# with open('files/ipsum.txt') as file:
#     lines = file.readlines()
#     print(lines)


#write
with open('files/ipsum.txt','a') as write_file:
    write_file.write('\nflabosta vai ganhar nada')
   
text = ['\npalmeiras','\nsera','\ncampeao']

with open('files/ipsum.txt','a') as write_file:
    write_file.write('\nchora, fdp')

with open('files/ipsum.txt','a') as write_file:
    write_file.writelines(text)
    