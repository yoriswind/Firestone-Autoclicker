from pyautogui import click
from time import sleep

fast_sleep = 0.02
slow_sleep = 0.2

# Coordinates for the guardian experience claim
open_town = (1851, 197)
open_magic_quarter = (606, 245)
press_train_guardian = (1146, 798)
press_enlightenment_guardian = (1605, 793)
press_guardian_2 = (881, 1002)
press_guardian_1 = (736, 996)
close_magic_quarter = (1843, 55)
close_town = (1843, 55)
close_settings = (1773, 84)

def claim_guardian_experience():
    """
    Claim guardian experience.
    """

    # Open town
    click(open_town[0], open_town[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Press magic quarter building
    click(open_magic_quarter[0], open_magic_quarter[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Press guardian 2 train
    click(press_guardian_2[0], press_guardian_2[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    click(press_train_guardian[0], press_train_guardian[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # # Press enlightenment
    # click(press_enlightenment_guardian[0], press_enlightenment_guardian[1], interval=0.01, button='left')
    # sleep(slow_sleep)

    click(press_guardian_1[0], press_guardian_1[1], interval=0.01, button='left')
    sleep(slow_sleep)

    click(press_train_guardian[0], press_train_guardian[1], interval=0.01, button='left')
    sleep(slow_sleep) 

    # # Press enlightenment
    # click(press_enlightenment_guardian[0], press_enlightenment_guardian[1], interval=0.01, button='left')
    # sleep(slow_sleep)

    # Bring back to guardian 2
    click(press_guardian_2[0], press_guardian_2[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Close out magic quarter
    click(close_magic_quarter[0], close_magic_quarter[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Close out town
    click(close_town[0], close_town[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Close out settings
    click(close_settings[0], close_settings[1], interval=0.01, button='left')
    sleep(slow_sleep)
