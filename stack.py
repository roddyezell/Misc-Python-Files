from pythonds.basic.stack import Stack

def revstring(mystr):
    s = Stack()
    r = []
    for i in mystr:
        s.push(i)
    while s.isEmpty() != True:
        r.append(s.pop())
    return "".join(r)
        
again = True

while again == True:
    word = input("Give me a word: ")

    backitup = input("Want to see " + word + " in reverse? (Y/N): ")

    if backitup == 'Y' or backitup == 'y' or backitup == 'sure':
        rword = revstring(word)
        print(rword)
        goagain = input("Wanna go again? (Y/N): ")
        if goagain == 'Y' or goagain == 'y' or goagain == 'sure':
            again = True
        else:
            print("Then we're done here.")
            again = False
    else:
        print("Then we're done here.")
        again = False
