import argparse




def transform_line(line: str):
    # remove unnecessary symbol at the end and convert str to list
    return line.strip('\n').split('\t')


# python3 main.py data_file.tsv --total 2016
# python3 main.py data_file.tsv --medals AUT 1976 --output table.txt



def total(year):
    dictionary = {}
    with open('data_file.tsv', 'r') as file:
        headline = transform_line(file.readline()) # завантажує значення першого рядка для словника
        line = file.readline()
        while True:
            if not line: # якщо line is None, то ми вкінці файлу
                break
            country = transform_line(line)[6]
            medal = transform_line(line)[-1]
            if country not in dictionary and medal != "NA":
                dictionary[country] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
            if medal == 'Gold': # збільшуємо кількість медалей
                dictionary[country]['Gold'] += 1
            elif medal == 'Silver':
                dictionary[country]['Silver'] += 1
            elif medal == 'Bronze':
                dictionary[country]['Bronze'] += 1
            line = file.readline()


    if not dictionary:
        print("You've selected a wrong country or there was no game this that year")
        return
    else:
        for i in dictionary.items():
            print(i)



def ten_medalists(output, filename, country, year):
    gold_medal = 0
    silver_medal = 0
    bronze_medal = 0
    total = 0
    list_medals = ["Gold", "Silver", "Bronze"]
    counter = 0
    idx = 0
    names_sport_medal = []
    print(gold_medal, silver_medal, bronze_medal)
    with open(filename, "r") as file:
        for line in file:
            element = line.strip().split("\t") # strip - забирає пробіли
            if element[6] == country or element[7] == country and element[9] == year and element[14] in list_medals:
                medalist = [element[1], element[12], element[14]]
                counter += 1
                total += 1
                if element[14] == list_medals[0]:
                    gold_medal += 1
                if element[14] == list_medals[1]:
                    silver_medal += 1
                if element[14] == list_medals[2]:
                    bronze_medal += 1
                if counter <= 10:
                    first_medalists = ", ".join(medalist)
                    print(f"{first_medalists}")
                    names_sport_medal.append(first_medalists)
                    print(gold_medal, silver_medal, bronze_medal)
                    print(gold_medal + silver_medal + bronze_medal)
    if output is not None:
        with open(output, "w+") as output_file:
            idx += 1
            for lline in names_sport_medal:
                lline.split("\t")
                output_file.write(lline)






def overall():
    pass


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("filename")
    parser.add_argument("--total", help="Enter year", type=str)
    parser.add_argument("--medals", nargs="+") #можна передати рік і країну
    parser.add_argument("--output", "-o")

    args = parser.parse_args()
    filename = args.filename # можна при будь-яких командах передати аргумент(назву файла)
    print(args)
    if args.medals:
        country = args.medals[0]
        year = args.medals[1]
        if args.output:
            print(args.output)
            output = args.output
            ten_medalists(output, filename, country, year)
        else:
            output = None
            ten_medalists(output, filename, country, year)
    if args.total:
        print(args.total)
        total(args.total)


if __name__ == '__main__':
    main()







