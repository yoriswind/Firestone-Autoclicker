from pyautogui import press, click, locateOnScreen, center, useImageNotFoundException, ImageNotFoundException
from time import sleep

# Coordinates for DPS increase process
bag_hotkey = 'b'  # Opens the bag
press_inventory_section = (1456, 275)  # Presses the inventory section
press_scrolls_section = (1457, 364)  # Presses the scrolls section

# Upgrade positions
upgrade_hotkey = 'u'

press_upgrades_icon = (1419, 986)
press_first_upgrade = (1769, 185)
press_second_upgrade = (1772, 314)
press_third_upgrade = (1767, 434)
press_fourth_upgrade = (1773, 551)
press_fifth_upgrade = (1771, 673)
press_sixth_upgrade = (1766, 792)
press_seventh_upgrade = (1773, 915)
close_upgrade_page = (1863, 46)
upgrade_multiplier = (1589, 1016)

# Clicking and sleep settings
slow_sleep = 0.2
fast_sleep = 0.02

# Initializes error as object for exception handling
useImageNotFoundException()

class ImageNotFoundException(Exception):
    """Custom exception for image not found errors."""
    pass

def increase_dps_with_items():
    """
    Increases DPS using OCR to locate and click "Speed Scroll", "Damage Scroll", "War Drums", and "Gold Barrel" images.
    Includes a condition requiring both scrolls to be found and clicked, or retries by reopening the bag.
    """

    # Open the bag
    press(bag_hotkey)
    sleep(slow_sleep)

    # Press the inventory section
    click(x=press_inventory_section[0], y=press_inventory_section[1], interval=0.01, button='left')
    sleep(slow_sleep)

    try:
        gold_barrel = locateOnScreen("Gold Barrel.png", confidence=0.75)
        if gold_barrel:
            print("Image Found: Gold Barrel")
    except ImageNotFoundException:
        print("Gold Barrel image not found.")
        return 0
   
    # Look for "War Drums.png"
    try:
        war_drums = locateOnScreen("War Drums.png", confidence=0.75)
        if war_drums:
            print("Image Found: War Drums")
            war_drums_center = center(war_drums)
           
            click(war_drums_center[0], war_drums_center[1], interval=0.01, button='left')
            sleep(slow_sleep)
    except ImageNotFoundException:
        print("War Drums image not found.")
        return 0
   
    # Perform spacebar presses for 50 seconds
    press('space', presses=500, interval=0.1)
    sleep(fast_sleep)

    # Press the scrolls section
    click(x=press_scrolls_section[0], y=press_scrolls_section[1], interval=0.01, button='left')
    sleep(slow_sleep)

    # Look for both "Speed Scroll.png" and "Damage Scroll.png"
    try:
        speed_scroll = locateOnScreen("Speed Scroll.png", confidence=0.75)
        damage_scroll = locateOnScreen("Damage Scroll.png", confidence=0.75)

        if speed_scroll and damage_scroll:
            print("Both Speed Scroll and Damage Scroll found.")
            speed_scroll_center = center(speed_scroll)
            damage_scroll_center = center(damage_scroll)
           
            click(speed_scroll_center[0], speed_scroll_center[1], interval=0.01, button='left')
            sleep(slow_sleep)
            click(damage_scroll_center[0], damage_scroll_center[1], interval=0.01, button='left')
            sleep(slow_sleep)
        else:
            raise ImageNotFoundException("One or both scrolls not found.")
    except ImageNotFoundException:
        print("One or both scrolls not found.")
        sleep(slow_sleep)
        return 0
   
    # Press the inventory section
    click(x=press_inventory_section[0], y=press_inventory_section[1], interval=0.01, button='left')
    sleep(slow_sleep)

    for _ in range(2):
        # Look for "Gold Barrel.png"
        try:
            gold_barrel = locateOnScreen("Gold Barrel.png", confidence=0.75)
            if gold_barrel:
                print("Image Found: Gold Barrel")
                gold_barrel_center = center(gold_barrel)
           
            click(gold_barrel_center[0], gold_barrel_center[1], interval=0.01, button='left')
            sleep(slow_sleep)
        except ImageNotFoundException:
            print("Gold Barrel image not found.")
            return 0

        press(bag_hotkey)
        sleep(slow_sleep)
       
        # Wait for the gold barrel animation to finish to get the gold gained
        sleep(5)

        press(upgrade_hotkey)
        sleep(slow_sleep)

        click(press_first_upgrade[0], press_first_upgrade[1], interval=0.01, button='left')
        sleep(fast_sleep)
       
        click(press_sixth_upgrade[0], press_sixth_upgrade[1], interval=0.01, button='left')
        sleep(fast_sleep)

        press(upgrade_hotkey)
        sleep(slow_sleep)

        # Perform spacebar presses for guardian attack
        press('space', presses=500, interval=0.1)
        sleep(fast_sleep)

        press(bag_hotkey)
        sleep(slow_sleep)

        # Press the inventory section
        click(x=press_inventory_section[0], y=press_inventory_section[1], interval=0.01, button='left')
        sleep(slow_sleep)
   
    # Closes bag after loop
    press(bag_hotkey)
    sleep(slow_sleep)

    print("DPS increase process completed.")