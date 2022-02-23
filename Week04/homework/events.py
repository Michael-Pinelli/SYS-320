import logCheck, yaml, re
import importlib
importlib.reload(logCheck)

def event(filename, service):
    
    is_found = logCheck._logs(filename, service)

    found = []

    for eachFound in is_found:

        sp_results = eachFound.split(" ")

        found.append(sp_results[0] + " ")

    getValues = set(found)

    for eachHost in getValues:
        
        print(eachHost)