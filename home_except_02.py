def get_sum(num_one, num_two):
    try:
       return( int(num_one) + int(num_two))
    except ValueError:
        return('Какая-то дичь')

print (get_sum(2,'ff'))

