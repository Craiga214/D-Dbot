import os
#For all items in the game
def itemGather():
    #Grabbing all text from csv file
    fin = open('.\\cogs\\Processes\\item_storage\\item_list.csv', 'r')
    file = fin.read().split('\n')
    
    #Creating hashmap to hold items with names as keys
    itemDict = dict()
    catNames = file[0].split('&')
    #There are 1330 items in the game so we need that many lines
    for i in range (1, len(file)):
        line = file[i].split('&')
        tempDict = dict()
        #split by the catagory names thereafter
        for j in range (0, len(catNames)):
            if line[j] != None:
                tempDict[catNames[j]] = line[j]
        
        #Fill the line of names into itemdict 484 times
        itemDict[line[0]] = tempDict
    #Returns to item_shop to be held in memory
    fin.close()
    return itemDict

#For all items in a given player inventory----------------------------------------------------------------------------------------
def invGather(fileName):
    #Grabbing all text from csv file
    fin = open(f'.\\cogs\\Processes\\item_storage\\{fileName}', 'r')
    file = fin.read().split('\n')
    #Creating hashmap to hold items with names as keys
    itemDict = dict()
    catNames = file[0].split('&')
    #Simply get as many lines as there are items
    for i in range (1, len(file)):
        line = file[i].split('&')
        tempDict = dict()
        #split by the catagory names thereafter
        for j in range (0, len(catNames)):
            tempDict[catNames[j]] = line[j]
        #Fill the line of names into itemdict 
        itemDict[line[0]] = tempDict
    #Returns to item_shop to be held in memory
    fin.close()
    return itemDict

#Add an item to a dict----------------------------------------------------------------------------------------
def addItem(itemDict, qty, item):
    flag = True
    #Adds on the qty if the item exists
    for i in range (0, len(itemDict)):
        if itemDict[f'{i}']['Name'] == item:
            itemDict[f'{i}']['Qty'] = str(int(itemDict[f'{i}']['Qty']) + qty)
            flag = False
            break
    #If the item DNE, add it to page
    if flag:
        tempDict = dict()
        print(f'Adding item: {item}')
        tempDict['Index'] = str(len(itemDict))
        tempDict['Name'] = item
        tempDict['Qty'] = str(qty)
        itemDict[f'{len(itemDict)}'] =  tempDict
    return itemDict

#Print the hashmap to a file using csv format-------------------------------------------------------------------
def toFile(invDict, fileName):
    fileWrite = ''
    with open(f'.\\cogs\\Processes\\item_storage\\{fileName}', 'w') as file:
        if invDict != None:
            file.write('Index&Name&Qty\n')
            for i in range (len(invDict)):    
                fileWrite = fileWrite + invDict[f'{i}']['Index']+'&'+invDict[f'{i}']['Name']+'&'+invDict[f'{i}']['Qty']
                if len(invDict) != i+1:
                    fileWrite = fileWrite + '\n'
        else:
            file.write('Index&Name&Qty')
        file.write(fileWrite)

#A function to remove a specific element and readjust the entire dict
def removeItem(invDict, index):
    #Case if there is one item
    if len(invDict) == 1:
        invDict.pop(f'index', None)
        return
    #Return after deleting if the last element is removed
    if index == len(invDict)-1:
        invDict.pop(f'{index}', None)
        return invDict
    for i in range (index+1, len(invDict)):
        invDict[f'{i-1}']['Qty'] = invDict[f'{i}']['Qty']
        invDict[f'{i-1}']['Name'] = invDict[f'{i}']['Name']
    invDict.pop(f'{len(invDict)-1}', None)
    print(invDict)
    return invDict
#Erase a file---------------------------------------------------------------------------------------------------
def voidFile(fileName):
    os.remove(f'.\\cogs\\Processes\\item_storage\\{fileName}')
    print('File '+fileName+' removed')
    return