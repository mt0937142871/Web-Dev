import webbrowser
import time

i = 0
while i < 3:
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=qIF8xvSA0Gw", 1, True)
	i += 1
