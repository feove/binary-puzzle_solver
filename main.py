import os
import signal
import graphical_interface as gi
from pynput import keyboard  # type: ignore
from time import sleep

def main():
    try:
        app = os.fork()
    except OSError as e:
        print(f"Fork failed: {e}")
        return

    if app == 0:  # Child process
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
                    if key.char == 's': 
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

    os.wait()
    os.system("clear")
    print("Quit Pressed")
    return


if __name__ == "__main__":
    main()
