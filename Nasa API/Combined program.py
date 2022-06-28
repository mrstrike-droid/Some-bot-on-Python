import subprocess
script1 = subprocess.call("NasaAPOD.py", shell=True)

if __name__ == "__main__":
    chose_option = 0
    print('What would you like to save today: 1 - A picture of the day\n 2 - Pictures from Mars')
    chose_option = input()
    if chose_option == 1:
        script1.repeat_programm()
