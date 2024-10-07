# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class triple:
    def __init__(self, a, b, c):
        self.p1 = a
        self.p2 = b
        self.p3 = c


list1 = ['abc', 'abd', 'abe', 'abf', 'cad', 'cae', 'caf', 'dae', 'daf', 'eaf',
         'bcd', 'cbe', 'cbf', 'dbe', 'dbf', 'bef', 'cde', 'cdf', 'ecf', 'edf']
list2 = ['123', '214', '125', '126', '314', '135', '136', '415', '146', '516',
         '234', '235', '236', '425', '426', '526', '435', '436', '356', '546']

class postri():
    def __int__(self):
        pass

    def getpntset(self, trilist):
        # get list of all points
        allpnts = []
        for tri in trilist:
            for a in tri:
                if a not in allpnts:
                    allpnts.append(a)
        return allpnts



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tempobj = postri()
    print(tempobj.getpntset(list1))
    print(tempobj.getpntset(list2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
