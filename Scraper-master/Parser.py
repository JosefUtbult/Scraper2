import urllib.request
from io import UnsupportedOperation

illegalText = ["<", ">", "=", "!DOCTYPE", "<script>", "</script>", "/", u"\u005C", "(", ")", "&", "#", "\"", "\'", "[",
               "]", ",", ".", "-", ";", ":", "\n", "|", "~", "px", "em", "+", "{", "}"]



def append_words(word_list, site):
    file = ""

    if len(word_list) == 0:
        file = open("inputFile.txt", "r")

        while True:

            try:
                word = file.readline()

            except UnsupportedOperation as e:

                break

            if word == "":
                break

            elif word[-1] == '\n':
                word = word[:-1]

            word_list.append(word)

        file.close()

    words_append = parse_site(site)

    words_append = parse_list(words_append)

    word_list = sorted(parse_list(word_list + words_append), key=str.lower)

    output = "\n".join(word_list)

    file = open("inputFile.txt", "w")

    file.write(output)
    file.close()

    return word_list


def parse_list(inputList):

    return list(set(map(lambda x: str(x).lower(), inputList)))


def parse_site(site):

    output = []

    try:

        temp = site.split("<p>")[1:]

        for i in range(0, len(temp)):

            temp[i] = temp[i].split(" ")

            for word in temp[i]:

                if parse_illeagal(word):
                    output.append(word)

    except Exception as e:

        print(e)

    return output


def parse_illeagal(instance):
    if instance == "":
        return False

    elif instance.isdigit():
        return False

    for illeagal in illegalText:

        if instance.find(illeagal) != -1:
            return False

    return True
