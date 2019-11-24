import random, math
helptext = """Enter dice in standard format (d6, 2d4 + 2) to roll dice.
Can be used as simple calculator (2 + 4).
Separate all inputs with a space (2d4 + 2 / 3).
All numbers are rounded down (2/3 = 0).
p/prev: use previous input as input.
m/multi: roll multiple rolls. The number of rolls must be provided.
a/avg: get the average (as per DND rules) for the roll.
h/help: show this help text.
k/kill: kill the program.
"""
def roll(d):
	return random.randint(1,d)
tokens=[""]
detail=""
rolled=[]
def calculate(pos):
	global detail
	if pos == (len(tokens)):
		return math.floor(int(eval("".join(rolled))))
	if ('d' in tokens[pos] and tokens[pos][0] != "d"):
		c = tokens[pos].split("d")
		c = [int(x) for x in c]
		r = 0
		d = ""
		for x in range(c[0]):
			rr = roll(c[1])
			r += rr
			d += str(rr) + (" + " if (x + 1) < c[0] else "")
		rolled[pos] = str(r)
		detail += "(" + d + ") "
	elif tokens[pos][0] != "d":
		if (tokens[pos] != "+") & (tokens[pos] != "-") & (tokens[pos] != "/") & (tokens[pos] != "*") & (tokens[pos] != "(") & (tokens[pos] != ")"):
			if (tokens[pos].isdigit()):
				detail += tokens[pos] + " "
			else: 
				print("\"%\" is not a valid operator"%(tokens[pos]))
				exit()
		else:
			detail += tokens[pos] + " "
	else:
		r = roll(int(tokens[pos][1:]))
		rolled[pos] = str(r)
		detail += str(r) + " "
	return calculate(pos+1)
def average(pos):
	if pos == (len(tokens)):
		return math.floor(int(eval("".join(rolled))))
	if ('d' in tokens[pos] and tokens[pos][0] != "d"):
		c = tokens[pos].split("d")
		c = [int(x) for x in c]
		rolled[pos] = str(c[0] * (c[1] / 2))
	elif tokens[pos][0] != "d":
		if (tokens[pos] != "+") & (tokens[pos] != "-") & (tokens[pos] != "/") & (tokens[pos] != "*") & (tokens[pos] != "(") & (tokens[pos] != ")"):
			if (tokens[pos].isdigit()): 
				rolled[pos] = str(int(tokens[pos]) / 2)
			else:
				print("\"%\" is not a valid operator"%(tokens[pos]))
				exit()
	else:
		rolled[pos] = str(int(tokens[pos][1:]) / 2)
	return average(pos+1)
p=[]
print(helptext)
while (True):
	tokens = input("dice (seperate with spaces): ").split(" ")
	tokens = [x.lower() for x in tokens]
	if (tokens[0] == "prev" or tokens[0] == "p"):
		if (len(p) == 0):
			print("No previous input.")
			continue
		tokens = [x for x in p]
		detail = ""
		rolled = [x for x in tokens]
		print(str(calculate(0)))
		print("Individual rolls: " + detail)
		continue
	elif (tokens[0] == "kill" or tokens[0] == "k"):
		break
	elif (tokens[0] == "multi" or tokens[0] == "m"):
		if (len(tokens) < 2):
			print("Missing second argument: number of rolls")
			continue
		m = int(tokens[1])
		tokens = input("dice (seperate with spaces): ").split(" ")
		tokens = [x.lower() for x in tokens]
		if (tokens[0] == "prev" or tokens[0] == "p"):
			if (len(p) == 0):
				print("No previous input.")
				continue
			tokens = [x for x in p]
			for _ in range(m):
				detail = ""
				rolled = [x for x in tokens]
				print(str(calculate(0)))
				print("Individual rolls: " + detail)
			continue	
		p = [x for x in tokens]
		for _ in range(m):
			detail = ""
			rolled = [x for x in tokens]
			print(str(calculate(0)))
			print("Individual rolls: " + detail)
		continue
	elif (tokens[0] == "avg" or tokens[0] == "a"):
		tokens = input("dice (seperate with spaces): ").split(" ")
		tokens = [x.lower() for x in tokens]
		if (tokens[0] == "prev" or tokens[0] == "p"):
			if (len(p) == 0):
				print("No previous input.")
				continue
			tokens = [x for x in p]
			rolled = [x for x in tokens]
			print("Average roll: " + str(average(0)))
			continue	
		p = [x for x in tokens]
		rolled = [x for x in tokens]
		print("Average roll: " + str(average(0)))
		continue
	elif (tokens[0] == "help" or tokens[0] == "h"):
		print(helptext)
		continue
	p = [x for x in tokens]
	detail = ""
	rolled = [x for x in tokens]
	print(str(calculate(0)))
	print("Individual rolls: " + detail)