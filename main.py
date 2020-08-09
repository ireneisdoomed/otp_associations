#!/usr/bin/env python

import argparse
import numpy as np
from src.utils import *

def parsing():

    # Initiating parser
    parser = argparse.ArgumentParser(description=
    "A tool to fetch the association score data from the Open Targets REST API for a given disease id or target.")

    # Main optional arguments inside a mutually exclusive group
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", dest="target", type=str, help="The ID of the target for which you want to do the analysis.")
    group.add_argument("-d", dest="disease", type=str, help="The ID of the disease for which you want to do the analysis.")

    # Optional arguments
    parser.add_argument("-e", dest="export", type=str, help="JSON filename from the exported query result.")
    parser.add_argument("-m", dest="minimum", type=float, help="Minimum score value to filter associations with lower quality data points.")

    args = parser.parse_args()
    
    return args

def main():
    '''
    Prints to stdout the  result of the query and returns relevant association score values.

    Returns:
    mean: Average of every overall association score values.
    maximum: Highest overall association score value.
    minimum: Lowest overall association score value.
    standard deviation: Standar deviation of every overall association score values.
    '''

    args = parsing()

    # "type" defines the query parameter to differentiate between disease and target ID
    if args.disease:
        type = "disease"
        data = query(type, args.disease, scorevalue_min=args.minimum)
    elif args.target:
        type = "target"
        data = query(type, args.target, scorevalue_min=args.minimum)

    assert len(data), "A problem ocurred with the query. Please check that the ID provided is correct."
    
    # stdout prints for every association
    for record in data.values():
        print(record)
    
    # overall metrics
    scores = [record["association_score.overall"] for record in data.values()]
    mean = np.mean(scores)
    highest = np.max(scores)
    lowest = np.min(scores)
    stdev = np.std(scores)

    print("-------------------------------------")
    print(f"{len(scores)} associations have been found for this {type} ID.\n")
    print(f"""Association score values:
    Average score: {mean}
    Maximum score: {highest}
    Minimum score: {lowest}
    Standard Deviation: {stdev}""")
    print("-------------------------------------")

    if args.export:
        export(data, args.export)

    return mean, highest, lowest, stdev


if __name__ == "__main__":
    print("-----------------------------------------------")
    print("Welcome! Here's how to fetch associations from the Open Targets Platform.")
    main()