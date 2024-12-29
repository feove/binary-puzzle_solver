import os
import graphical_interface as gi
from pynput import keyboard # type: ignore

def main():
    processid = os.fork()

    if processid == 0:  
        while True:
            gi.intro()
    else:  
        def on_press(key):
            try:
                if key.char == 's':

                    os.kill(processid, 9) 
                    os.system("clear")
                    print("Start")
                    return False  
                


                elif key.char == 'q':
                    os.kill(processid, 9)  
                    os.system("clear")
                    print("Exit pressed")
                    return False  
                
            except AttributeError:
                pass
                

      
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

if __name__ == "__main__":
    main()
