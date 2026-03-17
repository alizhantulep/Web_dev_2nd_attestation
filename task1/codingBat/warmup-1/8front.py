def front_back(str):
    if(len(str)==1 or len(str)==0):
        return str
    new_str =""
    new_str=str[len(str)-1]
    for i in range (1,len(str)-1):
        new_str = new_str + str[i]

    new_str = new_str + str[0]
    return new_str

