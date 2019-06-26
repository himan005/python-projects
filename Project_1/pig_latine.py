import sys

vowels = 'aeiou'


def pig_latin(word):

    if word[0] in vowels:
        pig_latin = word + 'way'
    else:
        pig_latin = word[1:] + word[0] + 'ay'

    return pig_latin


if __name__ == "__main__":

    while True:
        word = input("Enter a word and get a pig latin translation: ")
        print(pig_latin(word), file=sys.stderr)
        try_again = input("\nWant to try again?(Press Enter else n to stop): ")
        if try_again.lower() == "n":
            break




