from __future__ import unicode_literals

import re
import math
from collections import Counter
# this class to get cosine similatry for tow text
# look for that is you don't know what is it https://en.wikipedia.org/wiki/Cosine_similarity
class similarity():
    def __init__(self , origin , text ):
        self.origin = origin
        self.text = text
    # calculate  cosine similarity for the two vectors "list of tokens counter"
    def __getCosine(self ,vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])

        sum1 = sum([vec1[x]**2 for x in vec1.keys()])
        sum2 = sum([vec2[x]**2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

    # return bag of words how each term appear in the document 
    def __textToVector(self ,text):
        word = re.compile(r'\w+')
        words = word.findall(text)
        return Counter(words)

    # returned the calculate value for the 2 text 
    def getSimilarityPercentage(self ):
        text1 = self.origin
        text2 = self.text

        vector1 = self.__textToVector(text1)
        vector2 = self.__textToVector(text2)

        cosine_result = self.__getCosine(vector1, vector2)
        return cosine_result * 100
        
