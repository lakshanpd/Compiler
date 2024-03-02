import tokens
import language

def scanner(file_path):
    with open(file_path, 'r') as file:
        characters = list(file.read())

    tokens_set = []
    token_types = []
    index = 0

    while index < len(characters):
        if characters[index] in (language.Letter + ['_']):
            token, index = tokens.identifier(characters, index)
            tokens_set.append(token)
            token_types.append('<IDENTIFIER>')
        elif characters[index] == '/' and characters[index+1] == '/':
            token, index = tokens.comment(characters, index)
            tokens_set.append(token)
            token_types.append('<DELETE>')
        elif characters[index] in language.Digit:
            token, index = tokens.integer(characters, index)
            tokens_set.append(token)
            token_types.append('’<INTEGER>')
        elif characters[index] in language.Operator_symbol:
            token, index = tokens.operator(characters, index)
            tokens_set.append(token)
            token_types.append('<OPERATOR>')
        elif characters[index] == '"':
            token, index = tokens.string(characters, index)
            tokens_set.append(token)
            token_types.append('<STRING>')
        elif characters[index] in [' ', '\t', '\n']:
            token, index = tokens.spaces(characters, index)
            tokens_set.append(token)
            token_types.append('<DELETE>')
        elif characters[index] in ['(', ')', ';', ',']:
            token, index = tokens.punction(characters, index)
            tokens_set.append(token)
            token_types.append('<PUNCTION>')
        else:
            index += 1

    return tokens_set, token_types