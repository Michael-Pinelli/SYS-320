import os, argparse, yaml, searchCSV
import importlib
importlib.reload(searchCSV)

parser = argparse.ArgumentParser(
    
    description = "Searches for mailicious activity",
    epilog = "Developed by Michael Pinelli, 20220224"
)

parser.add_argument("-d", "--directory", required = True, help = "Directory that you want to traverse.")
parser.add_argument("-a", "--attack", required = True, help = "Attack you want to search for. List: cred_collection, java_or_vbscript, or pwr_exec")

args = parser.parse_args()

rootdir = args.directory


if not os.path.isdir(rootdir):
    print("Invalid directory => {}".format(rootdir))
    exit()
    
fList = []

for root, subfolders, filenames in os.walk(rootdir):
    
    for f in filenames:
        
        #print(root + "/" + f)
        fileList = root + "/" + f
        #print(fileList)
        fList.append(fileList)

print(fList)

for eachFile in fList:
    searchCSV.search(eachFile, args.attack)