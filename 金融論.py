import glob
import csv
import os
import sys
import pandas as pd

files = glob.glob("./*.csv")

for file in files:
    new_filename = file.split(" ")[0] + ".csv"

    with open(file, "r", encoding = "utf-8-sig") as f:
        header = next(csv.reader(f))
        reader = csv.reader(f)
        access_log = [row for row in reader]
        for row in access_log:
            with open(new_filename, "a", newline = "", encoding = "utf-8") as g:
                writer = csv.writer(g, quoting=csv.QUOTE_ALL)
                writer.writerow(row)
                #print(row)
    os.remove(file)

files = glob.glob("./*.csv")
for file in files:
    reversed_csv = ""
    for count, line in enumerate(reversed(list(open(file, "r")))):
        reversed_csv += line
    
    with open(file, "w") as f:
        f.write(reversed_csv)

files = glob.glob("./*.csv")

#
#利益(p)
#

for file in files:
    print(file)
    with open(file, "r", encoding = "utf-8") as f:
        before_readers = csv.reader(f)
        for before_count, before_row in enumerate(before_readers):
            before_price = float(before_row[1].replace(',', ''))
            to_save_row = []
            with open(file, "r", encoding = "utf-8") as g:
                after_readers  = csv.reader(g) 
                for after_count, after_row in enumerate(after_readers):
                    after_price = float(after_row[1].replace(',', ''))
                    if before_count < after_count:
                        print(before_count, before_price, after_count, after_price, round(after_price - before_price, 2))
                        save_filename = file.split(".csv")[0] + "_p.csv"
                        if before_count == 0:
                            with open(save_filename, "a", newline = "", encoding = "utf-8") as h:
                                writer = csv.writer(h)
                                writer.writerow([round(after_price - before_price, 2)])
                        else:
                            to_save_row.append(round(after_price - before_price, 2))
            if before_count == 0:
                df = pd.read_csv(save_filename, header = None)
                #print(df)
                
            else:
                for i in range(before_count):
                    to_save_row.append("")
                df[before_count] = to_save_row
                #print(df)
    df.drop(df.columns[[before_count]], axis = 1, inplace=True)
    df.to_csv(save_filename, header = False, index = False, encoding = "utf-8", sep = ',')
    print(df)

files_list = ["S&P500_p.csv", "AAPL_p.csv", "BRKa_p.csv", "LLY_p.csv", "MSFT_p.csv", "BRKb_p.csv", "AMZN_p.csv", "NVDA_p.csv", "GOOGL_p.csv", "AVGO_p.csv", "TSLA_p.csv", "META_p.csv"]

for file_count, file in enumerate(files_list):
    ave_list = []
    with open(file, "r", encoding = "utf-8") as f:
        readers = csv.reader(f)
        for row_count, row in enumerate(readers):
            sum = 0
            for i in range(len(row) - row_count):
                sum += round(float(row[i]), 2)
                #print(float(row[i]))
            #print(round(sum, 2), len(row) - row_count)
            ave = round((round(sum, 2))/(len(row) - row_count), 2)
            print(ave)
            ave_list.append(ave)
    print(ave_list)
    if file_count == 0:
        df = pd.DataFrame(ave_list)
        print(df)
    else:
        to_conccat_df = pd.DataFrame(ave_list)
        df = pd.concat([df, to_conccat_df], axis = 1)
        print(df)

df.to_csv("利益.csv", header = False, index = False, encoding = "utf-8", sep = ',')


#
#利益(p2)
#

for file in files:
    print(file)
    with open(file, "r", encoding = "utf-8") as f:
        before_readers = csv.reader(f)
        for before_count, before_row in enumerate(before_readers):
            before_price = float(before_row[1].replace(',', ''))
            to_save_row = []
            with open(file, "r", encoding = "utf-8") as g:
                after_readers  = csv.reader(g) 
                for after_count, after_row in enumerate(after_readers):
                    after_price = float(after_row[1].replace(',', ''))
                    if before_count < after_count:
                        print(before_count, before_price, after_count, after_price, round(after_price - before_price, 2))
                        save_filename = file.split(".csv")[0] + "_p2.csv"
                        if before_count == 0:
                            with open(save_filename, "a", newline = "", encoding = "utf-8") as h:
                                writer = csv.writer(h)
                                writer.writerow([round(after_price - before_price, 2)])
                        else:
                            to_save_row.append(round(after_price - before_price, 2))
            if before_count == 0:
                df = pd.read_csv(save_filename, header = None)
                #print(df)
                
            else:
                for i in range(before_count):
                    to_save_row.append("")
                df[before_count] = to_save_row
                #print(df)
    df.drop(df.columns[[before_count]], axis = 1, inplace=True)
    df.to_csv(save_filename, header = False, index = False, encoding = "utf-8", sep = ',')
    print(df)

