def numberOfLines(fileName):
    lines = 0
    words = 0
    chars = 0
    f = open(fileName, 'r')
    while len(f.readline()) != 0:
        lines += 1
        words += len(f.readline().split())
        chars += sum(map(len,(f.readline().split())))
    f.close()
    return lines,words,chars

##    for line in f: #implies a line-by-line reading of the file
##        ans += 1

print numberOfLines('lines.txt')
