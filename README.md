# Generate Minecraft JSON Files

**PYTHON 3 MUST BE INSTALLED ON YOUR COMPUTER**

    usage: gen.py [-h] [-m MODID] -b BLOCK -t TEMPLATE
    
    Generate files for your minecraft mod
    
    optional arguments:
      -h, --help            show this help message and exit
      -m MODID, --modid MODID
                            your modid, e.g. examplemod (if empty will be read in config.json)
      -b BLOCK, --block BLOCK
                            name of your block, e.g. dark_oak
      -t TEMPLATE, --template TEMPLATE
                            generation template (must be a folder in template folder), e.g. wood

You can create your own templates directly inside the *template* folder.

**config.json**
Inside the root folder

    {
    "modid":"mymod",
    "keywords" : {    
    "JAVA_CLASS" : "MyMod"
	    }
    }

 - modid : name of your modid (will be overwrite is -m is set in command line)
 - keywords : custom keywords that can be used to replace in template, e.g. JAVA_CLASS will replace %_JAVA_CLASS% with the string MyMod (without double quotation marks).

**config.json**
Inside template folder
If template folder contains a *config.json* file, it will be read to load more template.

    {
    "also_generate":["wood_extra"]
    }

e.g. "also_generate":["wood_extra"] will also generate json file inside the template folder "wood_extra"
