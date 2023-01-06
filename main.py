from pynput import keyboard
import time
import random
import sys

from keydefs import KeyDefs

class InputHandler:
    def __init__(this):
        this.__cooldown = 0.0735
        this.__lastPressed = time.time()
        this.__pressedKeys = []
        this.__lastSound = None

    def start(this):
        listener = keyboard.Listener( 
            on_press = inputHandler.on_press,
            on_release = inputHandler.on_release
        )
        listener.daemon = True
        listener.start()
        listener.join()

    def __play_sound(this, key, eventType):
        sound = KeyDefs.query(key, eventType)
        if (sound):
            sound.play()
        this.__lastPressed = time.time()
        this.__lastSound = sound

    def on_press(this, key):
        this.__pressedKeys.append(key)
        if ( this.__pressedKeys == [
            keyboard.Key.ctrl_l,
            keyboard.Key.shift_l,
            keyboard.Key.delete
        ] ): sys.exit(0)
        
        timestamp = time.time()
        if ( timestamp - this.__lastPressed >= this.__cooldown/2 ):
            eventType = None
            if ( timestamp - this.__lastPressed >= this.__cooldown ):
                eventType = "press"
            else:
                eventType = "fast"

            this.__play_sound(key, eventType)

    def on_release(this, key):
        if ( key in this.__pressedKeys ):
            this.__pressedKeys.remove(key)

        timestamp = time.time()
        if ( this.__lastSound and 
            timestamp - this.__lastPressed >= this.__lastSound.get_length() 
        ): this.__play_sound(key, "release")

inputHandler = InputHandler()
inputHandler.start()