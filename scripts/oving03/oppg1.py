# -*- coding: UTF-8 -*-

with open("newFile.txt", "w+") as newFile:
    newFile.write("1. Hallo")
    newFile.write("\n2. Skriver en linje til ")
    newFile.write("\n3. Her kommer enda en linje")

with open("newFile.txt", "r") as newFile:
    lines = newFile.readlines()
    print lines[1]

    oneline = ''.join(lines).replace('\n', '')
    oneline = filter(str.isalpha, oneline)
    print oneline[:10]
