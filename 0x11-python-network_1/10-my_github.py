#!/usr/bin/python3
'''task 9 script'''

if __name__ == '__main__':
    import requests
    import sys

    user = sys.argv[1]
    token = sys.argv[2]
    headers = {
              'Authorization': 'token {}'.format(token),
              'Accept': 'application/vnd.github.v3+json',
              }
    res = requests.get('https://api.github.com/user', headers=headers)
    print(res.json().get('id', 'None'))
