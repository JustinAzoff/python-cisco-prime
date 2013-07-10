currently supports searching for a mac/ip/username and returning the data from prime..

    >>> c=cisco_prime.Client("ncs-prime",user,pass)
    >>> for r in c.search_client("192.168.100.100"):
    ...     print r["userName"], r['exportMacAddress'], r['lradName']
    ... 
    wpatest 00:26:5e:35:2b:b1 MSC100-WAP2

