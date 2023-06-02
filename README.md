# Pset6-CS50x

## Description:
I re-implemented cash, hello, mario , readability in Python.

- **folder dna**:
    - Backround: 
        - What might such a DNA database look like? Well, in its simplest form, you could imagine formatting a DNA database as a CSV file, wherein each row corresponds to an individual, and each column corresponds to a particular STR.

            ```
            name,AGAT,AATG,TATC
            Alice,28,42,14
            Bob,17,22,19
            Charlie,36,18,25

            ```
        - The data in the above file would suggest that Alice has the sequence AGAT repeated 28 times consecutively somewhere in her DNA, the sequence AATG repeated 42 times, and TATC repeated 14 times. Bob, meanwhile, has those same three STRs repeated 17 times, 22 times, and 19 times, respectively. And Charlie has those same three STRs repeated 36, 18, and 25 times, respectively.

        - So given a sequence of DNA, how might you identify to whom it belongs? Well, imagine that you looked through the DNA sequence for the longest consecutive sequence of repeated AGATs and found that the longest sequence was 17 repeats long. If you then found that the longest sequence of AATG is 22 repeats long, and the longest sequence of TATC is 19 repeats long, that would provide pretty good evidence that the DNA was Bob’s. Of course, it’s also possible that once you take the counts for each of the STRs, it doesn’t match anyone in your DNA database, in which case you have no match.

        - In practice, since analysts know on which chromosome and at which location in the DNA an STR will be found, they can localize their search to just a narrow section of DNA. But we’ll ignore that detail for this problem.

        - Your task is to write a program that will take a sequence of DNA and a CSV file containing STR counts for a list of individuals and then output to whom the DNA (most likely) belongs.

    - Implementation:
        - In a file called dna.py, implement a program that identifies to whom a sequence of DNA belongs.

        - The program should require as its first command-line argument the name of a CSV file containing the STR counts for a list of individuals and should require as its second command-line argument the name of a text file containing the DNA sequence to identify.
        - If your program is executed with the incorrect number of command-line arguments, your program should print an error message of your choice (with print). If the correct number of arguments are provided, you may assume that the first argument is indeed the filename of a valid CSV file and that the second argument is the filename of a valid text file.
        - Your program should open the CSV file and read its contents into memory.
        - You may assume that the first row of the CSV file will be the column names. The first column will be the word name and the remaining columns will be the STR sequences themselves.
        - Your program should open the DNA sequence and read its contents into memory.
        - For each of the STRs (from the first line of the CSV file), your program should compute the longest run of consecutive repeats of the STR in the DNA sequence to identify. Notice that we’ve defined a helper function for you, longest_match, which will do just that!
        - If the STR counts match exactly with any of the individuals in the CSV file, your program should print out the name of the matching individual.
        - You may assume that the STR counts will not match more than one individual.
        - If the STR counts do not match exactly with any of the individuals in the CSV file, your program should print No match.

    - Usage:
        - Your program should behave per the example below:
            ```
                $ python dna.py databases/large.csv sequences/5.txt
                Lavender
                $ python dna.py
                Usage: python dna.py data.csv sequence.txt
                $ python dna.py data.csv
                Usage: python dna.py data.csv sequence.txt
            ```


Note : figlet and bank folders are some practice.