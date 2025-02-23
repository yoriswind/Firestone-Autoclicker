from pyautogui import click
from time import sleep

fast_sleep = 0.02
slow_sleep = 0.2

# Define coordinate for claiming pickaxe
open_guild = (1856, 457) # duplicate but will be overwritten
press_guild_shop = (636, 241)
press_supplies = (163, 820)
press_claim_pickaxes = (709, 754)
close_guild_shop = (1837, 53)
close_guild = (1837, 53) # duplicate but will be overwritten
close_settings = (1780, 85) # duplicate but will be overwritten

# Define coordinates for arcane crystal pick-axing
open_guild = (1854, 462)
press_arcane_crystal = (1698, 895)
press_auto_pickaxe = (1778, 1024)
close_arcane_crystal = (1836, 56)
close_guild = (1836, 56)
close_settings = (1773, 84)

def claim_pickaxe_and_arcane_crystal():
    """
    Claim pickaxe and arcane crystal.
    """

    # Claim pickaxe
    click(open_guild[0], open_guild[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    click(press_guild_shop[0], press_guild_shop[1], interval=0.01, button='left')
    sleep(slow_sleep)

    click(press_supplies[0], press_supplies[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    click(press_claim_pickaxes[0], press_claim_pickaxes[1], interval=0.01, button='left')
    sleep(slow_sleep)

    click(close_guild_shop[0], close_guild_shop[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    click(close_guild[0], close_guild[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    click(close_settings[0], close_settings[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Claim arcane crystal
    click(open_guild[0], open_guild[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    click(press_arcane_crystal[0], press_arcane_crystal[1], interval=0.01, button='left')
    sleep(slow_sleep)

    click(press_auto_pickaxe[0], press_auto_pickaxe[1], interval=0.01, button='left')
    sleep(3)
    
    click(close_arcane_crystal[0], close_arcane_crystal[1], interval=0.01, button='left')
    sleep(slow_sleep)

    click(close_guild[0], close_guild[1], interval=0.01, button='left')
    sleep(slow_sleep)
    
    click(close_settings[0], close_settings[1], interval=0.01, button='left')
    sleep(slow_sleep)
