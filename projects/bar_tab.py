class Tab:

    menu = {
        'cuscuz': 4,
        'coxinha': 3.5,
        'café': 0.5,
        'batata': 10
    }

    def __init__(self):
        self.total = 0
        self.items = []
    
    def add(self,item):
        self.items.append(item)
        self.total +=self.menu[item]

    def print_conta(self,tax,service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total

        for item in self.items:
            print(f'{item} ${self.menu[item]}')

        print(f'{"Total"} ${self.total:.2f}')