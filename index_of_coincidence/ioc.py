"""
author: Rudresh Pandit
        

description: Program to find index of coincidence for key length 2-10
            and sort them in ascending order
"""


def execute():

    text = input("enter the text")
    text = list(text)
    db = []
    for a in range(2, 11):
        temp = []
        for i in range(a):
            data = text[i::a]
            temp.append(indexOfCoi(data))
        db.append(temp)

    for count in range(len(db)):
        tp2 = db[count]
        tp2.sort()
        print("For key length",len(tp2), tp2)


def indexOfCoi(data):
    '''
    Function which returns index of coincidence for any given data
    :param data: cipherext
    :return: index of coincidence
    '''
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabets = list(alphabets)

    count = []
    term = 0

    for i in range(len(alphabets)):
        count.append(data.count(alphabets[i]))

    for j in range(len(count)):
        term = term + (count[j] * (count[j] - 1))

    term = term / (len(data) * (len(data) - 1))
    return term


def main():
    execute()


if __name__ == "__main__":
    main()
