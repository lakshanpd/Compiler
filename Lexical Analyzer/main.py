import scanner

tokens_set, token_types = scanner.scanner('text_file.txt')

for i in range(len(tokens_set)):
    print(repr(tokens_set[i]), token_types[i])
    