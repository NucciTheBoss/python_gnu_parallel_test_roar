import click
import re
import csv


# Global variables
csv_pattern = re.compile('\Wcsv')  # .csv
yahoo_pattern = re.compile('\Wyahoo\Wcom')  # @yahoo.com
gmail_pattern = re.compile('\Wgmail\Wcom')  # @gmail.com
hotmail_pattern = re.compile('\Whotmail\Wcom')  # @hotmail.com
odt_pattern = re.compile('\Wodt')  # .odt
pdf_pattern = re.compile('\Wpdf')  # .pdf
docx_pattern = re.compile('\Wdocx')  # .docx
doc_pattern = re.compile('\Wdoc')  # .doc
pages_pattern = re.compile('\Wpages')  # .pages
avi_pattern = re.compile('\Wavi')  # .avi
wav_pattern = re.compile('\Wwav')  # .wav
mp3_pattern = re.compile('\Wmp3')  # .mp3
flac_pattern = re.compile('\Wflac')  # .flac
jpeg_pattern = re.compile('\Wjpeg')  # .jpeg
png_pattern = re.compile('\Wpng')  # .png
gif_pattern = re.compile('\Wgif')  # .gif
jpg_pattern = re.compile('\Wjpg')  # .jpg


# Define helper function the reads in csv
# file and return a list
def csvtolist(csvfile):
    with open(csvfile, "rt") as fin:
        csvin = csv.reader(fin)
        data_to_analyze = [row for row in csvin]

    return data_to_analyze


# Verify if input file is a csv file
def iscsv(input_file):
    x = re.search(csv_pattern, input_file)
    if x:
        return True
    else:
        return False


# Verify if email address is yahoo.com
def isyahoo(email_address):
    x = re.search(yahoo_pattern, email_address)
    if x:
        return True
    else:
        return False


# Verify if email address is gmail.com
def isgmail(email_address):
    x = re.search(gmail_pattern, email_address)
    if x:
        return True
    else:
        return False


# Verify if email address is hotmail.com
def ishotmail(email_address):
    x = re.search(hotmail_pattern, email_address)
    if x:
        return True
    else:
        return False


def isodt(doc_format):
    x = re.search(odt_pattern, doc_format)
    if x:
        return True
    else:
        return False


def ispdf(doc_format):
    x = re.search(pdf_pattern, doc_format)
    if x:
        return True
    else:
        return False


def isdocx(doc_format):
    x = re.search(docx_pattern, doc_format)
    if x:
        return True
    else:
        return False


def isdoc(doc_format):
    x = re.search(doc_pattern, doc_format)
    if x:
        return True
    else:
        return False


def ispages(doc_format):
    x = re.search(pages_pattern, doc_format)
    if x:
        return True
    else:
        return False


def isavi(audio_format):
    x = re.search(avi_pattern, audio_format)
    if x:
        return True
    else:
        return False


def iswav(audio_format):
    x = re.search(wav_pattern, audio_format)
    if x:
        return True
    else:
        return False


def ismp3(audio_format):
    x = re.search(mp3_pattern, audio_format)
    if x:
        return True
    else:
        return False


def isflac(audio_format):
    x = re.search(flac_pattern, audio_format)
    if x:
        return True
    else:
        return False


def isjpeg(image_format):
    x = re.search(jpeg_pattern, image_format)
    if x:
        return True
    else:
        return False


def ispng(image_format):
    x = re.search(png_pattern, image_format)
    if x:
        return True
    else:
        return False


def isgif(image_format):
    x = re.search(gif_pattern, image_format)
    if x:
        return True
    else:
        return False


def isjpg(image_format):
    x = re.search(jpg_pattern, image_format)
    if x:
        return True
    else:
        return False


def determinemostpopularemail(lst_input):
    # Set initial counts at zero
    yahoo_count = 0
    gmail_count = 0
    hotmail_count = 0
    other_count = 0

    # Cycle through all email addresses provided
    for row in lst_input:
        # Check if row[2] belongs to any of the categories
        if isyahoo(row[2]):
            yahoo_count += 1

        elif isgmail(row[2]):
            gmail_count += 1

        elif ishotmail(row[2]):
            hotmail_count += 1

        else:
            other_count += 1

    # Create output xml tag
    xml_string = "<data yahoo_count=\"{}\" gmail_count=\"{}\" hotmail_count=\"{}\" other_count=\"{}\"></data>"
    xml_string = xml_string.format(yahoo_count, gmail_count, hotmail_count, other_count)
    print(xml_string)


