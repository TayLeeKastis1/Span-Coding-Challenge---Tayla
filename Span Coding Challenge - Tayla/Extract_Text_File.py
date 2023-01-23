def extract_text_file():

	###TEXT FILE HANDLING###

	# Read text file and display input to user (maybe ask for confirmation on scores)

	# Variable declarations
	file = open('Input.txt', 'r')
	read = file.readlines()
	modifiedInputList = []
	userConfirmation = ''

	# Fetch data from text file
	for line in read:
		if line[-1] == '\n':
			modifiedInputList.append(line[:-1])
		else:
			modifiedInputList.append(line)

	return modifiedInputList

	###END TEXT FILE HANDLING###