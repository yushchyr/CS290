#Roman yushchyk
print("\n\n")
print("Liquid Resistor test")
print("We will create a new data set for each concentration of salt.")
print("Make sure to start the first cycle before adding any salt!")
print("Please Begin Your Experiment by placing two Electrodes Into a Cup of a Distilled Water")
print("\n\n")

# Test scope and size settings
import serial as s # Iport Serial 
ser = s.Serial('/dev/ttyACM1') # Open Serial port
print("Good news!")
print("Energia is connected at: " + ser.name) # Greating
print("\n\n")
sampleTrialNumber = int(input("Enter a number of Trials (Measured concentration of salt) in this Test: ")) # To set number of data points 
sampleNumberPerTrial = int(input("Enetr number of sample's per each Trial: ")) # To manipulate data sample's size
dataSetIndex = 1    # Reset data set counter
dataSubSetIndex = 1 # Reset sample size counter 

thefile = open('Data.txt', 'w') # Creating/rewriting a new file

# Function that scan Serial
def scan(): # Serial sacn function prototype
    # Data formating method
    data = str(ser.readline()) # Store serial data into the string  called data
    data = data.strip('b') # Strip string of file type
    data = data.strip("'") # Strip data of string characters
    data = data.strip('\\r\\n') # Strip data of the row and line endings
    data = data.strip('') # Strip data of any emty spaces
    
    if len(data)>=3: # If data lenght is greater or equal 3 characters
        print(data)  # Print data on the screen
        thefile.write(data) # Write data to the file
        thefile.write(",")  # Write a comma after each separated data reading
    else: # In case we recieved partial or broken bit date over Serial communication port
        scan() # Go back and sick next valid data scan
# The end of scan function

# Programm execution routine         
for y in range (0, sampleTrialNumber): # Reapeat for number of trials  
    print("\n") # Prints empty space before each data trial
    print("Data set: " + str(dataSetIndex)) # Printing Data set nuber on a screen
    dataSetIndex += 1 # Incrementing data set index by 1
    thefile.write('\n') # Write a new line character to the file named thefile
  
    for x in range (0,sampleNumberPerTrial): # Reapeat for nuber of samples in each trial
        print("Scan run: " + str(dataSubSetIndex)) # Print data sample number before each value 
        dataSubSetIndex += 1 # Increment sample nuber by 1
        scan() # Perform Serial scan function
    dataSubSetIndex = 1 # Re-set sample counter 
        
sampleTrialNumber = 1 # Re-set trial  counter
thefile.close() # Close the file
# End of the program 

### Error Bar

#import matplotlib.pyplot as plt
#x=[200,300, 400, 500, 600, 700, 800, 900]
#y=[1.1, 1.5, 1.9, 2.8, 3.4, 3.5, 4.6, 5.4]
#ey =[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,]
#plt.errorbar(x,y,yerr=ey, fmt='0') 
#plt.plot([0,1000], [0, 5.5], 'k-','lw=2')
#plt.show

###
