def spellGather():
    #Grabbing all text from csv file
    file = open('.\\cogs\\Processes\\spell_storage\\spell_list.csv', 'r')
    file = file.read().split('\n')
    
    #Creating hashmap to hold spells with names as keys
    spellDict = dict()
    catNames = file[0].split('&')
    #There are 484 spells in the game so we need that many lines
    for i in range (1, 484):
        line = file[i].split('&')
        tempDict = dict()
        #split by the catagory names thereafter
        for j in range (0, len(catNames)):
            if line[j] != None:
                tempDict[catNames[j]] = line[j]
        
        #Fill the line of names into spelldict 484 times
        spellDict[line[0]] = tempDict
    #Returns to spellbook to be held in memory
    return spellDict
    
            



