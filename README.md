# DC3 - A Diagnostic Case Challenge Collection for Clinical Decision Support
DC3 is a collection of 31 extremely difficult diagnostic case challenges, that were manually compiled and solved by clinical experts. For each case, there are a number of temporally ordered physician-generated observations alongside the eventually confirmed true diagnosis. We additionally provide inferred dense relevance judgments for these cases in the [PubMed Collection](https://www.ncbi.nlm.nih.gov/pubmed/) of scholarly biomedical articles.

## Dataset Description
The dataset is described in detail in our [ICTIR 2019 paper]().

## Requirements
* python > 2.7
* requests
* json
* datetime
* bs4

## Obtaining the Collection
For copyright reasons we cannot directly share the collection and instead provide a Python script that scrapes the collection for you. Running the following command: 
```
python download.py
```
will generate the `dc3.json` file containing all 31 case related topics.

To evaluate your diagnostic decision support system, `qrels.txt` contains inferred dense relevance judgments for the 2018 snapshot of the National Library of Medicine's PubMed database in [trec_eval](https://github.com/usnistgov/trec_eval) format.

## Citing DC3
If you want to refer to DC3, please cite:

```
@INPROCEEDINGS{eickhoff2019diagnostic,
  title={{DC$^3$ -- A Diagnostic Case Challenge Collection}},
  author={Eickhoff, Carsten and Gmehlin, Floran and Patel, Anu and Boullier, Jocelyn and Fraser, Hamish},
  booktitle={{Proceedings of the 5th ACM SIGIR International Conference on the Theory of Information Retrieval (ICTIR)}},
  year={2019},
  organization={ACM}
}
```
