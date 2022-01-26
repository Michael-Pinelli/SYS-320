import syslogCheck
import importlib
importlib.reload(syslogCheck)

def ssh_success(filename, searchTerms):

    is_found = syslogCheck._syslog(filename,searchTerms)

    found = []

    for eachFound in is_found:

        sp_results = eachFound.split(" ")

        found.append(sp_results[5])

    returnedValues = set(found)

    for eachValue in returnedValues:
        
        print(eachValue)