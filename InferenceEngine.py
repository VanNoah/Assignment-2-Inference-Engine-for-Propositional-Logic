import sys
from FileReader import FileReader
from KnowledgeBase import KnowledgeBase
from Sentence import Sentence
from TruthTable import TruthTable
from ForwardChaining import ForwardChaining
from BackwardChaining import BackwardChaining

def run_tests():
    methods = ['TT', 'FC', 'BC']
    results = {}

    for i in range(16):
        filename = f'test{i}.txt'
        try:
            tell, ask = FileReader.read(filename)
        except:
            print(f"File {filename} not found.")
            continue

        if len(tell) == 0:
            print(f"No tell found in {filename}.")
            continue
        if not ask:
            print(f"No ask found in {filename}.")
            continue

        results[filename] = {}

        for method in methods:
            if method == 'TT':
                kb = KnowledgeBase(tell, 'GS')  # setup knowledge base with general sentences
                tt = TruthTable(kb)
                result = tt.solve(ask)
            elif method == 'FC':
                kb = KnowledgeBase(tell, 'HF')  # setup knowledge base with horn form
                fc = ForwardChaining(kb)
                result = fc.solve(ask)
            elif method == 'BC':
                kb = KnowledgeBase(tell, 'HF')
                bc = BackwardChaining(kb)
                result = bc.solve(ask)
            else:
                result = "Unknown method entered."

            results[filename][method] = result

    return results

if __name__ == "__main__":
    results = run_tests()
    for filename, methods in results.items():
        print(f"Results for {filename}:")
        for method, result in methods.items():
            print(f"  {method}: {result}")
