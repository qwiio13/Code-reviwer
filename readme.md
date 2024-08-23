# Code-reviwer
Code Reviewer is a Python library for alnalyzing your Python code

## installation
Before useage, you need to install the required dependencies:

```bash
pip install -r requirements.txt
```
Next, create Python file and run the following code:
``` python
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()
```
## usage

**Options:**

- Use "all to analyze all words.
- Use "vb to analyze only vebs.
- Use "nn to analyze only noun.

To run the word count script:

```bash
python3 word_count.py all/vb/nn
```

**Flags:** 

- **-stream**: Specify the output format. Options are "txt", "json", "csv", or "print". The default is "print".

```bash
python3 word_count.py all -stream txt/json/csv/print
```

**-clone**: Clone a repository from a given URL and analyze it.

```bash
python3 word_count.py -clone your_url_rep
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
