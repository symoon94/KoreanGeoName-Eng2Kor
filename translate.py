import pandas as pd
from itertools import permutations

DICTIONARY = "dictionary.csv"

def make_dic():
    df = pd.read_csv(DICTIONARY, header=None)
    dic = {}
    for row in df[0]:
        split_row = row.split(" ")
        length = len(split_row)
        i = 0
        while i < length:
            item = split_row[i]
            if item == "":
                split_row.remove(item)
                length = length -1
                i -= 1
                continue
            i += 1
        for j in range(0,len(split_row),2):
            dic[split_row[j+1]] = split_row[j]
    return dic

def combination(word, en, ko):
    for n in range(1, len(en)+1):
        iter_en = map(''.join, permutations(en, n))
        iter_ko = map(''.join, permutations(ko, n))
        iter_list_en = list(iter_en)
        iter_list_ko = list(iter_ko)
        if word in iter_list_en:
            for i in range(len(iter_list_en)):
                if word == iter_list_en[i]:
                    return iter_list_ko[i]


def match(word, dic):
    words = word.split(" ")
    korean = []
    for word in words:
        word = word.lower()
        if any(x in ('a', 'e', 'i', 'o', 'u') for x in word):
            # English word
            candidate_en = []
            candidate_ko = []
            for k, v in dic.items():
                if k in word:
                    candidate_en.append(k)
                    candidate_ko.append(v)
            result = combination(word, candidate_en, candidate_ko)
            if result:
                korean.append(result)
            else:
                korean.append(word)
        else:
            # Korean word
            korean.append(word)
    try:
        result = " ".join(korean)
    except:
        pass

    return result

def main():
    dic = make_dic()
    word = input("Enter any words: \n")
    result = match(word, dic)
    if result:
        print(f"{word} --> {result}")
    else:
        print(f'Your word "{word}" did not match any Korean words')


if __name__ == "__main__":
    main()