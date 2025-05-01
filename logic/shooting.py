from logic.kmnet import kmnet_press, kmnet_release, kmnet_click
import threading

class Shooting(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.name = 'Shooting'
        self.button_pressed = False
        self.lock = threading.Lock()
        self.start()

    def run(self):
        while True:
            pass  # Implement your shooting queue logic if needed

    def shoot(self, bScope, shooting_state):
        with self.lock:
            if shooting_state and bScope:
                if not self.button_pressed:
                    kmnet_press()
                    self.button_pressed = True
            if (not shooting_state or not bScope) and self.button_pressed:
                kmnet_release()
                self.button_pressed = False

shooting = Shooting()