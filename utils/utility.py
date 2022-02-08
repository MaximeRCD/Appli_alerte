import re

from IOs.iphone import read_iphone_searched


def test_email(email):
    pattern = re.compile(r"""\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]{2,}\.[A-Z|a-z]{2,}\b""")
    return pattern.search(email)


def test_price(n):
    pattern = re.compile(r"""^\d{3,5}$""")
    return pattern.search(n)


def email_in_db(email):
    if email in [adress_mail["email"] for adress_mail in read_iphone_searched()]:
        return True
    else:
        return False
