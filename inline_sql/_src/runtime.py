from typing import Any, Dict, List, Tuple

import duckdb
import pandas as pd
import sqlparse


def prepare_query(query: str) -> Tuple[str, List[str]]:
    """Prepare a query, replacing all placeholders with numbered parameters."""
    pass


def run_query(query: str, context: Dict[str, Any]) -> pd.DataFrame:
    """Run a SQL query against an in-memory DuckDB database."""
    pass
