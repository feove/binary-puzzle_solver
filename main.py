import os
import signal
import graphical_interface as gi
from pynput import keyboard
from pynput.keyboard import Key  
from time import sleep

def main():

    gi.cursor_hide()
    try:
        processid = os.fork()
    except OSError as e:
        print(f"Fork failed: {e}")
        os._exit(1)

    if processid == 0:  
        while True:
            gi.intro()  
    else:
        def on_press(key):
            try:
                if key.char == 's' or key == Key.enter: 
                    
                    os.kill(processid, signal.SIGTERM)
                    os.system("clear")
                    num_grid = gi.grid_dimension()
                    gi.grid_filling(num_grid)
                    os.system("clear")
                    gi.cursor_show()
                    return False 

                elif key.char == 'q': 
                    os.kill(processid, signal.SIGTERM)
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
