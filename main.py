import re


def find(pattern, strings):
    result_strings = []
    group = []

    for string in strings:
        if string != '':
            match = re.search(pattern, string)
            if match:
                group.append(match.group())
                result_strings.append(string)

    return group, result_strings


def split(group, strings):
    result = set()
    maximum = 0

    for x in group:
        if len(x) > maximum:
            maximum = len(x)

    for i in range(0, len(group)):
        if len(group[i]) == maximum:
            result.add(strings[i])

    return result


def parsing(strings):
    result = set()
    pattern = r'[,.?!{}()\[\]\n\r\s\t\"«»]'
    strings = [string.lower() for string in re.split(pattern, strings)]
    f_group, f_strings = find('([b-df-hj-np-tv-xz])(\\1)', strings)
    s_group, s_strings = find('[b-df-hj-np-tv-xz]{2,}', strings)
    return f_group + s_group, f_strings + s_strings


group = []
strings = []
file_name = input("Input file name for parsing: ")
file = open(file_name)

for line in file:
    new_group, new_strings = parsing(line)

    if new_group:
        group += new_group
        strings += new_strings

strings = split(group, strings)

for word in strings:
    print(word)
