import xkcd2347
import json
from tqdm import tqdm
import sys

def getDependencies(input_file, output_file, git_hub_key, hop):
    dependency_data = {}
    no_dependency_data = []
    gitLink = []
    gh = xkcd2347.GitHub(key = git_hub_key)

    with open(input_file, 'r') as fp:
        gitLink = fp.readlines()

    with open(output_file, 'a') as fp:
        for link in tqdm(gitLink):
            link = link.rstrip()
            owner, repo = link.split(".com/")[1].split("/")
            result = [dep['packageName'] for dep in gh.get_dependencies(repo_owner = owner, repo_name = repo, depth = hop)]
            dependency_data = {}
            if(len(result) > 0):
                dependency_data[link] = result
                json.dump(dependency_data, fp)
                fp.write("\n")
            else:
                no_dependency_data.append(link)

    with open('no_result_data_' + output_file, 'w') as fp:
        json.dump(no_dependency_data, fp)




if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    git_hub_key = sys.argv[3]
    hop = sys.argv[4]
    getDependencies(input_file, output_file, git_hub_key, hop)