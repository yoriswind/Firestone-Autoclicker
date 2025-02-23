from pyautogui import click, press
import time

# Go back a level coordinates.
clicking_area = (932, 264)
go_back_level = (722, 68)

# Sleep settings
slow_sleep = 0.2
fast_sleep = 0.02

# Upgrade hotkey
upgrade_hotkey = 'u'

def perform_go_back_level_instruction():
    """
    Goes back a level.
    """

    click(go_back_level[0], go_back_level[1], interval=0.01, button='left')
    time.sleep(slow_sleep)
    click(go_back_level[0], go_back_level[1], interval=0.01, button='left')
    time.sleep(4)

    click(clicking_area[0], clicking_area[1], interval=0.01, button='left')
    time.sleep(slow_sleep)

    press(upgrade_hotkey)
    time.sleep(2)

    click(clicking_area[0], clicking_area[1], interval=0.01, button='left')
    time.sleep(slow_sleep)

    press(upgrade_hotkey)
    time.sleep(slow_sleep)

    click(clicking_area[0], clicking_area[1], interval=0.01, button='left')
    time.sleep(slow_sleep)