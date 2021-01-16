

def ninja_intro(dictionary):
    for key,val in dictionary.items():
        print(f'{key} {val}')


ninja_belts = {}

while True:
    ninja_name = input('enter a ninja name ')
    ninja_belt  = input('enter a belt colour ')
    ninja_belts[ninja_name] = ninja_belt 

    outro = input('add another? (y/n')

    if outro == 'y':
        continue
    else:
        break



ninja_intro(ninja_belts)