# AutoType Python Script

I created the "AutoType" Python script in 2019 to address a challenge during a server outage at a workplace where manual entry of membership card numbers became necessary. The script automates typing from a file, eliminating the need for manual data entry during server downtimes. Despite initial resistance to implement it within the organization, I decided to make the project open-source for the broader community.

## Motivation

The motivation is to make technology accessible to everyone, offering a simple solution for automating repetitive typing tasks. Whether in a professional, educational, or personal setting, the AutoType script aims to enhance efficiency and reduce the burden of manual data entry. I encourage collaboration, modification, and contributions to empower individuals and foster innovation. Happy coding!

## AutoType Script Overview

The provided Python script, named "AutoType," is designed to automate the typing of text from a specified file into an input field. The script utilizes the `pyautogui` library to simulate keyboard actions, allowing it to type each line from the specified file and press the Enter key after each entry.

### Key Components

1. **File Reading:** The script reads lines from a specified file (in this case, "note.txt").

2. **Delay:** It includes a time delay of 5 seconds, providing users with a window to switch to the desired input field before the typing begins.

3. **Typing and Enter Key Press:** Using `pyautogui.typewrite()`, the script types each line from the file after stripping leading and trailing whitespaces. It then simulates the pressing of the Enter key with `pyautogui.press('enter')`.

4. **Adjustable Sleep Duration:** Users can customize the sleep duration between typing each line by modifying the `time.sleep(1)` line based on their specific requirements.

### Usage

The script is encapsulated within a try-except block to handle the case where the specified file is not found, providing an informative error message.

In the `__main__` block, the script is set to read from "note.txt." Users can modify the `file_to_type` variable to point to their desired input file.

Feel free to contribute, modify, and enhance the script for various use cases!
