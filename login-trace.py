import re

def getUserAndIP(fileName, outFile):
    file = open(fileName, "rb")
    fileText = file.read()
    fileLines = fileText.splitlines()
    userLines = []
    for i in range(len(fileLines)):
        if(re.search(" user ", str(fileLines[i]))):
            userLines.append(fileLines[i])
    ipUserList = []
    for i in range(len(userLines)-1):
        tempList = str(userLines[i]).split()
        line = str(userLines[i])
        if(line.find("user") and re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)):
            ipUserList.append(tempList[tempList.index("user")+1])
            ipUserList.append(" ")
            ipUserList.append(re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", str(userLines[i])))
            ipUserList.append("\n")
    text = ""
    for i in range(len(ipUserList)):
        text = text + str(ipUserList[i])
        text = text.replace("'", "")
        text = text.replace("[", "")
        text = text.replace("]", "")
    fileOut = open(outFile, "w")
    fileOut.write(text)

inFile = input("Enter the full path of the file you want to get data from: ")
outFile = input("once done where would you like the data to be written to? ")

getUserAndIP(inFile, outFile)

with open(filename) as infile:
    for line in infile:
        do_something_to(line)