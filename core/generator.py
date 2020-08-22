import os, json, sys

class Generator:

    def __init__(self, source_root_path, template, destination_path, formated_keywords):
        self.__keywords = formated_keywords 
        self.__source_root_path = source_root_path 
        self.__destination_path = destination_path 
        self.__others = {}
        self.__others[template] = True                

        self.__source_template_path = os.path.join(source_root_path, template)  

        if not os.path.exists(self.__source_template_path): 
            print("Source path doesn't exists : " + self.__source_template_path)
            sys.exit(2)

    def generate(self):
        config_file_name = os.path.join(self.__source_template_path, "config.json")
        if os.path.isfile(config_file_name):
            with open(config_file_name) as config_file:
                data = json.load(config_file)
                other_types = data["also_generate"]

                for t in other_types:
                    if not t in self.__others:
                        self.__others[t] = True                
                        new_path = os.path.join(self.__source_root_path, t)
                        if not os.path.exists(self.__source_template_path): 
                            print("Source path doesn't exists : " + self.__source_template_path)
                        else:
                            self.__crawl(new_path, self.__destination_path)

        self.__crawl(self.__source_template_path, self.__destination_path)

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
                if entry != "config.json":
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