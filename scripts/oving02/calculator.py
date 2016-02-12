print 'Welcome to a simple calculator! Enter two values and choose an operator to calculate.'

val1 = input('Enter first value: ')
val2 = input('Enter second value: ')
operator = input('Choose operator (1:add 2:subtract 3:multiply): ')

if operator == 1:
    print str(val1) + ' + ' + str(val2) + ' = ' + str(val1 + val2)
elif operator == 2:
    print str(val1) + ' - ' + str(val2) + ' = ' + str(val1 - val2)
elif operator == 3:
    print str(val1) + ' * ' + str(val2) + ' = ' + str(val1 * val2)
