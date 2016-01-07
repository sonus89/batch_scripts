import win32api
import win32con
import win32gui
import time
import math
from PIL import ImageGrab
import win32com.client
#import pyscreenshot as ImageGrab

########################################### PYTHON TEST SCRIPT ############################################
# Screenshots will be saved into the same directory where the script is located.
# Screenshot names: "sc1.png","sc2.png","sc3.png","sc4.png"
# Save State will be created as "st1"

"""
# Procedure:
1. Login to some application
2. Click on something

# After Login, and clicking on something, the procedure is:
3. Screenshot
4. Moving mouse and holding left button								
5. Screenshot again
6. Fullscreen Screenshot
7. Resizing window
8. Fullscreen Screenshot
9. Click
10. Screenshot of Series List in Worklist Browser
"""
##########################################################################################################

window_name = "Microsoft Word"
PyHandle = win32gui.FindWindow(0,window_name) 				#set handle
win32gui.SetForegroundWindow(PyHandle)						#set window active
win32gui.ShowWindow(PyHandle, True)							#maximize window
win32gui.ShowWindow(PyHandle, win32con.SW_MAXIMIZE)			#the line is due to avoid resize error
win32gui.MoveWindow(PyHandle, 0, 0, 1280, 1024, True)		#resize to specified resolution

time.sleep(4)
win32api.SetCursorPos((200,35))								#mouse cursor into upper left corner

# SCREENSHOT OF SPECIFIC VIEWPORT ///////////////////////////////////////////////////////////////////////

win32api.SetCursorPos((900,400)) 				
time.sleep(1)								
															#bbox parameters
X1 = 639
X2 = 1273
Y1 = 180
Y2 = 560

bbox = (X1,Y1,X2,Y2)										#parameters for upper right NX window
screenshot = ImageGrab.grab(bbox) 							#save part of screen capture
screenshot.save("sc1.png", "PNG")							
time.sleep(1)

# PAGING ////////////////////////////////////////////////////////////////////////////////////////////////

win32api.SetCursorPos((900,400)) 							#click into NX window (no release)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)

for i in range(40):											#move cursor within 
	x = int(1000)											#two points repeatedly
	y = int(300+i)
	win32api.SetCursorPos((x,y))
	time.sleep(.1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)		#release left mouse button

# SCREENSHOT OF SPECIFIC VIEWPORT ///////////////////////////////////////////////////////////////////////

screenshot = ImageGrab.grab(bbox) 							#save part of screen capture
screenshot.save("sc2.png", "PNG")

# FULLSCREEN SCREENSHOT /////////////////////////////////////////////////////////////////////////////////

ImageGrab.grab().save("sc3.png", "PNG")

# RESIZE WINDOW /////////////////////////////////////////////////////////////////////////////////////////

win32gui.MoveWindow(PyHandle, 0, 0, 800, 600, True)
time.sleep(3)

# FULLSCREEN SCREENSHOT /////////////////////////////////////////////////////////////////////////////////

ImageGrab.grab().save("sc4.png", "PNG")

# CREATE SAVE STATE /////////////////////////////////////////////////////////////////////////////////////

win32api.SetCursorPos((400,180)) 					
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)

for i in range(400):										#scrolling to right
	x = int(400+i)				
	y = int(180)	
	win32api.SetCursorPos((x,y))
	time.sleep(.01)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	
win32api.SetCursorPos((680,130)) 							#clicking on save state button
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

win32api.SetCursorPos((680,250)) 							#double clicking into textbox
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(.5)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)		
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)		
time.sleep(1)
win32com.client.Dispatch("WScript.Shell").SendKeys('st1')	#Typing st1 into textbox
time.sleep(1)

win32api.SetCursorPos((750,410)) 							# Clicking on Save Button
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)

# SCREENSHOT ABOUT SERIES LIST ///////////////////////////////////////////////////////////////////////////

win32gui.MoveWindow(PyHandle, 0, 0, 1280, 1024, True)		#resize to specified resolution
			
win32api.SetCursorPos((200,35))								#Selecting Worklist Browser	
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)

X1 = 825													#coordinates of series list window
Y1 = 55
X2 = 1270
Y2 = 395

bbox = (X1,Y1,X2,Y2)										#parameters for series list windows
screenshot = ImageGrab.grab(bbox) 							#save part of screen capture
screenshot.save("sc5.png", "PNG")							
time.sleep(1)

################################################### END OF SCRIPT ########################################


