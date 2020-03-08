#!python3

import sys
from application.meaningful_terms_parser import MeaningfulTermsParser


if __name__ == '__main__':
    api_key = sys.argv[1]

    etsy_stores = [
        'ChrisHDesigns',
        'TheGreatMetalShop',
        'LostCarousel',
        'ATKINSPORT3D',
        'StreetGrid',
        'DriverApparel',
        'FullerFabrication',
        'CustomTableLegs',
        'MetalCraftSupplies',
        'GeniusLeather'
    ]

    for store in etsy_stores:
        parser = MeaningfulTermsParser(store, api_key)
        parser.find_store_items()
        parser.parse_meaningful_terms()
        top_terms = parser.top5_terms()
        print("Top 5 terms for {} are: {}.".format(store, ', '.join(top_terms)))
