import sys, os, getopt
from core import generator

def main(argv):
    command = "gen.py -m <modID> -b <name> -t <wood>"

    try:
        opts, args = getopt.getopt(argv, "hm:b:t:")
    except getopt.GetoptError:
        print(command)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-b"):
            blockName = arg
        if opt in ("-m"):
            modID = arg
        if opt in ("-t"):
            srcType = arg

    try:
        blockName
    except NameError:
        print("well, you forget to set your block name")
        print(command)
        sys.exit(2)

    try:
        modID
    except NameError:
        print("well, you forget to set your MOD_ID")
        print(command)
        sys.exit(2)

    try:
        srcType
    except NameError:
        print("well, you forget to set your source type")
        print(command)
        sys.exit(2)

    path = os.path.dirname(os.path.realpath(__file__))

    source_path = os.path.join(path, "template")
    source_path = os.path.join(source_path, srcType)  

    if not os.path.exists(source_path): 
        print("Source path doesn't exists : " + source_path)
        sys.exit(2)

    destination_path = os.path.join(path, "gen")
    destination_path = os.path.join(destination_path, srcType)

    if not os.path.exists(destination_path): 
         os.mkdir(destination_path)

    generator.Generator(source_path, destination_path, modID, blockName).generate()

if __name__ == "__main__":
    main(sys.argv[1:])  