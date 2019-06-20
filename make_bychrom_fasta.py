__author__ = 'odergai'

"""The script makes separate gz files for each chromosome.
    Args:
        -fa : path to source file (fasta file in  .gz format)
        -o : path to out

    Writes:
        fasta.gz file for each chromosome
    """

import os
import gzip
import sys
import argparse
import binascii


try:
    parser = argparse.ArgumentParser(description = "The script makes separate gz files for each chromosome")
    parser.add_argument("-fa","--fasta", dest="sourceFile", type=str, help="path to fasta.gz file")
    parser.add_argument("-o", "--output", dest = 'output_path', type = str,
                        help='path_to_genome file')
    args = parser.parse_args()
except NameError:
    sys.stderr.write(
            "An exception occured with argument parsing. Check your provided options.")

# sourceFile = sys.argv[1]
# output_path = sys.argv[2]

sourceFile=args.sourceFile
output_path=args.output_path

if not os.path.exists(output_path):
    os.makedirs(output_path)
if not os.access(output_path, os.W_OK):
    print('Check permissions')
    exit()


if sourceFile[-3:] == '.gz':
    file_name = None
    with gzip.open(sourceFile, "rt") as F:
        for line in F:
            if line.startswith('>'):
                line = line.rstrip('\n')
                if file_name is None:
                    file_name = line.split(' ')[0][1:]+'.fasta.gz'
                    chrom_file = gzip.open(output_path+'/'+file_name, "wt")
                else:
                    chrom_file.close()
                    file_name = line.split(' ')[0][1:] +'.fasta.gz'
                    chrom_file = gzip.open(output_path+'/'+file_name, "wt")

            else:
                chrom_file.write(line)
elif sourceFile[-3:] == '.fa':
    file_name = None
    with open(sourceFile, "r") as F:
        for line in F:
            if line.startswith('>'):
                line = line.rstrip('\n')
                if file_name is None:
                    file_name = line.split(' ')[0][1:] + '.fasta.gz'
                    chrom_file = open(output_path + '/' + file_name, "w")
                else:
                    chrom_file.close()
                    file_name = line.split(' ')[0][1:] + '.fasta.gz'
                    chrom_file = open(output_path + '/' + file_name, "w")

            else:
                chrom_file.write(line)
else:
    print('input file should be fasta with extension .fa or gzipped fasta with extension .gz')
    exit()
chrom_file.close()