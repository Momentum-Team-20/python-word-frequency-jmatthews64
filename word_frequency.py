import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def remove_stop_words(list):
    no_stop_words = []
    for word in list:
        if word not in STOP_WORDS:
            no_stop_words.append(word)
    return no_stop_words

# meant to add white space to front of string to make it same as longest string
#def add_white_space(list):
 #   longest_word = max(list, key=len)
  #  format_length = len(longest_word)
   # white_space_list = []
    #print(format_length)
    #for each in list:
     #   while len(each) < format_length:
      #      list = " " + each
       #     print(list)


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # open the file to be read, read it, and assign to open_doc
    with open(file, 'r') as reader:
        open_doc = reader.read()
    # remove puntion from string before breaking it to a list
    for character in open_doc:
        if character in string.punctuation:
            open_doc = open_doc.replace(character, "")
    # split the open_doc into a list of lower case strings for each word
    new_list = open_doc.lower().split()
    new_clean_list = remove_stop_words(new_list)
   #add_white_space(new_clean_list)   
    # initialize a dictionary and fill it from words in new_list
    word_count_dict = {}
    for word in new_clean_list:
        if word in word_count_dict.keys():
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    # format printed output
    for each in word_count_dict:
        print(each, " | ", word_count_dict[each])


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
