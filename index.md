## Welcome to Keybot

Keybot is a python script that clicks your keys for you! So you don't have to.

### Python?

Yes python, it's the only language i know apart from some basic html and css

This how the class is defined.
```python
class keybot:
    def __init__(self,keypress=4,interval=6,l=10):
        self.keypress = str(keypress)
        self.interval = interval
        self.l = l
        self.amount_of_loops(self.l)
```
So you would want to define in the class when called something like:
```python
ThisInstance = keybot(2,2,4)
```

Where the first number represents the button to be pressed. (passes any single digit or single letter)
The 2nd represents the interval of the key being pressed.
The last is the amount of times to iterate (defaults to 10)

### Sounds neat where is the link?
[right here](https://github.com/Joonsey/Keybot) Feel free to contact me if you have any issues with the script and i'll gladly adapt it.

### Does this work outside of WoW?
Well yes. Ofcourse, also make sure to not make it loop like 10000 times that's gonna be hell for you.
