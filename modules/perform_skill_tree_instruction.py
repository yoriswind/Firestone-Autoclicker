from pyautogui import click
import time
import random

# Sleep settings
slow_sleep = 0.2
fast_sleep = 0.02

# List of skill tree coordinates
skill_1_1 = (419, 278)
skill_1_2 = (419, 401)
skill_1_3 = (419, 525)
skill_1_4 = (419, 650)
skill_1_5 = (419, 772)

skill_2_1 = (892, 278)
skill_2_2 = (892, 401)
skill_2_3 = (892, 525)
skill_2_4 = (892, 650)
skill_2_5 = (892, 772)

skill_3_1 = (1356, 278)
skill_3_2 = (1356, 401)
skill_3_3 = (1356, 525)
skill_3_4 = (1356, 650)
skill_3_5 = (1356, 772)

# Skill tree positions
library_hotkey = 'l'

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
close_library = (1846, 86)
close_settings = (1773, 86)

# List of skill tree coordinates
skill_1_1 = (419, 278)
skill_1_2 = (419, 401)
skill_1_3 = (419, 525)
skill_1_4 = (419, 650)
skill_1_5 = (419, 772)

skill_2_1 = (892, 278)
skill_2_2 = (892, 401)
skill_2_3 = (892, 525)
skill_2_4 = (892, 650)
skill_2_5 = (892, 772)

skill_3_1 = (1356, 278)
skill_3_2 = (1356, 401)
skill_3_3 = (1356, 525)
skill_3_4 = (1356, 650)
skill_3_5 = (1356, 772)

# Skill positions of available skills to upgrade. Change according to available skills on the screen
skill_positions_first = [skill_2_2, skill_2_4, skill_3_1, skill_3_3]
# skill_positions_second = [skill_1_3, skill_2_2, skill_2_4]

def perform_skill_tree_instruction(skill_index=0):
    """
    Starts and completes a skill research.
    """
    skill_positions = skill_positions_first

    # # First account skill tree. Deprecated since I'm only using 1 account now.
    # if switch_account_counter % 2 == 0:
    #     skill_positions = skill_positions_first

    # else:
    #     skill_positions = skill_positions_second

    # # print(skill_positions)
    
    # Select two random skill positions
    skill_select = [random.choice(skill_positions), random.choice(skill_positions)]
    
    # Check if the skill index is out of range and close the library if so
    if skill_index >= len(skill_select):
        click(close_library[0], close_library[1], interval=0.01, button='left')
        time.sleep(slow_sleep)
        click(close_library[0], close_library[1], interval=0.01, button='left')
        time.sleep(slow_sleep)

        click(close_settings[0], close_settings[1], interval=0.01, button='left')
        time.sleep(slow_sleep)
        return

    else:
        # Select the current skill position based on the index
        current_skill_position = skill_select[skill_index]

        # Perform skill selection and claim or speed up
        click(current_skill_position[0], current_skill_position[1], interval=0.01, button='left')
        time.sleep(slow_sleep)
        click(skill_claim_or_speed_up[0], skill_claim_or_speed_up[1], interval=0.01, button='left')
        time.sleep(slow_sleep)
        click(close_skill[0], close_skill[1], interval=0.01, button='left')
        time.sleep(slow_sleep)
        click(close_skill[0], close_skill[1], interval=0.01, button='left')
        time.sleep(slow_sleep)

        # Perform skill research and close skill tree
        click(current_skill_position[0], current_skill_position[1], interval=0.01, button='left')
        time.sleep(slow_sleep)
        click(skill_research[0], skill_research[1], interval=0.01, button='left')
        time.sleep(slow_sleep)
        click(close_skill[0], close_skill[1], interval=0.01, button='left')
        time.sleep(slow_sleep)
        click(close_skill[0], close_skill[1], interval=0.01, button='left')
        time.sleep(slow_sleep)

    # Process the next skill position
    perform_skill_tree_instruction(skill_index+1)