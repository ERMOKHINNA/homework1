def ask_user(speak_list):
    user_input = ''
    while user_input != 'пока':
        try:
            user_input = input()
            print (speak_list.get(str(user_input),"Не обучен"))
        except KeyboardInterrupt:
            print ('Пока')
            break



speak_list = {'Привет':'Привет!','Как дела?':'Хорошо', 'Что делаешь?':'Программирую'}


ask_user(speak_list)

