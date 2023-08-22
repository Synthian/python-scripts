wordLists = {}
with open("./dict.txt") as file:
    for line in file:
        scoredWord = line.split(";")
        word = scoredWord[0]
        score = scoredWord[1]
        if int(score) >= 50:
            length = len(word)
            firstLetter = word[0]
            if length not in wordLists:
                wordLists[length] = {}
            if firstLetter not in wordLists[length]:
                wordLists[length][firstLetter] = []
            wordLists[length][firstLetter].append(word)

for length,dict in wordLists.items():
    if (length > 5):
        for firstLetter,list in dict.items():
            for word in list:
                lastLetter = word[-1]
                if lastLetter in dict:
                    for candidate in dict[word[-1]]:
                        if word == candidate[::-1] and word != candidate:
                            print('{0} = {1}'.format(word,candidate))