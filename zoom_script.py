import pyautogui
import subprocess
import datetime
import time
#import opencv

def join(id, password):
#open zoom / join
    subprocess.call("C:\\Users\\Natal Jr\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe", shell = True) 
    while True:
        join1 = pyautogui.locateCenterOnScreen('join1.png')
        if join1 != None:
            pyautogui.click(join1)
            print("Clicked Join 1")
            break
        else:
            print("Could not find join 1")
            time.sleep(2) 
    
# # click out of the box, fix the meeting_id input issue 
#     while True:
#         click = pyautogui.locateCenterOnScreen('click.png')
#         if click != None:
#             pyautogui.moveTo(click)
#             print("moved")
#             break
#         else:
#             print("Could not find")
#             time.sleep(2)  

   
#adding meeting_id and joining
    while True:
        meeting_id = pyautogui.locateOnScreen('meeting_id.png')
        if meeting_id != None:
            pyautogui.click(meeting_id)
            print("Made the Input meeting_id")
            pyautogui.typewrite(id)
            pyautogui.click(pyautogui.locateCenterOnScreen('join2.png'))
            break
        else:
            print("Could not find meeting_id")
            time.sleep(2)

#typing pswd
    while True:
        pswd = pyautogui.locateCenterOnScreen('pswd2.png')
        if pswd != None:
            pyautogui.click(pswd)
            print("Made the Input pswd")
            pyautogui.typewrite(password)
            pyautogui.click(pyautogui.locateCenterOnScreen('join_meeting.png'))
            break
        else:
            print("Could not find the input pswd")
            time.sleep(2)

#mute
    while True:
        mute = pyautogui.locateCenterOnScreen('mute.png')
        if mute != None:
            pyautogui.click(mute)
            print("Clicked Mute")
            break
        else:
            print("Could not find Mute")
            time.sleep(2) 

#stop video
    while True:
        stop_video = pyautogui.locateCenterOnScreen('stop_video.png')
        if stop_video != None:
            pyautogui.click(stop_video)
            print("Clicked stop_video")
            break
        else:
            print("Could not find stop_video")
            time.sleep(2) 


#join button 3
    while True:
        join3 = pyautogui.locateCenterOnScreen('join3.png')
        if join3 != None:
            pyautogui.click(join3)
            print("Clicked Join 3")
            break
        else:
            print("Could not find join 3")
            time.sleep(2) 



# # #maximize
#     while True:
#         maximize = pyautogui.locateCenterOnScreen('maximize.png')
#         if maximize != None:
#             pyautogui.click(maximize)
#             print("Clicked maximize")
#             break
#         else:
#             print("Could not find maximize")
#             time.sleep(2) 

#record
    while True:
        record = pyautogui.locateOnScreen('record.png')
        if record != None:
            pyautogui.click(record)
            print("Clicked Record")
            break
        else:
            print("Could not find record")
            time.sleep(2) 

#send_request
    while True:
        send_request = pyautogui.locateCenterOnScreen('send_request.png')
        if send_request != None:
            pyautogui.click(send_request)
            print("Clicked send_request")
            break
        else:
            print("Could not find send_request")
            time.sleep(2) 

join("6788885688","L1ZHRTcxc29jemNIUlZGLzhKYXBWQT09")