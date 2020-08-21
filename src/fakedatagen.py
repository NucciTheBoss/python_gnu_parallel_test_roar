import click
import csv
from faker import Faker
from progress.bar import Bar


@click.command()
@click.option("-c", "--count", default=1, help="Number of fake data entries to create")
@click.option("-o", "--output", default="./a.csv", help="Where to write out the csv file")
def fakedatagen(count, output):
    fake = Faker()
    fake_data = list()
    bar = Bar("Creating fake data", max=count)
    for iteration in range(count):
        tmp_list = [fake.first_name(), fake.last_name(), fake.email(),
                    fake.phone_number(), fake.country(), fake.file_name()]
        fake_data.append(tmp_list)
        bar.next()

    bar.finish()
    with open(output, "wt") as fout:
        csvout = csv.writer(fout)
        csvout.writerows(fake_data)


if __name__ == "__main__":
    fakedatagen()
