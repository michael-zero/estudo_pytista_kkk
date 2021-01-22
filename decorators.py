num = 2 

def duplica():
    global num
    print(f'num = {num}')
    num = num * 2
    return num

def subtrai():
    global num
    print(f'num = {num}')
    num = num - 3
    return num 

def decorador(fn):

    def encapsula():
       #print('** antes da execucao **')
        print(f'{duplica()}')
        print(f'{fn()}')
        print(f'{subtrai()}')
       #print('** depois da execucao **')
    return encapsula

@decorador 
def ola():
    global num 
    print(f'num = {num}')
    num = num/2
    return num

ola()