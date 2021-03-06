# Roman yushchyk
# 200368308
print("\n\n")
thefile = open('Data.txt', 'w') # Creating/rewriting a new file
print("Liquid Resistor test")
thefile.write("Liquid Resistor test" + '\n' + "Raw Data Collected:" + '\n\n')
print("We will create a new data set for each concentration of salt.")
print("Make sure to start the first cycle before adding any salt!")
print("Please Begin Your Experiment by placing two Electrodes Into a Cup of a Distilled Water")
print("\n\n")

# Test scope and size settings
import serial as s # Iport Serial 
ser = s.Serial('/dev/ttyACM0') # Open Serial port
print("Good news!")
print("Energia is connected at: " + ser.name) # Greating
print("\n\n")
sampleTrialNumber = int(input("Enter a number of Trials (Measured concentration of salt) in this Test: ")) # To set number of data points 
sampleNumberPerTrial = int(input("Enetr number of sample's per each Trial: ")) # To manipulate data sample's size
dataSetIndex = 1    # Reset data set counter
dataSubSetIndex = 1 # Reset sample size counter 
averageSum = [sampleTrialNumber]

# Function that scan Serial
def scan(dataSubSetIndex): # Serial sacn function prototype
    # Data formating method
    data = str(ser.readline()) # Store serial data into the string  called data
    data = data.strip('b') # Strip string of file type
    data = data.strip("'") # Strip data of string characters
    data = data.strip('\\r\\n') # Strip data of the row and line endings
    data = data.strip('') # Strip data of any emty spaces
    
    if len(data)>=3: # If data lenght is greater or equal to 3 characters
        print(data)  # Print data on the screen
        thefile.write(data) # Write data to the file 
        if(dataSubSetIndex != sampleNumberPerTrial): # If it is beatween trials
            thefile.write(",")  # Write a comma after each separated data reading
    else: # In case we recieved partial or broken bit date over Serial communication port data range is 0 - 1023
       scan(dataSubSetIndex) # Go back and sick next valid data scan
        
    dataSubSetIndex = dataSubSetIndex + 1 # Increment sample nuber by 1
    return dataSubSetIndex
    
# The end of scan function

# Data processing function
def find_Average():
    print("\n\n")
    # Specifiaclally do add a deatail "CONVERTING TO INTEGERS"
    dataSubSetIndex = 1
    print("Running average values: ")
    thefile = open('Data.txt', 'a+')
    thefile.write('\n\n' + "Running average values:" + '\n')
   
    
    for line in open('Data.txt', 'r+'):
        lineX = str(line)
        start = lineX.find('points: ') + 8
        if(lineX.find('points: ') != -1):
            integerString = (lineX[start:])
            integerString = [int(i) for i in integerString.split(',')]
            # Finds the running average
            sumOfIntegers = sum(integerString)
            averageSum = sumOfIntegers/sampleNumberPerTrial
            print("Running average of a point", dataSubSetIndex, ":" , averageSum)
            thefile.write("Running average of a point " + str(dataSubSetIndex) + ": " + str(averageSum) + '\n')
            dataSubSetIndex += 1
    thefile.close()
# End of the Data processing function

# Programm execution routine         
for y in range (0, sampleTrialNumber): # Reapeat for number of trials  
    print("\n") # Prints empty space before each data trial
    print("Data set: " + str(dataSetIndex)) # Printing Data set nuber on a screen
    if(dataSetIndex >= 2): # Skip new line character for the first data log
        thefile.write('\n') # Write a new line character to the file named thefile
        thefile.write("Point " + str(dataSetIndex) + ". Added salt: ")
        thefile.write(str(input("How much salt do you add? Give your answer in grams and milligrams! ")))
        thefile.write(" grams. ")
        thefile.write(" Processed data points: ")
    else: # in case it is the first or Zero data point
        thefile.write("Point 1. Added salt: 00 grams.  Processed data points: ")
    dataSetIndex += 1 # Incrementing data set index by 1  

    
    for x in range (0,sampleNumberPerTrial): # Reapeat for nuber of samples in each trial
        print("Scan run: " + str(dataSubSetIndex)) # Print data sample number before each value 
        dataSubSetIndex = scan(dataSubSetIndex) # Perform Serial scan function
    dataSubSetIndex = 1 # Re-set sample counter 
dataSetIndex = 1 # Re-set trial  counter
thefile.close() # Close the file
find_Average()
# End of the program 

#import matplotlib.pyplot as plt
#x=[200,300, 400, 500, 600, 700, 800, 900]
#y=[1.1, 1.5, 1.9, 2.8, 3.4, 3.5, 4.6, 5.4]
#ey =[0.1, 0.1, 0.1, 0.1, 0.1,0.1, 0.1, 0.1, 0.1,]
#plt.errorbar(x,y,yerr=ey, fmt='0') 
#plt.plot([0,1000], [0, 5.5], 'k-','lw=2')
#plt.sho
