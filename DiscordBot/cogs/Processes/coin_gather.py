def coinGather(fileName):
    #Grabbing all text from csv file
    fin = open(f'.\\cogs\\Processes\\item_storage\\{fileName}', 'r')
    file = fin.read().split('\n')
    
    #Creating hashmap to hold items with names as keys
    coinDict = dict()
    catNames = file[0].split('&')
    #There are 1330 items in the game so we need that many lines
    for i in range (0, 4):
        line = file[1].split('&')
        #Fill the line of names into coinDict
        coinDict[f'{catNames[i]}'] = line[i]
    #Returns to item_shop to be held in memory
    fin.close()
    return coinDict

def coinToFile(fileName, coinDict):
    fileWrite = ''
    with open(f'.\\cogs\\Processes\\item_storage\\{fileName}', 'w') as file:
        file.write('cp&sp&gp&pp\n')
        fileWrite = fileWrite + coinDict['cp']+'&'+coinDict['sp'] +'&'+ coinDict['gp']+'&'+coinDict['pp']
        file.write(fileWrite)
