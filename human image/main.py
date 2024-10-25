from inputOutput.main import Output
import os

class UI(Output):
    def __init__(self,index) -> None:
        self.__Index = index
    
    def __image(self):
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