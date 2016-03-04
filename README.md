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
