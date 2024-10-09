# Find_Orthologs_Diamond
Reciprocal best hits are pairs of sequences where the best alignment hit for each sequence is the other sequence.
Consider you have a sequence A from species sA whose best hit in species sB is the sequence B. A will be considered a reciprocal best hit of B if the best hit of B in species sA is A. <br/>
Example: when you align the complete set of human coding sequences against the complete set of mouse coding sequences, the best hit for the human gene histone H3.1 is the mouse gene histone H3.1 and vice versa. These two genes would be considered reciprocal best hits and orthologous. This is an overly simplistic way of defining orthologous. If, for example, there had been a gene duplication event in mouse lineage yielding two copies of the histone H3 gene, then simply picking one as the ortholog for the human version would be a rather bad idea.

This script is a modified version of https://github.com/ahishsujay/Find_Orthologs which has been altered to use the Diamond alignment program rather than BLAST+. As Diamond is focused on protein alignments both input files should be protein sequences.

## Requirements:
1. Diamond (https://github.com/bbuchfink/diamond) for making sequence databases and aligning. Diamond must be under your path for the script to work.

## Required input files:
1. Input file 1 - Species 1 FASTA file
2. Input file 2 - Species 2 FASTA file

## Execution of the script:
`./find_orthologs_diamond.py -i1 <Input file 1> -i2 <Input file 2> -o <Output file name>`

## Output file:
A file comprising the reciprocal best hits of the two species in output format 6. 
