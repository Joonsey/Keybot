
class keybot:
    def __init__(self,keypress=4,interval=6,l=10):
        self.keypress = str(keypress)
        self.interval = interval
        self.l = l
        self.amount_of_loops(self.l)
        """
        keypress = the key to be pressed, defined as single letter string or int
        interval = amount of time between each key press
        l = amount of times it will iterate
        """
    def keyinterval(self):
        """
        interval of time between each key press
        defined as integer
        """
        from time import sleep
        sleep(self.interval)

    def presskey(self):
        """
        function that presses the key"""
        from pynput.keyboard import Controller
        kb = Controller()
        kb.press(self.keypress)
        
    def amount_of_loops(self,n):
        """
        the amount of times the code will iterate
        defined as integer
        """
        for i in range(n):
            self.presskey()
            self.keyinterval()



