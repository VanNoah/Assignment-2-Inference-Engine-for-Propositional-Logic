from KnowledgeBase import KnowledgeBase
from Sentence import Sentence

class ForwardChaining:
    """Implementation of Forward Chaining Algorithm"""
    def __init__(self, knowledge_base):
        self.kb= knowledge_base

    # forward chaining algorithm to check if kb entails query
    # algorithm starts from symbols known to be true and makes way through premises of clauses
    # until the query is reached
    

    def solve(self, query):

        #PSUEDO CODE ON SLIDE 27 of week 7 lecture slides
        count = []
        inferred = []
        agenda = []

        while(agenda):
            p = agenda.pop()
            if not inferred[p]:
                inferred[p] = True
                # yea noah if you figure out this bit :^)
                # foreach HornClause c in whose premise appears p appears do
                    #decrement count[c]
                    #if count[c] == 0 do
                        #if HEAD[c] = q then # I think q is the ask?
                            # return true
                        #push(HEAD[c], agenda)

        return False