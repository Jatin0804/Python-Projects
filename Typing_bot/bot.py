from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

import time
import random
import pyautogui as pg

from threading import Thread
from pynput.keyboard import Key, Listener


# Thread Decorator
def thread(function):
    def wrapper(*args, **kwargs):
        thread_start = Thread(target=function, args=args, kwargs=kwargs)
        thread_start.start()
        return thread_start
    return wrapper

class TypingBot(object):
    # Constants
    TIMEINTERVAL = 0.0001
    TYPOS_RATE = 0.005
    TIMECONTROL = 30
    TIME_INT_ERR = 0.00001
    TIMELIMIT = 6000


    def __init__(self):
        self.driver = webdriver.Edge(options=Options(), service=Service(executable_path="msedgedriver.exe"))

    def open_website(self, accept_cookies, cookie):
        self.driver.get("https://monkeytype.com/")
        self.driver.execute_script('alert("Click Enter to Start the Bot")')

    @thread
    def enable_fail_safe(self):
        def on_release_key(key):
            if key == Key.esc:
                self.driver.close()
                return False
        with Listener(on_release=on_release_key) as listener:
            listener.join()

    def randomize_typing(self, words, intervals, error_rate, typos_rate):
        def add_noise():
            if random.random() > 0.5:
                return intervals + (random.random() * error_rate)
            else:
                return intervals - (random.random() * error_rate)

        def add_errors():
            error_words = ['during','point','place','from','problem','which','world','begin','face','go']
            if random.random() > (1 - typos_rate):
                random_word = random.choice(error_words)
                pg.write(random_word, interval = add_noise())
                pg.press('backspace', presses = len(random_word), interval = add_noise())

        for i in words.split('\n'):
            add_errors()
            pg.write(i + " ", interval = add_noise())


    def activate_bot(self, human_typing=True, enable_fail_safe=False):
        def find_words():
            temp = self.driver.find_element(by=By.XPATH, value='//*[@id="words"]').text
            # print(temp)
            return temp[temp.find(words[-10:])+10:] if len(words) != 0 else temp

        if enable_fail_safe:
            WebDriverWait(self.driver, self.TIMELIMIT).until_not(expected_conditions.alert_is_present())
            self.enable_fail_safe()

        while True:
            WebDriverWait(self.driver, self.TIMELIMIT).until_not(expected_conditions.alert_is_present())
            self.driver.execute_script('''
                function keyDownTextField(e) {
                    var keyCode = e.keyCode;
                    console.log(keyCode)
                    if (keyCode == 192) {
                        document.removeEventListener("keydown", keyDownTextField, false);
                        alert("Bot Activated! Hit Enter")
                    }   
                }
                document.addEventListener("keydown", keyDownTextField, false);
            ''')
            WebDriverWait(self.driver, self.TIMELIMIT).until(expected_conditions.alert_is_present())
            time.sleep(1.5)

            start = time.time()
            words = ''

            if human_typing:
                while time.time()-start < self.TIMECONTROL:
                    words += find_words()
                    self.randomize_typing(words, self.TIMEINTERVAL, self.TIME_INT_ERR, self.TYPOS_RATE)
            else:
                while time.time()-start < self.TIMECONTROL:
                    words = find_words()
                    for i in words.split("\n"):
                        pg.write(i + " ")
            self.driver.execute_script('alert("Bot Finished.")')

if __name__ == "__main__":
    bot = TypingBot()
    # bot.open_website(accept_cookies=True, cookie='//*[@id="cookiePopup"]/div[2]/div[2]/button[1]')
    bot.open_website(accept_cookies=True, cookie='//*[@id="cookiesModal"]/div[2]/div[2]/div[2]/button[1]')
    # '//*[@id="cookiesModal"]/div[2]/div[2]/div[2]/button[1]'
    bot.activate_bot(human_typing=False, enable_fail_safe=True)