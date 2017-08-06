iniPhonenumber = list(input("What is the pin you want to encrypt:"))

list1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
list2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[']
list3 = [']', '[', '{', '}', '|', '=', '+', '_', '-', 'z']
list4 = ['x', 'c', 'v', 'b', 'n', 'm', ',', '?', 'Q', 'W']
list5 = ['E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S']
list6 = ['D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C']
list7 = ['V', 'B', 'N', 'M', '<', '>', '!', '@', '#', '$']
list8 = ['%', '^', '^', '&', '*', '(', ')', '~', '`', ':']
list9 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list10= ['Aa', 'Ss', 'Ee', 'Tt', 'Ll', 'Oo', 'Pp', 'Kk', 'Gg', 'Cc']

encryptionList = [list1, list2, list3, list4, list5, list6, list7, list8, list9, list10]


def encryption(list):
    if len(list) != 6:
        return "Your pin have to be 6 numbers"
    else:
        return encryptMore(list)

def encryptMore(list):
    return [encrypt1(list) + encrypt2(list) + encrypt3(list) + encrypt4(list) + encrypt5(list) + encrypt6(list)]

def encrypt1(list):
    encrypt1List = encryptionList[int(list[0])]
    return encrypt1List[int(list[1])]

def encrypt2(list):
    encrypt2List = encryptionList[int(list[1])]
    return encrypt2List[int(list[2])]

def encrypt3(list):
    encrypt3List = encryptionList[int(list[2])]
    return encrypt3List[int(list[3])]

def encrypt4(list):
    encrypt4List = encryptionList[int(list[3])]
    return encrypt4List[int(list[4])]

def encrypt5(list):
    encrypt5List = encryptionList[int(list[4])]
    return encrypt5List[int(list[5])]

def encrypt6(list):
    encrypt6List = encryptionList[int(list[5])]
    return encrypt6List[int(list[0])]

print (encryption(iniPhonenumber))