high = ['2', '3', '4', '5', '6', '7', '8', '9', '1', 'J', 'Q', 'K', 'A']

# cards for player 1
p1 = []
n = int(input())  
for i in range(n):
    cardp_1 = input()
    p1.append(cardp_1)
    
# cards for player 2
p2 = []
m = int(input())  
for i in range(m):
    cardp_2 = input() 
    p2.append(cardp_2)

# game
rounds = 0
pw1 = []; pw2 = []
while p1 and p2:
    pos1 = high.index(p1[0][0])
    pos2 = high.index(p2[0][0])
    card1 = p1.pop(0); card2 = p2.pop(0)
    if pos1 > pos2:
        pw1.append(card1); pw2.append(card2)
        p1.extend(pw1); p1.extend(pw2)
        pw1 = []; pw2 = []
        rounds += 1 
    elif pos2 > pos1:
        pw1.append(card1); pw2.append(card2)
        p2.extend(pw1); p2.extend(pw2)
        pw1 = []; pw2 = []
        rounds += 1 
    elif pos1 == pos2:
        pw1.append(card1); pw2.append(card2)
        for i in range(3):
            if p1 and p2:
                card1 = p1.pop(0); card2 = p2.pop(0)
                pw1.append(card1); pw2.append(card2)
            else:
                p1 = []; p2 = []
                break

# result
if len(p1) == 0:
    if len(p2) == 0:
        res = 'PAT'
    else:
        res = '2 ' + str(rounds)
elif len(p2) == 0:
    if len(p1) == 0:
        res = 'PAT'
    else:
        res = '1 ' + str(rounds)
print(res)

