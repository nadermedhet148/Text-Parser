from __future__ import unicode_literals

from tokenizer import tokenize , TOK
# this class for transform a string to list of terms after normalization 
class TextTokenizing :
    def __init__(self, text) :
        self.text = text
    # returns a list of tokens
    def tokenizing(self ):
        result = []
        isNextTag = False
        for token in tokenize(str(self.text)):
            # print("{0}: '{1}' {2}".format(
            # TOK.descr[token.kind],
            # token.txt or "-",
            # token.val or ""))
            #  get only specific tokens and ignore the reset
            if(TOK.descr[token.kind] in ["WORD" , "NUMBER" , "USERNAME" , "YEAR"]  ):
                txt = token.txt
                if(isNextTag):
                    # $ is a flag for tag (what we want from the user) so we will add $ before tag token
                    txt = "$" + token.txt
                    isNextTag = False
                result.append(txt or None )
            if(token.txt == "$"):
                isNextTag = True         
        return result