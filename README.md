# CS321-NNHNL
how to use stanza(stanford) for parser
1. pip install stanza
2. run python parser.py input.conllu output.conllu
This script takes a CoNLL-U file, processes it with Stanza, updates the dependencies (DEPREL) and outputs the result to a new CoNLL-U file with a blank column at the end.
If you want to calculate UAS and LAS between groundtruth and predict
run python score.py groundtruth.conllu predict.conllu
