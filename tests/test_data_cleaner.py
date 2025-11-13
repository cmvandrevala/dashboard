from dashboard.data_cleaner import DataCleaner
import pandas as pd

def test_drop_unused_columns_drops_unused_columns_from_a_df():
    df = pd.DataFrame(data={'Context': [], 'Completion Date': [], 'Duration': [], 'Planned Date': [], 'Project': [], 'Notes': [], 'Start Date': [], 'Status': [], 'Tags': [], 'Type': [], 'Task ID': []})
    df = DataCleaner.drop_unused_columns(df)
    assert len(df.keys()) == 0

def test_format_due_date_converts_a_date_to_a_pandas_datetime():
    df = pd.DataFrame(data={'Due Date': ['2025-12-12'], 'Context': [''], 'Completion Date': [''], 'Duration': [''], 'Planned Date': [''], 'Project': [''], 'Notes': [''], 'Start Date': [''], 'Status': [''], 'Tags': [''], 'Type': [''], 'Task ID': ['']})
    df = DataCleaner.format_due_date(df)
    assert len(df['Due Date']) == 1
    assert df['Due Date'][0] == pd.Timestamp('2025-12-12 00:00:00')
