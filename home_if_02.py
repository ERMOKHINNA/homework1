def string_compare (first_string, second_string):
    if type(first_string) != str or type(second_string) != str:
        return 0
    elif first_string == second_string:
        return 1
    elif first_string != second_string and len(first_string) > len(second_string):
        return 2
    elif first_string != second_string and second_string == 'learn':
        return 3

print (string_compare(0,'привет'))
print (string_compare('привет','привет'))
print (string_compare('ghbdtn!','привет'))
print (string_compare('ghbdtn','приветnnnn'))
print (string_compare('Python,,','learn'))
print (string_compare('Pyt','learn'))