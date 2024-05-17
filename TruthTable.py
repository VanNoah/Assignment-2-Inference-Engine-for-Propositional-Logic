from KnowledgeBase import KnowledgeBase
from Sentence import Sentence


class TruthTable:
    """Implementation of Truth Table Entailment Method"""
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def solve(self, query):
        symbols = self.kb.symbols
        models = self.generate_models(symbols)
        count_models = 0
        entail_query = True

        for model in models:
            if self.evaluate_model(model):
                count_models += 1
                if not model[query]:
                    entail_query = False

        result = f"YES: {count_models}" if entail_query else "NO"
        return result

    def generate_models(self, symbols):
        models = []
        n = len(symbols)
        for i in range(2**n):
            model = {}
            for j in range(n):
                model[symbols[j]] = bool((i // (2 ** j)) % 2)
            models.append(model)
        return models

    def evaluate_model(self, model):
        for sentence in self.kb.sentences:
            if not sentence.solve(model):
                return False
        return True


