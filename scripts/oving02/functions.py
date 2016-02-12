def celsius_far(celsius):
    return celsius * (9.0 / 5.0) + 32  # must have decimals to prevent int-calc flooring


valIn = input('Enter celsius value to be converted: ')
print str(valIn) + ' degrees celsius in fahrenheit: ' + str(celsius_far(valIn))
