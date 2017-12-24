from itertools import groupby
from catch_id import CatchID
from catch_friends import CatchFriends
import numpy as np
import matplotlib.pyplot as plt

def PrintSimpleGraph(listOfDates):
    newListOfDates = [elem for elem, _ in groupby(listOfDates)]
    for x in newListOfDates:
        num = listOfDates.count(x)
        a = ''.join("#" for x in range(0, num))
        print(str(x) + a)

def PrintGraph(listOfDates):
    # hist()
    fig = plt.figure()
    plt.hist(listOfDates)
    plt.title('Result histogramm')
    plt.grid(True)

    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()
    plt.show()


username = input()
user = CatchID(str(username))
#print(user.ID)

listOfFriends = CatchFriends(user.ID)
#print(listOfFriends.friends)

print('\n')
PrintSimpleGraph(listOfFriends.friends)
print('\n')
PrintGraph(listOfFriends.friends)
