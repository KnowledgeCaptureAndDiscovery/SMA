# SMA
Software metadata analysis repository


## Clustering analysis based on Param's data (3k repos with dependency files)

1. Kmeans
2. GMM
3. Topic Modeling


### Dependency Extractor

The current version of GitHub dependecy extractor is a fork of xkcd2347. The inital setup is the same as found of the github page https://github.com/edsu/xkcd2347

To get dependency run the following command:

The command takes four inputs
- input file name
- output_file
- git_hub_key
- hop 

The output i.e. the list of dependencies in written the output file in the form of a json

```sh
$ python dependency_ectractor.py <<input_file>> <<output_file>> <<git_hub_key>> <<hop>>
```
