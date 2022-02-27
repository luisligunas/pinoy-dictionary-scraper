import argparse
import functools
import json

def main():
    parser = argparse.ArgumentParser(description='Combination IO')
    parser.add_argument("--input_files", dest="input_files", type=argparse.FileType('r', encoding='UTF-8'), nargs="+", required=True)
    parser.add_argument("--output_file", dest="output_file", type=argparse.FileType('w', encoding='UTF-8'))
    args = parser.parse_args()

    filipino_dictionary = []
    for input_file in args.input_files:
        dictionary = json.load(input_file)
        
        for entry in dictionary:
            filipino_dictionary.append(entry)
    filipino_dictionary.sort(key=functools.cmp_to_key(word_compare))

    output_string = json.dumps(filipino_dictionary, indent = 4, ensure_ascii=False)

    output_to_file_successful = False
    if args.output_file:
        args.output_file.write(output_string)
        output_to_file_successful = True
    
    if output_to_file_successful:
        print("Operation done! Successfully retrieved {} words.".format(len(filipino_dictionary)))
    else:
        print(output_string)

def word_compare(item1, item2):
    if item1["word"] < item2["word"]:
        return -1
    if item1["word"] == item2["word"]:
        return 0
    return 1

main()