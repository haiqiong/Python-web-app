import re
import os

class Wiki:
    HOME_PAGE = 'HomePage'

    def __init__(self, base):
        self.base = base
        if not os.path.exists(self.base):
            os.makedirs(self.base)
        elif not os.path.isdir(self.base):
            raise IOError('Wiki base "%s" is not a directory!' % self.base)

    def getPage(self, name=None):
        if not name:
            name = self.HOME_PAGE
        return Page(self, name)

class Page:
    #page name has at least 2 captial letter.
    WIKI_WORD_MATCH = '(([A-Z][a-z0-9]*){2,})'
    #WIKI_WORD = re.compile(WIKI_WORD_MATCH)
    WIKI_WORD_ALONE = re.compile('^%s$' % WIKI_WORD_MATCH)

    def __init__(self, wiki, name):
        #initialize the page for the given wiki with the given name.
        if not self.WIKI_WORD_ALONE.match(name):
            raise(NotWikiWord, name)
        self.wiki = wiki
        self.page = name
        self.path = os.path.join(self.wiki.base, name)

    def exist(self):
        return os.path.isfile(self.path)

    def load(self):
        if not hasattr(self, 'text'):
            self.text = ''
            if self.exist():
                self.text = open(self.path, 'r').read()

    def save(self):
        if not hasattr(self, 'text'):
            self.text = ''
        out = open(self.path, 'w')
        out.write(self.text)
        out.close()

    def delete(self):
        if self.exist():
            os.remove(self.path)

    def getText(self):
        self.load()
        return self.text

class NotWikiWord(Exception):
    pass


