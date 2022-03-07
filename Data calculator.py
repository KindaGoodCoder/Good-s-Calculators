from General_Maths_Functions import intinator
def repeater(length):
    return ''.join([' ' for _ in range(0,length)])
while True:
    data = input("Enter data set, seperate by commas\nLike 24,27,26 ").strip()
    try:
        data = sorted(tuple(map(float,data.split(','))))
    except:
        print("Invalid sequence, please enter a readable number sequence.For example: 1,2,7,3,0\n")
        continue
    print("\nThe Mean is: ",intinator(round(sum(data)/len(data),2)))
    kdata = intinator(round(max(data)-min(data),2))
    if kdata == 0:
        kdata = intinator(data[0])
    print("The Range is: ",kdata)
    amode = int(len(data)/2)
    if len(data)%2 == 0:
        kdata = (data[amode]+data[amode-1])/2
    else:
        kdata = data[amode]
    print("The Median is: ", intinator(kdata))
    amode = {}
    spaced = space = len(max([str(int(x)) for x in data],key=len))
    space = space/2
    if space % 2 != 0:
        space2 = int(space/2) + 2
    else:
        space2 = space
    space2 = repeater(int(space2)+1)
    space = repeater(int(space)+1)
    for x in data:
        x = intinator(x)
        if x not in amode:
            amode[x] = 1
        else:
            amode[x] += 1
    print("The Mode is:", max(amode,key=amode.get))
    print("Number of data provided: ", len(data))
    print("Sum of all data provided: ", intinator(sum(data)))
    print(f"""Frequency Table:
{space}x{space2}|   f""")
    keys = list(amode.keys())
    values = list(amode.values())
    for x in range(0,len(amode)):
        y= repeater(spaced - len(str(keys[x])))
        if len(str(x)) % 2 == 0 or spaced <= 2:
            y+=' '
        print(f"{y}{keys[x]}   |   {values[x]}")
    print()
