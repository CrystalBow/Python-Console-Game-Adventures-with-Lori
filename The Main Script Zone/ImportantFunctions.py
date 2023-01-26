def inputAndCheck(question, validAwnsers): # validAwnsers must be a list
	awnserString = input(question)
	validaty = False
	convertedAwnser = 0
	awnserFlag = False
	try:
		int(awnserString)
		validaty = True
	except ValueError:
		pass
	if validaty == False:
		return inputAndCheck(question, validAwnsers)
	else:
		convertedAwnser = int(awnserString)
		for awnser in validAwnsers:
			if convertedAwnser == awnser:
				awnserFlag = True
			else:
				continue
		if awnserFlag == False:
			return inputAndCheck(question, validAwnsers)
		else:
			return convertedAwnser