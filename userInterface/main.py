

import os

class UI():

    def __init__(self,index) -> None:
        self.__Index = index
    
    def image(self):
        if(self.__Index == 0):
            print("-------|")
            print("       |")
            print("       |")
            print("       |")
            print("       |")
        elif(self.__Index == 1):
            print("---|---|")
            print("   o   |")
            print("       |")
            print("       |")
            print("       |")
        elif(self.__Index == 2):
            print("---|---|")
            print("   o   |")
            print("   |   |")
            print("       |")
            print("       |")
        elif(self.__Index == 3):
            print("---|---|")
            print("   o   |")
            print("  /|   |")
            print("   |   |")
            print("       |")
        elif(self.__Index == 4):
            print("---|---|")
            print("   o   |")
            print("  /|\  |")
            print("   |   |")
            print("       |")
        elif(self.__Index == 5):
            print("---|---|")
            print("   o   |")
            print("  /|\  |")
            print("   |   |")
            print("  /    |")
        elif(self.__Index == 6):
            print("---|---|")
            print("   o   |")
            print("  /|\  |")
            print("   |   |")
            print("  / \  |")
            
    def generateGame(self):
        os.system("cls")


for i in range(7):
    inter = UI(i)
    inter.generateGame()
    inter.image()
    input()

