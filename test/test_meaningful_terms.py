#!python3

import unittest
from unittest.mock import patch
from application.meaningful_terms_parser import MeaningfulTermsParser


def mock_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, data, status_code):
            self.json_data = data
            self.status_code = status_code

        def json(self):
            return self.json_data

    json_data = {
        'count': 3,
        'results': [
            {
                'listing_id': 773142437,
                'title': 'Logitech G29, G920, and G27 Magnetic Shifter Mod',
                'description': 'Will Ford Boosted Media Review: '
                               'https://www.youtube.com/watch?v=ZEilXfHDUBw\n\nYoutube video for comparison and '
                               'install:\nhttps://youtu.be/Bi2A8UEqCyU (may need to copy and paste into your '
                               'browser)!\n\nFREE SHIPPING WITH ANY 2 ITEMS PURCHASED IN MY STORE OR ANY ORDER OVER '
                               '40$ CAD!\n\nCompatible with G27, G29 and G920 Wheels. This mod WILL NOT work with the '
                               'Logitech G25.\n\nThe stock feeling of the Logitech paddle shifters are very '
                               'disappointing and lack the proper feedback to truly give proper immersion. With this '
                               'incredibly simple mod give your paddles the correct feel that they have always '
                               'needed! Simply stretch the mod around the wheel hub, line up the magnets to the '
                               'paddles and tighten the single bolt to hold it in place. No removal of the wheel or '
                               'components required! The mod is not permanent and will not affect your warranty in '
                               'any way. It is also printed in high quality PETG to ensure that it will not break '
                               'while stretching it around the wheel hub. The magnets are placed to ensure sufficient '
                               'tactile feedback but will avoid being overly loud and disturbing to others while you '
                               'race!\n\nAll orders from my store are shipped via untracked air packet. Delivery '
                               'times can be found in my FAQ. '
            },
            {
                'listing_id': 743947495,
                'title': 'Thrustmaster Wheel Magnetic Shifter Mod FULL PRINT - Version for Sparco P310, Sparco R383, '
                         'and Ferrari 488 Challenge',
                'description': 'PLEASE READ THIS ENTIRE DESCRIPTION FOR IMPORTANT COMPATIBILITY INFO!\n\nDemo Video: '
                               '(May need to copy and paste)\nhttps://www.youtube.com/watch?v=0ch9Zhmp9Jc\n\nSim '
                               'Racing Garage Review:\nhttps://youtu.be/2yCiC6IofJA\n\nFREE SHIPPING ON ORDERS WITH '
                               'ANY 2 ITEMS OR MORE FROM MY STORE!\n\nThis listing is for a Thrustmaster Magnetic '
                               'Tactile Shifter Modification that I custom made for my racing wheel rig. This '
                               'modification makes up and down shifts feel more precise and realistic - much like an '
                               'actual racecar. You will feel each shift resonate through your hands, '
                               'feeling enhanced realism when you race. You will receive a pair of these so you are '
                               'able to convert both sides. \n\nThis modification is for the following:\n\nSparco '
                               'P310 Mod\nSparco R383 Mod\nFerrari 488 Challenge\n\nPlease see my other listing for a '
                               'different version for these '
                               'wheels:\nhttps://www.etsy.com/ca/listing/740685893/thrustmaster-wheel-magnetic'
                               '-tactile\n\nThrustmaster Open-Wheel\n458 Ferrari Alcantara\nTX Leather Edition \nT300 '
                               'RS \nT300 RS GT \nT300 Ferrari GTE\nTMX and TMX Pro\n\n\nNOT COMPATIBLE:\nFerrari F1 '
                               'Wheel\n458 Italia (From the TX kit that has the 2 pedal setup)\nT-GT\nAny other TM '
                               'wheel not listed.\n\nIf you have questions about compatibility please send me a '
                               'message with a picture of the back of your wheel to confirm before '
                               'ordering.\n\nAvailable in black or red, and with or without CF vinyl finish in black '
                               'and red as well. Printed in PETG (much more durable, heat, and sunlight resistant '
                               'than other thermoplastics) with strong high quality Neodymium magnets and Gorilla '
                               'brand mounting tape.\n\nInstructions for install will be provided with purchase. It '
                               'is very simple and straightforward and will NOT void any warranties.\n\nNo tools '
                               'required for install. It is also easy to remove if needed and will not damage your '
                               'wheel. \n\nPlease note that this product is handmade and while I take pride in my '
                               'workmanship, some cosmetic artifacts may be present. If you are unhappy with your '
                               'product please let me know before leaving a review so I have an opportunity to fix '
                               'it.\n\nAll items are shipped via Canada Post and do not include tracking. If you '
                               'would like to upgrade to tracked or faster shipping, please select the Expedited '
                               'Shipping at checkout. '
            },
            {
                'listing_id': 742090319,
                'title': 'Thrustmaster Wheel Quick Change Modification',
                'description': 'Demo Video: (May need to copy and '
                               'paste)\nhttps://www.youtube.com/watch?v=Jj8sJHI8mtM&t=24s\n\nSim Racing Garage '
                               'Review:\nhttps://youtu.be/2yCiC6IofJA\n\nFREE SHIPPING ON ORDERS WITH ANY 2 ITEMS OR '
                               'MORE FROM MY STORE!\n\nNEW VERSION - Added a second fin to help loosen wheel as well '
                               '- product may vary slightly from my original video and product photos but install and '
                               'function overall remains the same. ALL NEW ORDERS SHIP WITH THE NEW VERSION.\n\nHave '
                               'you ever had your Thrustmaster wheel come loose while trying to set a fast lap? Are '
                               'you tired of having to tighten the finicky screw that Thrustmaster relies on to keep '
                               'your wheel in place? Worry no more! With this quick change modification, '
                               'you will have the extra leverage to ensure that your wheel never comes loose again! '
                               'Simply slide the ring into place and you will find you have much more grip to ensure '
                               'that your wheel is good and tight, never needing to worry about your wheel coming off '
                               'your base until you want it to ever again!\n\nWhy is this mod better than other quick '
                               'release options? Here are 3 reasons:\n1. Flex. This mod does not add any other '
                               'hardware or extensions so the system does not experience any unnecessary flex that is '
                               'typical with other aftermarket mods.\n2. Ease of install and universal to all wheels. '
                               'The mod installs in seconds and you do not need to purchase any extra adapters for '
                               'all of your wheels. With just 1 ring your setup is ready to go!\n3. Cost. This mod is '
                               'a fraction of the cost of other quick release options and you won&#39;t need to '
                               'purchase anything else to get going!\n\nThis modification is compatible with all '
                               'Thrustmaster wheel bases that feature the option of interchangeable wheels. It will '
                               'not interfere with the use of your wheel and is compatible with my magnetic shift mod '
                               'as well! Each of these modifications are made to order with high quality PETG that is '
                               'extremely durable and heat resistant. \n\nInstallation is simple, slide the ring onto '
                               'the wheel hub and install your wheel. The ring is a tight fit to ensure it does not '
                               'rattle during use. Each ring features an optional hole to insert a screw to hold the '
                               'ring in a definitive position if desired however this will likely require you to '
                               'drill your own hole to insert the scew into the plastic hub. Again, '
                               'this is completely optional. The wheel mod can move on the hub if needed and will not '
                               'cause any issues. Please note, if using the screw option to hold the ring in place, '
                               'slide the ring all the way back on the collar and use an M3 machine screw to hold the '
                               'ring in place. Do NOT use the stock Thrustmaster screw that is supplied with your '
                               'base or it could break the tightening ring. I am not responsible for replacement if '
                               'this is ignored.\n\nThis modification is for all Thrustmaster bases that feature '
                               'removable wheels including the T300, TX, TS-PC Racer, and TS-XW.\n\nThis modification '
                               'is handmade - there may be some cosmetic artifacts present that will NOT affect the '
                               'overall function of the mod.\n\nItem is shipped worldwide via untracked packet. If '
                               'you would like a tracked service, please ensure you select it at checkout.\n\nThank '
                               'you for visiting my shop and please check out my other designs if you are interested! '
            }
        ]
    }

    if args[0] == 'https://openapi.etsy.com/v2/shops/fake_store/listings/active?api_key=test_api_key':
        return MockResponse(json_data, 200)
    elif args[0] == 'https://openapi.etsy.com/v2/shops/404_store/listings/active?api_key=test_api_key':
        return MockResponse({"key": "value"}, 404)


