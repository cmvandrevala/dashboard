# Dashboard

## Initial Setup

```bash
poetry install
```

## Setting Up Data

1. Open Omnifocus
2. Select "Remaining" under "View"
3. Export a CSV document with projects and tasks using File > Export...
4. Save the exported CSV document to the root of this project as "Omnifocus.csv"

## Running the App

```bash
poetry run dashboard
```

## Running the Test Suite

```bash
poetry run pytest
```
