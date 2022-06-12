
def pathChoose(answer):
    if answer == str(1):
        return ('You are dead... Ha-Ha-Ha')
    if answer == str(2):
        return ('Please take your kindom wise khnight')
    if answer == str(3):
        return ('Welcome to Bar amogo!)')
def questions():
    print ('Hello stranger, you stand near crossroad, please choose your future path:\n 1 - Straight\n 2 - Right\n 3 - Left\n')
    answer = input()
    print (pathChoose(answer))
    print ('Want to repeat:\n 1 - Yes\n 2 - No\n')
questions()
repeat = input()
if repeat == '1':
    questions()
else:
    print ('Thank you for join')
input()

