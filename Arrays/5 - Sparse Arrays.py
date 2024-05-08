# Author: Bintang Fajarianto
# Date: May 8 2024

def matchingStrings(stringList, queries):
    return list(map(lambda x: stringList.count(x), queries))