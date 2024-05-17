from KnowledgeBase import KnowledgeBase
from Sentence import Sentence


class BackwardChaining:
    """Implementation of Backward Chaining Algorithm"""

    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def __bc_entails(self, query, inferred, chain):
        # If the query is already known to be true, return true
        if inferred[query]:
            return True, chain

        # Add the query to the chain
        chain.append(query)

        # Get all sentences where the head is the query
        relevant_sentences = [sentence for sentence in self.kb.sentences if sentence.head == query]

        for sentence in relevant_sentences:
            premises_satisfied = True

            for premise in sentence.conjuncts:
                if not self.__bc_entails(premise, inferred, chain.copy())[0]:
                    premises_satisfied = False
                    break

            if premises_satisfied:
                inferred[query] = True
                return True, chain

        return False, []

    def solve(self, query):
        inferred = {symbol: False for symbol in self.kb.symbols}
        chain = []

        # Initialize inferred facts from the knowledge base
        for sentence in self.kb.sentences:
            if not sentence.conjuncts:  # If a sentence has no conjuncts, it's a fact
                inferred[sentence.head] = True

        solution_found, chain = self.__bc_entails(query, inferred, chain)

        if solution_found:
            solution = "YES: " + ", ".join(chain)
        else:
            solution = "NO"

        return solution