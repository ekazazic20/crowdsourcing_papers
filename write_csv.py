import pandas as pd
import get_labels
import get_paper_info
import get_urls


def write_csv(input_csv_filename,function_map_csv, output_csv_filename):
    # labels = get_labels.get_labels(input_csv_filename)
    labels = ["test", "test", "test", "test"]
    urls = get_urls.get_urls(input_csv_filename)
    df = pd.read_csv(input_csv_filename)
    for index in df.index:
        paper_info = get_paper_info.get_paper_info(urls[index], labels[index], function_map_csv)
        df.loc[index, "Paper title"] = paper_info[0]
        df.loc[index, "DOI"] = paper_info[1]
        df.loc[index, "Abstract"] = paper_info[2]
        # df.loc[index, ""] = paper_info[3] #PDF link?
        df.loc[index, "Open access?"] = paper_info[4]
        # df.loc[index, "Functions Level I"] = paper_info[5]
        # df.loc[index, "Functions Level II"] = paper_info[6]
        # df.loc[index, "Functions Level III- NEW"] = paper_info[7]
    df.to_csv(output_csv_filename, index=False)