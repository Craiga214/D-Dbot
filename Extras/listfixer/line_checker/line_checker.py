#Grabbing all text from csv file
fin = open('spell_list5.csv', 'r')
count = 0
for line in fin:
    count = count + 1
    if count == 205:
        print(line)
fin.close()
