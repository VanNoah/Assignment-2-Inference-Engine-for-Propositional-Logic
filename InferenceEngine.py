import sys
import os
import re
from FileReader import FileReader
from KnowledgeBase import KnowledgeBase
from Sentence import Sentence
from TruthTable import TruthTable
from ForwardChaining import ForwardChaining
from BackwardChaining import BackwardChaining
import time

def get_test_files():
    """Return a list of all test files matching the pattern test*.txt in the current directory, sorted numerically."""
    files = [f for f in os.listdir('.') if f.startswith('test') and f.endswith('.txt')]
    # Sort files based on the numerical part of the filename
    files.sort(key=lambda f: int(re.search(r'\d+', f).group()))
    return files

def run_tests(filenames, methods = ['TT', 'FC', 'BC'], do_time = False):

    if len(methods) < 1:
        methods = ['TT', 'FC', 'BC']
    
    results = {}

    for filename in filenames:
        try:
            tell, ask = FileReader.read(filename)  # Read the file
        except FileNotFoundError:
            print(f"File {filename} not found.")
            continue

        if len(tell) == 0:
            print(f"No tell found in {filename}.")
            continue
        if not ask:
            print(f"No ask found in {filename}.")
            continue

        # Initialize an empty dictionary for storing results for this file
        results[filename] = {}

        # Process each inference method
        for method in methods:
            if do_time:
                start_time = time.time()

            if method == 'TT':
                kb = KnowledgeBase(tell, 'GS')  # Setup knowledge base with general sentences
                tt = TruthTable(kb)
                result = tt.solve(ask)
            elif method == 'FC':
                kb = KnowledgeBase(tell, 'HF')  # Setup knowledge base with horn form
                fc = ForwardChaining(kb)
                result = fc.solve(ask)
            elif method == 'BC':
                kb = KnowledgeBase(tell, 'HF')  # Setup knowledge base with horn form
                bc = BackwardChaining(kb)
                result = bc.solve(ask)
            else:
                result = "Unknown method entered."

            if do_time:
                result += " - {} seconds".format(time.time() - start_time)

            # Store the result in the inner dictionary
            results[filename][method] = result
            

    return results

if __name__ == "__main__":
    timer = False
    methods = []
    if len(sys.argv) > 1:
        filenames = sys.argv[1:]  # Use command-line arguments if provided

        if "timer" in filenames:
            timer = True
            filenames.remove("timer")
        if "TT" in filenames:
            methods.append('TT')
            filenames.remove("TT")
        if "FC" in filenames:
            methods.append('FC')
            filenames.remove("FC")
        if "BC" in filenames:
            methods.append('BC')
            filenames.remove("BC")

        if len(filenames) < 1:
            filenames = get_test_files()
    else:
        filenames = get_test_files()  # Dynamically get all test files


    results = run_tests(filenames, methods, timer)  # Run the tests
    for filename, methods in results.items():
        print(f"Results for {filename}:")
        for method, result in methods.items():
            print(f"  {method}: {result}")
