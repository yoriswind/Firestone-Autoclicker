from pyautogui import click
from time import sleep

# Define coordinate variables for Claiming War Vehicle Loot
open_town = (1853, 208)  # open town
press_battles_building = (318, 199)  # press battles building
press_campaign = (759, 548)  # press campaign image
press_claim_loot = (151, 995)  # press claim loot
close_war_map = (1834, 55)  # close out war map
close_town = (1834, 55)  # close out town
close_settings = (1780, 85)  # close out settings

# Clicking and sleep settings
slow_sleep = 0.2
fast_sleep = 0.02

def claim_war_vehicle_loot():
    """
    Claim war vehicle loot.
    """

    # Open town
    click(open_town[0], open_town[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Press battles building
    click(press_battles_building[0], press_battles_building[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Press campaign image
    click(press_campaign[0], press_campaign[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Press claim loot
    click(press_claim_loot[0], press_claim_loot[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Close out war map
    click(close_war_map[0], close_war_map[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Close out town
    click(close_town[0], close_town[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    # Close out settings
    click(close_settings[0], close_settings[1], interval=0.01, button='left')
    sleep(slow_sleep)
