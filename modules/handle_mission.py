from pyautogui import click, locateAllOnScreen, center
import time
import easyocr

# Initializes error as object for exception handling
class ImageNotFoundException(Exception):
    """Custom exception for image not found errors."""
    pass

# Sleep settings
slow_sleep = 0.2
fast_sleep = 0.02

# Map Mission positions
map_hotkey = 'm'
press_map_icon = (1854, 343)
claim_reward = (961, 644)
start_mission = (1080, 879)
close_mission_page = (1503, 239)
close_map_page = (1863, 46)
close_settings = (1773, 86)

def handle_mission(mission_name):
    """
    Finds, claims, and starts a mission in the map.
    """

    # Click the map icon to open the map
    click(press_map_icon[0], press_map_icon[1], interval=0.01, button='left')
    time.sleep(slow_sleep)

    try:
        # Locate all occurrences of the mission icon on the screen
        missions_raw = list(locateAllOnScreen(f'{mission_name}.png', confidence=0.75))
        missions_tuple = [tuple(center(mission)) for mission in missions_raw]
        missions_dedup_1st_ele = list({t[0]: t for t in missions_tuple}.values())  # Dedup based on the 1st element of coords
        seen_2nd_ele = set()
        missions = [t for t in missions_dedup_1st_ele if t[1] not in seen_2nd_ele and not seen_2nd_ele.add(t[1])]  # Dedup based on the 2nd element

        print(missions)
        if not missions:  # If no images are found, raise the custom exception
            raise ImageNotFoundException(f"Image for {mission_name} not found.")
        
        print(f"Raw images Found for {mission_name} but some were deduped. Total: {len(missions_tuple)}")
        print(f"Images Found for {mission_name}. Total: {len(missions)}")

        for mission in missions:
            # Claim the reward and close the mission page
            click(mission[0], mission[1], interval=0.01, button='left')
            time.sleep(slow_sleep)
            click(claim_reward[0], claim_reward[1], interval=0.01, button='left')
            time.sleep(slow_sleep)
            click(close_mission_page[0], close_mission_page[1], interval=0.01, button='left')
            time.sleep(slow_sleep)

            # Start the mission and close the mission page
            click(mission[0], mission[1], interval=0.01, button='left')
            time.sleep(slow_sleep)
            click(start_mission[0], start_mission[1], interval=0.01, button='left')
            time.sleep(slow_sleep)
            click(close_mission_page[0], close_mission_page[1], interval=0.01, button='left')
            time.sleep(slow_sleep)

        # Close the map page
        click(close_map_page[0], close_map_page[1], interval=0.01, button='left')
        time.sleep(slow_sleep)

        # Close settings
        click(close_settings[0], close_settings[1], interval=0.01, button='left')
        time.sleep(fast_sleep)

        return 1

    except Exception as e:
        print(f"An unexpected error occurred for {mission_name}: {e}")

        # Close the map page to reset the state
        click(close_map_page[0], close_map_page[1], interval=0.01, button='left')
        time.sleep(slow_sleep)

        # Close settings
        click(close_settings[0], close_settings[1], interval=0.01, button='left')
        time.sleep(fast_sleep)
        
        return 0