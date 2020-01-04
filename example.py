from __future__ import unicode_literals
from Parsers import Parsing

text = ("Your Credit Card ****3933 had a Successful transaction of EGP 203.15 @ORANGE KARGO MALL,your available bal.EGP20.28 for lost/stolen card call 19700")
template = ("Your Credit Card ****$card had a Successful transaction of $AmountCurrency $amount $beneficiary ,your available bal.$BalanceCurrency$balance for lost/stolen card call 19700")

parsing = Parsing.Parsing(template , text)
values = parsing.getValuesFromText()






