#Grabbing all text from csv file
fin = open('Items.csv', 'r')
fout = open('ItemsList.csv', 'w')

for line in fin:
    if 'Name&Source' in line:
        fout.write(line)
        continue
    line = line.replace('""', '"---"')
    line = line.replace('","', '&')
    line = line.replace('"', '')
    fout.write(line)





#Fixing old shit
#fin = open('spell_list5.csv', 'r')
#fout = open('spell_list7.csv', 'w')
#
#for line in fin:
#    if 'Name&Source' in line:
#        fout.write(line)
#        continue
#    line = line.replace('Concentration&', 'Concentration,')
#    line = line.replace(',"', '&"')
#    line = line.replace('"&"',' ')
#    if 'This spell\'s damage increases' in line or 'This spell\'s damage increases' in line or 'At Higher Levels.' in line:
#        line = line.replace('This spell\'s damage increases','&This spell\'s damage increases')
#        line = line.replace('The spell\'s damage increases','&This spell\'s damage increases')
#        line = line.replace('At Higher Levels.', '&At Higher Levels.')
#    else:
#        fout.write(line[:-1]+'&This spell does not scale'+'\n')
#        continue    
#    fout.write(line)
#fin.close()
#fout.close()
