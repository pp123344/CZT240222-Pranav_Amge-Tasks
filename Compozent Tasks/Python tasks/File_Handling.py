def handle_file():
    input_file = "Read_file.txt"
    output_file = "Write_file.txt"

    try:
        with open(input_file, 'r') as file:
            content = file.read()
            word_count = len(content.split())

        with open(output_file, 'w') as file:
            file.write(f"Number of words: {word_count}")

        print(f"Word count written to {output_file}")
    except FileNotFoundError:
        print(f"File {input_file} not found.")

handle_file()
