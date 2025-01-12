import os
import graphical_interface as gi
from time import sleep
from pynput import keyboard # type: ignore

def main():
    
    gi.cursor_hide()
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
                    num_grid = gi.grid_dimension()
                    
                    gi.grid_filling(num_grid)
                    os.system("clear")
                    gi.cursor_show()
                    return False  
                
                
                elif key.char == 'q':
                    os.kill(processid, 9)  
                    os.system("clear")
                    print("Exit pressed")

                    gi.cursor_show()
                    return False  
            
                
            except AttributeError:
                pass
                

      
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

if __name__ == "__main__":
    main()
