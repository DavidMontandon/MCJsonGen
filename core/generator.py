import os 

class Generator:

    def __init__(self, source_path, destination_path, modID, blockName):
        self.__modID = modID 
        self.__blockName = blockName 
        self.__source_path = source_path 
        self.__destination_path = destination_path 

    def generate(self):
        self.__crawl(self.__source_path, self.__destination_path)

    def __crawl(self, source, destination):
        list_of_entries = os.listdir(source)
        for entry in list_of_entries:
            full_path = os.path.join(source, entry)
            new_source = os.path.join(source, entry)
            if os.path.isdir(full_path):
                new_destination = os.path.join(destination, entry)
                if not os.path.exists(new_destination): 
                    os.mkdir(new_destination)
                self.__crawl(new_source, new_destination)
            else:
                new_destination = os.path.join(destination, self.__blockName + "_" + entry)
                self.__writeFile(new_source, new_destination)


    def __writeFile(self, source, destination):
        print("Reading : " + source)
        self.__write(source, destination)
        print("Generating : " + destination)
        print("=====")

    def __write(self, source, destination):
        f = open(source, "r") 
        s = f.read()
        f.close

        s = s.replace("%MOD_ID%", self.__modID)
        s = s.replace("%BLOCK%", self.__blockName)

        f  = open(destination, "w+") 
        f.write(s)
        f.close() 

    def __createSign(self):
        #BLOCKSTATE
        self.__write("./template/blockstates/wall_sign.json", "./gen/blockstates/" + self.__blockName + "_wall_sign.json")

    def __createButton(self):
        #BLOCKSTATE
        self.__write("./template/blockstates/button.json", "./gen/blockstates/" + self.__blockName + "_button.json")

    def __createStairs(self):
        #BLOCKSTATE
        self.__write("./template/blockstates/stairs.json", "./gen/blockstates/" + self.__blockName + "_stairs.json")

        #BLOCK_STAIRS_INNER        
        self.__write("./template/models/block/stairs_inner.json", "./gen/models/block/" + self.__blockName + "_stairs_inner.json")

        #BLOCK_STAIRS_OUTER
        self.__write("./template/models/block/stairs_outer.json", "./gen/models/block/" + self.__blockName + "_stairs_outer.json")

        #BLOCK_STAIRS
        self.__write("./template/models/block/stairs.json", "./gen/models/block/" + self.__blockName + "_stairs.json")

        #ITEM_STAIRS
        self.__write("./template/models/item/stairs.json", "./gen/models/item/" + self.__blockName + "_stairs.json")
