#Roman yushchyk
print("Liquid Resistor test")
print("We will examine a new same for each new concentration of salt.")
print("Make sure to start the first cycle before adding any salt")
print("Please Begin Your Experiment by placing two Electrodes Into a Cup of a Distilled Water")
print("")
# Test scope and size settings

import serial as s # Iport Serial 
ser = s.Serial('/dev/ttyACM1') # Open Serial port
print("Energia is connected at: " + ser.name) # Greating

sampleTrialNumber = input("Enter number of Trials in this Test: ")
sampleNumberPerTrial = input("Enetr number of sample's per each Trial: ")
dataSetIndex = 1
thefile = open('Data.txt', 'w')



# Function that scan Serial
def scan(dataSetIndex):
    sampleIndex = 1
    thefile.write(str(dataSetIndex))
    thefile.write(',')
    dataSetIndex += 1
    return int(dataSetIndex)
    
# Function Call
for x in range(0,int(sampleTrialNumber)):
    dataSetIndex = scan(dataSetIndex)

thefile.close()
### Error Bar

#import matplotlib.pyplot as plt
#x=[200,300, 400, 500, 600, 700, 800, 900]
#y=[1.1, 1.5, 1.9, 2.8, 3.4, 3.5, 4.6, 5.4]
#ey =[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,]
#plt.errorbar(x,y,yerr=ey, fmt='0') 
#plt.plot([0,1000], [0, 5.5], 'k-','lw=2')
#plt.show

###