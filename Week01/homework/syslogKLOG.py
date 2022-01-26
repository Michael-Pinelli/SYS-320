import syslogCheck
import importlib
importlib.reload(syslogCheck)

def klogind_fail(filename, searchTerms):

    is_found = syslogCheck._syslog(filename,searchTerms)

    found = []

    for eachFound in is_found:

        sp_results = eachFound.split(" ")

        found.append(sp_results[4])

    hosts = set(found)

    for eachHost in hosts:
        
        print(eachHost)
