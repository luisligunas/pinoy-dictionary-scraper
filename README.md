# Pinoy Dictionary Scraper
Scrapes Tagalog, Cebuano, Hiligaynon, and Ilocano words from [Pinoy Dictionary](https://www.pinoydictionary.com)

The scraped words can then be printed into an output file in a JSON format.

## Setup
We need to have [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) and [Requests](https://docs.python-requests.org/en/latest/) installed on the machine. If you already have these, then you should be able to run the scraper files without any additional setup.

### Pip Installation
To install BeautifulSoup and Requests, we need Python's pip package.

According to [pip's documentation](https://pip.pypa.io/en/stable/installation/#supported-methods), you can install pip by running:
```
sudo python -m ensurepip --upgrade
```

### BeautifulSoup Installation
According to [BeautifulSoup's implementation](https://beautiful-soup-4.readthedocs.io/en/latest/), you can install BeautifulSoup by running:
```
pip install beautifulsoup4
```
If this doesn't work you may have to try
```
pip install beautifulsoup4 --user
```
or
```
sudo pip install beautifulsoup4
```

### Requests Installation
According to [Requests' implementation](https://docs.python-requests.org/en/latest/user/install/#python-m-pip-install-requests), you can install Requests by running:
```
python -m pip install requests
```

## Scraping
Run the following command:
<pre>
<b>python scraper.py</b> [--dictionaries &ltdictionaries&gt] [--output_file &ltfile_name&gt]
</pre>

### Options
#### --dictionaries &lt;dictionaries&gt;
The `dictionaries` value that you should pass in should be a comma-separated string containing any of the following strings:
`"tagalog", "cebuano", "hiligaynon", "ilocano"`

For example, if you wanted to scrape the data for Tagalog, Cebuano, and Hiligaynon, you would use `--dictionaries tagalog,cebuano,hiligaynon`.

If this argument is not specified, words from all dictionaries will be scraped.

#### --output_file &lt;file_name&gt;
The `file_name` value that you should pass in should be the file that you would like to print the words in.

For example, if you wanted to print the Tagalog words into a file named `tagalog_words.json`, you would run the command `python scraper.py --dictionaries tagalog --output_file tagalog_words.json`.

It is advised to specify this argument; if it is not specified, the value will be printed out on the console (or wherever the console output may be redirected to).