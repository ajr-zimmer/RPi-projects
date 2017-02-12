import pigpio
import csv
import sys
import time

#initialize the pi
pi = pigpio.pi() 
#set servo to 90 degrees
pi.set_servo_pulsewidth(17,1600)
time.sleep(1)
#empty dictonary that will hold stats from csv
stateVotes = {}
#read data from csv and hold in stateVotes
with open('Election2016.csv', 'rb') as csvfile:
    rowreader = csv.DictReader(csvfile)
    for row in rowreader:
        #print(row['State'])
        stateVotes[row['Code']] = (int(row['Dv']), int(row['Rv']), row['State'])

#program cycle
while True:
    #get users input (state code, 'genera', or 'quit')
    usrInput = raw_input("Enter a state abbreviation (e.g. CA) to show poll results for that state\nEnter 'general' to show distribution of electoral votes\nEnter 'quit' to end program\n>> ")
    usrInput = usrInput.upper()
    #when user enters quit, say bye, and turn off servo, then exit
    if (usrInput == 'QUIT'):
        print "Bye!"
        pi.set_servo_pulsewidth(17, 0);
        pi.stop()
        sys.exit()
    #when user types general, show results of general election by electoral votes. Adding one state at a time, by alphabetical order (including DC)
    elif (usrInput == 'GENERAL'):
        print "not right now m8"
        time.sleep(1) #one second delay so user input dialog isn't in your face
    #when user enters a state code (which is used as a key in the dictonary) look up the dem and rep votes of that state and calculate the degree to turn, then turn servo
    elif (usrInput in stateVotes):
        stateValues = stateVotes.get(usrInput)
        pulseWidth = 10.*(stateValues[0]*1./(stateValues[0]+stateValues[1])*180)+700
        pi.set_servo_pulsewidth(17, pulseWidth)
        time.sleep(0.005) #servo turn time
        time.sleep(1) #one second delay so user input dialog isn't in your face
    else:
        print "That is not a valid input!"