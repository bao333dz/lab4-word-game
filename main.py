wtg = "banana"
def w(wtg):
    lives = 5
    lwtg = list(wtg)
    guessed = []
    #Make a list for display
    display = lwtg.copy()
    for p in range(0,len(display)):
        if lwtg[p] == "-":
            display[p] = "-"
        else:
            display[p] = "_" 
    #Main loop for player to keep guessing
    while lives > 0 and display != lwtg:
        a = str(input("Input sum cuh:"))

        if len(a) > 1:
            if a != wtg:
                lives -= 1
                print("Wrong word cuh")
                print("Progress:", display)
            else:
                print("Damn cuh, you good cuh")
                
        #If already guessed then have to guess again
        if a in guessed:
            print("Input sum else cuh")

        #If not guessed yet
        else:

            #If right guess
            if a in lwtg:
                temp = []
                for q in range(0, len(lwtg)):
                    if lwtg[q] == a:
                        temp.append(q)
                for u in range(0,len(display)):
                    if u in temp:
                        display[u] = a
                guessed.append(a)
                print("Gud job cuh")
                print("Progress:", display)

            #If wrong guess
            if a not in lwtg:
                lives -= 1
                guessed.append(a)
                print("Wrong guess cuh, lives remaining:", lives)
                print("Progress:", display)
    if lives == 0:
        return "You failed cuh"
    if display == lwtg:
        return "You good cuh"

print(w(wtg))



