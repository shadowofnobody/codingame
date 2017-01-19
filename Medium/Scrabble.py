# init data
n = int(input())
words = []
for i in range(n):
    words.append(input())
letters = input()
dic = {}
for i in letters:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

# game
ml = 0
for w in words:
    m = 0
    
    # check
    addicts = {}
    for i in w:
        if not i in dic.keys():
            break  
        elif not i in addicts:
            addicts[i] = 1
        elif i in addicts:
            addicts[i] += 1
    else:
        for z in addicts.keys():
            if addicts[z] > dic[z]:
                break
            
        # count
        else:
            for j in w:
                    if j in 'eaionrtlsu':
                        m += 1
                    elif j in 'dg':
                        m += 2
                    elif j in 'bcmp':
                        m += 3
                    elif j in 'fhvwy':
                        m += 4
                    elif j in 'k':
                        m += 5
                    elif j in 'jx':
                        m += 8
                    elif j in 'qz':
                        m += 10
    
            # decision            
            if m > ml:
                ml = m
                mw = w

# answer
print(mw)

