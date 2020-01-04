from Tokenizers import Tokinizer
from Similarty import Similarity 
# parser helper which returned extracted values from text when compare it for a tag 
class Parsing:
    def __init__(self , origin , text ):
        self.origin = origin
        self.text = text
    # returns a parsed value and similarity for the 2 document 
    def getValuesFromText(self):
        values = {}
        similarityHelper = Similarity.similarity(self.origin , self.text )
        similarity = similarityHelper.getSimilarityPercentage()
        # TODO must be updated with add weight for text length
        if(similarity > 55):
            originTokens = Tokinizer.TextTokenizing(self.origin).tokenizing()
            textTokens = Tokinizer.TextTokenizing(self.text).tokenizing()
            values = self.__getParsedValues(originTokens , textTokens)
        return { "values" : values , "similarity" : similarity }
    #  compare template tokens with text tokens to return parsed values 
    def __getParsedValues(self , originTokens = [] , textTokens = []) :
        values = {}
        for originToken in originTokens:
            for textToken in textTokens:
                # remove matched value
                if(originToken == textToken):
                    textTokens.remove(textToken)
                    break
                # if not matched and originToken is a tag we will assign it to values dictionary 
                elif originToken != textToken and "$" in originToken :
                    values[originToken]= [textToken]
                    textTokens.remove(textToken)
                    # go to next words till find the nex word that match it 
                    nextOriginToken = originTokens[originTokens.index(originToken) + 1]
                    nextTextToken = textTokens[0]
                    while nextOriginToken != nextTextToken and "$" not in nextOriginToken :
                        values[originToken].append(nextTextToken)
                        textTokens.remove(nextTextToken)
                        nextTextToken = textTokens[0]
                    break
        # connect values in the dick with each other as a string
        for key in values:
            values[key] =  ' '.join(values[key])
        return values


