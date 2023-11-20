import pandas as pd


def main():

    url2 = "https://gml.noaa.gov/ccgg/trends/gl_gr.html"
    tables2 = pd.read_html(url2)[0].iloc[:, 0:2]
    df = pd.DataFrame(tables2)
    print(df.to_string(index=False))

    df.to_csv('CSC221-webscrape-data.csv', index=False)


main()
