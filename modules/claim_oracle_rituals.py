from pyautogui import click
from time import sleep

fast_sleep = 0.02
slow_sleep = 0.2

# Define coordinates for claiming oracle rituals
press_town = (1854, 209)
press_building = (1028, 982)
press_ritual_section = (817, 433)
press_harmony = (1186, 510)
press_serenity = (1629, 500)
press_concentration = (1631, 877)
press_obedience = (1189, 876)
close_oracle = (1836, 55)
close_town = (1836, 55)
close_settings = (1776, 87)

def claim_oracle_rituals():
    """
    Claim oracle rituals, including harmony, serenity, concentration, and obedience.
    """

    # Press town
    click(press_town[0], press_town[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Press oracle building
    click(press_building[0], press_building[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Press ritual section
    click(press_ritual_section[0], press_ritual_section[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Press harmony ritual
    click(press_harmony[0], press_harmony[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Press serenity ritual
    click(press_serenity[0], press_serenity[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Press concentration ritual
    click(press_concentration[0], press_concentration[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Press obedience ritual
    click(press_obedience[0], press_obedience[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Close out of oracle
    click(close_oracle[0], close_oracle[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Close out of town
    click(close_town[0], close_town[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Close out of settings
    click(close_settings[0], close_settings[1], interval=0.01, button='left')
    sleep(slow_sleep)
