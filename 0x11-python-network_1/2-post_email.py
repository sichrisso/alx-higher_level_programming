#!/usr/bin/python3
'''task 2 script'''

if __name__ == '__main__':
    import sys
    from urllib import request, parse

    data = parse.urlencode({'email': sys.argv[2]}).encode()
    req = request.Request(sys.argv[1], data=data)
    with request.urlopen(req) as res:
        print(res.read().decode('UTF-8'))
