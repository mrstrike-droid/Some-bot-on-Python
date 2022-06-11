print ('Please, enter your name')
Name = str(input())
print ('Please, enter your age')
Age = int(input())
print ('Please, enter your ocupations')
Job = str(input())
L = [Name, Age, Job]
print ('Your answers is:')
print (L[0] + ' - Name')
print (str(L[1]) + ' - Age')
print (L[2] + ' - Job')
print ('If you what to change the information type what do you what to change bellow:\n1 - Name\n2 - Age\n3 - Occupation\n')
print ('If all data is correct please type: 0')
Choose = int(input())
while Choose in range (1,4):
    if Choose == 1:
        print ('Please, enter your name')
        Name = str(input())
        L[0] = Name
    elif Choose == 2:
        print ('Please, enter your age')
        Age = int(input())
        L[1] = Age
    elif Choose == 3:
        print ('Please, enter your ocupations')
        Job = str(input())
        L[2] = Job
    print ('Your answers is:')
    print (L[0] + ' - Name')
    print (str(L[1]) + ' - Age')
    print (L[2] + ' - Job')
    
    print ('If all data is correct please type: 0')
    print ('If not choose option again:\n1 - Name\n2 - Age\n3 - Occupation\n')
    Choose = int(input())
print("Thank you for your answer, it will be stored in base")
print("Press Enter to continue ...")
input()