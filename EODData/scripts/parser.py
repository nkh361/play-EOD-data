"""
- create parsing for AAPL closing dates
- create markov chain to predict the time series. the algorithm will calculate the transition probabilities
  between the states based on historical data, then uses these probabilities to make trading decisions.
"""

import csv

def parser(csv_file: str) -> str:
    with open(csv_file, newline=" ") as infile:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row["Symbol"], row["Close"])

