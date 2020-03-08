#!python3

import requests
import string

OK = 200
ITEM_INFO = ['title', 'description']
USELESS_WORDS = ['100', '12', '21', '26', '28', '3', '30', '30quot', '40', '45', '5', '7', '9', '90', 'a', 'about',
                 'accept', 'add', 'all', 'also', 'am', 'an', 'and', 'any', 'are', 'as', 'at', 'automatic', 'available',
                 'be', 'before', 'black', 'box', 'brown', 'business', 'but', 'buying', 'by', 'can', 'canada', 'carry',
                 'click', 'cm', 'color', 'colors', 'contact', 'dark', 'days', 'default', 'delivery', 'desired',
                 'different', 'do', 'due', 'e', 'else', 'exchanges', 'extra', 'fit', 'following', 'for', 'found',
                 'freight', 'from', 'fuller', 'g', 'get', 'gift', 'go', 'h', 'has', 'have', 'haven39t', 'height',
                 'here', 'high', 'home', 'i', 'if', 'in', 'infolostcarouselcomau', 'inquiries', 'is', 'it', 'it39s',
                 'item', 'items', 'just', 'larger', 'length', 'let', 'like', 'long', 'look', 'm', 'made', 'make', 'may',
                 'maybe', 'me', 'measurements', 'message', 'more', 'my', 'n', 'name', 'neck', 'need', 'not', 'note',
                 'of', 'on', 'once', 'onto', 'options', 'or', 'order', 'other', 'out', 'oz', 'p', 'per', 'please',
                 'pounds', 'quality', 'quotthingquot', 'r', 'returns', 's', 'sch', 'see', 'send', 'set', 'shipping',
                 'shop', 'short', 'simply', 'size', 'sizes', 'small', 'so', 'something', 'standard', 'store', 't',
                 'takes', 'tall', 'thank', 'that', 'the', 'these', 'they', 'they39re', 'this', 'time', 'to', 'tracking',
                 'us', 'usa', 'used', 'we', 'weeks', 'weight', 'where', 'why', 'width', 'will', 'with', 'within',
                 'working', 'would', 'x', 'you', 'your', '–', '▬▬▬▬▬▬']


class MeaningfulTermsParser:
    def __init__(self, store_url, api_key):
        self.api_key = api_key
        self.store_url = store_url
        self.items = []
        self.meaningful_terms = []

    def find_store_items(self):
        """Find the title and description of all active store items.

        The store items' information is stored as a list of dictionaries in the class variable items.

        :return: no value
        :rtype: none
        """

        url = "https://openapi.etsy.com/v2/shops/{}/listings/active?api_key={}".format(self.store_url, self.api_key)
        response = requests.get(url)
        if response.status_code == OK:
            self.items = [{key: item[key] for key in ITEM_INFO} for item in response.json()['results']]

    def parse_meaningful_terms(self):
        """Parse the most meaningful terms from the titles and descriptions of store items.

        The store terms in increasing order in the class variable meaningful_terms.
        Determining how meaningful a word is in the context of a store is a difficult task, and there are multiple
        statistical analysis approaches and libraries to accomplish this task. For the purposes of this exercise I chose
        to define "most meaningful" as occurring the most, and not in a list of words to exclude.

        :return: no value
        :rtype: none
        """

        terms_count = {}
        for item in self.items:
            words = []
            for info_section in ITEM_INFO:
                words += item[info_section].translate(str.maketrans('', '', string.punctuation)).split()
            for word in words:
                word_lower = word.lower()
                if word_lower not in USELESS_WORDS:
                    if word_lower in terms_count:
                        terms_count[word_lower] += 1
                    else:
                        terms_count[word_lower] = 1
        self.meaningful_terms = [k for k, _ in sorted(terms_count.items(), key=lambda item: item[1])]

    def top5_terms(self):
        """Return the top 5 most meaningful terms from the items in a store, from most to least meaningful.

        :return:
        :rtype: list of str
        """
        terms = self.meaningful_terms[-5:]
        terms.reverse()
        return terms
