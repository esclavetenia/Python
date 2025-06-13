from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

with SB(uc=True, test=True) as sb:
    if True:
        if True:
            url = "https://kick.com/brutalles"
            sb.uc_open_with_reconnect(url, 5)
            sb.uc_gui_click_captcha()
            sb.sleep(2)
            sb.uc_gui_handle_captcha()
            sb.sleep(5)
            if sb.is_element_present('button:contains("Accept")'):
                sb.uc_click('button:contains("Accept")', reconnect_time=4)
            if sb.is_element_present('button:contains("I am 18+")'):
                sb.uc_click('button:contains("I am 18+")', reconnect_time=4)
            if sb.is_element_visible('#injected-channel-player'):
                xxx = sb.get_new_driver(undetectable=True)
                xxx.uc_open_with_reconnect(url, 5)
                xxx.uc_gui_click_captcha()
                sb.sleep(2)
                xxx.uc_gui_handle_captcha()
                sb.sleep(15)
                while sb.is_element_visible('#injected-channel-player'):
                    sb.sleep(111)
                sb.quit_extra_driver()
        sb.sleep(1)
