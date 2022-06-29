import NasaAPOD
import Nasa_Image_Mars
def two_programm():
    chose_option = 0
    print('What would you like to save today: 1 - A picture of the day\n2 - Pictures from Mars')
    chose_option = input()
    if chose_option == 1:
        NasaAPOD.NasaApod()
    elif chose_option == 2:
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
    
