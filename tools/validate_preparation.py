"""Validate notebook syntax and preparation without changing files or fitting models.

Run from the project root: python tools/validate_preparation.py
"""
import ast
import contextlib
import io
import os
from pathlib import Path

import nbformat
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def main():
    root = Path(__file__).resolve().parents[1]
    notebook_path = root / "Group01_EShopClothing.ipynb"
    notebook = nbformat.read(notebook_path, as_version=4)
    nbformat.validate(notebook)

    code_cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
    for number, cell in enumerate(code_cells, 1):
        compile(cell.source, f"notebook_code_cell_{number}", "exec")
    print(f"Notebook format and syntax passed: {len(code_cells)} code cells.")

    # Select preparation cells by their first assignment, not a fragile cell index.
    prefixes = [
        'df = pd.read_csv("e-shop clothing 2008.csv")',
        'df = df.sort_values(',
        'df["prev_category"] =',
        'df["prev_price"] =',
        'df["previous_clicks"] =',
        'historical_features =',
        'df["next_category"] =',
        'current_features =',
        'session_ids =',
    ]
    selected = [cell for cell in code_cells
                if any(cell.source.startswith(prefix) for prefix in prefixes)]
    assert len(selected) == len(prefixes), "Preparation structure changed; review validator."
    assert all(cell.source.startswith(prefix)
               for cell, prefix in zip(selected, prefixes))

    namespace = {"pd": pd, "np": np, "train_test_split": train_test_split}
    starting_directory = Path.cwd()
    try:
        os.chdir(root)
        for cell in selected:
            tree = ast.parse(cell.source)
            # The final expression only previews a table or prints a status.
            if tree.body and isinstance(tree.body[-1], ast.Expr):
                tree.body.pop()
            with contextlib.redirect_stdout(io.StringIO()):
                exec(compile(tree, "<preparation>", "exec"), namespace)
    finally:
        os.chdir(starting_directory)

    raw = pd.read_csv(root / "e-shop clothing 2008.csv")
    assert raw.shape == (165474, 14)
    assert raw["session ID"].nunique() == 24026
    expected_shapes = {"train": (112491, 26), "test": (28957, 26)}
    for name, shape in expected_shapes.items():
        calculated = namespace[f"{name}_df"]
        exported = pd.read_csv(root / f"{name}.csv")
        assert calculated.shape == shape
        pd.testing.assert_frame_equal(calculated.reset_index(drop=True), exported)
        print(f"{name}: {len(calculated):,} rows, "
              f"{calculated['session ID'].nunique():,} sessions; export matches.")

    assert namespace["df"].shape == (141448, 26)
    assert not namespace["overlap"]
    assert namespace["df"]["next_category"].value_counts().sort_index().to_dict() == {
        1.0: 40495, 2.0: 31936, 3.0: 34132, 4.0: 34885
    }
    print("All 11 history features and target checks passed; session overlap is 0.")
    print("No notebook or CSV files changed. No preprocessing or models fitted.")


if __name__ == "__main__":
    main()
