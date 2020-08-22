import matplotlib.pyplot as plt
import numpy as np
from xml.dom import minidom
import click
import re


# Global variables
xml_pattern = re.compile('\Wxml')


# Use this function to verify that the input is xml
def isxml(xml_file):
    x = re.search(xml_pattern, xml_file)
    if x:
        return True
    else:
        return False


# 5 input files are the .xml files generated
@click.command()
@click.option("-f", "--files", nargs=5, default=None, type=str, help="Input the five xml generated during analysis")
def main(files):
    if files is None:
        print("Please input the five xml files created during analysis")

    else:
        # most_popular_email.xml
        if isxml(files[0]):
            current_doc = minidom.parse(files[0])
        # most_popular_free_email.xml
        if isxml(files[1]):
            current_doc = minidom.parse(files[1])
        # most_popular_document_format.xml
        if isxml(files[2]):
            current_doc = minidom.parse(files[2])
        # most_popular_audio_format.xml
        if isxml(files[3]):
            current_doc = minidom.parse(files[3])
        # most_popular_image_format.xml
        if isxml(files[4]):
            current_doc = minidom.parse(files[4])


if __name__ == "__main__":
    main()
