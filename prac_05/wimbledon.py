def read_data(filename):
    """Reads data from the CSV file into a list of lists."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header
        for line in in_file:
            fields = line.strip().split(",")
            if len(fields) >= 3:
                data.append(fields)
    return data

def build_champ_counts(data):
    """Builds a dictionary with champion name as key and win count as value."""
    champ_counts = {}
    for record in data:
        champion = record[1]  # Assuming 2nd column is Champion
        champ_counts[champion] = champ_counts.get(champion, 0) + 1
    return champ_counts

def get_countries(data):
    """Extracts unique countries from the data and returns them alphabetically."""
    countries = set()
    for record in data:
        country = record[2]  # Assuming 3rd column is Country code
        countries.add(country)
    return sorted(countries)

def main():
    filename = "wimbledon.csv"
    data = read_data(filename)
    champ_counts = build_champ_counts(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, count in sorted(champ_counts.items()):
        print(f"{champion} {count}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))

if __name__ == "__main__":
    main()