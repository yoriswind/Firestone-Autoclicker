from pyautogui import click
from time import sleep

# Define coordinate variables for Claiming Tools
open_town = (1849, 206)  # open town
press_engineer_bldg = (1273, 815)  # press engineer building
press_engineer_image = (571, 541)  # press engineer image
press_tools = (1614, 723)  # press tools
close_engineer_page = (1835, 57)  # close out engineer page
close_town = (1835, 57)  # close out town
close_settings = (1780, 85)  # close out settings

# Clicking and sleep settings
slow_sleep = 0.2
fast_sleep = 0.02

def claim_tools():
    """
    Claim war vehicle tools.
    """

    # Open town
    click(open_town[0], open_town[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Press engineer building
    click(press_engineer_bldg[0], press_engineer_bldg[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Press engineer image
    click(press_engineer_image[0], press_engineer_image[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Press tools
    click(press_tools[0], press_tools[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Close out engineer page
    click(close_engineer_page[0], close_engineer_page[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Close out town
    click(close_town[0], close_town[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Close out settings
    click(close_settings[0], close_settings[1], interval=0.01, button='left')
    sleep(slow_sleep)