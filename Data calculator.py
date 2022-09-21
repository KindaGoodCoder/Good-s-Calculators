from General_Maths_Functions import intinator #Import from another file

print("Example input: 26,27,29") #Example input

while True: #FOREVER!
    data = input("Enter data set, seperate by commas ").strip() #Input
    try:
        data = sorted(tuple(map(intinator,map(float,data.split(','))))) #What is happening?
    except:
        print("Invalid sequence, please enter a readable number sequence.For example: 1,2,7,3,0\n")
        continue #If invalid input, display message and restart loop
    data_length = len(data) 
    data_sum = sum(data)

    print("Number of data provided: ", data_length)
    print("Sum of all data provided: ", data_sum)

    print("The Mean is: ",intinator(round(data_sum/data_length,2)))

    kdata = round(max(data)-min(data),2) #kdata = range
    if kdata == 0:
        kdata = 1
    print("The Range is: ",kdata)

    amode = int(data_length/2) #amode = median
    if data_length % 2 == 0:
        kdata = intinator((data[amode]+data[amode-1])/2)
    else:
        kdata = data[amode]
    print("The Median is: ", kdata)

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
    kdata = tuple(amode.keys())
    values = tuple(amode.values())
    for x in range(0,len(amode)):
        print(f"{kdata[x]}   |   {values[x]}")
    print()
