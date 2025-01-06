def sort_on(dict):
    return dict["num"]


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()
    lower = file_contents.lower()
    letters = {}
    for character in lower:
        if character.isalpha():
            if character in letters:
                letters[character] += 1
            else:
                letters[character] = 1

    list_of_dict = []
    keys = letters.keys()
    for key in keys:
        list_of_dict.append({'name': key, 'num': letters[key]})

    list_of_dict.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {f.name} ---")
    print(f"{len(words)} words found in document")
    print()
    for letter in list_of_dict:
        print(f"The '{letter['name']}' character was found {letter['num']} times")

    print("--- End report ---")


main()