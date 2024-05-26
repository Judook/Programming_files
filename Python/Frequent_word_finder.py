words =[]
print("Enter the words, type in '*' when finished")
while True :
    x = (input("Enter the word :"))
    if x == "*":
        break
    else :
        words.append(x)
ls = []
num = []
for word in words:
    if word not in ls:
        ls.append(word)
        num.append(1)
    else :
        num[ls.index(word)] += 1
most = ls[num.index(max(num))]
print(most)