files_list = ["S&P500_p2.csv", "AAPL_p2.csv", "LLY_p2.csv", "MSFT_p2.csv", "BRKb_p2.csv", "AMZN_p2.csv", "NVDA_p2.csv", "GOOGL_p2.csv", "AVGO_p2.csv", "TSLA_p2.csv", "META_p2.csv"]

for file_count, file in enumerate(files_list):
    ave_list = []
    with open(file, "r", encoding = "utf-8") as f:
        readers = csv.reader(f)
        for row_count, row in enumerate(readers):
            sum = 0
            for i in range(len(row) - row_count):
                sum += round(float(row[i]), 2)
                #print(float(row[i]))
            #print(round(sum, 2), len(row) - row_count)
            ave = round((round(sum, 2))/(len(row) - row_count), 2)
            print(ave)
            ave_list.append(ave)
    print(ave_list)
    if file_count == 0:
        df = pd.DataFrame(ave_list)
        print(df)
    else:
        to_conccat_df = pd.DataFrame(ave_list)
        df = pd.concat([df, to_conccat_df], axis = 1)
        print(df)

df.to_csv("利益2.csv", header = False, index = False, encoding = "utf-8", sep = ',')


#
#リターン(ret)
#

for file in files:
    print(file)
    with open(file, "r", encoding = "utf-8") as f:
        before_readers = csv.reader(f)
        for before_count, before_row in enumerate(before_readers):
            before_price = float(before_row[1].replace(',', ''))
            to_save_row = []
            with open(file, "r", encoding = "utf-8") as g:
                after_readers  = csv.reader(g) 
                for after_count, after_row in enumerate(after_readers):
                    after_price = float(after_row[1].replace(',', ''))
                    if before_count < after_count:
                        print(before_count, before_price, after_count, after_price, round((after_price - before_price)/before_price, 2))
                        save_filename = file.split(".csv")[0] + "_ret.csv"
                        if before_count == 0:
                            with open(save_filename, "a", newline = "", encoding = "utf-8") as h:
                                writer = csv.writer(h)
                                writer.writerow([round((after_price - before_price)/before_price, 2)])
                        else:
                            to_save_row.append(round((after_price - before_price)/before_price, 2))
            if before_count == 0:
                df = pd.read_csv(save_filename, header = None)
                #print(df)
                
            else:
                for i in range(before_count):
                    to_save_row.append("")
                df[before_count] = to_save_row
                #print(df)
    df.drop(df.columns[[before_count]], axis = 1, inplace=True)
    df.to_csv(save_filename, header = False, index = False, encoding = "utf-8", sep = ',')
    print(df)

files_list = ["S&P500_ret.csv", "AAPL_ret.csv", "BRKa_ret.csv", "LLY_ret.csv", "MSFT_ret.csv", "BRKb_ret.csv", "AMZN_ret.csv", "NVDA_ret.csv", "GOOGL_ret.csv", "AVGO_ret.csv", "TSLA_ret.csv", "META_ret.csv"]

for file_count, file in enumerate(files_list):
    ave_list = []
    with open(file, "r", encoding = "utf-8") as f:
        readers = csv.reader(f)
        for row_count, row in enumerate(readers):
            sum = 0
            for i in range(len(row) - row_count):
                sum += round(float(row[i]), 2)
                #print(float(row[i]))
            #print(round(sum, 2), len(row) - row_count)
            ave = round((round(sum, 2))/(len(row) - row_count), 2)
            print(ave)
            ave_list.append(ave)
    print(ave_list)
    if file_count == 0:
        df = pd.DataFrame(ave_list)
        print(df)
    else:
        to_conccat_df = pd.DataFrame(ave_list)
        df = pd.concat([df, to_conccat_df], axis = 1)
        print(df)

df.to_csv("リターン.csv", header = False, index = False, encoding = "utf-8", sep = ',')



file_list = ["利益.csv", "利益2.csv", "リターン.csv"]
for count, filename in enumerate(file_list):
    to_save_list = []
    df = pd.read_csv(filename, header = None)
    pd.set_option('display.max_rows', None)
    ddf = df.mean(axis = 1).round(2)
    to_save_list.append(ddf.iloc[0])
    to_save_list.append(round(ddf.iloc[0:6].mean(), 2))
    to_save_list.append(round(ddf.iloc[0:12].mean(), 2))
    to_save_list.append(round(ddf.iloc[0:60].mean(), 2))
    to_save_list.append(round(ddf.iloc[0:120].mean(), 2))
    to_save_list.append(round(ddf.iloc[0:240].mean(), 2))
    to_save_list.append(round(ddf.iloc[0:360].mean(), 2))
    to_save_list.append(round(ddf.iloc[0:480].mean(), 2))
    
    if count == 0:
        to_save_df = pd.DataFrame(to_save_list)
    else:
        to_conccat_df = pd.DataFrame(to_save_list)
        to_save_df = pd.concat([to_save_df, to_conccat_df], axis = 1)

    print(to_save_list)

print(to_save_df)
to_save_df.to_csv("各平均.csv", header = False, index = False, encoding = "utf-8", sep = ',')