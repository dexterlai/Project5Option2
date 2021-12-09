import csv
from chemspipy import ChemSpider
file = "pubchempydata.txt"
cs = ChemSpider('4zklCu9VxYiYT5FBW528J3GXuNKzoZzs')

def converter(file_name):
    with open(file_name) as file, open("combinedout.txt", "w") as out_file, open("out.txt") as chemspipydata_file:
        tsv_file = csv.reader(file, delimiter = "\t")
        new_file = csv.writer(out_file, delimiter = "\t")
        pubchem_file = csv.reader(chemspipydata_file, delimiter = "\t")
        i = 0
        SMILES = []
        for aline in pubchem_file:
            if not aline or len(aline) < 4:
                SMILES.append("null")
                continue
            SMILES.append(aline[3])
        for line in tsv_file:
            if len(line) < 4:
                continue
            if line[3] == "null" and i < len(SMILES):
                line[3] = SMILES[i]
            i += 1
            print(i)
            new_file.writerow(line)

converter(file)
