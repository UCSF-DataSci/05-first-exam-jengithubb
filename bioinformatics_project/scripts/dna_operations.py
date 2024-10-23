import argparse
#This function returns the complement of a sequence
def complement(sequence):
    #initialize an empty string
    result = ''
    #stores the key value pairs
    mydict = {
            "A" : "T",
            "T" : "A",
            "C" : "G",
            "G" : "C"
        } 
    #loop through the sequence and replace each character with its complement
    for char in sequence:
        result += mydict[char]
    return result

#This function returns the reversed sequence
def reverse(sequence):
    return sequence[::-1]

#This function returns the reversed complement of a sequence
def reverse_complement(sequence):
    return reverse(complement(sequence))

#This function change a sequence to uppercase
def uppercase(sequence):
    return sequence.upper()

def main():
    #Initialize argparse
    parser = argparse.ArgumentParser()
    #Add arguments
    parser.add_argument("sequence", type = uppercase, help="The sequence.")
    #Parse the arguments
    args = parser.parse_args()

    print(f"Original sequence: {args.sequence}")
    print(f"Complement: {complement(args.sequence)}")
    print(f"Reverse: {reverse(args.sequence)}")
    print(f"Reverse complement: {reverse_complement(args.sequence)}")

if __name__ == "__main__":
    main()
