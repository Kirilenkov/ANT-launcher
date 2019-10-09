def letter_encoder(letter, decoding):
    result = str(decoding.find(letter) + 1)
    if len(result) == 1:
        result = '0' + result
    return result

code = 'абвгде'

print(letter_encoder('в', code))
