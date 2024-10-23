import argparse

def main():
    #Initialize argparse
    parser = argparse.ArgumentParser()
    #Add arguments
    parser.add_argument("FASTA_file", help="The FASTA file.")
    parser.add_argument("cut_site", help="The cut site sequence")
    #Parse the arguments
    args = parser.parse_args()

    #Open file to read
    try:
        with open(args.FASTA_file,'r') as inputF:
            seq = inputF.read()

    #Catch all the possible errors and display to the console
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission error")
    except Exception as exception:
        print(f"An unexpected error occured: {exception}")

    #Delete all the newline chars and spaces
    seq = seq.replace(" ", "").replace("\n", "")

    #Remove | character in user input
    cut_site = args.cut_site.replace("|", "")

    #Find all the occuring sequences
    index = seq.find(cut_site)
    position = []
    while index != -1:
        position.append(index)
        index = seq.find(cut_site, index + 1)
    total_cut_site = len(position)
    
    #Find cut site pairs that are within 80-120 kbp range
    #Use two pointers, one points to the first part of the pair
    #second points to the second part of the pair.
    ind1 = 0
    ind2 = 1
    pair = []
    while ind1 < len(position)-1:
        #Case 1: if the second pointer reaches to the end, then only
        # move the first pointer to the next
        if ind2 == len(position)-1:
            ind1 += 1
        
        #Case 2: if the pair subtraction is less than 80000, then move 
        # the second pointer to the right
        elif position[ind2] - position[ind1] < 80000:
            ind2+=1 

        #Case 3: if the pair subtraction is within the range, then move 
        # the second pointer to the right
        elif position[ind2] - position[ind1] >= 80000 and position[ind2] - position[ind1] <= 120000:
            #Store the values to a matrix
            pair.append([position[ind1], position[ind2]])
            ind2+=1

        #Case 4: if the pair subtraction is greater than 120000, then move 
        # the left pointer to the right
        elif position[ind2] - position[ind1] > 120000:
            ind1+=1
    cut_site_pairs = len(pair)


    #Print the results
    print(f"Analyzing cut site: {args.cut_site}")
    print(f"Total cut sites found: {total_cut_site}")
    print(f"Cut site pairs 80-120 kbp apart: {cut_site_pairs}")
    print(f"First 5 pairs: ")
    #Loop through the matrix and print the first 5 pairs
    first_five = 0
    while(first_five < 5):
        print(f"{first_five+1}. {pair[first_five][0]} - {pair[first_five][1]}")
        first_five+=1

    #Open the output file, and write the summary to it
    first_five = 0
    try: 
        with open("results/cutsite_summary.txt","w")as outputF:
            outputF.write(f"Analyzing cut site: {args.cut_site}\n")
            outputF.write(f"Total cut sites found: {total_cut_site}\n")  
            outputF.write(f"Cut site pairs 80-120 kbp apart: {cut_site_pairs}\n")
            outputF.write(f"First 5 pairs: \n")
            while(first_five < 5):
                outputF.write(f"{first_five+1}. {pair[first_five][0]} - {pair[first_five][1]}\n")
                first_five+=1
                
    #Check for errors
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission error")
    except Exception as exception:
        print(f"An unexpected error occured: {exception}")      
                        

    

if __name__ == "__main__":
    main()

