import csv
from sys import argv
import os.path


def main():

    # TODO: Check for command-line usage
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # TODO: Read database file into a variable
    try:
        with open(argv[1]) as csvfile:
            csv_reader = csv.DictReader(csvfile) 
            sequences_csv = list(csv_reader)
            # print(sequences_csv)
            keys = list(sequences_csv[0].keys())
            keys = keys[1:]
            # print(keys)
    except FileNotFoundError:
        print("file not found")

    # TODO: Read DNA sequence file into a variable
    try:
        with open(argv[2]) as dna:
            dna_reader = dna.read()
            # for j in dna_reader:
            # print(j, end= '')
    except FileNotFoundError:
        print("file not found")

    # TODO: Find longest match of each STR in DNA sequence
    dict_sequence = {}
    for i in keys:
        count_run = longest_match(dna_reader, i)
        dict_sequence[i] = str(count_run)
    # print(dict_sequence)
    # print(sequences_csv)

    # TODO: Check database for matching profiles
    name = "No match"
    for row in sequences_csv:
        copy = {}
        for key, value in row.items():
            if key != "name":
                copy[key] = value
            if copy == dict_sequence:
                name = row['name']
                break
    print(name)
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
