import numpy
import random
random.seed(3)

# Sets length of control documents, in words. Choose documents whose word count
# is greater than or equal to the intended length of your control docs.

# Works well with 10000 word docs in 10 chunks
final_len = 100000
# Make sure your document length is evenly divisible by your number of chunks
chunk_number = 10
# These are the filenames of the texts we are using to create the controls
things_to_check = ['File_1.txt', 'File_2.txt']
# Here are the percents to replace, as decimals.
percents_to_check = [0, .01, .02, .05, .1, .25, .5, 1]

texts = []
# read in texts, and split them on whitespace
for name in things_to_check:
    with open(name, 'r', encoding='utf8')as my_file:
        text1 = my_file.read()
        texts.append(text1.split())


def block_maker(in_text, size):
    # returns a random block of words of the specified size
    if len(in_text) < size:
        print("Your text is smaller than we are trying to truncate it!")
        return
    else:
        itemlen = len(item)
        extra_range = itemlen - final_len
        start_value = random.randint(0, extra_range)
        end_value = start_value + final_len
        newitem = item[start_value:end_value]
        return newitem


sized_texts = []
for item in texts:
    sized_texts.append(block_maker(item, final_len))

first_text = sized_texts[0]
second_text = sized_texts[1]


def deleter(text, percent_to_delete):
    # deletes a random chunk of the indicated percent of the input text
    rangesize = len(text) * percent_to_delete
    rangesize_int = int(rangesize)
    upper_limit = len(text) - rangesize_int
    start_value = random.randint(0, upper_limit)
    end_value = start_value + rangesize_int
    newtext = []
    [newtext.append(thing) for thing in text[0:start_value]]
    [newtext.append(thing) for thing in text[end_value:]]
    return newtext


def replacement_finder(text, percent_to_return):
    # returns a random chunk of the indicated percent of the input text
    rangesize = len(text) * percent_to_return
    rangesize_int = int(rangesize)
    upper_limit = len(text) - rangesize_int
    start_value = random.randint(0, upper_limit)
    end_value = start_value + rangesize_int
    newtext = text[start_value:end_value]
    return newtext


def chunker(text):
    # splits text into 10 chunks
    chunked = numpy.array_split(text, chunk_number)
    return chunked


def percent_swapper(target_percent, text1, text2):
    # grabs a bit from one text, and swaps it into the other document, after deleting a portion of the same size
    chunked1 = chunker(text1)
    chunked2 = chunker(text2)
    output = []
    for i in range(10):
        [output.append(j) for j in deleter(chunked1[i], target_percent)]
        [output.append(j) for j in replacement_finder(chunked2[i], target_percent)]
    return output


for value in percents_to_check:
    # this lets the filenames include the percent as an integer rather than a decimal.
    percent = value * 100
    with open('text1_' + str(percent)+'_percent_replaced.txt', 'w', encoding='utf-8') as my_file:

        final_out = ' '.join(percent_swapper(value, first_text, second_text))
        print(final_out, file=my_file)


with open('text1_control.txt', 'w', encoding='utf-8') as my_file:
    print(' '.join(first_text), file=my_file)

with open('text2_control.txt', 'w', encoding='utf-8') as my_file:
    print(' '.join(second_text), file=my_file)
