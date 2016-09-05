#!/usr/bin/env python
from __future__ import print_function
import sys

"""
In this exercise, follow along with text below sequentially instead of
going straight to the `main` method. The real work is going to take
place outside `main`.

Using the functions defined in `normalize_reviews.py`, let's process a
bunch of texts and output some stats like how many words there are in
total, how many unique words there are, and the 10 most common words.
Keep in mind that by "word", I'm really referring to just a string in
the text. There's no requirement that it actually be a word.

For this to work, you will have to have finished the second exercise.
Furthermore, you will need to change the import line below so that it
is importing from your own module (unless you just edited the
`normalize_reviews.py` file directly instead of creating a new file
with a slightly different name).
"""
### EDIT THIS LINE BELOW IF YOUR FINISHED VERSION OF
### `frequency_distribution.py` IS NAMED SOMETHING ELSE

### NOTE: Whatever file you import from, it must be contained in the
###       same directory (and also you must run the Python program from
###       that directory). This is to ensure that this Python program
###       can find the file and import stuff from it. Python will search
###       the directory you're currently in by default.

from frequency_distribution import get_freq_dist, get_sorted_word_freqs

"""
Notice how I was able to import from `frequency_distribution` (which is
just the code that is in `frequency_distribution.py`) as if it were a
module/library/package (whatever you want to call it). This is just like
any import from the `sys` package or `re` (regular expressions), etc.
There's a reason for this: Because it's the same exact thing. Somewhere
there are files or packages named `sys` or `sys.py` and `re` or `re.py`.
When importing functions/methods from these packages, it's the same
exact thing as importing from any module that you create yourself (as
we are doing now with `frequency_distribution.py`). We can either import
`frequency_distribution` as a module directly (and then have access to
code within this module, via `frequency_distribution.get_freq_dist` or
`frequency_distribution.get_sorted_word_freqs`, for example) or we can
import certain functions or methods, etc., from the module so that we
can reference them directly without needing to include
`frequency_distribution` in the name. We can even change the names of
functions to suit our purposes. Let's say that we wanted to also import
a function that just happened to also be named `get_freq_dist` from
another module (there's nothing stopping anyone from defining functions
that conflict in name with functions defined in other places). Maybe to
keep things straight, we'll call the first one `get_freq_dist_1` and the
second one `get_freq_dist_2`:

>>> from frequency_distribution import get_freq_dist as get_freq_dist_1
>>> from other_module_that_i_didnt_write import get_freq_dist as get_freq_dist_2

Now we can use the two functions in our code and maybe compare the
performance of each or if each gives the same exact output, etc.

This exercise will also introduce you to the concept of arguments. It's
often helpful when writing a program to provide a way to interact with
the program. Providing arguments to a script when running it is one way
of doing this. In this task, you will pass in a list of one or more
text file paths to the script and it will process each text provided. If
no text paths are provided or the text file paths are not valid paths,
then an exception (i.e., error) will be raised and the program will
stop.

Go down to the `main` method and follow along with the comments until
you are directed elsewhere.
"""

