import os 

class Generator:

    def __init__(self, source_path, destination_path, formated_keywords):
        self.__keywords = formated_keywords 
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

                if "BLOCKNAME" in entry:
                    entry = entry.replace("BLOCKNAME", self.__keywords["%BLOCK%"])
                else :
                    entry = self.__keywords["%BLOCK%"] + "_" + entry 

                new_destination = os.path.join(destination, entry)
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

        for k,v in self.__keywords.items():
            s = s.replace(k, v)

        f  = open(destination, "w+") 
        f.write(s)
        f.close() 