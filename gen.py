import sys, os, argparse, json
from core import generator

def main(argv):
    parser = argparse.ArgumentParser(description="Generate files for your minecraft mod")

    parser.add_argument("-m", "--modid", help="your modid, e.g. examplemod (if empty will be read in config.json)", type=str, required=False)
    parser.add_argument("-b", "--block", help="name of your block, e.g. dark_oak", type=str, required=True)
    parser.add_argument("-t", "--template", help="generation template (must be a folder in template folder), e.g. wood", type=str, required=True)
    parser.add_argument("-p", "--push", help="push generation into mod ressource folder", type=bool, required=False)
    parser.add_argument("-c", "--config", help="config file to read (default is config.json)", type=str, required=False)
    
    args = parser.parse_args()

    mod_ID = args.modid
    block_name = args.block
    template = args.template
    config_file_name = args.config 
    if config_file_name == None:
        config_file_name = "config.json"

    path = os.path.dirname(os.path.realpath(__file__))
    if os.path.isfile(config_file_name):
        with open(config_file_name) as config_file:
            data = json.load(config_file)
            if mod_ID == None:
                mod_ID = data["modid"]

            keywords = data["keywords"]
    else:
        print(config_file_name + " doesn't exists")
        sys.exit(2)

    if mod_ID == None:
        print("modid is invalid")
        sys.exit(2)

    formated_keywords = {}
    formated_keywords["%BLOCK_UPPER%"] = block_name.upper()
    formated_keywords["%BLOCK_LOWER%"] = block_name.lower()
    formated_keywords["%BLOCK_COMMON_NAME%"] = block_name.title().replace("_", " ") 
    formated_keywords["%BLOCK%"] = block_name
    formated_keywords["%MOD_ID%"] = mod_ID

    for k,v in keywords.items():
        if k[0] == "%" and k[-1] == "%":
            formated_keywords[k] = v
        elif(k[0] == "%"):
            formated_keywords[k + "%"] = v
        elif(k[-1] == "%"):
            formated_keywords["%" + k] = v
        else:
            formated_keywords["%" + k + "%"] = v

    source_root_path = os.path.join(path, "template")
    source_template_path = os.path.join(source_root_path, template)  

    if not os.path.exists(source_template_path): 
        print("Source path doesn't exists : " + source_template_path)
        sys.exit(2)

    destination_path = os.path.join(path, "gen")
    if not os.path.exists(destination_path): 
         os.mkdir(destination_path)

    destination_path = os.path.join(destination_path, template)
    if not os.path.exists(destination_path): 
         os.mkdir(destination_path)

    destination_path = os.path.join(destination_path, block_name)
    if not os.path.exists(destination_path): 
         os.mkdir(destination_path)

    generator.Generator(source_root_path, template, destination_path, formated_keywords).generate()

if __name__ == "__main__":
    main(sys.argv[1:])  