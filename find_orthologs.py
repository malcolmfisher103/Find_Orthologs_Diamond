#!/usr/bin/python3.8

'''
Script for finding orthologs using reciprocal BLAST hits.

Sript usage is as follows:
    ./find_orthologs.py -i1 <Input file 1> -i2 <Input file 2> -o <Output file name>

'''
import argparse
import subprocess

def get_reciprocal_hits(file_one,file_two):
    
    a = []                  #List a stores the first index headers (db values)
    a1 = []                 #List a1 stores the second index headers (query headers)
    b = []                  #List b stores the first index headers (db values)
    b1 = []
    output_list_1 = []
    output_list_2 = []      #Inversing the list in order to find common things bw output_list_1 and output_list_2
    output_list = []        #Contains only reciprocal blast hits
    
    if not file_one:
        print('No input file specified')
    else:
        file_1_db = "diamond makedb --in " + str(file_one) + " -d tmp/db1"   #Creating db for input1
        file_1_db_subprocess = subprocess.check_output(file_1_db.split())
        
        result_1 = "diamond blastp -d tmp/db1.dmnd -q " + str(file_two) + " --iterate --very-sensitive --max-target-seqs 1 --max-hsps 1 --outfmt 6 --out tmp/output_file_1" #Output for query = input2 and db = input1
        result_1_subprocess = subprocess.check_output(result_1.split())
        
        file_2_db = "diamond makedb --in " + str(file_two) + " -d tmp/db2"   #Creating db for input2
        file_2_db_subprocess = subprocess.check_output(file_2_db.split())
        
        result_2 = "diamond blastp -d tmp/db2.dmnd -q " + str(file_one) + " --iterate --very-sensitive --max-target-seqs 1 --max-hsps 1 --outfmt 6 --out tmp/output_file_2" #Output for query = input1 and db = input2
        result_2_subprocess = subprocess.check_output(result_2.split())
        
        with open("tmp/output_file_1") as fh1:
            for line in fh1.readlines():
                a.append(line.split()[0])
                a1.append(line.split()[1])
                    
        for i,j in zip(a,a1):
            output_list_1.append(i+"\t"+j+"\n")
            
        with open("tmp/output_file_2") as fh2:
            for line in fh2.readlines():
                b.append(line.split()[0])
                b1.append(line.split()[1])
                    
        for i,j in zip(b,b1):
            output_list_2.append(j+"\t"+i+"\n")
            
        for x in output_list_1:         #Checking common hits beween output_list_1 and output_list_2
            if x in output_list_2:
                output_list.append(x)   #Contains only reciprocal blast hits
    return(output_list)

def main():
    # Argparse code

    parser = argparse.ArgumentParser()
    parser.add_argument("-i1", help = "Takes in input sequence 1.")
    parser.add_argument("-i2", help = "Takes in input sequence 2.")
    parser.add_argument("-o", help = "Your output file.")
    args = parser.parse_args()

    file_one = args.i1             #Populating the variables
    file_two = args.i2
    output_file = args.o

    # Subprocess code

    '''
    output_list is a list of reciprocal BLAST hits. Each element is a tab
    separated pair of gene names. Eg:
    ["A0A5S6MBM4|A0A5S6MBM4_XENTR	XBXT10g000564|mRNA002866|runx1t1", "A0A6I8Q0X6|A0A6I8Q0X6_XENTR	XBXT10g012953|mRNA064117|ano10", "A0A6I8Q7J7|A0A6I8Q7J7_XENTR	XBXT10g020004|mRNA098774|LOC101733477", ...]
    '''

    make_dir = "mkdir tmp"
    subprocess.call(make_dir.split())

    output_list = get_reciprocal_hits(file_one, file_two)
    with open(output_file, 'w') as output_fh:
        for ortholog_pair in output_list:
            output_fh.write(ortholog_pair)

    remove_dir = "rm -rf tmp"
    subprocess.call(remove_dir.split())

if __name__ == "__main__":
    main()
    
