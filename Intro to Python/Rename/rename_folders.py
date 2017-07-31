import os


def rename_files():
	files = os.listdir("/Users/mute/Desktop/college/2017Summer/Intro to Python/Rename/prank")
	print os.getcwd()
	os.chdir("/Users/mute/Desktop/college/2017Summer/Intro to Python/Rename/prank")
	for e in files:
		os.rename(e, e.translate(None, "0123456789"))
	print files
rename_files()