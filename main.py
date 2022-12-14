import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--filename", "-f", required=True)
    parser.add_argument("--medals", action="store_true", required=False)
    parser.add_argument("--country", required=False)
    parser.add_argument("--noc", required=False)
    parser.add_argument("--year", required=False)
    parser.add_argument("--sport", required=False)
    parser.add_argument("--output", "-o", required=False)

    args = parser.parse_args()
    if args.medals:
        ten_medalists(args.medals, args.output, args.filename, args.country, args.year, args.noc, args.sport)


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
            element = line.strip().split("\t")
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