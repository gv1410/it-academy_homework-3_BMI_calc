# Домашнее задание. Калькулятор массы тела. 
# Исполнитель: Холдеев Алексей


cycle = True
database = {}

while cycle:
    user_name = input('Введите ваше имя: ')
    weight = float(input('Введите свой вес (кг): '))
    height = float(input('Введите свой рост (см): '))



    calc_result = int(weight / ((height / 100)**2))
    
    database[user_name] = calc_result
    
    question = input('Ввести еще данные?(1 - да, 0 - нет ) ')



    if question == '1':
        cycle = True
    elif question == '0':
        cycle = False

        
    
user_request = input('Чьи данные вывести на экран?' + str(database.keys()) + ': ')

print('\n Индекс массы тела ' + user_request + ' равен: ', database[user_request])
print('20' + ('=' * (database[user_request] - 20)) + '|' + ('=' * (50 - database[user_request])) + '50')

