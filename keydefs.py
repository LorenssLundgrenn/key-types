from pygame import mixer
from pynput import keyboard
import random

mixer.init()

def LoadSound(path, volume=0.5):
    sound = mixer.Sound(path)
    sound.set_volume(volume)
    return sound

class KeyDefs:
    __BASE_PATH = "./sounds"
    __MASTER_VOL = 0.07

    __STREAM = LoadSound(__BASE_PATH + "/stream.wav", __MASTER_VOL*0.4)

    _enter = {
        "press": LoadSound(__BASE_PATH + "/enter_press.wav", __MASTER_VOL*0.8),
        "fast": __STREAM,
        "release": None
    }

    _tab = {
        "press": LoadSound(__BASE_PATH + "/tab_press.wav", __MASTER_VOL*0.8),
        "fast": __STREAM,
        "release": None
    }

    _backspace = {
        "press": [
            LoadSound(__BASE_PATH + "/backspace_press_01.wav", __MASTER_VOL*2.3),
            LoadSound(__BASE_PATH + "/backspace_press_02.wav", __MASTER_VOL*2.3)
        ],
        "fast": [
            LoadSound(__BASE_PATH + "/backspace_fast_01.wav", __MASTER_VOL),
            LoadSound(__BASE_PATH + "/backspace_fast_02.wav", __MASTER_VOL),
            LoadSound(__BASE_PATH + "/backspace_fast_03.wav", __MASTER_VOL)
        ],
        "release": None
    }

    _space = {
        "press": LoadSound(__BASE_PATH + "/space_press.wav", __MASTER_VOL*1.5),
        "fast": __STREAM,
        "release": None
    }

    _save_macro = {
        "press": LoadSound(__BASE_PATH + "/save.wav", __MASTER_VOL*0.5),
        "fast": None,
        "release": None
    }

    _std = {
        "press": [
            LoadSound(__BASE_PATH + "/std_press_01.wav", __MASTER_VOL),
            LoadSound(__BASE_PATH + "/std_press_02.wav", __MASTER_VOL),
            LoadSound(__BASE_PATH + "/std_press_03.wav", __MASTER_VOL),
            LoadSound(__BASE_PATH + "/std_press_04.wav", __MASTER_VOL)
        ],
        "fast": [
            LoadSound(__BASE_PATH + "/std_fast_01.wav", __MASTER_VOL),
            LoadSound(__BASE_PATH + "/std_fast_02.wav", __MASTER_VOL),
            LoadSound(__BASE_PATH + "/std_fast_03.wav", __MASTER_VOL)
        ],
        "release": None
    }

    def query(key, eventType):
        print(key, eventType)
        keyType = None

        #special keys
        if ( key == keyboard.Key.enter ):
            keyType = KeyDefs._enter
        elif ( key == keyboard.Key.tab ):
            keyType = KeyDefs._tab
        elif ( key == keyboard.Key.backspace ):
            keyType = KeyDefs._backspace
        elif ( key == keyboard.Key.space ):
            keyType = KeyDefs._space
        elif ( key == keyboard.Key.ctrl_l ):
            return None

        #macros
        elif ( key == keyboard.KeyCode.from_char('\x13') ):
            keyType = KeyDefs._save_macro

        #everything else
        else:
            keyType = KeyDefs._std
        
        soundEntry = keyType[eventType]
        if (soundEntry):
            sound = soundEntry[random.randrange(len(soundEntry))] if type(soundEntry) == list else soundEntry
            return sound
        return None