import win32com.client as win

# you can insert gaps in the narration by adding sleep calls
import time

speak = win.Dispatch("SAPI.SpVoice")
text = input("enter the text:")
speak.Speak(text)
time.sleep(3)
text = "This text is read after 3 seconds"
speak.Speak(text)