def determinemostpopularfreeemail(lst_input):
    yahoo_count = 0
    gmail_count = 0
    hotmail_count = 0

    # Cycle through all email addresses provided
    for row in lst_input:
        # Check if row[2] belongs to any of the categories
        if isyahoo(row[2]):
            yahoo_count += 1

        elif isgmail(row[2]):
            gmail_count += 1

        elif ishotmail(row[2]):
            hotmail_count += 1

        else:
            continue

    # Create output xml tag
    xml_string = "<data yahoo_count=\"{}\" gmail_count=\"{}\" hotmail_count=\"{}\"></data>"
    xml_string = xml_string.format(yahoo_count, gmail_count, hotmail_count)
    print(xml_string)


def determinemostpopulardocumentformat(lst_input):
    odt_count = 0
    pdf_count = 0
    docx_count = 0
    doc_count = 0
    pages_count = 0

    for row in lst_input:
        if isodt(row[5]):
            odt_count += 1

        elif ispdf(row[5]):
            pdf_count += 1

        elif isdocx(row[5]):
            docx_count += 1

        elif isdoc(row[5]):
            doc_count += 1

        elif ispages(row[5]):
            pages_count += 1

        else:
            continue

    xml_string = "<data odt_count=\"{}\" pdf_count=\"{}\" docx_count=\"{}\" doc_count=\"{}\" pages_count=\"{}\"></data>"
    xml_string = xml_string.format(odt_count, pdf_count, docx_count, doc_count, pages_count)
    print(xml_string)


def determinemostpopularaudioformat(lst_input):
    avi_count = 0
    wav_count = 0
    mp3_count = 0
    flac_count = 0

    for row in lst_input:
        if isavi(row[5]):
            avi_count += 1

        elif iswav(row[5]):
            wav_count += 1

        elif ismp3(row[5]):
            mp3_count += 1

        elif isflac(row[5]):
            flac_count += 1

        else:
            continue

    xml_string = "<data avi_count=\"{}\" wav_count=\"{}\" mp3_count=\"{}\" flac_count=\"{}\"></data>"
    xml_string = xml_string.format(avi_count, wav_count, mp3_count, flac_count)
    print(xml_string)


def determinemostpopularimageformat(lst_input):
    jpeg_count = 0
    png_count = 0
    gif_count = 0
    jpg_count = 0

    for row in lst_input:
        if isjpeg(row[5]):
            jpeg_count += 1

        elif ispng(row[5]):
            png_count += 1

        elif isgif(row[5]):
            gif_count += 1

        elif isjpg(row[5]):
            jpg_count += 1

        else:
            continue

    xml_string = "<data jpeg_count=\"{}\" png_count=\"{}\" gif_count=\"{}\" jpg_count=\"{}\"></data>"
    xml_string = xml_string.format(jpeg_count, png_count, gif_count, jpg_count)
    print(xml_string)


@click.command()
@click.option("-i", "--input", default=None, help="Input csv file")
@click.option("-c", "--command", default=None, help="Use one of the following analysis commands:\n\n"
                                                    "determine_most_popular_email\n"
                                                    "determine_most_popular_free_email\n"
                                                    "determine_most_popular_document_format\n"
                                                    "determine_most_popular_audio_format\n"
                                                    "determine_most_popular_image_format")
def main(input, command):
    if input is None:
        print("Please specify and input csv file")

    else:
        answer = iscsv(input)
        if answer:
            if command is None:
                print("Please insert one of the following analysis commands:\n\n"
                      "determine_most_popular_email\n"
                      "determine_most_popular_free_email\n"
                      "determine_most_popular_document_format\n"
                      "determine_most_popular_audio_format\n"
                      "determine_most_popular_image_format")

            elif command.lower() == "determine_most_popular_email":
                data_lst = csvtolist(input)
                determinemostpopularemail(data_lst)

            elif command.lower() == "determine_most_popular_free_email":
                data_lst = csvtolist(input)
                determinemostpopularfreeemail(data_lst)

            elif command.lower() == "determine_most_popular_document_format":
                data_lst = csvtolist(input)
                determinemostpopulardocumentformat(data_lst)

            elif command.lower() == "determine_most_popular_audio_format":
                data_lst = csvtolist(input)
                determinemostpopularaudioformat(data_lst)

            elif command.lower() == "determine_most_popular_image_format":
                data_lst = csvtolist(input)
                determinemostpopularimageformat(data_lst)

            else:
                print("There was an invalid command entered. Please use one of the following\n"
                      "analysis commands:\n\n"
                      "determine_most_popular_email\n"
                      "determine_most_popular_free_email\n"
                      "determine_most_popular_document_format\n"
                      "determine_most_popular_audio_format\n"
                      "determine_most_popular_image_format")

        else:
            print("Please ensure that the input file is a csv file")


if __name__ == "__main__":
    main()
