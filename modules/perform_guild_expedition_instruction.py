from pyautogui import click
import time

# Sleep settings
slow_sleep = 0.2
fast_sleep = 0.02

# Guild Expedition positions
press_guild_icon = (1854, 470)
press_expedition_building = (375, 360)
press_expedition = (1318, 337)
close_expedition_page = (1479, 100)
close_guild_page = (1863, 84)
close_settings = (1773, 86)

def perform_guild_expedition_instruction():
    """
    Completes and starts a guild expedition.
    """
    
    # Open the guild
    click(press_guild_icon[0], press_guild_icon[1], interval=0.01, button='left')
    time.sleep(slow_sleep)

    # Opens the expedition building and start the expedition, then close the page
    click(press_expedition_building[0], press_expedition_building[1], interval=0.01, button='left')
    time.sleep(slow_sleep)
    click(press_expedition[0], press_expedition[1], interval=0.01, button='left')
    time.sleep(slow_sleep)
    click(close_expedition_page[0], close_expedition_page[1], interval=0.01, button='left')
    time.sleep(slow_sleep)

    # Opens the expedition building and start the expedition again if one was completed on the first run
    click(press_expedition_building[0], press_expedition_building[1], interval=0.01, button='left')
    time.sleep(slow_sleep)
    click(press_expedition[0], press_expedition[1], interval=0.01, button='left')
    time.sleep(slow_sleep)
    click(close_expedition_page[0], close_expedition_page[1], interval=0.01, button='left')
    time.sleep(slow_sleep)

    # Close the guild page
    click(close_guild_page[0], close_guild_page[1], interval=0.01, button='left')
    time.sleep(slow_sleep)

    click(close_settings[0], close_settings[1], interval=0.01, button='left')
    time.sleep(fast_sleep)