class TextProcessing:
    """
    Class for representing an instance of text processing (where the
    "processing" refers to what we're specifically doing in this case,
    i.e., getting a frequency distribution and some other data about an
    input text).
    """

    def __init__(self, text_path):
        """
        Initialize a `TextProcessing` object.

        The `__init__` method is required (well, not really, but let's
        say that it is for our purposes) when creating a class in
        Python. It is called automatically when an object of type
        `TextProcessing` is created, e.g.:

        >>> text1 = TextProcessing(text_path)

        The `self` argument can be ignored for now. Simply pretend it's
        not there. However, understand that within the class's source
        code below, `self` refers to the instance itself. So, when you
        see something like "self.text = text", it's assigning the value
        of `text` (whatever it is) to an attribute named `text` that is
        part of the `TextProcessing` object. This can be referenced
        using dot notation. Consider the following:

        >>> text1 = TextProcessing(text_path)
        >>> print(text1.text)

        This will print out the `text` attribute of the `text1` object.

        :param text_path: path to text file
        :type text_path: str
        """

        # Get text from file at given path and make a `text` attribute,
        # i.e., in the line "self.text = text_file.read()" below,
        # `self.text` is the thing that actually creates the attribute
        text_file = open(text_path)
        self.text = text_file.read()
        text_file.close()

        # Save the text path
        self.text_path = text_path

        # Let's create some other attributes, but leave their values
        # assigned to None for now (their value will be computed as part
        # of this object's other methods)
        self.word_list = None
        self.freq_dist = None
        self.num_words = None
        self.num_unique_words = None
        self.top_20_words = None

        # Add some other attributes if you want, but, if you do, know
        # that you will have to design a function to compute them later
        # on

    # Make a function that processes `self.text` into a list of words
    def get_words(self):
        """
        Get list of words.
        """

        self.word_list = []

        # Iterate over the lines in `self.text` by splitting on
        # newlines ("\n")
        for line in self.text.split('\n'):

            # Make `line` lower-case and strip off spaces from either
            # end
            # Hint: Use "lower()" and "strip()" (both with no
            # arguments).
            line = ### FILL IN

            # Discard empty lines
            if line == "":
                continue

            # Split line into a list of words
            for word in line.split():
                self.word_list.append(word)

    # The next thing we want to do is design functions that will process
    # the data. Let's create one that makes a frequency distribution.
    # And, what do you know, we actually have a frequency distribution
    # function that we made in the last exercise. All we need to do is
    # create a wrapper around it.
    def get_freq_dist(self):
        """
        Use the imported `get_freq_dist` to get the frequency
        distribution.
        """

        self.freq_dist = get_freq_dist(self.word_list)

    # Make a function that returns the number of total words
    def get_num_words(self):
        """
        Get the total number of words in the text.
        """

        self.num_words = ### Fill in

    # Make a function that gets the total number of unique words
    def get_num_unique_words(self):
        """
        Get the number of unique words.
        """

        # Use `self.word_list` to compute the number of unique words
        # Hint: Use `set()` and take the length of it
        # Another way to do it would be to get the length of
        # `self.freq_dist`, which will count the keys in the dictionary.
        self.num_unique_words = ### FILL IN

    # Get the top 20 words (words only) in terms of frequency
    def get_top_20_words(self):
        """
        Get the top 20 words in the text.
        """

        self.top_20_words = []

        # Get the top 20 words by calling the `get_sorted_word_freqs`
        # function defined in the last assignment, which has already
        # been imported here and can be used directly.
        top_20_word_and_frequency_tuples = ### FILL IN

        # The code below gets the words out of the word/frequency tuples
        # contained in `top_20_word_and_frequency_tuples` computed
        # above. It uses a "list comprehension". Try to think about what
        # the list comprehension actually does.
        self.top_20_words = [word for (word, frequency)
                             in top_20_word_and_frequency_tuples]

    # So far, we have only defined functions that compute specific
    # things, but none of them are executed at any point and, in fact,
    # the order in which they are executed is important since the
    # computation of some attributes depends on the computation of
    # others. Let's create a general `process_text` function that
    # executes all of the processing functions defined above (when
    # called).
    def process_text(self):
        """
        Get all of the attributes of the text.
        """

        self.get_words()
        self.get_freq_dist()
        self.get_num_words()

        # FILL IN THE CALLS TO THE REMAINING FUNCTIONS

        # After all of the functions have been called, all of the
        # attributes defined in `__init__` will have values.
        # After finishing this part, go back to the `main` method where
        # we left off.


