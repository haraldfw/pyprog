import os


# returns the size of the file corresponding with the given filename in bytes
def getsize(filename):
    return os.stat(filename).st_size


print getsize("newFile.txt")
