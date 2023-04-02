from General_Maths_Functions import intinator,math #Import from another file
#Also import math module from General_Math_Functions cause y not

print("Example input: 26,27,29") #Example input

if __name__ == "__main__":
    while True: #FOREVER!
        data = input("Enter data set, seperate by commas\n> ") #Input
        try:
            data = tuple(sorted(map(intinator,data.split(',')))) #What is happening?
        except:
            print("Invalid sequence, please enter a readable number sequence.For example: 1,2,7,3,0\n")
            continue #If invalid input, display message and restart loop
        data_length = len(data)
        data_sum = sum(data)

        print("\nNumber of data provided: ", data_length)
        print("Sum of all data provided: ", data_sum)

        mean = data_sum/data_length
        print(f"The Mean is: {intinator(mean)}")

        #kdata is placeholder value, just holds values for each operation
        kdata = max(data)-min(data) #kdata = range
        kdata = 1 if kdata == 0 else kdata        
        print(f"The Range is:",kdata)

        #amode is same as kdata's role
        amode = int(data_length/2) #amode = median
        print("The Median is:", intinator((data[amode]+data[amode-1])/2) if data_length % 2 == 0 else data[amode])

        #Standard Deviation
        kdata = 0
        for x in data: kdata += (x-mean)**2 #For each value, find the square of the x-mean
        print("Standard Deviation is",intinator(math.sqrt(kdata/data_length)))

        #IQR
        if data_length > 3:
            kdata = int((amode-1)/2)
            q1 = intinator((data[kdata]+data[kdata+1])/2) if data_length % 4 != 0 else data[kdata]
            kdata = int((data_length+kdata+1)/2)
            #Q2 aint working. Too lazy to fix
            q2 = intinator((data[kdata]+data[kdata+1])/2) if data_length % 4 != 0 else data[kdata]
            print("Q1 is:",q1)
        
        # print("IQR is: ",kdata)

        amode = {} #amode = mode
        for x in data:
            if x not in amode:
                amode[x] = 1
            else:
                amode[x] += 1
        print("The Mode is:", max(amode,key=amode.get))
        
        print(
    f"""Frequency Table:
x   |   f""")
        for x,y in zip(amode.keys(),amode.values()):
            print(f"{x}   |   {y}")
        print()