isifile = open("indonesian-words.txt", "r")
wordlist = []

for items in isifile:
    wordlist.append(isifile.readline()[:-2])
isifile.close()

print("Mencari statistik dari database atas",len(wordlist),"kata")
alpabet_statistics = {}

for i in range(ord('a'), ord('z')+1):
    alpabet_statistics[str(chr(i))] = 0

for words in range (0, len(wordlist)):
    for x in range(0, len(wordlist[words])):
        if wordlist[words][x] in alpabet_statistics:
            alpabet_statistics[wordlist[words][x]] +=1 

#print(alpabet_statistics) #statistik tanpa diurutkan

alpabet_statistics_sorted = sorted(alpabet_statistics.items(), key=lambda x:x[1], reverse=True)
print('Top-5 kemunculan huruf: ')
for i in range(0, 6):
    print(alpabet_statistics_sorted[i])