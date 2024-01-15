import time
import pyautogui

def auto_type(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            # Wait for a few seconds to give time to switch to the desired input field
            time.sleep(5)

            # Type each line and press Enter
            for line in lines:
                pyautogui.typewrite(line.strip())
                pyautogui.press('enter')
                time.sleep(1)  # Adjust this sleep duration based on your needs

    except FileNotFoundError:
        print(f"Error: {filename} not found.")

if __name__ == "__main__":
    ##data.txt: Keep in mind that these are not valid barcodes for commercial use and are provided only as sequences of digits for illustrative purposes.
    file_to_type = "data.txt"
    auto_type(file_to_type)
