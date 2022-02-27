from bs4 import BeautifulSoup
import requests
import sys
import json
import argparse

def main():
    parser = argparse.ArgumentParser(description='Dictionary Configurations')
    parser.add_argument("--dictionaries", dest="dictionaries", type=comma_separated)
    parser.add_argument("--output_file", dest="output_file", type=argparse.FileType('w'))#, encoding='UTF-8'))
    args = parser.parse_args()

    dictionaries = ["tagalog", "cebuano", "hiligaynon", "ilocano"]
    dictionaries_requested = dictionaries
    if args.dictionaries:
        specified_dictionaries = [dictionary for dictionary in args.dictionaries if dictionary in dictionaries]
        if specified_dictionaries:
            dictionaries_requested = specified_dictionaries

    print("Getting words from the following dictionaries: {}\n".format(", ".join(dictionaries_requested)))

    words_from_all_dictionaries = []
    for dictionary in dictionaries_requested:
        words_from_all_dictionaries += get_all_words(dictionary)
    jsonString = json.dumps(words_from_all_dictionaries, indent = 4)

    output_to_file_successful = False
    if args.output_file:
        args.output_file.write(jsonString)
        output_to_file_successful = True
    
    if output_to_file_successful:
        print("Operation done! Successfully scraped {} words.".format(len(words_from_all_dictionaries)))
    else:
        print(jsonString)

def get_words(dictionary, starting_letter):
    page_number = 1
    words = []
    while True:
        # The last slash is important as removing it results in a 404.
        url = "https://{}.pinoydictionary.com/list/{}/{}/".format(dictionary, starting_letter, page_number)
        print("Reading {}...".format(url))
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        
        page_not_found = soup.find(class_="page-not-found")
        if page_not_found:
            break
        
        word_groups = soup.find_all(class_="word-group")
        if not word_groups:
            break
        for word_group in word_groups:
            word_html = word_group.find(class_="word")
            word_entry_html = word_html.find(class_="word-entry").find("a")
            definition_html = word_group.find(class_="definition")

            word = word_entry_html.text
            link = word_entry_html.get("href")
            definition = definition_html.text
            language = word_html.find("p").text
            words.append({"word": word, "link": link, "definition": definition, "language": language})
        page_number += 1
    return words

def get_all_words(dictionary):
    starting_letters = "abcdefghijklmnopqrstuvwxyz"
    all_words = []
    for starting_letter in starting_letters:
        all_words += get_words(dictionary, starting_letter)
    return all_words

def comma_separated(string):
    return string.split(",")

main()