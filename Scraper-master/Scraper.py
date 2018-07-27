import Parser
import time

def main():
    i = 0

    wordlist = []
    startTime = int(time.time())

    print("Begin scraping")

    while True:
        i += 1

        try:
            wordlist = Parser.append_words(wordlist)

        except:
            print("\n")
            return 0

        print("\rRead page nr: [%d]\t\tNr of words: [%d]\t\tSeconds: [%d]" % (
        i, len(wordlist), int(time.time()) - startTime), end='')




if __name__ == '__main__':
    main()
