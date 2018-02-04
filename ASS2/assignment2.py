#Roman yushchyk
print("Liquid Resistor test")
print("We will examine a new same for each new concentration of salt.")
print("Make sure to start the first cycle before adding any salt")
print("Please Begin Your Experiment by placing two Electrodes Into a Cup of a Distilled Water")

# Test scope and size settings
sampleTrialNumber = input("Enter number of Trials in this Test: ")
sampleNumberPerTrial = input("Enetr number of sample's per each Trial: ")

# Function that scan Serial
def scan():
    import serial as s # Iport Serial 
    import time as t # Import Time

    ser = s.Serial('/dev/ttyACM0') # Open Serial port
    print("Energia is connected at: " + ser.name) # Greating
    
    dataSetIndaex = 1
    sampleIndex = 1
    thefile = open('Data[1].txt', 'w')
    for x in range(0, int(sampleNumberPerTrial)):
        data = str(ser.readline().strip()) 
        if data!='' and data!='/r' and data!='/n' and len(data) <= 3:
            if(sampleIndex == 1 and dataSetIndaex == 1):
                print("Trial One - Distilled water - NO salt")
                input("Press Enter to begin!")
                print("Data Set " + str(dataSetIndaex))
                print("Sample# 1")
                print(data)
                thefile.write(str(data))
                sampleIndex = 2
            elif(sampleIndex >= sampleTrialNumber):
                print("You are all done! Let's do some math!")
                input("Please press Enter key...")
            else:
                sampleIndex += 1
            print("Data Set " + str(dataSetIndaex))
            print("Sample# " + str(sampleIndex))
            print(data)
            thefile.write(data)
            t.sleep(1)
            dataSetIndaex += 1
    thefile.close()
    ser.close()
    dataSetIndaex += 1

# Function Call
for x in range(0,int(sampleTrialNumber)):
    scan()

