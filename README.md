# python_applied
- Python tutorial via actually using Python to do things

1. Reading in a file, doing something with the read-in content, and then writing a new file with the modified content
    - Files: `normalize_reviews.py`, `reviews.txt`
    - Each line of `reviews.txt` contains a review of a video game.
    - Task: Read in each line from `reviews.txt`, lower-case it, then write it to a new file named `reviews_normalized.txt`.
    - Run the Python script with: `python normalize_reviews.py` (after it's been modified by filling in the parts indicated by comments)
    - As elsewhere, it might be best to make a copy of the script and call it something else and run that script file instead.

2. Reading in a big text file, counting all the words, and making a frequency distribution
    - Files: `frequency_distribution.py`, `pride-and-prejudice.txt`
    - `pride-and-prejudice.txt` contains the raw text of--you guessed it--Pride and Prejudice by Jane Austen, a mostly random selection
    - Task: Read in the text of the novel, process the text a little bit (lower-case, split into tokens, etc.), then make a frequency distribution of the words and print out the 20 most/least common words.
    - Run the Python script with: `python frequency_distribution.py` (after it's been modified)
    - As elsewhere, it might be best to make a copy of the script and call it something else and run that script file instead.

3. Processing text files and computing features and compiling a spreadsheet; an introduction to object-oriented programming (for better or worse)
    - Files: `text_processor.py` (Python script) and a bunch of text files (`pride-and-prejudice.txt`, `alices_adventures_in_wonderland.txt`, `dracula.txt`, emma.txt`, `metamorphosis.txt`, `war_and_peace.txt`, `beowulf.txt`, `dubliners.txt`, `heart_of_darkness.txt`, and `ulysses.txt`)
    - `text_processor.py` contains the code for representing `TextProcessing` objects, i.e., an
    object that stores a text and can be used to process it (computing the frequency distribution, the number of words, etc.). It also contains the code for creating a spreadsheet of these text attributes.
    - Task: Process a set of files by calculating attributes such as the number of total words, the number of unique words, and the top 20 most frequent words, and compile this information itno a spreadsheet. Do this for all of the texts specified by the user when the script is run.
    - Run the Python script with: `python text_processor.py FILE1[ FILE2][ FILE3]...`, where `FILE1`, etc., refer to the names of specific text files to process. A bunch of text files listed above have been added to the repository. The user can pick any number of these texts to use (maybe all of them).
    - As elsewhere, it might be best to make a copy of the script and call it something else and run that script file instead.
