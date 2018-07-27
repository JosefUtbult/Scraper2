import urllib.request
import time
import _thread

import Parser

global_run = True

def main():

    try:
        site_buffer = []

        _thread.start_new_thread(parse_site, (site_buffer,))

        for i in range(0, 10):
            _thread.start_new_thread(load_site, (site_buffer,))

        while True:
            pass

    except:

        global_run = False

        print("\n")
        return 0


def parse_site(site_buffer):

    global global_run

    i = 0

    wordlist = []
    startTime = int(time.time())

    print("Begin scraping")

    while global_run:

        if len(site_buffer) > 0:

            i += 1

            wordlist = Parser.append_words(wordlist, site_buffer.pop(0))

            print("\rRead page nr: [%d]\t\tNr of words: [%d]\t\tSites in buffer: [%d]\t\tSeconds: [%d]" % (
                i, len(wordlist), len(site_buffer), int(time.time()) - startTime), end='')


def load_site(site_buffer):

    global global_run

    while global_run:

        if len(site_buffer) < 30:
            site_buffer.append(str(urllib.request.urlopen('https://sv.wikipedia.org/wiki/Special:Slumpsida').read()))


if __name__ == '__main__':
    main()
