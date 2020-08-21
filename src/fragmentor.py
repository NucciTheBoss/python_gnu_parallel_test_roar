#!/opt/aci/sw/python/3.6.3_anaconda-5.0.1/bin/python

import click
import csv
import re
import math


# Define helper function the reads in csv
# file and return a list
def csvtolist(csvfile):
    with open(csvfile, "rt") as fin:
        csvin = csv.reader(fin)
        data_to_fragment = [row for row in csvin]

    return data_to_fragment


# Verify if the input file is a csv file
def iscsv(input_file):
    x = re.search('.csv', input_file)
    if x:
        return True
    else:
        return False


# Split the csv file into the various fragments that we need
def chunks(lst, n):
    # Yield n-sized chunks from the input list
    chunk_list = list()
    for iteration in range(0, len(lst), n):
        chunk_list.append(lst[iteration:iteration+n])

    return chunk_list


# Define function to take in csv file
# and split it into the specified parts
@click.command()
@click.option("-i", "--input", help="Input csv file")
@click.option("-f", "--fragments", default=1, help="Number of fragments to split csv file into")
@click.option("-p", "--path", default="./", help="Directory to write fragments out to")
def fragmentor(input, fragments, path):
    # Verify that input file is a csv file
    answer = iscsv(input)
    if answer:
        fragment_name = "fragment"
        if fragments == 1:
            # Get csv file in list format
            fragment_part = csvtolist(input)
            fragment_part_name = fragment_name + "_1.csv"
            output_path = path + fragment_part_name
            # Create csv fragment file
            with open(output_path, "wt") as fout:
                csvout = csv.writer(fout)
                csvout.writerows(fragment_part)

        else:
            list_to_fragment = csvtolist(input)
            # Determine how big the chunks need to be
            # using the specified amount of fragments
            chunk_size = math.ceil(len(list_to_fragment) / fragments)
            # Get the list of fragments
            fragment_part_list = chunks(list_to_fragment, chunk_size)
            # Write out the multiple csv fragment files
            for iteration in range(0, len(fragment_part_list)):
                fragment_part_name = fragment_name + "_" + str(iteration+1) + ".csv"
                output_path = path + fragment_part_name
                with open(output_path, "wt") as fout:
                    csvout = csv.writer(fout)
                    csvout.writerows(fragment_part_list[iteration])

    else:
        print("Please ensure that the input file is a csv file")


if __name__ == "__main__":
    fragmentor()
