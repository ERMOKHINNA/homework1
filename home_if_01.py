def age_classificate(age_from_input):
    if age_from_input < 7 and age_from_input >= 0:
        place = 'Детский сад'
    elif age_from_input >= 7 and age_from_input <= 18:
        place = 'Школа'
    elif age_from_input >= 19 and age_from_input < 24:
        place = 'Универ'
    elif age_from_input >= 24 and age_from_input <= 65:
        place = 'Работа'
    elif age_from_input > 65 and age_from_input < 100:
        place = ('Пенсия')
    else:
        place = ('Столько не живут')
    return (place)



age_from_user = float(input('Введите ваш возраст '))
place_from_age = age_classificate(age_from_user)
print (place_from_age)