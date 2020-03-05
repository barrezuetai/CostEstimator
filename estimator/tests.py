from django.test import TestCase
from .utils.pdfparse import normalize as norm


class PDFScanTestCase(TestCase):
    """ A group of test cases to ensure that the pdf can be
    successfully and correctly parsed """
    def setUp(self):
        pass

    def test_pdf_scans(self):
        self.assertEqual(1, 1)

    def test_normalize_makes_lowercase(self):
        test_data = ["This is Uppercase", "AAAAAA", "O!"]
        expected = ["this is uppercase", "aaaaaa", "o!"]

        normalized = norm(test_data)

        for i, n in enumerate(normalized):
            self.assertEqual(n, expected[i])

    def test_normalize_removes_non_ascii_chars(self):
        pass
