with open ("estudiantes.txt", "r") as file:
    content = file.readlines()
    print(content[0:13])


    def read_lines(filename, num_lines):
        with open (filename, 'r') as file:
            for _ in range(num_lines):
                line= file, read_line()
                if not line:
                    break
                    print(line.strip())

read_lines('estudiantes.txt')