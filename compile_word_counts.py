import pandas as pd
import argparse
import json


def get_words(inputfile, names):
    df = pd.read_csv(inputfile)
    df = df.iloc[:, 2:]
    text = df.loc[df['pony'] == names].dialog.str.lower().str.split(" ").sum()

    l = []
    for i in text:
        if i.isalpha() == True:
            i = i.replace("!", "").replace("?", "").replace("-", "").replace("'", "").replace(".", "").replace(",",
                                                                                                               "").replace(
                "&", "").replace("[]", "").replace(":", "").replace(";", "").replace("#", "")
            l.append(i)

    words_dict = dict()

    for i in l:
        words_dict[i] = l.count(i)

    new_dict = {}
    for key, v in words_dict.items():
        first_value = v
        if first_value >= 5:
            new_dict[key] = v

    return new_dict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    parser.add_argument('-o', '--f_name')
    args = parser.parse_args()

    words_twilightsparkle = get_words(args.file_name, "Twilight Sparkle")
    words_fluttershy = get_words(args.file_name, "Fluttershy")
    words_rarity = get_words(args.file_name, "Rarity")
    words_applejack = get_words(args.file_name, "Applejack")
    words_rainbow = get_words(args.file_name, "Rainbow Dash")
    words_pinkie = get_words(args.file_name, "Pinkie Pie")

    results = {"Twilight Sparkle": words_twilightsparkle, "Fluttershy": words_fluttershy, "Applejack": words_applejack,
               "Pinkie Pie": words_pinkie, "Rainbow Dash": words_rainbow, "Rarity": words_rarity}

    with open(args.f_name, "a+") as json_file:
        json.dump(results, json_file, indent=2)
        json_file.write("\n")
        json_file.close()


if __name__ == "__main__":
    main()
