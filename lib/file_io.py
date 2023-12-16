def write_file(file_name="logfile", file_content="Log 1: 5 Bananas added"):
    with open(f'{file_name}.txt', 'w') as file:
        file.write(file_content)

def append_file(file_name="logfile", append_content="Log 2: 3 Bananas added"):
    with open(f'{file_name}.txt', 'a') as file:
        file.write(append_content)

def read_file(file_name="logfile"):
    with open(f'{file_name}.txt', 'r') as file:
        file_content = file.read()
    return file_content

write_file(file_name="logfile", file_content="Log 1: 5 bananas added")
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

result = read_file(file_name="logfile")
print(result)
