import os, argparse, yaml, re, sys

with open('searchTerms.yaml', 'r') as f:
    keywords = yaml.safe_load(f)
        

parser = argparse.ArgumentParser(
    
    description = "Traverses a directory and builds a forensic body file",
    epilog = "Developed by Michael Pinelli, 20220210"
)

parser.add_argument("-d", "--directory", required = True, help = "Directory that you want to traverse.")
parser.add_argument("-b", "--book", required = True, help = "Attack you want to search for")
parser.add_argument("-t", "--term", required = True, help = "Term you want to search for")

args = parser.parse_args()

rootdir = args.directory
#print(sys.argv)

#rootdir = sys.argv[1]

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

#def statFile(toStat):
    
 #   i = os.stat(toStat,follow_symlinks=False)
 #   mode = i[0]
 #   inode = i[1]
 #   uid = i[4]
 #   gid = i[5]
 #   fsize = i[6]
 #   atime = i[7]
 #   mtime = i[8]
 #   ctime = i[9]
 #   crtime = i[9]
    
#    print("0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(toStat, inode, mode, uid, gid, fsize, atime, mtime, ctime, crtime))
    
#for eachFile in fList:
 #   statFile(eachFile)

def attackSearch():
    
    terms = keywords[service][term]

    listOfKeywords = terms.split(",")
    
    # Open a file
    with open(rootdir) as f:

        # Read the file
        contents = f.readlines()
    # Lists to store the results
    results = []

    # Loop through the list
    for line in contents:
    
         for eachKeyword in listOfKeywords:

            x = re.findall(r''+eachKeyword+'', line)

            for found in x:

                results.append(found)
    
    if len(results) == 0:
        print("No Results")
        sys.exit(1)

    results = sorted(results)

    results = set(results)

    return results

def events():
    
    is_found = attackSearch()

    found = []

    for eachFound in is_found:

        sp_results = eachFound.split(" ")

        found.append(sp_results[0])

    getValues = set(found)

    for eachHost in getValues:
        
        print(eachHost)
        
for eachFile in fList:
    events(eachFile)