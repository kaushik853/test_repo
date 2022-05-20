#! /usr/bin/env python

import requests
import json
from pprint import pprint
from github import Github

def user():
    username = 'kaushik853'
    req_url = f"https://api.github.com/users/{username}"
    
    user_data = requests.get(req_url).json()
    
    pprint(user_data)

def user_repo():
    username = 'kaushik853'
    g = Github()
    user = g.get_user(username)
    for repo in user.get_repos():
        print(repo)

if __name__=="__main__":
    user_repo()