def main():

    # Let's read in the arguments passed in. This can be done using
    # `sys.argv`, which is a list of arguments that the user supplies
    # when the program is run. `sys.argv[0]` is the name of the script,
    # `sys.argv[1]` is the name of the first argument, `sys.argv[2]` the
    # next, and so on.
    # NOTE: Always rememner that the first value in `sys.argv` is the
    #       name of the script itself.

    # First check if any arguments were provided (other than the script
    # name itself)
    if len(sys.argv) == 1:
        raise ValueError("No arguments were passed in!")

    # Now, since we know there were arguments, let's get them and put
    # them in a list
    # We'll also check that each one is a valid path. To do this, we can
    # use the `os.path` module, which includes an `exists` function and
    # some other very useful functions. Get used to these functions
    # since they are used all the time in real programs.
    from os.path import exists, abspath, join
    text_paths = []

    # Let's iterate over the list of arguments (skipping over the
    # first). Notice the brackets following `sys.argv`. Basically, I'm
    # saying: Use everything in `sys.argv` from index 1 and up (i.e.,
    # skip over index 0). This is called "slicing". It allows you to
    # work with "slices" of a list instead of the whole thing without
    # needing to create a new list.
    for arg in sys.argv[1:]:

        # Get the absolute path (deals with arguments that have relative
        # paths, such as "../file.txt")
        text_path = abspath(arg)

        # Check if the path exists
        if not exists(text_path):
            raise ValueError("{} is an invalid path!".format(text_path))

        text_paths.append(text_path)

    # For each text, we want to get the frequency distribution and
    # calculate some other attributes. We could just iterate over the
    # list of text paths and get the frequency distribution for each one
    # and then compute each thing we want to compute and store all the
    # values in some lists or dictionaries, but let's instead define a
    # custom class to do all of this for us. While in this toy case
    # creating a class to represent each text processing instance is not
    # very necessary and maybe even more complicated than it really
    # needs to be, it will introduce you to the idea of classes and
    # objects (i.e., object-oriented programming).
    # Go up to the section above the `main` method where the
    # `TextProcessing` class is defined and follow along with the
    # comments and implement the class. Then, come back down here where
    # the class will be used to process the texts.

    # Now we'll iterate over the text file paths, processing each text
    # one at a time and add them to the `texts` (defined below). Each
    # element of this list will be an object of type `TextProcessing`
    # and will have the attributes we're looking for, including the
    # number of total words, the number of unique words, etc.
    texts = []
    for text_path in text_paths:

        print("Processing {}...".format(text_path))

        text = TextProcessing(text_path)

        ### FILL IN THIS PART THAT ACTUALLY PROCESSES THE TEXT
        # Hint: Call the `text` object's `process_text` function to
        # compute the attributes.

        texts.append(text)

    # Now, let's make an output file that compiles all of the data we
    # just computed when the texts were processed

    # This next line creates a file that we can write to
    output_file = open('processed_texts.tsv', 'w')

    # Write a header row first
    # Notice that at the end of the line that I'm printing out below
    # there is a newline ("\n"). If I didn't put this there, the next
    # time I tried to write to `output_file`, the text would just start
    # right where the string below ended (i.e., it would be on the same
    # line). This will have to be done below when new lines are written
    # to the file for each text.
    output_file.write("text_path\tnum_words\tnum_unique_words\ttop_20_words\n")

    # Let's iterate over the `TextProcessing` objects
    for text in texts:

        # Create a string that has the data indicated by the header line
        # and write it to `output_file`
        # There are many ways to do this, but the way I chose is to just
        # create an output string (for the line) with the first value,
        # then add a tab and then the next value, and so on until we're
        # finished. Remember to add a newline ("\n") at the end of the
        # line. You could choose to do all of this in one line (and it
        # would probably make it simpler and easier to read.)
        output_string = text.text_path
        output_string = output_string + '\t' + str(text.num_words)
        output_string = ### FILL IN THE REST AND REMEMBER THAT THE
                        ### VALUES NEED TO BE SEPARATED BY A TAB AS IS
                        ### DONE ABOVE
                        ### NOTE: I had to use `str` to convert the
                        ###       number of words to a string since it
                        ###       is actually an int. This will need to
                        ###       be done for the other values also.
                        ###       (But not fot `text.text_path`. Why?)

        # Write the line to the file
        ### FILL IN

    # Close the file
    output_file.close()

    print("Program complete!")


if __name__ == '__main__':
    main()
