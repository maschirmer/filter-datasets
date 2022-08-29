# filter-datasets

This repo creates training dataset used for training of the BERT future reference classifier from three sources:
- Reddit dump may 2015
- twitter stream 01/02/2020
- blogs and news dataset from kaggle

there are sequential versions of the extraction scripts an parallel ones

parallel ones produced a lot out of memory errors which were hard to fix as running them on the cluster

maybe use spark instances instead of multiprocessing nex time

coarse steps:
- texts are extracted from the files and stored into csv files
- from the csv files equal proportions of texts are sampled
- data is filtered for english language
- data is shuffled
- "source" - tag is annotated
