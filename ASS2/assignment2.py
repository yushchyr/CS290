#Roman yushchyk
print("Liquid Resistor test")
print("We will examine a new same for each new concentration of salt.")
print("Make sure to start the first cycle before adding any salt")
print("Please Begin Your Experiment by placing two Electrodes Into a Cup of a Distilled Water")

# Function that scan Serial
def scan():
    import serial as s
    import time as t
    ser = s.Serial('/dev/ttyACM0')
    print("Energia is connected at: " + ser.name)
    dataSetIndaex = 1
    sampleIndex = 1
    thefile = open('Data[1].txt', 'w')
    for x in range(0, 32):
        data = str(ser.readline().strip()) 
        if data!='' and data!='/r' and data!='/n' and len(data)>=4:
            if(sampleIndex == 1):
                print("Trial One - Distilled water - NO salt")
                input("Press Enter to begin!")
                print("Data Set 1")
                print("Sample# 1")
                sampleIndex = 2
            else:
                sampleIndex += 1
            print("Data Set " + str(dataSetIndaex))
            print("Sample# " + str(sampleIndex))
            print(data)
            thefile.write(data)
            t.sleep(1)
    thefile.close()
    ser.close()

# Function Call
scan()


