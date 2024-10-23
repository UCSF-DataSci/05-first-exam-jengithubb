import random
import textwrap

def main():
    #Stored all the sequence
    mySeq = ["A","C","G","T"]

    #Use a loop to make 1 million base pairs
    count = 0
    result = ""
    while(count < 1000000):
        count+=1
        result = result + (mySeq[random.randint(0,3)])

    #Divide the result into 80 pairs per line
    result = textwrap.fill(result, width = 80)

    #Open and write the result to the file
    try:
        with open('./bioinformatics_project/data/random_sequence.fasta','w') as ran_seq:
                ran_seq.write(">\n")
                ran_seq.write(result)   
        print("Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta")

    #Catch all the possible errors and display to the console
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission error")
    except Exception as exception:
        print(f"An unexpected error occured: {exception}")

if __name__ == "__main__":
    main()