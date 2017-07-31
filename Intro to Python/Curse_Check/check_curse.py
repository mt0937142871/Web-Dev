import urllib

def read_text():
	quotes = open("/Users/mute/Desktop/college/2017Summer/Intro to Python/Curse_Check/movie_quotes.txt")
	content = quotes.read()
	# print content
	check_profanity(content)
	quotes.close()

def check_profanity(text):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
	output = connection.read()
	if output == "true":
		print("Profanity Alert !!!!")
	else:
		print("This file is safe")

	connection.close()

read_text()
