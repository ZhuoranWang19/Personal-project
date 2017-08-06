SeaValue = {'empty': 0 , 'shell': 3, 'sardine': 6 , 'garrupa': 12, 'shark': 25, 'dolphin': 50, 'whale': 100}

myBucket = ['empty']

bucket = []

myWallet = [0]

EmptyNumber = []
Empty1 = ['empty', 'empty']
Empty2 = ['empty', 'empty']
n = 24
while n > 0 :
     Empty1 [0:0] = Empty2
     n = n - 1
EmptyNumber = Empty1

ShellNumber = []
Shell1 = ['shell', 'shell']
Shell2 = ['shell', 'shell']
n = 11
while n > 0 :
     Shell1 [0:0] = Shell2
     n = n - 1
ShellNumber = Shell1 + ['shell']

SardineNumber = []
Sardine1 = ['sardine', 'sardine']
Sardine2 = ['sardine', 'sardine']
n = 5
while n > 0 :
     Sardine1 [0:0] = Sardine2
     n = n - 1
SardineNumber = Sardine1 + ['sardine']

GarrupaNumber = []
Garrupa1 = ['garrupa', 'garrupa']
Garrupa2 = ['garrupa', 'garrupa']
n = 2
while n > 0 :
     Garrupa1 [0:0] = Garrupa2
     n = n - 1
GarrupaNumber = Garrupa1

SharkNumber = ['shark', 'shark', 'shark']

DolphinNumber = ['dolphin', 'dolphin']

WhaleNumber = ['whale']

SeaValue = EmptyNumber + SardineNumber + SharkNumber + ShellNumber + DolphinNumber + WhaleNumber + GarrupaNumber

def fishingOut(n):
    if SeaValue[n] == 'empty':
        return 'empty'
    else:
        return SeaValue[n]

def randomSwim(n):
    if 0 <= n <= 50:
        return 2*n - 2
    elif n <= 100:
        return n/2 + 2

def sellFish(str):
     if str == 'empty':
        myWallet[0] += 0
     elif str == 'shell':
        myWallet[0] += 3
     elif str == 'sardine':
        myWallet[0] += 6
     elif str == 'garrupa':
        myWallet[0] += 12
     elif str == 'shark':
        myWallet[0] += 25
     elif str == 'dolphin':
        myWallet[0] += 50
     elif str == 'whale':
        myWallet[0] += 100
     else:
        myWallet[0] += 0

def Imfishing():
    n = 0
    action = raw_input('You want to: ')
    number = int(raw_input('How far you want to throw: '))
    while n <= 100:
        n += 1
        if action == 'Fish':
         print "You just got:", fishingOut(randomSwim(number))
         myBucket.append(fishingOut(randomSwim(number)))
         return Imfishing()
        elif action == 'Check wallet':
         print myWallet
         return Imfishing()
        elif action == 'Check bucket':
         print myBucket
         return Imfishing()
        elif action == 'Sell':
         map(sellFish, myBucket)
         myBucket.remove(fishingOut(randomSwim(number)))
         print myWallet
         return Imfishing()
        else:
         print 'You can only make oder: Check bucket/Fish/Sell/Check wallet'
         return Imfishing()

Imfishing()
