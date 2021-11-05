# https://www.codewars.com/kata/52ed326b8df6540e06000029/python


levels = [0,1,2,3]
buttons = ["0","1","2","3"]

def goto(level,button):
	if level not in levels and button not in buttons:
		return 0
	else:
		return int(button)- level


