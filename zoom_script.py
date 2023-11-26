import pyautogui
import subprocess
import datetime
import time
# import opencv

def join(id, password):
    # Open the Zoom application. Update the path to your own Zoom executable file. - \\ required - 
    subprocess.call("C:\\Users\\USER\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe", shell=True)
    
    # Loop until finding and clicking the 'Join' button.
    while True:
        join1 = pyautogui.locateCenterOnScreen('join1.png')
        if join1 is not None:
            pyautogui.click(join1)
            print("Clicked Join 1")
            break
        else:
            print("Could not find join 1")
            time.sleep(2)
    
    # Locate the meeting ID input field and enter the meeting ID to join.
    while True:
        meeting_id = pyautogui.locateOnScreen('meeting_id.png')
        if meeting_id is not None:
            pyautogui.click(meeting_id)
            print("Entered the Meeting ID")
            pyautogui.typewrite(id)
            pyautogui.click(pyautogui.locateCenterOnScreen('join2.png'))
            break
        else:
            print("Could not find meeting ID input field")
            time.sleep(2)

    # Locate the password input field and enter the meeting password.
    while True:
        pswd = pyautogui.locateCenterOnScreen('pswd2.png')
        if pswd is not None:
            pyautogui.click(pswd)
            print("Entered the Meeting Password")
            pyautogui.typewrite(password)
            pyautogui.click(pyautogui.locateCenterOnScreen('join_meeting.png'))
            break
        else:
            print("Could not find the input password field")
            time.sleep(2)

    # Mute the microphone.
    while True:
        mute = pyautogui.locateCenterOnScreen('mute.png')
        if mute is not None:
            pyautogui.click(mute)
            print("Clicked Mute")
            break
        else:
            print("Could not find Mute button")
            time.sleep(2)

    # Stop the video.
    while True:
        stop_video = pyautogui.locateCenterOnScreen('stop_video.png')
        if stop_video is not None:
            pyautogui.click(stop_video)
            print("Clicked Stop Video")
            break
        else:
            print("Could not find Stop Video button")
            time.sleep(2)

    # Click the third 'Join' button.
    while True:
        join3 = pyautogui.locateCenterOnScreen('join3.png')
        if join3 is not None:
            pyautogui.click(join3)
            print("Clicked Join 3")
            break
        else:
            print("Could not find Join 3 button")
            time.sleep(2)

    # Attempt to maximize the meeting window in Zoom (commented out due to Zoom configuration options).
    # While True:
    #     maximize = pyautogui.locateCenterOnScreen('maximize.png')
    #     if maximize is not None:
    #         pyautogui.click(maximize)
    #         print("Clicked maximize")
    #         break
    #     else:
    #         print("Could not find maximize button")
    #         time.sleep(2)

    # Start the meeting recording.
    while True:
        record = pyautogui.locateOnScreen('record.png')
        if record is not None:
            pyautogui.click(record)
            print("Clicked Record")
            break
        else:
            print("Could not find Record button")
            time.sleep(2)

    # Send a request to start recording the meeting.
    while True:
        send_request = pyautogui.locateCenterOnScreen('send_request.png')
        if send_request is not None:
            pyautogui.click(send_request)
            print("Clicked Send Request")
            break
        else:
            print("Could not find Send Request button")
            time.sleep(2)

# Replace 'meeting_id' and 'meeting_password' with your actual meeting ID and password.
join("meeting_id", "meeting_password")
