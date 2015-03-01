if __name__ == "__main__":
    inputfile = open("NodeIds.csv")
    outputfile = open("../opcua/uaprotocol/object_ids.py", "w")
    outputfile.write("#AUTOGENERATED!!!\n")
    outputfile.write("\n")
    outputfile.write("\n")
    outputfile.write("class ObjectIds:\n")
    for line in inputfile:
        name, nb, datatype = line.split(",")
        outputfile.write("    {} = {}\n".format(name, nb))