print('-------ATM-------\n---Caixa Automatico--')
x = int(input('Val: '))
ced = [100,50,20,10,5,2,1]
c = 0   
for i in ced:
    d = x // i
    
    x = x % i
    
    c = c + 1
    if d > 0:
        print(f'{d} ===> {i}')
