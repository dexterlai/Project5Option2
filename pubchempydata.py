import csv
import pubchempy as pcp
file = "good_chems.txt"


def converter(file_name):
    with open(file_name) as file, open("pubchempydata.txt", "w") as out_file:
        tsv_file = csv.reader(file, delimiter = "\t")
        new_file = csv.writer(out_file, delimiter = "\t")
        i = 0
        for line in tsv_file:
            if line[3] == "null":
                name = line[1]
                compound = pcp.get_compounds(name, "name")
                if compound:
                    smiles = compound[0].canonical_smiles
                    line[3] = smiles
                    i += 1
                    print(i)
            new_file.writerow(line)

converter(file)
