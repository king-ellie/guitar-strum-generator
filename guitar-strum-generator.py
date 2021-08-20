def strum_generator():
    import random

    # 1) create two lists of ('D', '+') and ('U', '+')

    downlist = ('D ', '+ ')
    uplist = ('U ', '+ ')

    # 2) create empty list to fill with strumming pattern

    strummingpattern = ''
    strummingpattern2 = ''
    
    # 3) build both lines of the strumming pattern

    for slot in range(4):
        strummingpattern = strummingpattern + random.choice(downlist)
        strummingpattern = strummingpattern + random.choice(uplist)

    for slot in range(4):
        strummingpattern2 = strummingpattern2 + random.choice(downlist)
        strummingpattern2 = strummingpattern2 + random.choice(uplist)

    # 4) print full strumming pattern

    print(strummingpattern + "\n" + strummingpattern2 )

    # 5) ask if user wants another pattern

    user_another = raw_input("Press enter to generate another pattern, enter 'X' to exit: ")
    if user_another == ('X'):
        print("See you next time.")
    else:
        strum_generator()
    

if __name__ == '__main__':
    print ("Time to practice strumming, you little rockstar, you.\n")
    strum_generator()