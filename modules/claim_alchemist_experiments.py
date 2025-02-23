from pyautogui import click
from time import sleep

# Sleep settings
fast_sleep = 0.02
slow_sleep = 0.2

# Define coordinate variables for Claiming Alchemist Experiments
open_town = (1854, 201)
press_building = (460, 853)
press_1st_experiment = (940, 810)
press_2nd_experiment = (1314, 817)
press_3rd_experiment = (1690, 815)
close_experiment = (1342, 275)
close_alchemist = (1838, 53)
close_town = (1838, 53)
close_settings = (1781, 84)

def claim_alchemist_experiments():
    """
    Claim alchemist experiments.
    """
    
    # Open town
    click(open_town[0], open_town[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Press alchemist building
    click(press_building[0], press_building[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Press 1st experiment (twice, with closing in between)
    click(press_1st_experiment[0], press_1st_experiment[1], interval=0.01, button='left')
    sleep(slow_sleep)
    click(close_experiment[0], close_experiment[1], interval=0.01, button='left')
    sleep(slow_sleep)

    click(press_1st_experiment[0], press_1st_experiment[1], interval=0.01, button='left')
    sleep(slow_sleep)
    click(close_experiment[0], close_experiment[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Press 2nd experiment (twice, with closing in between)
    # click(press_2nd_experiment[0], press_2nd_experiment[1], interval=0.01, button='left')
    # sleep(slow_sleep)
    # click(close_experiment[0], close_experiment[1], interval=0.01, button='left')
    # sleep(slow_sleep)

    # click(press_2nd_experiment[0], press_2nd_experiment[1], interval=0.01, button='left')
    # sleep(slow_sleep)
    # click(close_experiment[0], close_experiment[1], interval=0.01, button='left')
    # sleep(slow_sleep)

    # Press 3rd experiment (twice, with closing in between)
    click(press_3rd_experiment[0], press_3rd_experiment[1], interval=0.01, button='left')
    sleep(slow_sleep)
    click(close_experiment[0], close_experiment[1], interval=0.01, button='left')
    sleep(slow_sleep)

    click(press_3rd_experiment[0], press_3rd_experiment[1], interval=0.01, button='left')
    sleep(slow_sleep)
    click(close_experiment[0], close_experiment[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Close out alchemist
    click(close_alchemist[0], close_alchemist[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Close out town
    click(close_town[0], close_town[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Close settings
    click(close_settings[0], close_settings[1], interval=0.01, button='left')
    sleep(slow_sleep)
