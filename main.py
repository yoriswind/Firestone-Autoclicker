import pyautogui
import keyboard
import time
import random
import easyocr
import re
import numpy as np

from modules.perform_guild_expedition_instruction import perform_guild_expedition_instruction
from modules.perform_go_back_level_instruction import perform_go_back_level_instruction
from modules.perform_skill_tree_instruction import perform_skill_tree_instruction
from modules.increase_dps_with_items import increase_dps_with_items
from modules.handle_mission import handle_mission
from modules.claim_oracle_rituals import claim_oracle_rituals
from modules.claim_alchemist_experiments import claim_alchemist_experiments
from modules.claim_pickaxe_and_arcane_crystal import claim_pickaxe_and_arcane_crystal
from modules.claim_guardian_experience import claim_guardian_experience
from modules.claim_war_vehicle_loot import claim_war_vehicle_loot
from modules.claim_tools import claim_tools

# # Move between accounts. Deprecated since I'm only using 1 account now.
# # 1st account is Steam App and is to the right.
# # 2nd account is Google Chrome and is to the left.
# # Coordinates for the accounts
# first_account = (1166, 1039)
# second_account = (1098, 1035)

# For analyzing DPS and Enemy HP value to determine if to go back a level
dps_coord = (81, 1040)  
enemy_hp_coord = (886, 71) 

# Initializes error as object for exception handling
pyautogui.useImageNotFoundException()

class ImageNotFoundException(Exception):
    """Custom exception for image not found errors."""
    pass

# OCR reader (English, no GPU)
reader = easyocr.Reader(['en'], gpu=False)

# Clicking and sleep settings
clicking_area = (932, 264)
go_back_level = (722, 68)
slow_sleep = 0.2
fast_sleep = 0.02
presses = 50

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

# Prestige positions
prestige_hotkey = 'e'

press_town_icon = (1851, 203)
press_temple_of_eternals = (944, 232)
press_free_prestige = (1159, 833)
confirm_prestige = (1100, 706)
continue_game = (971,731)

# For analyzing firestone percentage
firestone_percentage_coord = (1162, 736) # Firestone percentage coordinate
close_temple_of_eternals = (1834, 55)  # close out of temple of eternals
close_town_firestone = (1843, 55)  # Close out town
close_settings_firestone = (1773, 84)  # Close out settings

# Navigating to skill tree 
press_library_icon = (1852, 209)
press_library_building = (280, 669)
press_firestone_icon = (1812, 630)

# Pressing skill tree positions
first_skill_slot = (612, 957)
second_skill_slot = (1263, 960)

skill_claim_or_speed_up = (957, 773)
close_speed_up = (1322, 294)

skill_research = (699, 773)
close_research_occupied = (1351, 372)

close_skill = (308, 176) # This is the moon in the skill tree page instead of the 'x'

library_close_out = (1846, 86)

# Accumulated clicks counters
switch_account_counter = 0
accumulated_prestige_clicks = 0
accumulated_skill_tree_clicks = 0
accumulated_go_back_level_clicks = 54000
after_accumulated_go_back_level_clicks = 0
accumulated_map_mission_clicks = 0
accumulated_guild_expedition_clicks = 0
accumulated_tools_claim_clicks = 0
accumulated_vehicle_loot_claim_clicks = 0
accumulated_pickaxe_and_arcane_crystal_claim_clicks = 0
accumulated_guardian_claim_clicks = 0
accumulated_alchemy_experiments_clicks = 0
accumulated_oracle_rituals_clicks = 0 


# Thresholds for trigger
click_threshold = 250
firestone_percentage_threshold = 100
go_back_level_counter = 0

prestige_trigger = click_threshold // 24
skill_tree_trigger = click_threshold // 24
go_back_level_trigger = 55500
map_mission_trigger = click_threshold // 24
guild_expedition_trigger = click_threshold // 24
tools_claim_trigger = click_threshold // 6
vehicle_loot__claim_trigger = click_threshold // 6
pickaxe_and_arcane_crystal_trigger = click_threshold // 6
guardian_claim_trigger = click_threshold // 6
alchemy_experiments_trigger = click_threshold // 6
oracle_rituals_trigger = click_threshold // 6

# Reverse order setting
reverse_order = False

# def switch_account(): Deprecated since I'm only using 1 account now.
    
#     global switch_account_counter
    
