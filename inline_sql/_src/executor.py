import inspect
from typing import Generic, TypeVar

from .runtime import run_query

T = TypeVar("T")


class InlineSQL(Generic[T]):
    """A magic object that lets you run inline SQL queries.

    ### Usage

    ```
    from inline_sql import sql, sql_val

    sql_val^ "SELECT 1 + 1"  # => 2
    sql_val^ "SELECT COUNT() FROM 'disasters.csv'"  # => 803

    n = 50
    df = sql^ "SELECT * FROM 'disasters.csv' LIMIT $n"  # => pd.DataFrame({...})
    sql_val^ "SELECT COUNT() FROM df"  # => 50
    ```
    """

    def __init__(self, scalar: bool) -> None:
        pass

    def __xor__(self, query: str) -> T:
        """Run an inline SQL query."""
        pass
