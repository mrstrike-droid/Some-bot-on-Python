def div42by(divideBy0):
    try:
        return 42/divideBy0
    except ZeroDivisionError:
        print ('Error: you try to divide by zero')
print (div42by(2))
print (div42by(12))
print (div42by(0))
print (div42by(4))