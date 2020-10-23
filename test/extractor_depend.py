#!/usr/bin/env python
# coding: utf-8

# In[1]:
import sys
sys.path.append(r'../xkcd2347/')
import xkcd2347
import json
from tqdm import tqdm


def getDependencies(input_file, output_file, git_hub_key, hop):
    dependency_data = {}
    no_dependency_data = []
    gitLink = []

    with open(input_file, 'r') as fp:
        gitLink = fp.readlines()

    for link in tqdm(gitLink):
        gh = xkcd2347.GitHub(key = git_hub_key)
        link = link.rstrip()
        owner, repo = link.split(".com/")[1].split("/")
        result = [dep['packageName'] for dep in gh.get_dependencies(repo_owner = owner, repo_name = repo, depth = hop)]
        if(len(result) > 0):
            dependency_data[link] = result
    with open(output_file, 'w') as fp:
        json.dump(dependency_data, fp, indent=4)

# In[ ]:




