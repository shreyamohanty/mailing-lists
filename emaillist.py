rawemails = open('C:/Users/Shreya Mohanty/Documents/UC Berkeley/Voyager/Spring 2019 Recruitment/rawemails.txt', 'r')
emaillist = open('C:/Users/Shreya Mohanty/Documents/UC Berkeley/Voyager/Spring 2019 Recruitment/emaillist.txt', 'w')

elist = rawemails.read()

for item in elist.split(','):
    emaillist.write(item + '\n')

rawemails.close()
emaillist.close()
