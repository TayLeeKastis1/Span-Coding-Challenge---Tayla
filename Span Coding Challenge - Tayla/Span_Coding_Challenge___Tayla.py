# Imports
from Calc_And_Display import *
from Extract_Text_File import *

# Run function to fetch text file data from Extract_Text_File python file
modifiedInputList = extract_text_file()

###INITIATE RANKING###

# Output welcome message and score data for confirmation
print('Welcome to the Arbitrary League Ranking System!\n\nBelow are the recieved game scores, please confirm that the information is correct.\n')

i = 0
while i < len(modifiedInputList):
  print(modifiedInputList[i])
  i = i + 1

# Request confirmation of score data from user
userConfirmation = ''
	
while userConfirmation != 'Y' or userConfirmation != 'N':
	userConfirmation = input('\nPlease enter "Y" to confirm that the scores above are correct or "N" if they are incorrect:') 

	if userConfirmation == 'Y':
		print('\nGreat! Please hold while we calculate the ranks')
		# Run function to calculate and display ranks from Calc_And_Display python file 
		calc_and_display(modifiedInputList)
		break
	elif userConfirmation == 'N':
		#print(userConfirmation)
		print('\nOh no ! We cannot calculate the league rankings without the correct scores. Please provide the correct file prior to executing this system.')
		break
###END INITIATE RANKING###


