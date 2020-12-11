import argparse
import sys

import get_urls
import get_paper_info
import write_csv
import get_labels


parser = argparse.ArgumentParser(description='Prepare CSV Command Line Tool')

parser.add_argument('input_csv', type=str, help='CSV file from Airtable')

parser.add_argument('output_csv', type=str, help='Output CSV file')

args = parser.parse_args(sys.argv)  # sys.argv is used if argv parameter is None
input_csv_filename = args.input_csv
output_csv_filename = args.output_csv

urls = get_urls.get_urls(input_csv_filename)
labels = get_labels.get_labels(input_csv_filename)
function_map = "function_map.csv"  # should be variable?

info_on_papers = []
for i in range(len(urls)):
    label = labels[i]
    url = urls[i]
    title, doi, abstract, full_doc_link, is_open_access, label_one, label_two, label_three = get_paper_info.get_paper_info(url, label, function_map)
    info_on_papers.append((title, doi, abstract, full_doc_link, is_open_access, label_one, label_two, label_three))

write_csv.write_csv(info_on_papers, output_csv_filename)
