Bioinformatics project: 
In this project's repository, the big structure looks like below:
'''
Jennifer's repository/
├── bioinformatics
│   ├── README.md
│   ├── data/
│   │   ├── random_sequence.fasta
│   ├── scripts/
│   │   ├── generate_fasta.py
│   │   ├── dna_operations.py
│   │   ├── find_cutsites.py
│   ├── results/
│   │   ├── cutsite_summary.txt
├── setup_project.sh
└── README.md
'''

 -  The generate_fasta.py file generate random DNA sequence base pairs 1 million times and store it in random_sequence.fasta file
 -  dna_operations.py file finds the complement, reverse, and reversed complement of a DNA sequence
 -  find_cutsites.py file uses the output from generate_fasta.py and find how many times a certain restriction enzymes cut DNA occur and write the output to cutsite_summary.txt file
