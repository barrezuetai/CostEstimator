""" This module organizes all of the methods relating to parsing pdf files """
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFPageInterpreter


def pdf_to_text(pdf=None):
    """ Converts pdf file into text one can run computations on
    params: pdf file
    returns: a list of strings corresponding to segments of pdf text
    """
    if pdf is None:
        pdf = open('/Users/isaacbarrezueta/Downloads/LoanPacket.pdf', 'rb')

    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    eb = []
    for page in PDFPage.get_pages(pdf):
        interpreter.process_page(page)
        layout = device.get_result()
        for element in layout:
            if isinstance(element, LTTextBoxHorizontal):
                eb.append(element.get_text())
    return eb


def normalize(text):
    """ Get's rid of non-ascii symbols and makes everything lower case
    for further processing"""
    for i, t in enumerate(text):
        text[i] = t.lower()
    return text


def find_relevant_data():
    pass
