'''
2 Problem 2 : The Number of Rich Customers ( https://leetcode.com/problems/the-number-of-rich-customers/ )
'''

import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    store = store[store['amount'] > 500]
    return pd.DataFrame({'rich_count':[store['customer_id'].nunique()]})