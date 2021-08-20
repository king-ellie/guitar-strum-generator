def strum_generator():
    import random

    # 1) create two lists of ('D', '+') and ('U', '+')

    downlist = ('D ', '+ ')
    uplist = ('U ', '+ ')

    # 2) create empty list to fill with strumming pattern

    strummingpattern = ''
    strummingpattern2 = ''
    
    # 3) while loop, while count >17 insert strum alternating from up and down buckets

    for slot in range(4):
        strummingpattern = strummingpattern + random.choice(downlist)
        strummingpattern = strummingpattern + random.choice(uplist)

    for slot in range(4):
        strummingpattern2 = strummingpattern2 + random.choice(downlist)
        strummingpattern2 = strummingpattern2 + random.choice(uplist)

    # 4) print strumming list

    print(strummingpattern)
    print(strummingpattern2)


if __name__ == '__main__':
    print ("Time to practice strumming, you little rockstar, you.\n...")
    strum_generator()