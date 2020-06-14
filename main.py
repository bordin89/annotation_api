#!/usr/bin/python3
from classes import parse_input_file
from classes import retrieve_blast_result 
import argparse

parser = argparse.ArgumentParser(description='With a flat FASTA file as input, tests the various APIs')
parser.add_argument("sequence", help="Amino acid sequences without headers", metavar="SEQUENCE_PATH")
parser.add_argument("email_address", help="Email address for EBI-NCBI-blastp API", metavar="EMAIL_ADDRESS")
args = parser.parse_args()
sequence = parse_input_file().sequences(args.sequence)
retrieve_blast_result().launch_blast(sequence,args.email_address)
    
    
