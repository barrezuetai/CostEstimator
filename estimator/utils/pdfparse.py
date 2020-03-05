""" This module organizes all of the methods relating to parsing pdf files """


def pdf_to_text():
    """ Converts pdf file into text one can run computations on"""
    pass


def normalize(text):
    """ Get's rid of non-ascii symbols and makes everything lower case
    for further processing"""
    for i, t in enumerate(text):
        text[i] = t.lower()
    return text


def find_relevant_data():
    pass
