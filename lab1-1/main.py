import numpy as np

def vote(fileInfo):
    n = int(fileInfo[0])
    m = int(fileInfo[1])
    D = fileInfo[2]
    L = fileInfo[3]
    while (True):
        l2 = []
        winner = []
        loser = []
        for i in range(m):
            l2.append(L[i][0])
        objects, counts = np.unique(l2, return_counts = True) # ([1, 2, 3, 4], [2, 4, 5, 1])
        mn, mx = min(counts), max(counts)
        for i in range(1, n + 1):
            if l2.count(i) == mx:
                winner.append(i)
            if l2.count(i) == mn:
                loser.append(i)
        if (mx / len(l2) > 0.5) and (len(winner) == 1):
            print("Кандидат", *[D[i] for i in winner], "побеждает!")
            break
        elif len(winner) == n:
            print("Кандидаты", *[D[i] for i in winner], "собрали одинаковое кол-во голосов!")
            break
        else:
            for i in loser:
                for j in L:
                    j.remove(i)

def fileRead(text):
    f = open(text, 'r', encoding = "UTF-8")
    n = f.readline()
    D = {}
    for i in range(int(n)):
        s = f.readline()
        D[i + 1] = s.strip()
    L = []
    m = 0
    while True:
        line = f.readline()
        if not line:
            break
        l = []
        l = [int(i.strip()) for i in line.split(' ')]
        m = m + 1
        L.append(l)
    fileInfo = [n, m, D, L]
    return(fileInfo)

print("Тест 1")
text = 'text.txt'
fileInfo = fileRead(text)
vote(fileInfo)
print("Тест 2")
text = 'text2.txt'
fileInfo = fileRead(text)
vote(fileInfo)
print("Тест 3")
text = 'text3.txt'
fileInfo = fileRead(text)
vote(fileInfo)
print("Тест 4")
text = 'text4.txt'
fileInfo = fileRead(text)
vote(fileInfo)
print("Тест 5")
text = 'text5.txt'
fileInfo = fileRead(text)
vote(fileInfo)





