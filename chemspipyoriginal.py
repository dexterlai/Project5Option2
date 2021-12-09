import csv
from chemspipy import ChemSpider
file = "out.txt"
cs = ChemSpider('4zklCu9VxYiYT5FBW528J3GXuNKzoZzs')

def converter(file_name):
    with open(file_name) as file, open("combinedout.txt", "w") as out_file:
        tsv_file = csv.reader(file, delimiter = "\t")
        new_file = csv.writer(out_file, delimiter = "\t")
        i = 0
        for line in tsv_file:
            if line[3] == "null":
                inchi = line[2]
                smiles = cs.convert(inchi, "InChI", "SMILES")
                line[3] = smiles
                i += 1
                print(i)
            new_file.writerow(line)

converter(file)
