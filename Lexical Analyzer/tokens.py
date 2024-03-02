import language

def identifier(sequence, index):
    token = sequence[index]
    index += 1
    while index < len(sequence) and (sequence[index] in (language.Letter + language.Digit + ['_'])):
        token += sequence[index]
        index += 1
    return token, index

def integer(sequence, index):
    token = sequence[index]
    index += 1
    while index < len(sequence) and (sequence[index] in language.Digit):
        token += sequence[index]
        index += 1
    return token, index

def operator(sequence, index):
    token = sequence[index]
    index += 1
    while index < len(sequence) and (sequence[index] in language.Operator_symbol):
        token += sequence[index]
        index += 1
    return token, index

def string(sequence, index):
    token = sequence[index]
    index += 1
    while index < len(sequence) and (sequence[index] != '"'):
        token += sequence[index]
        index += 1
    token += sequence[index]
    index += 1
    return token, index

def spaces(sequence, index):
    token = sequence[index]
    index += 1
    while index < len(sequence) and (sequence[index] in [' ', '\t', '\n']):
        token += sequence[index]
        index += 1
    return token, index

def comment(sequence, index):
    token = sequence[index]
    index += 1
    while index < len(sequence) and (sequence[index] != '\n'):
        token += sequence[index]
        index += 1
    return token, index

def punction(sequence, index):
    token = sequence[index]
    index += 1
    return token, index