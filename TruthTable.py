from KnowledgeBase import KnowledgeBase
from Sentence import Sentence

class TruthTable:
    """Implementation of Truth Table Entailment Method"""
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.count = 0

    def solve(self, query):
        symbols = self.kb.symbols
        models = self.generate_models(symbols)
        table = []
        for model in models:
            row = {symbol: model[symbol] for symbol in symbols}
            row[query] = self.evaluate_query(query, model)
            table.append(row)
        print(table)
        self.display_table(table)
        return all(row[query] for row in table)

    def generate_models(self, symbols):
        models = []
        n = len(symbols)
        for i in range(2**n):
            model = {}
            for j in range(n):
                model[symbols[j]] = bool((i // (2 ** j)) % 2)
            models.append(model)
        return models

    def evaluate_query(self, query, model):
        for sentence in self.kb.sentences:
            if not sentence.solve(model):
                return False
        return model[query]

    def display_table(self, table):
        if not table:
            print("No models generated.")
            return
        header = list(table[0].keys())
        print("|", end="")
        for col_name in header:
            print(f" {col_name} |", end="")
        print()
        print("|" + "-" * (4 * len(header) - 1) + "|")
        for row in table:
            print("|", end="")
            for col_name in header:
                print(f" {str(row[col_name])[0]} |", end="")
            print()
        print()