#     # if switch_account_counter % 2 == 0:
#     #     # Switch to the first account
        
#     #     pyautogui.press('win')
#     #     time.sleep(2)
#     #     pyautogui.click(first_account[0], first_account[1], interval=0.01, button='left')
#     #     time.sleep(2)
#     #     print("Switched to first account.")

#     # else:
#     #     # Switch to the second account
        
#     #     pyautogui.press('win')
#     #     time.sleep(2)
#     #     pyautogui.click(second_account[0], second_account[1], interval=0.01, button='left')
#     #     time.sleep(1)
#     #     print("Switched to second account.")
    
#     switch_account_counter = 0 

def analyze_dps_enemy_hp(): # More complicated to turn into separate file since there's global variable
    """
    Captures DPS and Enemy HP regions, performs OCR to extract values, 
    and triggers an action if DPS is lower than Enemy HP.
    """

    global go_back_level_counter

    # Capture screenshots of DPS and Enemy HP regions
    dps_screenshot = pyautogui.screenshot(region=(dps_coord[0], dps_coord[1], 110, 35))
    enemy_hp_screenshot = pyautogui.screenshot(region=(enemy_hp_coord[0], enemy_hp_coord[1], 110, 35))

    # dps_screenshot.save('DPS Value.png')
    # enemy_hp_screenshot.save('Enemy HP Value.png')

    # Perform OCR on screenshots
    dps_ocr = reader.readtext(np.array(dps_screenshot))
    enemy_hp_ocr = reader.readtext(np.array(enemy_hp_screenshot))

    try:
        print(dps_ocr[0][1])
        print(enemy_hp_ocr[0][1])

        # Extract numeric values from OCR results
        dps_value = int(re.findall('(?<=e)\d+', dps_ocr[0][1])[0])
        enemy_hp_value = int(re.findall('(?<=e)\d+', enemy_hp_ocr[0][1])[0])

        # Trigger action if DPS is less than Enemy HP
        if dps_value < enemy_hp_value:
            # print('Level too hard. Going back a level..'+'\n')
            perform_go_back_level_instruction()
            go_back_level_counter += 1
            print(f"Go back level counter now: {go_back_level_counter}\n")

        else: 
            # print('Level is okay. DPS is high enough to proceed to boss battle.'+'\n')    
            
            pyautogui.click(clicking_area[0], clicking_area[1], interval=0.01, button='left')
            time.sleep(fast_sleep)

    except (IndexError, ValueError):
    # Handle errors in OCR or invalid data
    # print("OCR did not recognize or returned invalid data. Press boss."+'\n')

    # pyautogui.click(clicking_area[0], clicking_area[1], interval=0.01, button='left')
    # time.sleep(fast_sleep)
        pass

