#!/bin/zsh
echo "hello"
# create the main dirctory 
mkdir -p bioinformatics_project

#create three subdirctories
mkdir -p bioinformatics_project/data
mkdir -p bioinformatics_project/scripts
mkdir -p bioinformatics_project/results

#create three empty python files in scripts dirctory
touch bioinformatics_project/scripts/generate_fasta.py
touch bioinformatics_project/scripts/dna_operations.py
touch bioinformatics_project/scripts/find_cutsites.py

#create an empty text file in results dirctory
touch bioinformatics_project/results/cutsite_summary.txt

#create an empty files in data dirctory
touch bioinformatics_project/data/random_sequence.fasta

#create README file in main dirctory
touch bioinformatics_project/README.md
#add a brief description into README file
echo "Bioinformatics project: " >> bioinformatics_project/README.md
echo "In this project's repository, the big structure looks like below:

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
└── README.md" >> bioinformatics_project/README.md
echo "" >> bioinformatics_project/README.md

echo " -  The generate_fasta.py file generate random DNA sequence base pairs 1 million times and store it in random_sequence.fasta file" >> bioinformatics_project/README.md

echo " -  dna_operations.py file finds the complement, reverse, and reversed complement of a DNA sequence" >> bioinformatics_project/README.md

echo " -  find_cutsites.py file uses the output from generate_fasta.py and find how many times a certain restriction enzymes cut DNA occur and write the output to cutsite_summary.txt file" >> bioinformatics_project/README.md

