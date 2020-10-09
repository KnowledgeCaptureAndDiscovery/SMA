import xkcd2347
import json
from pyspark import SparkContext
from tqdm import tqdm
import sys

def getDependencies(input_file, output_file, git_hub_key, hop, partitions):
    dependency_data = {}
    no_dependency_data = []
    gitLink = []

    gh = xkcd2347.GitHub(key = git_hub_key)
    result = []

    def process_line(link):
        link = link.rstrip()
        owner, repo = link.split(".com/")[1].split("/")
        result = [dep['packageName'] for dep in gh.get_dependencies(repo_owner = owner, repo_name = repo, depth = hop)]
        if(len(result) > 0):
            return (link, result)
        else:
            return (link, ["No dependency"])
    try:
        sc = SparkContext("local[*]","PySpark Tutorial")
        result = sc.textFile(input_file, partitions).map(process_line).collect()
    except:
        print("Error running spark job")

    with open(output_file, 'w') as fp:
        json.dump(dict(result), fp, indent=4)
    sc.stop()

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    git_hub_key = sys.argv[3]
    hop = sys.argv[4]
    partitions = sys.argv[5]
    getDependencies(input_file, output_file, git_hub_key, hop, partitions)