def perform_prestige_instruction(): # More complicated to turn into separate file since there's global variable
    """
    Prestiges the game.
    """
    global accumulated_go_back_level_clicks
    
    # Open the town and temple of eternals
    pyautogui.click(press_town_icon[0], press_town_icon[1], interval=0.01, button='left')
    time.sleep(slow_sleep)
    pyautogui.click(press_temple_of_eternals[0], press_temple_of_eternals[1], interval=0.01, button='left')
    time.sleep(slow_sleep)

    # Capture a screenshot of the Firestone crystal percentage region
    firestone_screenshot = pyautogui.screenshot(region=(firestone_percentage_coord[0], firestone_percentage_coord[1], 125, 35))

    # Perform OCR on the screenshot to extract the Firestone percentage
    firestone_ocr = reader.readtext(np.array(firestone_screenshot))

    try:
        # Extract numeric value from OCR result
        firestone_percentage = int(re.findall('\d?,?\d+', firestone_ocr[0][1])[0])

        # Trigger an action based on the Firestone percentage
        if firestone_percentage < firestone_percentage_threshold:  # Example threshold of 50% for a low percentage
            print(f"Firestone percentage is low: {firestone_percentage}%\n")
            
            # Closes out Temple of Eternals and Town
            pyautogui.click(close_temple_of_eternals[0], close_temple_of_eternals[1], interval=0.01, button='left')
            time.sleep(slow_sleep)

            pyautogui.click(close_town_firestone[0], close_town_firestone[1], interval=0.01, button='left')
            time.sleep(slow_sleep)

            pyautogui.click(close_settings_firestone[0], close_settings_firestone[1], interval=0.01, button='left')
            time.sleep(slow_sleep)

        else:
            print(f"Firestone percentage is high enough: {firestone_percentage}%. Proceeding with the task.\n")

            # Perform free prestige and confirm
            pyautogui.click(press_free_prestige[0], press_free_prestige[1], interval=0.01, button='left')
            time.sleep(slow_sleep)
            pyautogui.click(confirm_prestige[0], confirm_prestige[1], interval=0.01, button='left')
            time.sleep(5)

            pyautogui.click(continue_game[0], continue_game[1], interval=0.01, button='left')
            time.sleep(3)

            # Preps the upgrade multiplier to max
            pyautogui.press(upgrade_hotkey)
            time.sleep(slow_sleep)
            
            pyautogui.click(upgrade_multiplier[0], upgrade_multiplier[1], interval=0.01, button='left')
            time.sleep(slow_sleep)
            pyautogui.click(upgrade_multiplier[0], upgrade_multiplier[1], interval=0.01, button='left')
            time.sleep(slow_sleep)
            pyautogui.click(upgrade_multiplier[0], upgrade_multiplier[1], interval=0.01, button='left')
            time.sleep(slow_sleep)
            pyautogui.click(upgrade_multiplier[0], upgrade_multiplier[1], interval=0.01, button='left')
            time.sleep(slow_sleep)

            time.sleep(5) #Wait for a kill so that it can upgrade 

            pyautogui.click(press_first_upgrade[0], press_first_upgrade[1], interval=0.01, button='left')
            time.sleep(3)

            pyautogui.click(press_second_upgrade[0], press_second_upgrade[1], interval=0.01, button='left')
            time.sleep(fast_sleep)
            pyautogui.click(press_third_upgrade[0], press_third_upgrade[1], interval=0.01, button='left')
            time.sleep(fast_sleep)
            pyautogui.click(press_fourth_upgrade[0], press_fourth_upgrade[1], interval=0.01, button='left')
            time.sleep(fast_sleep)
            pyautogui.click(press_fifth_upgrade[0], press_fifth_upgrade[1], interval=0.01, button='left')
            time.sleep(fast_sleep)
            pyautogui.click(press_sixth_upgrade[0], press_sixth_upgrade[1], interval=0.01, button='left')
            time.sleep(fast_sleep)
            pyautogui.click(press_seventh_upgrade[0], press_seventh_upgrade[1], interval=0.01, button='left')
            time.sleep(fast_sleep)

            pyautogui.click(upgrade_multiplier[0], upgrade_multiplier[1], interval=0.01, button='left')
            time.sleep(slow_sleep)
            pyautogui.click(upgrade_multiplier[0], upgrade_multiplier[1], interval=0.01, button='left')
            time.sleep(slow_sleep)
            pyautogui.click(upgrade_multiplier[0], upgrade_multiplier[1], interval=0.01, button='left')
            time.sleep(slow_sleep)
            pyautogui.click(upgrade_multiplier[0], upgrade_multiplier[1], interval=0.01, button='left')
            time.sleep(slow_sleep)
            
            pyautogui.press(upgrade_hotkey)
            time.sleep(slow_sleep)

            accumulated_go_back_level_clicks = 0

    except (IndexError, ValueError):
        # Handle errors in OCR or invalid data
        print("OCR did not recognize or returned invalid data. Cannot proceed.\n")

        # Closes out Temple of Eternals and Town
        pyautogui.click(close_temple_of_eternals[0], close_temple_of_eternals[1], interval=0.01, button='left')
        time.sleep(slow_sleep)

        pyautogui.click(close_town_firestone[0], close_town_firestone[1], interval=0.01, button='left')
        time.sleep(slow_sleep)

        pyautogui.click(close_settings_firestone[0], close_settings_firestone[1], interval=0.01, button='left')
        time.sleep(slow_sleep)

