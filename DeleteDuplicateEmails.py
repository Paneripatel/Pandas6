'''Pandas6

1 Problem 1 : Delete Duplicate Emails ( https://leetcode.com/problems/delete-duplicate-emails/)
'''

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by = 'id', inplace=True)
    person.drop_duplicates(subset = 'email', inplace=True)