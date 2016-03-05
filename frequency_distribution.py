#/bin/python

# Main idea: Count the words in a file and make a frequency distribution
# and then print out a list of the top 20 words and their frequencies
# and the bottom 20 words and their frequencies.

# Text to read in: pride-and-prejudice.txt

def get_sorted_word_freqs(freq_dist, n, reverse=False):
    """
    Sort a dictionary of word/frequency pairs and return the first n
    word/frequency pairs as a list of tuples.

    :param freq_dist: frequency distribution of words
    :type freq_dist: dict
    :param n: number of pairs to return
    :type n: int

    :returns: list of tuples containing word/frequency pairs
    :rtype: list
    """

    # Let's first turn the dictionary of word/frequency pairs into a
    # list of word/frequency tuples. This can be done automatically using
    # the "items()" method, i.e., d.items(), where d is a dictionary.
    word_freq_tuples = # FILL IN

    # Now, sort the list by the second value of every tuple (i.e., the
    # frequency part)
    # To do this, we'll use the "sorted" function and define an anonymous
    # function, i.e., a "lambda" function, to define the sorting
    word_freq_tuples = sorted(word_freq_tuples, key=lambda x: x[1])
    # This lambda function in the line above basically says, for each x in
    # word_freq_tuples, give me the index 1 part (i.e., the second part of
    # the tuple). This is what the sorting uses to sort

    # Now, we need to deal with whether or not we're sorting from lowest
    # to highest or highest to lowest. Normally, it will be the former.
    if reverse: # Same as "if reverse == True"

        # Note: Either use the "reversed" function to reverse the list and
        # assign it back to itself or use the reverse slicing trick, which
        # I really like for some reason. The reverse slicing trick goes
        # like: [1, 2, 3, 4, 5][::-1] # ==> [5, 4, 3, 2, 1]. The "[::-1]"
        # part is the slicer.
        word_freq_tuples = # FILL IN

    # Now, we need to return a list of first n samples in the list
    # Hint: Use slicing to get the first n elements in the list and return
    # only that part of the list
    n_word_freq_tuples = # FILL IN

    return n_word_freq_tuples


def print_most_common(freq_dist):
    """
    Print out the 20 most common words and their frequencies.

    :param freq_dist: frequency distribution of words
    :type freq_dist: dict

    :returns: None
    """

    # Call "get_sorted_word_freqs" with the correct parameters (is this one
    # the one where the "reverse" parameter has to be specified or is it
    # the other one?)
    # Hint: Remember to use the "freq_dist" parameter that gets passed
    # in to this function!
    # FILL IN


def print_least_common(freq_dist):
    """
    Print out the 20 least common words and their frequencies.

    :param freq_dist: frequency distribution of words
    :type freq_dist: dict

    :returns: None
    """

    # Call "get_sorted_word_freqs" with the correct parameters
    # FILL IN


def get_freq_dist(word_list):
    """
    Make a dictionary that has word-to-frequency mappings.

    :param word_list: list of word tokens
    :type word_list: list

    :returns: dictionary of word-to-frequency mappings
    :rtype: dict
    """

    # Make empty dictionary
    word_freqs = {}

    # Iterate over the words in the word list and, for each word, check if
    # it's in "word_freqs": if it is, add 1 to the number and, if it's
    # not, add an entry for the word to the dictionary and then set it to
    # 1
    # Hint: To check whether a word is in the dictionary, use the "get()"
    # method, i.e., word_freqs.get(word)
    for word in word_list:

        # Check if the word is in the dictionary first; if it is, you can
        # just add 1 to its current frequency value
        if # FILL IN
            # FILL IN

        # Now deal with the situation where the word is not yet in the
        # dictionary
        else:
            # FILL IN

    return word_freqs


def main():

    # Read in the file
    inf = open # finish the line, file's name is "pride-and-prejudice.txt"

    # Let's make a list of the words that occur in the text
    # Note: Don't worry about commas and weird stuff in the text. Just
    # assume that every line looks like "this is a line", no weird stuff.
    words = []
    for line in inf.readlines():

        # Strip off spaces at the ends of the line (either beginning or
        # end) and lower-case the line, but do it in only one line, hint:
        # use the "strip()" method and the "lower()" method and chain them
        # together
        line = # FILL IN
        # Note: The line above starts off with "line = ...". This
        # will just change the value of the "line" variable, so we can
        # keep reusing the same name and not need to create new variables
        # for each step. Although, obviously, once it's been changed, its
        # original value can't be recovered (unless you specifically save
        # it to a different variable, for example).

        # Split line on whitespace to get actual words, hint: use the
        # "split()" method
        # Note: This will turn the string into a list of strings, so,
        # after executing, "line" will be a list of strings, not a string.
        line = # FILL IN

        # Add words to list of words
        # Hint: use "extend()" method on the words list
        # Question: Why can't you just use append() instead of extend()?
        # FILL IN

    # Ok, now we got a big, big list of words
    # In order to deal with it, I'm going to explain what I think you
    # should do and I want you to do it, but there's a twist. I want you
    # to implement it in a function which is actually above. It's called
    # get_freq_dist() and it accepts a list of words. This is what
    # learning programming is all about. You find out what a function
    # needs and you build that so that you can use the function or you
    # are tasked with designing a function that is supposed to handle a
    # thing like a list and do something like get the frequencies of all
    # the items. So, you'll do that now.
    freq_dist = get_freq_dist(words)

    # Now, for the last part
    # This is going to be a little more difficult in some ways. What I
    # want you to do is implement a "print_most_common" method AND a
    # "print_least_common" method. Each one will print out the 20
    # most/least common words and their corresponding frequencies.
    # Sounds simple enough, right? Wrong! I want you to actually also
    # implement a third, more abstract function called
    # "get_sorted_word_freqs", which will be used by both of the other
    # methods. This function will return a list of word/frequency pairs
    # sorted by frequency and it will have an option return the pairs
    # in reverse (i.e., to make it simpler for the "print_least_common"
    # method). See the functions/method above for more info. Hint: work
    # on the more abstract function first. It will be used by the other
    # methods, so it should be finished first.
    print_most_common(word_freqs)
    print_least_common(word_freqs)

    # Extra credit: Modify the functions called in the lines above so
    # that they return lists of tuples instead. Then, call them and
    # write their contents to two different files called
    # "20_most_frequent_words.txt" and "20_least_frequent_words.txt".


if __name__ == '__main__':
    main()
