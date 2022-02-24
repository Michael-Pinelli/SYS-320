import os, argparse, yaml, searchCSV
import importlib
importlib.reload(searchCSV)

with open('searchTerms.yaml', 'r') as f:
    keywords = yaml.safe_load(f)
        

parser = argparse.ArgumentParser(
    
    description = "Searches for mailicious activity",
    epilog = "Developed by Michael Pinelli, 20220224"
)

parser.add_argument("-d", "--directory", required = True, help = "Directory that you want to traverse.")
parser.add_argument("-a", "--attack", required = True, help = "Attack you want to search for")

args = parser.parse_args()

rootdir = args.directory


# if not os.path.isdir(rootdir):
#     print("Invalid directory => {}".format(rootdir))
#     exit()
    
# fList = []

# for root, subfolders, filenames in os.walk(rootdir):
    
#     for f in filenames:
        
#         #print(root + "/" + f)
#         fileList = root + "/" + f
#         #print(fileList)
#         fList.append(fileList)

# print(fList)

searchCSV.open(rootdir, args.attack)
# for eachFile in fList:
#     searchCSV.open(rootdir, args.attack)