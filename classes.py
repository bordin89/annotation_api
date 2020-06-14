import ncbiblast
import requests
import os

class parse_input_file(object):
    def sequences(self,input_file):
        seqs=[]
        with open(input_file,'r') as fasta_flat_file:
            for line in fasta_flat_file:
                line=line.rstrip()
                seqs.append(line)
        return seqs

class retrieve_blast_result(object):
    def launch_blast(self,sequence,email_address):
        title = {'title' : 'test'}
        params = {
            'sequence' : sequence[0],
            'program' : 'blastp',
            'stype' : 'protein',
            'database' : 'uniprotkb',

        }
        return ncbiblast.serviceRun(email_address,title,params)

class retrieve_uniprot_target_id(object):
    def parse_blast_output(self,blast_output):
        pass
        #TODO return UniProtID, start, end, evalue and bitscore
    def retrieve_up_id_features(self,uid,start,end):
        BASE = 'https://www.ebi.ac.uk/proteins/api/'
        ENTRY_ENDPOINT = 'proteins/'+uniprot_query_id
        FEATURE_ENDPOINT = 'features/'+uniprot_query_id
        uniprot_id_requestURL = BASE + ENTRY_ENDPOINT
        feature_requestURL = BASE + FEATURE_ENDPOINT
        id_feature = requests.get(uniprot_id_requestURL, headers={ "Accept" : "text/x-gff"})
        id_json = requests.get(feature_requestURL, headers={ "Accept" : "application/json"})
        if not id_json.ok or not id_feature:
            id_json.raise_for_status()
            id_feature.raise_for_status()
            sys.exit()
        


        
    
