from PIL import Image
import numpy as np

img = Image.open(r"iddddk.jpeg").convert('L')
mat = np.array(img)

w, h = img.size

print(mat)

choice = input('\n1-Image 2-Text: ')
if choice == '2':
    F = open('File1.txt', 'r')
else:
    F = ''
    for line in mat:
        for elem in line:
            F += str(elem) + ' '
    F += 'ö'
    print(F)
   
   
Dictionary = [
    '!', '“', '#', '$', '%', '&', '‘', '(', ')', '*', '+', ',', '–', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
    '8',
    '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '', '€', '&', '‚', 'ƒ', '„', '…', '†', '‡', 'ˆ', '‰', 'Š',
    '‹', 'Œ', '&', 'Ž', '‘', '’', '“',
    '”', '•', '–', '—', '˜', '™', 'š', '›', 'œ', '&', 'ž', 'Ÿ', '&', '¡', '¢', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª',
    '«', '¬', '­', '®', '¯', '°', '±',
    '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È',
    'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï',
    'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ',
    'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í',
    'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ', 'ÿ', ' ', '\n', '-']


def compress(Dictionary):
    dic = Dictionary
    w = ''
    code = ''

    for line in F:
        for char in line:
            p = w + char
            if p in dic:
                w = p
            else:
                dic.append(p)
                code += str(dic.index(w)) + ' '
                w = char
    code += str(dic.index(w))
    return code


def decompress(code):
    tab = code.split(' ')[:-1]
    v = tab[0]
    string = str(Dictionary[int(v)])
    w = Dictionary[int(v)]

    for i in range(1, len(tab)):
        v = tab[i]
        if int(v) < len(Dictionary):
            entry = Dictionary[int(v)]
        else:
            entry += w + w[0]
        string += entry
        Dictionary.append(w + entry[0])
        w = entry
    return string


print('\nLe code:')
print(len(Dictionary))
code = compress(Dictionary)
print(code)
print(len(Dictionary))

print('\nLe text:')
stri = decompress(code)
print(stri)
if choice == '1':
    Fimg = stri.split(' ')[:-1]
    inter = []

    for i in range(len(Fimg)):
        inter.append(int(Fimg[i]))

    inter = np.reshape(inter, (h, w))
    Image.fromarray(inter).show()
print(len(Dictionary))    