#!/bin/python

def main():
    # Read in the lines from reviews.txt and lower-case them and then
    # write out the new lines to a new file called
    # `reviews_normalized.txt`
    inf = open('data/reviews.txt')

    # Store the reviews in a list
    reviews = []

    # Iterate over the lines in `reviews.txt` and add the normalized
    # lines to the reviews list
    for line in inf.readlines():
        # Fill in the code here to lower-case the line and append it to
        # the reviews list (hint: Use the `lower()` method to
        # lower-case the line and the `append()` method to append to
        # the reviews list)
    inf.close()

    # Write new file that contains normalized lines
    outf = open('reviews_normalized.txt', 'w')
    for review in reviews:
        # Fill in the code here to write the review to the output file
        # Hint: Use the `outf.write()` method to write the string to
        # the file, but remember that you'll have to add a newline,
        # "\n", to the end of each line so that each review text is on
        # a separate line)
    outf.close()


if __name__ == '__main__':
    main()