class FindStoreItemsTests(unittest.TestCase):
    @patch('requests.get', side_effect=mock_requests_get)
    def test_init_state(self, mock_get):
        parser = MeaningfulTermsParser('fake_store', 'test_api_key')

        self.assertEqual(parser.items, [])

    @patch('requests.get', side_effect=mock_requests_get)
    def test_items_retrieved(self, mock_get):
        parser = MeaningfulTermsParser('fake_store', 'test_api_key')

        parser.find_store_items()
        items_count = len(parser.items)

        self.assertEqual(items_count, 3)

    @patch('requests.get', side_effect=mock_requests_get)
    def test_non_ok_response(self, mock_get):
        parser = MeaningfulTermsParser('404_store', 'test_api_key')

        parser.find_store_items()
        items_count = len(parser.items)

        self.assertEqual(items_count, 0)


class ParseMeaningfulTermsTests(unittest.TestCase):
    @patch('requests.get', side_effect=mock_requests_get)
    def test_init_state(self, mock_get):
        parser = MeaningfulTermsParser('fake_store', 'test_api_key')

        self.assertEqual(parser.meaningful_terms, [])

    @patch('requests.get', side_effect=mock_requests_get)
    def test_terms_retrieved(self, mock_get):
        parser = MeaningfulTermsParser('fake_store', 'test_api_key')

        parser.find_store_items()
        parser.parse_meaningful_terms()
        terms_count = len(parser.meaningful_terms)

        self.assertEqual(terms_count, 340)

    @patch('requests.get', side_effect=mock_requests_get)
    def test_non_ok_response(self, mock_get):
        parser = MeaningfulTermsParser('404_store', 'test_api_key')

        parser.find_store_items()
        parser.parse_meaningful_terms()
        terms_count = len(parser.meaningful_terms)

        self.assertEqual(terms_count, 0)


class Top5TermsTests(unittest.TestCase):
    @patch('requests.get', side_effect=mock_requests_get)
    def test_init_state(self, mock_get):
        parser = MeaningfulTermsParser('fake_store', 'test_api_key')

        parser.parse_meaningful_terms()
        terms = parser.top5_terms()
        self.assertEqual(terms, [])

    @patch('requests.get', side_effect=mock_requests_get)
    def test_terms_retrieved(self, mock_get):
        parser = MeaningfulTermsParser('fake_store', 'test_api_key')

        parser.find_store_items()
        parser.parse_meaningful_terms()
        terms = parser.top5_terms()

        self.assertEqual(terms, ['wheel', 'mod', 'ring', 'thrustmaster', 'modification'])

    @patch('requests.get', side_effect=mock_requests_get)
    def test_non_ok_response(self, mock_get):
        parser = MeaningfulTermsParser('404_store', 'test_api_key')

        parser.find_store_items()
        parser.parse_meaningful_terms()
        terms = parser.top5_terms()

        self.assertEqual(terms, [])


if __name__ == '__main__':
    unittest.main()
