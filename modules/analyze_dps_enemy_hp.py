import pyautogui
import time
import re
import numpy as np
import easyocr

from modules.perform_go_back_level_instruction import perform_go_back_level_instruction

# For analyzing DPS and Enemy HP value to determine if to go back a level
dps_coord = (81, 1040)  
enemy_hp_coord = (886, 71) 

# Sleep settings
slow_sleep = 0.2
fast_sleep = 0.02

# Clicking area
clicking_area = (932, 264)

# OCR reader (English, no GPU)
reader = easyocr.Reader(['en'], gpu=False)

def analyze_dps_enemy_hp():
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