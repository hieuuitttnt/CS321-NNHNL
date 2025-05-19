# CS321-NNHNL: Dependency Parsing with Stanza (Stanford NLP)

This project demonstrates how to use the [Stanza](https://stanfordnlp.github.io/stanza/) library from Stanford NLP for dependency parsing in CoNLL-U format, and how to evaluate parsing quality using UAS and LAS metrics.

---

## 📦 Installation

First, install the required Python package:

```bash
pip install stanza
```

You may also need to download the Stanza models (e.g., for Vietnamese):

```python
import stanza
stanza.download('vi')  # Replace 'vi' with your target language code
```

---

## ⚙️ Parsing CoNLL-U Files

To run the parser on a CoNLL-U formatted input file:

```bash
python parser.py input.conllu output.conllu
```

### Description:
- `input.conllu`: The input file in CoNLL-U format.
- `output.conllu`: The output file after processing.

The script will:
- Load the `input.conllu` file.
- Parse it with Stanza.
- Update the dependency relations (`HEAD` and `DEPREL`).
- Write the result to `output.conllu`, with a final empty column appended.

---

## 🧪 Evaluation with UAS and LAS

To evaluate parsing accuracy:

```bash
python score.py groundtruth.conllu predict.conllu
```

### Parameters:
- `groundtruth.conllu`: File containing gold-standard annotations.
- `predict.conllu`: File produced by the parser.

The script calculates:
- **UAS** (Unlabeled Attachment Score): Measures the percentage of words that have the correct head.
- **LAS** (Labeled Attachment Score): Measures the percentage of words that have both the correct head and the correct dependency label.

---

## 📁 Example Directory Structure

```
├── parser.py
├── score.py
├── input.conllu
├── output.conllu
├── groundtruth.conllu
├── predict.conllu
└── README.md
```

---

## 📚 References

- [Stanza Documentation](https://stanfordnlp.github.io/stanza/)
- [Universal Dependencies Format](https://universaldependencies.org/format.html)

---

## 👩‍💻 Authors

- CS321-NNHNL Project Team
