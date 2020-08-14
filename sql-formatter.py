import sys

def formatSql(input_agrs):
    inputFileLocation = input_agrs[1]
    OutputFileLocation = input_agrs[2]
    readInputSql(inputFileLocation, OutputFileLocation)

def readInputSql(inputFileLocation, OutputFileLocation):
    outsql = ""
    gtrCount = 0
    intent = "\t\t"

    with open(inputFileLocation) as f:
        while True:
            character = f.read(1)
            if not character:
                break

            if (character == "<"):
                gtrCount = gtrCount + 1
            if (character == ">"):
                gtrCount = gtrCount - 1

            spacing = ""
            for i in range(gtrCount):
                spacing = spacing + "\t\t\t"

            if (character == "("):
                outsql = outsql + character + "\n" + spacing
            elif (character == ")"):
                outsql = outsql + "\n" + character + spacing
            elif (character == "," and gtrCount != 0):
                outsql = outsql + character + "\n" + spacing + intent
            elif (character == ","):
                outsql = outsql + character + "\n" + spacing
            elif (character == "<"):
                outsql = outsql + "\n" + intent + spacing + character + "\n" + spacing + intent + " "
            elif (character == ">"):
                outsql = outsql + "\n" + spacing + intent + "\t\t\t" + character
            else:
                outsql = outsql + character

            if (outsql[-5:] == "ARRAY"):
                length = len(outsql)

            if outsql[-7:] == "\tSTRUCT":
                outsql = outsql

            if (outsql[-6:] == "STRUCT" and outsql[-7:] != " STRUCT"):
                outsql = outsql[:-6] + "\n " + spacing + intent + "STRUCT"

    # Write the generated sql into a file
    outputFile = open(OutputFileLocation, "w")
    outputFile.write(outsql)
    outputFile.close()


if __name__ == "__main__":
    formatSql(sys.argv)
