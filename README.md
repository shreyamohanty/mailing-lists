# mailing-lists
This program semi-automates the process of getting a list of students from a bCourses class and typing their names into gmail to find their Berkeley email addresses.

General Instructions:
1. Copy and paste all the students from the the people tab of a class into a text file. Make sure you are on the tab students. When pasted, you should usually see the students followed by some more lines (often repeated) of class data. Name the file 'rawnames.txt'.

2. Edit the 'namelist.py' program to fit your needs. Change the paths for the initial file open commands. Change the number of 'temp = ' commands to the number of lines between one name and the next when you copied the student list. Run the program and check the newly created 'namelist.txt' file. Sometimes a student may have had a different number of lines following their names, which messed up the order for all the following students. Find these problem people and remove them from the list. Rerun the program until you have a properly formatted list of names and then add the names of students you removed to the end.

3. Open up your Berkeley email account, click compose email, and splitscreen the tab with your Python environment. In the command line, type 'import pyautogui' (note: this is assuming you already have the package installed) and press enter. Type 'pyautogui.position()' and move your mouse to hover over the recipients part of your compose box. Press enter to run the command. Copy the coordinates into the click commands in the 'gmailtype.py' program. Run the program. Make sure to not move your mouse while the program is running, but if anything does go wrong, move your mouse to the upper left corner of the screen to stop the program. 

4. There will usually be some names whose emails were not found after the program has finished running. Manually fill those into your recicpients list on gmail. Copy and paste the entire list into a text file and name it 'rawemails.txt'.

5. Edit the 'emaillist.py' program to fit your needs. Change the paths for the initial file open commands. Check the newly created 'emaillist.txt' file. 

6. You can copy the email list into Excel and separate the names from emails by using the text-to-columns command and separating by the '<' character. 

Jonah Tang has improved the code for this task. His code can be found at https://github.com/jonahc-tang/canvas_data_pull?fbclid=IwAR1_g3r6fqemGV6i3PCgPxDl0ick4bjqbBLrCW4DK9I57bq95dRnhLcFHMg. 
