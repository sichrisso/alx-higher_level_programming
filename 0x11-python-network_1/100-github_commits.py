#!/usr/bin/python3
'''task 10 script'''

if __name__ == '__main__':
    import requests
    import sys

    repo_name = sys.argv[1]
    owner = sys.argv[2]
    headers = {
              'Accept': 'application/vnd.github.v3+json',
              }
    params = {
        'per_page': 10,
    }

    res = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
                      owner, repo_name),
                      headers=headers, params=params)
    json_res = res.json()
    for commit in json_res:
        print(commit['sha'] + ':', commit['commit']['author']['name'])
