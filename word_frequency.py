STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

import string

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    #open the file to be read, read it, and assign to open_doc
    with open(file, 'r') as reader:
        open_doc = reader.read()
    print(open_doc)
    #remove puntion from string before breaking it to a list
    for character in open_doc:
        if character in string.punctuation:
            open_doc = open_doc.replace(character, "")
    #split the open_doc into a list of lower case strings for each word
    new_list = open_doc.lower().split()
    print(new_list)
    word_count_dict = {}
    for word in new_list:
        if word in word_count_dict.keys():
            word_count_dict[word] = word_count_dict[word] + 1
            print(word_count_dict)
        else:
            word_count_dict[word] = 1
    print(word_count_dict, " out of if")
    print(word_count_dict.keys())

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
