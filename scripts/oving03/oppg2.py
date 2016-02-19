def countLinesAndChars(filename):
    with open(filename, "r") as opened:
        lines = opened.readlines()
        print "linecount: " + str(len(lines))

        oneline = ''.join(lines).replace('\n', ' ')
        print "wordcount: " + str(len(oneline.split(" ")))


countLinesAndChars("newFile.txt")
