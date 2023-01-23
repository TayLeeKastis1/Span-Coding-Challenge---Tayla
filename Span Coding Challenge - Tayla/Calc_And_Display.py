###CALCULATE SCORES###

# Get list of teams and scores from the text file information
def calc_and_display(modifiedInputList):

	scoresListByLine = []
	tempString = ''
	tempList = []
	
	for line in modifiedInputList:	
		tempString = line
		tempList = tempString.split(',')
	
		for item in tempList:
			scoresListByLine.append(item.strip());
		tempList.clear
		tempString = ''
	
	# Make final scores dictionary (elimiate duplicate teams and setup for scoring)
	finalRanksDict = {}
	
	for line in scoresListByLine:
		finalRanksDict.update({line[:-2]: 0})
	
	# Calculate ranking scores using: tie = 1 pt, win = 3 pts, loss = 0 pts
	totalScoresDone = 0
	i = 0;
	teamA = ''
	teamB = ''
	scoreA = 0
	scoreB = 0
	
	while totalScoresDone < len(scoresListByLine)/2:
		teamA = scoresListByLine[i][:-2]
		teamB = scoresListByLine[i+1][:-2]
		
		scoreA = scoresListByLine[i][-1]
		scoreB = scoresListByLine[i+1][-1]
	
		currentScoreA = 0
		currentScoreB = 0
		
		# Find teams in dictionary to tally scores 
		if(scoreA == scoreB):
			currentScoreA = finalRanksDict.get(teamA)
			currentScoreB = finalRanksDict.get(teamB)
	
			if(currentScoreA == None):
				currentScoreA = 0
	
			if(currentScoreB == None):
				currentScoreB = 0
		
	
			finalRanksDict.update({teamA: currentScoreA + 1})
			finalRanksDict.update({teamB: currentScoreB + 1})
	
		elif(scoreA > scoreB):
			currentScoreA = finalRanksDict.get(teamA)
			currentScoreB = finalRanksDict.get(teamB)
	
			finalRanksDict.update({teamA: currentScoreA + 3})	
	
		elif(scoreB > scoreA):
			currentScoreA = finalRanksDict.get(teamA)
			currentScoreB = finalRanksDict.get(teamB)
	
			finalRanksDict.update({teamB: currentScoreB + 3})
	
		i = i + 2
		totalScoresDone = totalScoresDone + 1
	
	###END CALCULATE SCORES###
	
	###DISPLAY RANKS###
	
	# Sorts by value then key
	sorted_test = sorted(finalRanksDict.items(), key=lambda k: (-k[1], k[0]))  
	
	print('\nThe teams are ranked as follows: \n')
	
	for item in sorted_test:
		if item[1] == 1:
			print(item[0] + ', ' + str(item[1]) + ' pt')
		elif item[1] != 1:
			print(item[0] + ', ' + str(item[1]) + ' pts')
	
	print('\nThank you for using the Arbitrary League Ranking System.\n')

###END DISPLAY RANKS###
