import os, argparse, yaml, logCheck, events
import importlib
importlib.reload(logCheck)
importlib.reload(events)

parser = argparse.ArgumentParser(
    
    description = "Traverses a directory and searches for an attack.",
    epilog = "Developed by Michael Pinelli, 20220210"
)

parser.add_argument("-d", "--directory", required = True, help = "Directory that you want to traverse.")
parser.add_argument("-s", "--service", required = True, help = "Attack you want to search for")

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
      print(root + "/" + f)
      fileList = root + "/" + f
      print(fileList)
      fList.append(fileList)

print(fList)

for eachFile in fList:
        events.event(eachFile, args.service)
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

#for eachFile in fList:
#    events(eachFile, args.service)
