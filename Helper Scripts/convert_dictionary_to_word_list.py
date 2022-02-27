import json
import argparse

def main():
    parser = argparse.ArgumentParser(description='Conversion IO')
    parser.add_argument("--input_file", dest="input_file", type=argparse.FileType('r', encoding='UTF-8'), required=True)
    parser.add_argument("--output_file", dest="output_file", type=argparse.FileType('w', encoding='UTF-8'))
    parser.add_argument("--output_type", dest="output_type", type=str)
    args = parser.parse_args()

    dictionary = json.load(args.input_file)
    word_list = []
    for entry in dictionary:
        word_list.append(entry["word"])
    word_list.sort()

    output_string = ""
    if args.output_type == "txt":
        output_string = "\n".join(word_list)
    else:
        output_string = json.dumps(word_list, indent = 4, ensure_ascii=False)

    output_to_file_successful = False
    if args.output_file:
        args.output_file.write(output_string)
        output_to_file_successful = True
    
    if output_to_file_successful:
        print("Operation done! Successfully retrieved {} words.".format(len(word_list)))
    else:
        print(output_string)

main()