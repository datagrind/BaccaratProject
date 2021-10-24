import random

def baccarat():
    global bankroll
    global bankrollNum
    global tieNum
    global simNum
    global betNum
    global cost
    global sim
    global streakLoss
    global hand
    global streakWin
    global payout
    global runBet
    global highestLosingStreak
    global highestWinningStreak
    global secondHighestLosingStreak
    global secondHighestWinningStreak
    global thirdHighestLosingStreak
    global thirdHighestWinningStreak
    global timesBankrupted
    global lossArray
    global winArray
    global previousHand
    global currentHand
    global nextHand
    global win
    global loss
    global prevBet
    global lossStreakPercent
    global winStreakPercent
    global lossStreakTotal
    loss = {
        'less10' : 0,
        'less20' : 0,
        'less30' : 0,
        'less40' : 0,
        'less50' : 0,
        'less60' : 0,
        'less70' : 0,
        'less80' : 0,
        'less90' : 0,
        'less100' : 0,
        'less110' : 0,
        'less120' : 0,
        'less130' : 0
        }

    win = {
        'win1' : 0,
        'win2' : 0,
        'win3' : 0,
        'win4' : 0,
        'win5' : 0,
        'win6' : 0,
        'win7' : 0,
        'win8' : 0,
        'win9' : 0,
        'win10' : 0
        }
    winStreakPercent = {
        'win1' : 0,
        'win2' : 0,
        'win3' : 0,
        'win4' : 0,
        'win5' : 0,
        'win6' : 0,
        'win7' : 0,
        'win8' : 0,
        'win9' : 0,
        'win10' : 0
        }
    nextHand = None
    lossArray = []
    winArray = []
    timesBankrupted = 0
    highestLosingStreak = 0
    highestWinningStreak = 0
    secondHighestWinningStreak = 0
    secondHighestLosingStreak = 0
    thirdHighestWinningStreak = 0
    thirdHighestLosingStreak = 0
    payout = 8
    streakWin = 0
    streakLoss = 0
    previousHand = None
    currentHand = None
    hand = 0
    cost = 0
    bankroll = 0
    bankrollNum = int(input("How much is your bankroll?"))
    bankroll += bankrollNum
    bet = 0
    betNum = int(input("How much is your bet increment?"))
    bet += betNum
    runBet = 0
    runBet += bet
    simNum = int(input("How many hands do you want to simulate?"))
    sim = simNum
    breakeven = runBet*payout
    for i in range(sim):
        tieNum = random.randint(0,10)
        i = 1
        if i == tieNum:
            if previousHand == "loss":
                lossArray += [streakLoss]
            previousHand = currentHand
            win = runBet*payout
            hand += 1
            bankroll += win
            prevBet = runBet
            runBet = bet
            cost = 0
            streakWin += 1
            currentHand = "win"
            streakLoss = 0
            breakeven = runBet*payout
            if streakWin > highestWinningStreak:
                thirdHighestWinningStreak = secondHighestWinningStreak
                secondHighestWinningStreak = highestWinningStreak
                highestWinningStreak = streakWin
            print("Hand: " + str(hand))
            print("Bet: $"+str(prevBet))
            print("You win " + "$"+str(win)+"!")
            print("Bankroll: $"+str(bankroll))
            print("Winning Streak: " + str(streakWin)+"\n")
        else:
            if previousHand == "win":
                winArray += [streakWin]
            previousHand = currentHand
            hand += 1
            cost += runBet
            bankroll -= runBet
            streakLoss += 1
            currentHand = "loss"
            streakWin = 0
            if cost > breakeven:
                while cost > breakeven:
                    runBet += bet
                    breakeven = runBet*payout
            if streakLoss > highestLosingStreak:
                thirdHighestLosingStreak = secondHighestLosingStreak
                secondHighestLosingStreak = highestLosingStreak
                highestLosingStreak = streakLoss
            print("Hand: " + str(hand))
            print("You lose!")
            print("Bet: $"+str(runBet))
            print("Cost: $"+str(cost))
            print("Bankroll: $"+str(bankroll))
            print("Losing Streak: " + str(streakLoss)+"\n")
        # if bankroll <= 0:
        #     break
        if bankroll <= 0:
            timesBankrupted += 1
            bankroll = bankrollNum
    for i in lossArray:
        if i < 10:
            loss['less10'] += 1
        elif i >= 10 and i <20:
            loss['less20'] += 1
        elif i >= 20 and i <30:
            loss['less30'] += 1
        elif i >= 30 and i <40:
            loss['less40'] += 1
        elif i >= 40 and i <50:
            loss['less50'] += 1
        elif i >= 50 and i <60:
            loss['less60'] += 1
        elif i >= 60 and i <70:
            loss['less70'] += 1
        elif i >= 70 and i <80:
            loss['less80'] += 1
        elif i >= 80 and i <90:
            loss['less90'] += 1
        elif i >= 90 and i <100:
            loss['less100'] += 1
        elif i >= 100 and i <110:
            loss['less110'] += 1
        elif i >= 110 and i <120:
            loss['less120'] += 1
        elif i >= 120 and i <130:
            loss['less130'] += 1

    lossStreakTotal = sum(loss.values())
    lossStreakPercent = {
        'less10' : str(((loss['less10']/lossStreakTotal)*100))+"%",
        'less20' : str(((loss['less20']/lossStreakTotal)*100))+"%",
        'less30' : str(((loss['less30']/lossStreakTotal)*100))+"%",
        'less40' : str(((loss['less40']/lossStreakTotal)*100))+"%",
        'less50' : str(((loss['less50']/lossStreakTotal)*100))+"%",
        'less60' : str(((loss['less60']/lossStreakTotal)*100))+"%",
        'less70' : str(((loss['less70']/lossStreakTotal)*100))+"%",
        'less80' : str(((loss['less80']/lossStreakTotal)*100))+"%",
        'less90' : str(((loss['less90']/lossStreakTotal)*100))+"%",
        'less100' : str(((loss['less100']/lossStreakTotal)*100))+"%",
        'less110' : str(((loss['less110']/lossStreakTotal)*100))+"%",
        'less120' : str(((loss['less120']/lossStreakTotal)*100))+"%",
        'less130' : str(((loss['less130']/lossStreakTotal)*100))+"%",
        }
    # for total in loss:
    #     values = loss.values()
    #     total = sum(values)
    #     lossStreakTotal += total
    #     return lossStreakTotal
            
    # for i in winArray:
    #     if i == 1:
    #         win['win1'] += 1
    #     elif i == 2:
    #         win['win2'] += 1
    #     elif i == 3:
    #         win['win3'] += 1
    #     elif i == 4:
    #         win['win4'] += 1
    #     elif i == 5:
    #         win['win5'] += 1
    #     elif i == 6:
    #         win['win6'] += 1
    #     elif i == 7:
    #         win['win7'] += 1
    #     elif i == 8:
    #         win['win8'] += 1
    #     elif i == 9:
    #         win['win9'] += 1
    #     elif i == 10:
    #         win['win10'] += 1

    if bankroll > 0:
        print("Total Hands: " + str(hand))
        print("Highest Losing Streak: " + str(highestLosingStreak))
        print("2nd Highest Losing Streak: " + str(secondHighestLosingStreak))
        print("3rd Highest Losing Streak: " + str(thirdHighestLosingStreak))
        print("Highest Winning Streak: " + str(highestWinningStreak))
        print("2nd Highest Winning Streak: " + str(secondHighestWinningStreak))
        print("3rd Highest Winning Streak: " + str(thirdHighestWinningStreak))
        print("Times Bankrupted: " + str(timesBankrupted)+ "\n")
        # print("Loss Streaks: \n")
        # print(lossArray)
        # print("Win Streaks: \n")
        # print(winArray)
        # print(win)
        print(loss+ "\n")
        print(lossStreakPercent)
    if bankroll <= 0:
        print("Game Over!")
        print("Total Hands: " + str(hand))
        print("Highest Losing Streak: " + str(highestLosingStreak))
        print("2nd Highest Losing Streak: " + str(secondHighestLosingStreak))
        print("3rd Highest Losing Streak: " + str(thirdHighestLosingStreak))
        print("Highest Winning Streak: " + str(highestWinningStreak))
        print("2nd Highest Winning Streak: " + str(secondHighestWinningStreak))
        print("3rd Highest Winning Streak: " + str(thirdHighestWinningStreak) + "\n")
        # print("Loss Streaks: \n")
        # print(lossArray)
        # print("Win Streaks: \n")
        # print(winArray)
        # print(win)
        print(loss+ "\n")
        print(lossStreakPercent)
        game = False
        return game
    game = False
    





game = True
while game == True:
    game = baccarat()