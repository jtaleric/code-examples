#!/bin/python

struct= {
        "hosts" : {
            "c08": {
                "start": {
                    "day": 1,
                    "month": 1,
                    "year": 2017
                    }
            },
            "c07": {
                "start": {
                    "day": 2,
                    "month": 2,
                    "year": 2017
                    }
            },
            "c06": {
                "start": {
                    "day": 3,
                    "month": 3,
                    "year": 2017
                    }
                }
            }
        }

def search_start(data,day=0,month=1,year=2017) :
    matched_hosts = []
    for host in data :
        if data[host]['start']['month'] == month and \
                data[host]['start']['year'] == year :
                    if day is not 0 :
                        if data[host]['start']['day'] == day :
                            matched_hosts.append(host)
                    else :
                        matched_hosts.append(host)

    return matched_hosts

print "Checking for 1-2017"
print search_start(struct['hosts'])
print "Checking for 2-1-2017"
print search_start(struct['hosts'],month=2,day=1)
print "Checking for 2-2017"
print search_start(struct['hosts'],month=2)
