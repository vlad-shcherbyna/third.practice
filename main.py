import argparse

def total(year):
    dictionary = {}
    with open('data_file.tsc', "r") as file: #умовне відображення файлу в нашій програмі
        headline = file.readline()#ID
        element = file.readline()
        element = file.split("\t")
        if year == element[9]:
            if element[-1] != "NA\n":
                if element[1] not in dictionary:
                    dictionary[element[1]] = [element[-1]]
                else:
                    dictionary[element[1]].append(element[-1])
            print(dictionary)
            for people in dictionary:
                print(people, " : ", dictionary[people])

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--filename", "-f")
    parser.add_argument("-total", help= "Enter year")
    parser.add_argument("--medals", action="store_true")
    parser.add_argument("--country", required=False)
    parser.add_argument("--noc", required=False)
    parser.add_argument("--year", required=False)
    parser.add_argument("--sport", required=False)
    parser.add_argument("--output", "-o", required=False)

    args = parser.parse_args()
    if args.medals:
        ten_medalists(args.medals, args.output, args.filename, args.country, args.year, args.noc, args.sport)
    if args.total:
        print(args.total)
        total(args.total)


def ten_medalists(medals, output, filename, country, year, noc, sport):
    gold_medal = 0
    silver_medal = 0
    bronze_medal = 0
    total = 0
    list_medals = ["Gold", "Silver", "Bronze"]
    counter = 0
    output_file = None
    idx = 0
    print(gold_medal, silver_medal, bronze_medal)
    if output is not None:
        output_file = open(output, "wt")
    with open(filename, "r") as file:
        for line in file:
            element = line.strip().split("\t") # strip - забирає пробіли
            if element[6] == country or element[7] == noc and element[9] == year and element[12] == sport and element[14] in list_medals:
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
                    print(gold_medal, silver_medal, bronze_medal)
                    print(gold_medal + silver_medal + bronze_medal)
    if output_file is not None:
        idx += 1
        output_file.write(str(idx) + ",".join(element) + "\n")
    if output_file is not None:
        output_file.close()


if __name__ == '__main__':
    main()


year_set = set()





# def overall():
#     with open(file_with_data, "r") as file:  # умовне відображення файлу в нашій програмі
#         line = file.readlines()#ID
#         while line != "":
#             line_splitted = line.split("\t")
#             if country == line_splitted[7]:
#                 print(line_splitted)
#             year = int(line_splitted[9])
#             year_set.add(year)
#             line = file.readline()

        #     year = int(line_splitted[9])
        #     year_set.add(year)
        #     line = file.readline()
        # for line in file:
        #     line = file.readlines()
        #     line = file.split("\t")
        #     if year == line[9]:
        #         print(line)


# import sys
#
#
# def total():
#     year = sys.argv[3]
#     for line in lines:
#         line = line.split("\t")
#         if year == line[9]:
#             print(line)
#
#
# def medals():
#     country = sys.argv[3]
#
#
#
# file_with_data = sys.argv[1]
# mode = sys.argv[2] # 2 modes: -medals -total
#
#
# medals = sys.argv[2]
# country = sys.argv[3]
# # code_number = sys.argv[5]
# # year = sys.argv[6]
# print(mode)
#
# year_set = set()
#
#
#
# #print("country = ", country, "medals = ", medals)
#
# with open(file_with_data, "r") as file: #умовне відображення файлу в нашій програмі
#     line = file.readlines()#ID
#     while line != "":
#         line_splitted = line.split("\t")
#         if country == line_splitted[7]:
#             print(line_splitted)
#         year = int(line_splitted[9])
#         year_set.add(year)
#         line = file.readline()
#
# if mode == "-total":
#     total()
# else:
#     medals()
# year_list = sorted(year_set)
# print(year_set)
#
# for i, y in enumerate(year_list[:10], 1):
#     print(i, "\t", y)




