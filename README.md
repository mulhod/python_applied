# python_applied
- Python tutorial via actually using Python to do things

1. Reading in a file, doing something with the read-in content, and then writing a new file with the modified content
    - Files: `normalize_reviews.py`, `data/reviews.txt`
    - Each line in `data/reviews.txt` contains a review of a video game.
    - Task: Read in each line from `data/reviews.txt`, lower-case it, then write it to a new file named `reviews_normalized.txt`.
    - Run the Python script with: `python normalize_reviews.py` (after it's been modified by filling in the parts indicated by comments)
    - As elsewhere, it might be best to make a copy of the script and call it something else and run that script file instead.

2. Reading in a big text file, counting all the words, and making a frequency distribution
    - Files: `frequency_distribution.py`, `data/pride_and_prejudice.txt`
    - `data/pride_and_prejudice.txt` contains the raw text of--you guessed it--"Pride and Prejudice" by Jane Austen, a mostly random selection
    - Task: Read in the text of the novel, process the text a little bit (lower-case, split into tokens, etc.), then make a frequency distribution of the words and print out the 20 most/least common words.
    - Run the Python script with: `python frequency_distribution.py` (after it's been modified)
    - As elsewhere, it might be best to make a copy of the script and call it something else and run that script file instead.

3. Processing text files and computing features and compiling a spreadsheet; an introduction to object-oriented programming (for better or worse)
    - Files: `text_processor.py` and `frequency_distribution.py` (Python scripts) and a bunch of text files contained in the `data` directory (`pride_and_prejudice.txt`, `alices_adventures_in_wonderland.txt`, `dracula.txt`, `emma.txt`, `metamorphosis.txt`, `war_and_peace.txt`, `beowulf.txt`, `dubliners.txt`, `heart_of_darkness.txt`, and `ulysses.txt`)
    - `text_processor.py` contains the code for representing `TextProcessing` objects, i.e., a type of object that stores a text and can be used to process it (computing the frequency distribution, the number of words, etc.). It also contains the code for creating a spreadsheet of these text attributes.
    - Task: Process a set of files by calculating the number of total words, the number of unique words, and the top 20 most frequent words and compile this information into a spreadsheet (named `processed_texts.tsv`). Do this for all of the texts specified by the user when the script is run.
    - Run the Python script with: `python text_processor.py FILE1[ FILE2][ FILE3]...`, where `FILE1`, etc., refer to the paths to specific text files to process. A bunch of text files listed above have been added to the repository. The user can pick any number of these texts to use (maybe all of them). Example command:
        ```
        python text_processor.py data/alices_adventures_in_wonderland.txt data/beowulf.txt data/dracula.txt data/dubliners.txt data/emma.txt data/heart_of_darkness.txt data/metamorphosis.txt data/ulysses.txt data/war_and_peace.txt data/pride_and_prejudice.txt
        ```
    - As elsewhere, it might be best to make a copy of the script and call it something else and run that script file instead.

4. Linked list implementation: Implement a data structure called a "linked list", which is basically a list. Python already has a `list` type, of course. But this exercise, which is probably a good deal more difficult than those that have come before, is all about implementing a `list`-like container data structure from scratch.
    - Files: `LinkedList.py` and `data/pride_and_prejudice.txt`
    - Task: Implement a linked list type and interact with it.
    - Run the Python script with: `python LinkedList.py`
    - As always, it might be best to make a copy of the script and call it something else and run that script file instead.