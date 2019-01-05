rawnames = open('C:/Users/Shreya Mohanty/Documents/UC Berkeley/Voyager/Spring 2019 Recruitment/rawnames.txt', 'r')
namelist = open('C:/Users/Shreya Mohanty/Documents/UC Berkeley/Voyager/Spring 2019 Recruitment/namelist.txt', 'w')

while True:
    name = rawnames.readline()
    namelist.write(name)
    
    temp = rawnames.readline()
    temp = rawnames.readline()
    temp = rawnames.readline()
    temp = rawnames.readline()
    temp = rawnames.readline()
    
    if name == '':
        break
rawnames.close()
namelist.close() 
     