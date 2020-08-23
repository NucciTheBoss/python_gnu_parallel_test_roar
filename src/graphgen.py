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
@click.option("-f", "--files", nargs=5, default=None, type=str, help="Input the five xml files generated during "
                                                                     "analysis")
def main(files):
    if files is None:
        print("Please input the five xml files created during analysis")

    else:
        # most_popular_email.xml
        if isxml(files[0]):
            current_doc = minidom.parse(files[0])
            current_data = current_doc.getElementsByTagName("data")

            # Calculate the total counts from all the xml tags
            yahoo_total = 0
            gmail_total = 0
            hotmail_total = 0
            other_total = 0

            for data_entry in current_data:
                yahoo_total += int(data_entry.attributes['yahoo_count'].value)
                gmail_total += int(data_entry.attributes['gmail_count'].value)
                hotmail_total += int(data_entry.attributes['hotmail_count'].value)
                other_total += int(data_entry.attributes['other_count'].value)

            # Plot the data as a bar graph
            counts = [yahoo_total, gmail_total, hotmail_total, other_total]
            email_clients = ["yahoo.com", "gmail.com", "hotmail.com", "Other"]
            index = np.arange(len(email_clients))
            plt.figure()
            plt.bar(index, counts)
            plt.xlabel("Email Clients")
            plt.ylabel("Number of Users")
            plt.title("Most Popular Email Client")
            plt.xticks(index, email_clients)
            plt.savefig("most_popular_email_client_bar_graph.png")  # Figure is saved to $CWD
            plt.close()

            # Plot the data as a pie chart
            plt.figure()
            plt.pie(counts, labels=email_clients)
            plt.title("Most Popular Email Client")
            plt.savefig("most_popular_email_client_pie_chart.png")
            plt.close()

        # most_popular_free_email.xml
        if isxml(files[1]):
            current_doc = minidom.parse(files[1])
            current_data = current_doc.getElementsByTagName("data")

            # Calculate the totals for the most popular free email client
            yahoo_free_total = 0
            gmail_free_total = 0
            hotmail_free_total = 0

            for data_entry in current_data:
                yahoo_free_total += int(data_entry.attributes['yahoo_count'].value)
                gmail_free_total += int(data_entry.attributes['gmail_count'].value)
                hotmail_free_total += int(data_entry.attributes['hotmail_count'].value)

            free_counts = [yahoo_free_total, gmail_free_total, hotmail_free_total]
            free_email_clients = ["yahoo.com", "gmail.com", "hotmail.com"]
            free_index = np.arange(len(free_email_clients))
            # Plot the bar graph
            plt.figure()
            plt.bar(free_index, free_counts)
            plt.xlabel("Free Email Clients")
            plt.ylabel("Number of Users")
            plt.title("Most popular free email client")
            plt.xticks(free_index, free_email_clients)
            plt.savefig("most_popular_free_email_client_bar_graph.png")
            plt.close()

            # Plot the pie chart
            plt.figure()
            plt.pie(free_counts, labels=free_email_clients)
            plt.title("Most Popular Free Email Client")
            plt.savefig("most_popular_free_email_client_pie_chart.png")
            plt.close()

        # most_popular_document_format.xml
        if isxml(files[2]):
            current_doc = minidom.parse(files[2])
            current_data = current_doc.getElementsByTagName("data")

            # Calculate the totals of the most popular document formats
            odt_total = 0
            pdf_total = 0
            docx_total = 0
            doc_total = 0
            pages_total = 0

            for data_entry in current_data:
                odt_total += int(data_entry.attributes['odt_count'].value)
                pdf_total += int(data_entry.attributes['pdf_count'].value)
                docx_total += int(data_entry.attributes['docx_count'].value)
                doc_total += int(data_entry.attributes['doc_count'].value)
                pages_total += int(data_entry.attributes['pages_count'].value)

            documents_count = [odt_total, pdf_total, docx_total, doc_total, pages_total]
            document_formats = ["odt", "pdf", "docx", "doc", "pages"]
            document_index = np.arange(len(document_formats))
            # Plot the bar graph
            plt.figure()
            plt.bar(document_index, documents_count)
            plt.xlabel("Document format")
            plt.ylabel("Occurrence")
            plt.title("Most Popular Document Format")
            plt.xticks(document_index, document_formats)
            plt.savefig("most_popular_document_format_bar_graph.png")
            plt.close()

            # Plot the pie chart
            plt.figure()
            plt.pie(documents_count, labels=document_formats)
            plt.title("Most Popular Document Format")
            plt.savefig("most_popular_document_format_pie_chart.png")
            plt.close()

        # most_popular_audio_format.xml
        if isxml(files[3]):
            current_doc = minidom.parse(files[3])
            current_data = current_doc.getElementsByTagName("data")

            # Calculate the totals of the most popular audio format
            avi_total = 0
            wav_total = 0
            mp3_total = 0
            flac_total = 0

            for data_entry in current_data:
                avi_total += int(data_entry.attributes['avi_count'].value)
                wav_total += int(data_entry.attributes['wav_count'].value)
                mp3_total += int(data_entry.attributes['mp3_count'].value)
                flac_total += int(data_entry.attributes['flac_count'].value)

            audio_count = [avi_total, wav_total, mp3_total, flac_total]
            audio_formats = ["avi", "wav", "mp3", "flac"]
            audio_index = np.arange(len(audio_formats))
            # Plot the bar graph
            plt.figure()
            plt.bar(audio_index, audio_count)
            plt.xlabel("Audio format")
            plt.ylabel("Occurrence")
            plt.title("Most Popular Audio Format")
            plt.xticks(audio_index, audio_formats)
            plt.savefig("most_popular_audio_format_bar_graph.png")
            plt.close()

            # Plot the pie chart
            plt.figure()
            plt.pie(audio_count, labels=audio_formats)
            plt.title("Most Popular Audio Format")
            plt.savefig("most_popular_audio_format_pie_chart.png")
            plt.close()

        # most_popular_image_format.xml
        if isxml(files[4]):
            current_doc = minidom.parse(files[4])
            current_data = current_doc.getElementsByTagName("data")

            jpeg_total = 0
            png_total = 0
            gif_total = 0
            jpg_total = 0

            for data_entry in current_data:
                jpeg_total += int(data_entry.attributes['jpeg_count'].value)
                png_total += int(data_entry.attributes['jpeg_count'].value)
                gif_total += int(data_entry.attributes['jpeg_count'].value)
                jpg_total += int(data_entry.attributes['jpeg_count'].value)

            image_count = [jpeg_total, png_total, gif_total, jpg_total]
            image_formats = ["jpeg", "png", "gif", "jpg"]
            image_index = np.arange(len(image_formats))
            # Plot the bar graph
            plt.figure()
            plt.bar(image_index, image_count)
            plt.xlabel("Image format")
            plt.ylabel("Occurrence")
            plt.title("Most Popular Image Format")
            plt.xticks(image_index, image_formats)
            plt.savefig("most_popular_image_format_bar_graph.png")
            plt.close()

            # Plot the pie chart
            plt.figure()
            plt.pie(image_count, labels=image_formats)
            plt.title("Most Popular Image Format")
            plt.savefig("most_popular_image_format_pie_chart.png")
            plt.close()


if __name__ == "__main__":
    main()
