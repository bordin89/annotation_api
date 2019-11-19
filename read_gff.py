import pprint
import gffutils


# print(open('example.gff').read())

db = gffutils.create_db('example.gff', dbfn='test.db', force=True,
                        keep_order=True, merge_strategy='merge', sort_attribute_values=True)
