import logCheck
import importlib
importlib.reload(logCheck)

def apache_events(filename, service, term):

    is_found = logCheck._logs(filename, service, term)

    found = []

    for eachFound in is_found:

        sp_results = eachFound.split(" ")

        found.append(sp_results[0] + " " + sp_results[1] + " "+ sp_results[3])

    getValues = set(found)

    for eachHost in getValues:
        
        print(eachHost)