# zoom_bot_join_and_record
## Zoom Meeting Automation Project
This Python project provides an automation script for joining and recording Zoom meetings through image recognition using PyAutoGUI library. The script aims to streamline the process of joining a meeting, inputting meeting credentials, and initiating recording.

### Prerequisites
 - Python
 - PyAutoGUI library
   
### How to Use
Clone the repository to your local machine.
Install the necessary libraries, especially PyAutoGUI.
Run the Python script zoom_automation.py.
Replace the meeting_id and password parameters in the join() function with your Zoom meeting details.
Execute the script.

### Functionality
The code performs the following actions:
- Opens Zoom application.
- Automatically locates and clicks on join buttons and input fields using image recognition (*.png files).
- Enters meeting ID and password.
- Mutes microphone and stops video.
- Joins the meeting and initiates the recording.
- Sends the meeting request.
Note: Please ensure that the image files (*.png) used for recognition correspond to the Zoom interface in your system. Adjustments might be needed based on your screen resolution or Zoom interface changes.

### Caution: Use this script responsibly and in compliance with Zoom's terms of service. Automated actions in applications like Zoom might have implications and should be used with proper authorization.

### Disclaimer
This script is solely for educational purposes and convenience in automating personal tasks. Misuse of this script for unauthorized access or unethical behavior is strictly discouraged.
