import argparse
import json
import math


def get_freq(inputfile, numwords):
    with open(inputfile) as fd:
        data = json.load((fd))
        total_words = 0
        for k, v in data.items():
            firstval = k
            secondval = v
            for key, value in v.items():
                first = key
                second = value
                total_words += value

        dict1 = data["Rarity"]
        dict2 = data["Fluttershy"]
        dict3 = data["Twilight Sparkle"]
        dict4 = data["Pinkie Pie"]
        dict5 = data["Applejack"]
        dict6 = data["Rainbow Dash"]

        result = {}

        for key in (dict1.keys() | dict2.keys() | dict3.keys() | dict4.keys() | dict5.keys() | dict6.keys()):
            if key in dict1: result.setdefault(key, []).append(dict1[key])
            if key in dict2: result.setdefault(key, []).append(dict2[key])
            if key in dict3: result.setdefault(key, []).append(dict3[key])
            if key in dict4: result.setdefault(key, []).append(dict4[key])
            if key in dict5: result.setdefault(key, []).append(dict5[key])
            if key in dict6: result.setdefault(key, []).append(dict6[key])

        for k, v in result.items():
            tot = total_words / sum(v)
            logarithm = math.log(tot)
            idf = (round(logarithm, 2))
            result[k] = idf

        rarityDict = create_pony_dict(result, dict1)
        flutterShyDict = create_pony_dict(result, dict2)
        twiDict = create_pony_dict(result, dict3)
        pinkiePieDict = create_pony_dict(result, dict4)
        applejackDict = create_pony_dict(result, dict5)
        rainbowDashDict = create_pony_dict(result, dict6)

        dict_final = {}

        dict_final["Twilight Sparkle"] = lastDict(twiDict, numwords)
        dict_final["Rainbow Dash"] = lastDict(rainbowDashDict, numwords)
        dict_final["Fluttershy"] = lastDict(flutterShyDict, numwords)
        dict_final["Pinkie Pie"] = lastDict(pinkiePieDict, numwords)
        dict_final["Applejack"] = lastDict(applejackDict, numwords)
        dict_final["Rarity"] = lastDict(rarityDict, numwords)
        x = json.dumps(dict_final, indent=4)
        print(x)


def lastDict(pony_dict, arg):

    sorted_dict = {}
    sorted_values = sorted(pony_dict.values())
    for i in sorted_values:
        for k in pony_dict.keys():
            if pony_dict[k] == i:
                sorted_dict[k] = pony_dict[k]
                break

    i = 0
    val = -1

    key_list = list(sorted_dict.keys())
    returnList = []
    while (i < arg):
        returnList.append(key_list[val])
        val -= 1
        i += 1
    return returnList


def create_pony_dict(result, names):
    Dict = {}
    for s in result:
        for k in names:
            if s == k:
                total = round(result[s] * names[k], 2)
                Dict[s] = total
    return Dict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fileName')
    parser.add_argument('number')
    args = parser.parse_args()
    num = int(args.number)
    get_freq(args.fileName, num)


if __name__ == "__main__":
    main()