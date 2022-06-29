import NasaAPOD
import Nasa_Image_Mars
import os
def two_programm():
    chose_option = 0
    print('What would you like to save today: 1 - A picture of the day\n2 - Pictures from Mars')
    chose_option = int(input())
    if chose_option == 1:
        print ('Chose your directory to save files:(Click on the path bar of the Windows Explorer and tap Ctrl+C and then Ctrl+V)')
        os.chdir(input())
        NasaAPOD.repeat_programm()
    elif chose_option == 2:
        print ('Chose your directory to save files:(Click on the path bar of the Windows Explorer and tap Ctrl+C and then Ctrl+V)')
        os.chdir(input())
        Nasa_Image_Mars.repeatprogramm()
if __name__ == "__main__":
    restart = 1
    while restart == 1:
        try:
            two_programm()
            print('Whant to start again: 1 - Yes\n2 - No')
            restart = input()
        except ValueError:
            print('Please enter 1 or 2')
    
