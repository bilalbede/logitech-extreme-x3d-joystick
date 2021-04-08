from inputs import get_gamepad

throttleState = 0
xState = 0
yState = 0
hatXState = 0
hatYState = 0
twistState = 0
triggerState = 0

# Returns whether or not x is within n of y
def withinNOf(x, n, y):
	if x in range(n-y, n+y):
		return True
	else:
		return False

def getStickPosition(centreAssist=True, centreAssistSens=10, edgeAssist = True, edgeAssistSens=5):
	xPos = xState - 512
	yPos = (yState - 512) * -1

	# Snap the position to the centre if close enough
	if centreAssist == True:
		if withinNOf(xPos, 0, centreAssistSens):
			xPos = 0
		if withinNOf(yPos, 0, centreAssistSens):
			yPos = 0
	
	# Snap the position to the edge if close enough
	if edgeAssist == True:
		if withinNOf(xPos, 512, edgeAssistSens):
			xPos = 512
		if withinNOf(yPos, 512, edgeAssistSens):
			yPos = 512
		if withinNOf(xPos, -512, edgeAssistSens):
			xPos = -512
		if withinNOf(yPos, -512, edgeAssistSens):
			yPos = -512

	return (xPos, yPos)	

def getHatPosition():
	return (hatXState, hatYState * -1)

def getTwistPosition(centreAssist = True, centreAssistSens = 2, edgeAssist = True, edgeAssistSens = 1):
	twistPos = twistState - 128

	# Snap the position to the centre if close enough
	if centreAssist == True:
		if withinNOf(twistPos, 0, centreAssistSens):
			twistPos = 0
	
	# Snap the position to the edge if close enough
	if edgeAssist == True:
		if withinNOf(twistPos, 128, edgeAssistSens):
			twistPos = 128
		if withinNOf(twistPos, -128, edgeAssistSens):
			twistPos = -128
	return twistPos

while True:
	events = get_gamepad()
	for event in events:
		if event.ev_type == "Absolute":
			# Update the throttle state
			if event.code == "ABS_THROTTLE":
				throttleState = int(event.state)
			# Update the X and Y axes
			elif event.code == "ABS_X":
				xState = int(event.state)
			elif event.code == "ABS_Y":
				yState = int(event.state)
			elif event.code == "ABS_HAT0X":
				hatXState = int(event.state)
			elif event.code == "ABS_HAT0Y":
				hatYState = int(event.state)
			elif event.code == "ABS_RZ":
				twistState = int(event.state)
		elif event.ev_type == "Key":
			if event.code == "BTN_TRIGGER":
				triggerState = int(event.state)


