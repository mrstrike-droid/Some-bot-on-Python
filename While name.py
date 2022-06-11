print ('Please type your name')
name = input()
while name.isdecimal():
    print ('Please type your name, not number or what ever you type there)')
    name = input()
print ("Thank you!")