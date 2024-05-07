import sys

def check_country(country_name, path_to_fle):
    with open(path_to_fle) as file_stream:

        file_stream.readline()  # Skip the first line

        for line in file_stream:
            line_parts = line.split(',')
            country = line_parts[0]
            if country == country_name:
                return True

    return False


def check_years(first_year, second_year):
    return 1960 <= first_year <= second_year <= 2017


def pop_diff(country_name, year1, year2, path_file):
    if not check_country(country_name, path_file):
        sys.exit(f"The provided country name '{country_name}' was not found")

    if not check_years(year1, year2):
        sys.exit(f"The provided years are either out of bound or crossed: {year1}, {year2}")

    with open(path_file) as file_stream:
        file_stream.readline()  # Skip the first line
        for line in file_stream:
            line_parts = line.split(',')

            if line_parts[0] == country_name:
                first_year_population = int((line_parts[year1 - 1960 + 5].replace('"', '')))
                second_year_population = int((line_parts[year2 - 1960 + 5].replace('"', '')))
                break

    return (second_year_population / first_year_population) - 1


def max_diff(year1, year2, path_to_file):
    max_diff_val = None
    max_country = ""
    with open(path_to_file) as file_stream:
        file_stream.readline()  # Skip the first line
        for line in file_stream:
            line_parts = line.split(',')
            country_name = line_parts[0].replace('"', '')
            pop_diff_val = pop_diff(country_name, year1, year2, path_to_file)
            if (max_diff_val is None) or (pop_diff_val > max_diff_val):
                max_diff_val = pop_diff_val
                max_country = country_name
    return max_country, max_diff_val


def neg_diff(year1, year2, path_to_file):
    with open(path_to_file) as file_stream:
        file_stream.readline()  # Skip the first line
        for line in file_stream:
            line_parts = line.split(',')
            country_name = line_parts[0].replace('"', '')
            pop_diff_val = pop_diff(country_name, year1, year2, path_to_file)
            if pop_diff_val < 0:
                print(country_name)


if __name__ == '__main__':
    with open('world_population.csv', 'r') as file:
        for line in split_csv_text(file.read()):
            print(line)
    country_name = input("Enter country name: ")
    while country_name != "stop":
        year1 = int(input("Enter first year: "))
        year2 = int(input("Enter first year: "))
        # print(pop_diff(country_name, year1, year2, "world_population.csv"))
        # max_diff(year1, year2, 'world_population.csv')
        neg_diff(year1, year2, 'world_population.csv')
        country_name = input("Enter country name: ")
