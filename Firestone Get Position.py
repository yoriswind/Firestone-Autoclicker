import pyautogui
import keyboard

def get_mouse_position():
    # Get and print the current mouse position
    pos = pyautogui.position()
    print(f"Mouse position: {pos}")

print("Press 'y' to get the mouse position. Press 'Esc' to exit.")

while True:
    # Listen for the 'u' key press
    if keyboard.is_pressed('y'):
        get_mouse_position()
        # Add a small delay to prevent multiple prints from a single key press
        keyboard.wait('y')  # Wait for the key to be released
    # Exit the program when 'Esc' is pressed
    if keyboard.is_pressed('esc'):
        print("Exiting program.")
        break
