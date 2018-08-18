import csv

bingoList = [dict() for i in range(25)]

with open("input.csv", newline='') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        index = int(row[1])-1
        tags = [x.strip() for x in row[2].split(',')]
        bingoList[index][row[0]] = tags

with open("bingo.js", "w+") as f:
    f.write("var bingoList = [];\n")
    for i in range(len(bingoList)):
        f.write("bingoList[%i] = [\n" % (i+1))
        d = bingoList[i]
        goals = []
        for k in d:
            goal = "  { name: \""
            goal += k
            goal += "\", types: ["
            tags = []
            for t in d[k]:
                if t != '':
                    tags.append("\"%s\"" % t)
            goal += ','.join(tags)
            goal += "] }"
            goals.append(goal)
        f.write(',\n'.join(goals))
        f.write("\n];\n")
    f.write("$(function() { srl.bingo(bingoList, 5); });")
