
# init data
budgets = []
ans = []
oods = int(input())
price = int(input())
for i in range(oods):
    budgets.append(int(input()))
budgets = sorted(budgets)

# solution
if sum(budgets) < price:
    print('IMPOSSIBLE')
elif sum(budgets) == price:
    for i in budgets:
        print(i)
elif sum(budgets) > price:
    for i in budgets:
        dif = price//oods
        if i < dif:
            ans.append(i)
            price -= i
        else:
            ans.append(dif)
            price -= dif
        oods -= 1
    for i in ans:
        print(i)