def perform_actions():
    global accumulated_go_back_level_clicks, after_accumulated_go_back_level_clicks
    global accumulated_skill_tree_clicks, accumulated_map_mission_clicks
    global accumulated_prestige_clicks, accumulated_guild_expedition_clicks
    global accumulated_tools_claim_clicks, accumulated_vehicle_loot_claim_clicks
    global accumulated_pickaxe_and_arcane_crystal_claim_clicks, accumulated_guardian_claim_clicks
    global accumulated_alchemy_experiments_clicks, accumulated_oracle_rituals_clicks
    
    global go_back_level_counter, reverse_order

    # Perform key presses to trigger hero's abilities
    pyautogui.press('1')
    time.sleep(fast_sleep)
    pyautogui.press('1')
    time.sleep(fast_sleep)
    pyautogui.press('1')
    time.sleep(fast_sleep)

    # Perform spacebar presses for guardian attack
    pyautogui.press('space', presses=presses, interval=0.1)
    time.sleep(fast_sleep)

    # Perform key presses to trigger hero's abilities again
    pyautogui.press('1')
    time.sleep(fast_sleep)
    pyautogui.press('1')
    time.sleep(fast_sleep)
    pyautogui.press('1')
    time.sleep(fast_sleep)

    # # Update accumulated clicks for counter of specific functions
    accumulated_prestige_clicks += presses
    accumulated_go_back_level_clicks += presses
    accumulated_map_mission_clicks += presses
    accumulated_skill_tree_clicks += presses
    accumulated_guild_expedition_clicks += presses
    accumulated_tools_claim_clicks += presses
    accumulated_vehicle_loot_claim_clicks += presses
    accumulated_pickaxe_and_arcane_crystal_claim_clicks += presses
    accumulated_guardian_claim_clicks += presses
    accumulated_alchemy_experiments_clicks += presses

    # Trigger prestige actions when the threshold is reached
    if accumulated_prestige_clicks >= prestige_trigger:

        perform_prestige_instruction()
        accumulated_prestige_clicks = 0

    # Trigger skill tree clicks when the threshold is reached
    if accumulated_skill_tree_clicks >= skill_tree_trigger: # perform_skill_tree_instruction is a recursive function, so this is a work-around
        # Open the library for skill slots and skill tree actions
        pyautogui.click(press_library_icon[0], press_library_icon[1], interval=0.01, button='left')
        time.sleep(slow_sleep)
        pyautogui.click(press_library_building[0], press_library_building[1], interval=0.01, button='left')
        time.sleep(slow_sleep)
        pyautogui.click(press_firestone_icon[0], press_firestone_icon[1], interval=0.01, button='left')
        time.sleep(slow_sleep)

        # Select and claim skills from the skill slots
        pyautogui.click(first_skill_slot[0], first_skill_slot[1], interval=0.01, button='left')
        time.sleep(slow_sleep)
        pyautogui.click(close_skill[0], close_skill[1], interval=0.01, button='left')
        time.sleep(slow_sleep)

        pyautogui.click(second_skill_slot[0], second_skill_slot[1], interval=0.01, button='left')
        time.sleep(slow_sleep)
        pyautogui.click(close_skill[0], close_skill[1], interval=0.01, button='left')
        time.sleep(slow_sleep)

        # Perform skill tree instruction and reset clicks
        perform_skill_tree_instruction()
        accumulated_skill_tree_clicks = 0

    # Trigger go back level click when the threshold is reached
    if accumulated_go_back_level_clicks >= 54000:
        if accumulated_go_back_level_clicks + after_accumulated_go_back_level_clicks >= go_back_level_trigger:
            perform_go_back_level_instruction()
            accumulated_go_back_level_clicks = 54000
            after_accumulated_go_back_level_clicks = 0 

    # Trigger map mission clicks when the threshold is reached
    if accumulated_map_mission_clicks >= map_mission_trigger:
        # Handle multiple missions sequentially

        handle_mission("Map Mission Claim")
        time.sleep(slow_sleep)
        handle_mission("Gift Box Mission")
        time.sleep(slow_sleep)
        handle_mission("Scout Mission")
        time.sleep(slow_sleep)
        handle_mission("Adventure Mission")
        time.sleep(slow_sleep)
        handle_mission("War Mission")
        time.sleep(slow_sleep)
        handle_mission("Dragon Mission")
        time.sleep(slow_sleep)
        handle_mission("Monster Mission")
        time.sleep(slow_sleep)
        handle_mission("Naval Mission")
        time.sleep(slow_sleep)

        pyautogui.click(clicking_area[0], clicking_area[1], interval=0.01, button='left')
        time.sleep(fast_sleep)

        # Reset accumulated mission clicks
        accumulated_map_mission_clicks = 0

    # Trigger guild expedition clicks when the threshold is reached
    if accumulated_guild_expedition_clicks >= guild_expedition_trigger:
        perform_guild_expedition_instruction()
        accumulated_guild_expedition_clicks = 0

    # Trigger tools claim when the threshold is reached
    if accumulated_tools_claim_clicks >= tools_claim_trigger:
        claim_tools()
        accumulated_tools_claim_clicks = 0

    # Trigger war vehicle loot claim when the threshold is reached
    if accumulated_vehicle_loot_claim_clicks >= vehicle_loot__claim_trigger:
        claim_war_vehicle_loot()
        accumulated_vehicle_loot_claim_clicks = 0

    # Trigger pickaxe and arcane crystal claim when the threshold is reached
    if accumulated_pickaxe_and_arcane_crystal_claim_clicks >= pickaxe_and_arcane_crystal_trigger:
        claim_pickaxe_and_arcane_crystal()
        accumulated_pickaxe_and_arcane_crystal_claim_clicks = 0

    # Trigger guardian experience claim when the threshold is reached
    if accumulated_guardian_claim_clicks >= guardian_claim_trigger:
        claim_guardian_experience()
        accumulated_guardian_claim_clicks = 0

    # Trigger alchemist experiements claim when the threshold is reached
    if accumulated_alchemy_experiments_clicks >= alchemy_experiments_trigger:
        claim_alchemist_experiments()
        accumulated_alchemy_experiments_clicks = 0

    # Trigger increase dps instruction when the threshold is reached to increase prestige
    if go_back_level_counter == 25:
        increase_dps_with_items()
        time.sleep(slow_sleep)

        perform_prestige_instruction
        time.sleep(slow_sleep)

        go_back_level_counter = 0

    # Trigger alchemist experiements claim when the threshold is reached
    if accumulated_oracle_rituals_clicks >= oracle_rituals_trigger:
        claim_oracle_rituals()
        accumulated_oracle_rituals_clicks = 0

    # Handle upgrade actions based on reverse order setting
    if reverse_order:
        pyautogui.press(upgrade_hotkey)
        time.sleep(slow_sleep)

        # Optionally, specify the positions to click first regardless of order. See below:

        pyautogui.click(press_first_upgrade[0], press_first_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        pyautogui.click(press_sixth_upgrade[0], press_sixth_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)

        # Reverse order   

        pyautogui.click(press_seventh_upgrade[0], press_seventh_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        pyautogui.click(press_sixth_upgrade[0], press_sixth_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        pyautogui.click(press_fifth_upgrade[0], press_fifth_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        pyautogui.click(press_fourth_upgrade[0], press_fourth_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        pyautogui.click(press_third_upgrade[0], press_third_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        pyautogui.click(press_second_upgrade[0], press_second_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        pyautogui.click(press_first_upgrade[0], press_first_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)

        pyautogui.press(upgrade_hotkey)
        time.sleep(slow_sleep)

        try:
            mission_alert = pyautogui.locateOnScreen("Map Scroll.png", confidence=0.75)
            mission_alert_center = pyautogui.center(mission_alert)
            # print(f"    Image Found: {'Map Scroll'}. Performing map mission actions..."+'\n')

            if handle_mission("Map Mission Claim") == 1:
                
                handle_mission("Gift Box Mission")
                time.sleep(slow_sleep)
                handle_mission("Scout Mission")
                time.sleep(slow_sleep)
                handle_mission("Adventure Mission")
                time.sleep(slow_sleep)
                handle_mission("War Mission")
                time.sleep(slow_sleep)
                handle_mission("Dragon Mission")
                time.sleep(slow_sleep)
                handle_mission("Monster Mission")
                time.sleep(slow_sleep)
                handle_mission("Naval Mission")
                time.sleep(slow_sleep)
                
            else:
                pass
        
        except pyautogui.ImageNotFoundException:
            # print(f"Image Not Found: Map Scroll.png"+'\n')
            pass
    else:
        pyautogui.press(upgrade_hotkey)
        time.sleep(slow_sleep)

        # Optionally, specify the positions to click first regardless of order. See below:

        pyautogui.click(press_first_upgrade[0], press_first_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        pyautogui.click(press_sixth_upgrade[0], press_sixth_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)

        # Regular order    

        pyautogui.click(press_first_upgrade[0], press_first_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        pyautogui.click(press_second_upgrade[0], press_second_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        pyautogui.click(press_third_upgrade[0], press_third_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        pyautogui.click(press_fourth_upgrade[0], press_fourth_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        pyautogui.click(press_fifth_upgrade[0], press_fifth_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        pyautogui.click(press_sixth_upgrade[0], press_sixth_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        pyautogui.click(press_seventh_upgrade[0], press_seventh_upgrade[1], interval=0.01, button='left')
        time.sleep(fast_sleep)

        # Call this function to check if need to go back a level
        analyze_dps_enemy_hp()
        time.sleep(slow_sleep)

        pyautogui.press(upgrade_hotkey)
        time.sleep(slow_sleep)

        # List of images and their corresponding functions
        image_actions = [
            ("Expedition Guild.png", perform_guild_expedition_instruction, "accumulated_guild_expedition_clicks"),
            ("Skill Book.png", perform_skill_tree_instruction, "accumulated_skill_tree_clicks"),
            ("Prestige Crystal.png", perform_prestige_instruction, "accumulated_prestige_clicks"),
            ("Construction Hat.png", claim_tools, "accumulated_tools_claim_clicks"),
            ("War Vehicle.png", claim_war_vehicle_loot, "accumulated_vehicle_loot_claim_clicks"),
            ("Dragon Head.png", claim_guardian_experience, "accumulated_guardian_claim_clicks"),
            ("Pickaxe.png", claim_pickaxe_and_arcane_crystal, "accumulated_pickaxe_and_arcane_crystal_claim_clicks"),
            ("Arcane Crystal.png", claim_pickaxe_and_arcane_crystal, "accumulated_pickaxe_and_arcane_crystal_claim_clicks"),
            ("Alchemy Bottle.png", claim_alchemist_experiments, "accumulated_alchemy_experiments_clicks"),
            ("Oracle Candle.png", claim_oracle_rituals, "accumulated_oracle_rituals_clicks")
        ]
        # Loop through the images and their respective actions
        for image_name, action_function, counter_variable in image_actions:
            
            try:
                alert = pyautogui.locateOnScreen(image_name, confidence=0.75)
                center = pyautogui.center(alert)
                # print(f"    Image Found: {image_name}. Performing {image_name} actions..."+'\n')

                if action_function == perform_skill_tree_instruction: # perform_skill_tree_instruction is a recursive function, so this is a work-around
                    
                    # Open the library for skill slots and skill tree actions
                    pyautogui.click(press_library_icon[0], press_library_icon[1], interval=0.01, button='left')
                    time.sleep(slow_sleep)
                    pyautogui.click(press_library_building[0], press_library_building[1], interval=0.01, button='left')
                    time.sleep(slow_sleep)
                    pyautogui.click(press_firestone_icon[0], press_firestone_icon[1], interval=0.01, button='left')
                    time.sleep(slow_sleep)

                    # Select and claim skills from the skill slots
                    pyautogui.click(first_skill_slot[0], first_skill_slot[1], interval=0.01, button='left')
                    time.sleep(slow_sleep)
                    pyautogui.click(close_skill[0], close_skill[1], interval=0.01, button='left')
                    time.sleep(slow_sleep)

                    pyautogui.click(second_skill_slot[0], second_skill_slot[1], interval=0.01, button='left')
                    time.sleep(slow_sleep)
                    pyautogui.click(close_skill[0], close_skill[1], interval=0.01, button='left')
                    time.sleep(slow_sleep)

                    # Call the corresponding function
                    action_function()
                    
                    # Reset the respective counter
                    globals()[counter_variable] = 0

                elif action_function != perform_skill_tree_instruction:
                
                    # Call the corresponding function
                    action_function()
                    
                    # Reset the respective counter
                    globals()[counter_variable] = 0

                else:
                    continue
            
            except pyautogui.ImageNotFoundException:
                # print(f"Image Not Found: {image_name}"+'\n')
                continue

        # switch_account()

    # Toggle the order for the next cycle
    reverse_order = not reverse_order

def main():
    print("Press '=' to start the process, 'i' to stop, and 'Esc' to exit.")
    running = False

    while True:
        if keyboard.is_pressed('esc'):
            print("Exiting program.")
            break

        if keyboard.is_pressed('=') and not running:
            print("Process started.")
            running = True

        if keyboard.is_pressed('i') and running:
            print("Process paused.")
            running = False

        if running:
            perform_actions()  # Call the function to perform actions
            # Small delay to avoid excessive CPU usage
            time.sleep(0.01)

# Ensure that main() is called when this script is run directly
if __name__ == "__main__":
    main()