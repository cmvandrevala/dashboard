from dashboard.eisenhower_matrix import EisenhowerMatrix
import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

def test_urgent_and_important_returns_an_empty_df_given_an_empty_df():
    df = pd.DataFrame(data={'Due Date': [], 'Flagged': []})
    assert len(df) == 0
    urgent_and_important = EisenhowerMatrix(df).urgent_and_important()
    assert len(urgent_and_important) == 0

def test_urgent_and_important_does_not_return_a_not_important_item():
    due_date = datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("1 day")
    df = pd.DataFrame(data={'Due Date': [due_date], 'Flagged': [False]})
    assert len(df) == 1
    urgent_and_important = EisenhowerMatrix(df).urgent_and_important()
    assert len(urgent_and_important) == 0

def test_urgent_and_important_returns_an_important_item_which_is_due_in_one_day():
    due_date = datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("1 day")
    df = pd.DataFrame(data={'Due Date': [due_date], 'Flagged': [True]})
    assert len(df) == 1
    urgent_and_important = EisenhowerMatrix(df).urgent_and_important()
    assert len(urgent_and_important) == 1
    assert urgent_and_important.iloc[0]["Due Date"] == due_date
    assert urgent_and_important.iloc[0]["Flagged"]

def test_urgent_and_important_returns_an_important_item_which_is_due_in_one_week():
    due_date = datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("1 W")
    df = pd.DataFrame(data={'Due Date': [due_date], 'Flagged': [True]})
    assert len(df) == 1
    urgent_and_important = EisenhowerMatrix(df).urgent_and_important()
    assert len(urgent_and_important) == 1
    assert urgent_and_important.iloc[0]["Due Date"] == due_date
    assert urgent_and_important.iloc[0]["Flagged"]

def test_urgent_and_important_does_not_return_an_important_item_which_is_due_in_eight_days():
    due_date = datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("8 D")
    df = pd.DataFrame(data={'Due Date': [due_date], 'Flagged': [True]})
    assert len(df) == 1
    urgent_and_important = EisenhowerMatrix(df).urgent_and_important()
    assert len(urgent_and_important) == 0

def test_urgent_not_important_returns_an_empty_df_given_an_empty_df():
    df = pd.DataFrame(data={'Due Date': [], 'Flagged': []})
    assert len(df) == 0
    urgent_not_important = EisenhowerMatrix(df).urgent_not_important()
    assert len(urgent_not_important) == 0

def test_urgent_not_important_filters_out_important_items():
    due_date = datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("1 day")
    df = pd.DataFrame(data={'Due Date': [due_date], 'Flagged': [True]})
    assert len(df) == 1
    urgent_not_important = EisenhowerMatrix(df).urgent_not_important()
    assert len(urgent_not_important) == 0

def test_urgent_not_important_returns_a_not_important_item_which_is_due_in_one_day():
    due_date = datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("1 day")
    df = pd.DataFrame(data={'Due Date': [due_date], 'Flagged': [False]})
    assert len(df) == 1
    urgent_not_important = EisenhowerMatrix(df).urgent_not_important()
    assert len(urgent_not_important) == 1
    assert urgent_not_important.iloc[0]["Due Date"] == due_date
    assert not urgent_not_important.iloc[0]["Flagged"]

def test_urgent_not_important_returns_a_not_important_item_which_is_due_in_one_week():
    due_date = datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("1 W")
    df = pd.DataFrame(data={'Due Date': [due_date], 'Flagged': [False]})
    assert len(df) == 1
    urgent_not_important = EisenhowerMatrix(df).urgent_not_important()
    assert len(urgent_not_important) == 1
    assert urgent_not_important.iloc[0]["Due Date"] == due_date
    assert not urgent_not_important.iloc[0]["Flagged"]

def test_urgent_not_important_filters_out_a_not_important_item_which_is_due_in_eight_days():
    due_date = datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("8 D")
    df = pd.DataFrame(data={'Due Date': [due_date], 'Flagged': [False]})
    assert len(df) == 1
    urgent_not_important = EisenhowerMatrix(df).urgent_not_important()
    assert len(urgent_not_important) == 0

def test_important_not_urgent_returns_an_empty_df_given_an_empty_df():
    df = pd.DataFrame(data={'Due Date': [], 'Flagged': []})
    assert len(df) == 0
    important_not_urgent = EisenhowerMatrix(df).important_not_urgent()
    assert len(important_not_urgent) == 0

def test_important_not_urgent_filters_out_not_important_items():
    due_date = datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("8 D")
    df = pd.DataFrame(data={'Due Date': [due_date], 'Flagged': [False]})
    assert len(df) == 1
    important_not_urgent = EisenhowerMatrix(df).important_not_urgent()
    assert len(important_not_urgent) == 0

def test_important_not_urgent_returns_an_important_item_which_is_due_in_10_days():
    due_date = datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("10 D")
    df = pd.DataFrame(data={'Due Date': [due_date], 'Flagged': [True]})
    assert len(df) == 1
    important_not_urgent = EisenhowerMatrix(df).important_not_urgent()
    assert len(important_not_urgent) == 1
    assert important_not_urgent.iloc[0]["Due Date"] == due_date
    assert important_not_urgent.iloc[0]["Flagged"]

def test_important_not_urgent_filters_out_an_important_item_which_is_due_in_one_day():
    due_date = datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("1 day")
    df = pd.DataFrame(data={'Due Date': [due_date], 'Flagged': [True]})
    assert len(df) == 1
    important_not_urgent = EisenhowerMatrix(df).important_not_urgent()
    assert len(important_not_urgent) == 0

def test_not_urgent_not_important_returns_an_empty_df_given_an_empty_df():
    df = pd.DataFrame(data={'Due Date': [], 'Flagged': []})
    assert len(df) == 0
    not_urgent_not_important = EisenhowerMatrix(df).not_urgent_not_important()
    assert len(not_urgent_not_important) == 0

def test_not_urgent_not_important_filters_out_important_items():
    due_date = datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("8 D")
    df = pd.DataFrame(data={'Due Date': [due_date], 'Flagged': [True]})
    assert len(df) == 1
    not_urgent_not_important = EisenhowerMatrix(df).not_urgent_not_important()
    assert len(not_urgent_not_important) == 0

def test_not_urgent_not_important_returns_a_not_important_item_which_is_due_in_10_days():
    due_date = datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("10 D")
    df = pd.DataFrame(data={'Due Date': [due_date], 'Flagged': [False]})
    assert len(df) == 1
    not_urgent_not_important = EisenhowerMatrix(df).not_urgent_not_important()
    assert len(not_urgent_not_important) == 1
    assert not_urgent_not_important.iloc[0]["Due Date"] == due_date
    assert not not_urgent_not_important.iloc[0]["Flagged"]

def test_not_urgent_not_important_filters_out_a_not_important_item_which_is_due_in_one_day():
    due_date = datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("1 day")
    df = pd.DataFrame(data={'Due Date': [due_date], 'Flagged': [False]})
    assert len(df) == 1
    not_urgent_not_important = EisenhowerMatrix(df).not_urgent_not_important()
    assert len(not_urgent_not_important) == 0
