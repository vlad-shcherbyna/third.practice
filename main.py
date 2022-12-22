import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--filename", "-f", required=True)
parser.add_argument("--total", help="Enter year", type=str)
parser.add_argument("--medals", action="store_true")
parser.add_argument("--country", required=False)
parser.add_argument("--noc", required=False)
parser.add_argument("--year", required=False)
parser.add_argument("--sport", required=False)
parser.add_argument("--output", required=False)
parser.add_argument("--overall", nargs='+', required=False)
parser.add_argument("--interactive", action="store_true", required=False)

args = parser.parse_args()


def transform_line(line: str):
    return line.strip('\n').split('\t')


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


def ten_medalists(output, filename, country, year, noc, sport):
    gold_medal = 0
    silver_medal = 0
    bronze_medal = 0
    total = 0
    list_medals = ["Gold", "Silver", "Bronze"]
    counter = 0
    output_file = None
    indx = 0
    idx = 0
    names_sport_medal = []
    print(gold_medal, silver_medal, bronze_medal)
    with open(filename, "r") as file:
        for line in file:
            element = line.strip().split("\t")
            if element[6] == country or element[7] == noc and element[9] == year and element[12] == sport and element[14] in list_medals:
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
    if output_file is not None:
        indx += 1
        output_file.write(str(indx) + ",".join(element) + "\n")
    if output_file is not None:
        output_file.close()
    if output is not None:
        with open(output, "w+") as output_file:
            idx += 1
            for lline in names_sport_medal:
                lline.split("\t")
                output_file.write(lline)


def overall(filename, overall):
    dictionary = {}
    best_years = []
    for i in overall:
        dictionary[i] = dict() #заносить всі країни в словник
    with open(filename, 'r') as file:
        element = file.readline().split('\t')
        while len(element) > 1:
            country_name = element[6]
            year = element[9]
            if country_name in dictionary:
                if year not in dictionary[country_name]: #якщо інфа про цей рік відсутня для цієї країни то створити цей рік
                    dictionary[country_name][year] = 0
                dictionary[country_name][year] += 1
            element = file.readline().split('\t')
    for country in dictionary:
        medals_by_years = dictionary[country]
        all_medals = medals_by_years.values()
        max_data = max(all_medals)
        for all_year in medals_by_years:
            if medals_by_years[all_year] == max_data:
                best_years.append(f"{country}, {all_year} year, {max_data} medal\n")
                print(f"{country}, {all_year} year, {max_data} medal\n")
        if args.output is not None:
            file_name = args.output
            file = open(file_name, 'w')
            file.write("\n".join(best_years))
            file.close()


def interactive(filename):
    print("Hello user!")
    users_hello = ''
    while users_hello != "no":
        users_hello = input("Would you like to continue?\n")
        if users_hello == "yes":
            users_country = input("Enter your country:\n")
            dict_medals = dict()
            best_year = 0
            best_number = 0
            worst_year = 0
            worst_number = 100
            count_years = 0
            gold_medals = 0
            silver_medals = 0
            bronze_medals = 0
            first_year = 2022
            with open(filename, 'r') as file:
                element = file.readline().split('\t')
                element = file.readline().split('\t')
                while len(element) > 1:
                    country_name = element[6]
                    noc_name = element[7]
                    year = element[9]
                    medal = element[-1][:-1]
                    if (int(year) < int(first_year)) and (country_name == users_country or noc_name == users_country):
                        first_year = year
                    if country_name == users_country or noc_name in users_country:
                        if year not in dict_medals:
                            dict_medals[year] = [0, 0, 0]
                        if medal == "Gold":
                            dict_medals[year][0] += 1
                        elif medal == "Silver":
                            dict_medals[year][1] += 1
                        elif medal == "Bronze":
                            dict_medals[year][2] += 1
                    element = file.readline().split('\t')
            print(f'First year in game for this country: {first_year}\n')
            for i in dict_medals:
                gold_medals += int(dict_medals[i][0])
                silver_medals += int(dict_medals[i][1])
                bronze_medals += int(dict_medals[i][2])
                sum_to_compare = int(dict_medals[i][0]) + int(dict_medals[i][1]) + int(dict_medals[i][2])
                count_years += 1
                if sum_to_compare > best_number:
                    best_year = i
                    best_number = sum_to_compare
                if sum_to_compare < worst_number:
                    worst_year = i
                    worst_number = sum_to_compare

            print(f'Best year: {best_year}, medals - {dict_medals[best_year][0]} gold - {dict_medals[best_year][1]} '
                  f'silver - {dict_medals[best_year][2]} bronze\n')
            print(f'Worst year: {worst_year},  medals - {dict_medals[worst_year][0]} gold - {dict_medals[worst_year][1]} '
                  f'silver - {dict_medals[worst_year][2]} bronze\n')
            print(f'Mediana - {gold_medals/count_years, 2} gold medals, '
                  f'{silver_medals/count_years, 2} silver medals, '
                  f'{bronze_medals/count_years} bronze medals')


def main():
    if args.medals:
        ten_medalists(args.medals, args.output, args.filename, args.country, args.year, args.noc, args.sport)
    if args.total:
        print(args.total)
        total(total)
    if args.overall:
        overall(args.filename, args.overall)
    if args.interactive:
        interactive(args.filename)



if __name__ == '__main__':
    main()
