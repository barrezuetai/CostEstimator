from django.test import TestCase
from .utils.pdfparse import normalize as norm
# from .utils.pdfparse import pdf_to_text as p2t
from .utils.estimate import get_pcr, get_prices
from .utils.estimate import find_average_price, generate_prices


class PDFScanTestCase(TestCase):
    """ A group of test cases to ensure that the pdf can be
    successfully and correctly parsed """
    def setUp(self):
        pass

    def test_pdf_scans(self):
        # converted_text = p2t()
        # self.assertTrue(len(converted_text) > 0)
        pass

    def test_normalize_makes_lowercase(self):
        test_data = ["This is Uppercase", "AAAAAA", "O!"]
        expected = ["this is uppercase", "aaaaaa", "o!"]
        normalized = norm(test_data)
        for i, n in enumerate(normalized):
            self.assertEqual(n, expected[i])

    def test_normalize_removes_non_ascii_chars(self):
        pass


class EstimateTestCase(TestCase):

    def setUp(self):
        pass

    def test_get_pcr(self):
        test_data = {
            'net_revenue': 1,
            'gross_revenue': 2
        }
        res = get_pcr(test_data)
        self.assertAlmostEqual(res, .5)

    def test_get_prices_populates_dict(self):
        prices = get_prices()
        self.assertGreater(len(prices), 0)

    def test_get_prices_keys_only_nums(self):
        prices = get_prices()
        for _, v in prices.items():
            self.assertTrue(v.isnumeric())

    def test_find_average_price_returns_value(self):
        self.assertTrue(find_average_price(5, 10))

    def test_generate_prices_returns_prices(self):
        prices = generate_prices(1)
        self.assertGreater(len(prices), 0)


class ModelTestCase(TestCase):

    def setup(self):
        pass
