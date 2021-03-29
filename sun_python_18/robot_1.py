name = input('Введите имя: ') 
print('Приветствую, '+name)

while True:
    message = input('-> ')
    if message == 'привет':
        print('Ни хао, '+name)
        
    elif message == 'сколько тебе лет?':
        print('17, '+name)
    
    elif message == '1':
        print('Ни хао, '+name)   
        
    # после else ничего!
    else:
        print('НЕ понимаю тебя, '+name)
    
