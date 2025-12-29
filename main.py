def read_file():
    with open("character.csv") as file_data:
        char_data = file_data.read()
    return char_data

file_data = read_file()

def load_character(file_data):
    split_file = file_data.split("\n")
    csv_data = []
    for data in split_file:
        line = data.split(",")
        csv_data.append(line)

    header_data = csv_data[0]
    row_data= csv_data[1:]


    character = {}
    for header in header_data:
        character[header] = []


    for row in row_data:
        for header_name, cell_value in zip(header_data, row):
            if cell_value != "":
                character[header_name].append(cell_value)

    return character

def main():
    current_char = load_character(file_data)
    
    




if __name__ == "__main__":
    main()