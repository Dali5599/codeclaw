"""Workspace Symbol Indexer with fast in-memory dictionary lookup."""

import ast
from pathlib import Path
from typing import Dict, List, Tuple

SymbolEntry = Tuple[str, int]  # (symbol_name, line_number)


class WorkspaceSymbolIndexer:
    """Indexes symbols (functions, classes) from Python source files in a workspace.

    The internal ``_index`` dict provides O(1) lookup by symbol name.
    """

    def __init__(self) -> None:
        self._index: Dict[str, List[SymbolEntry]] = {}

    def index_workspace(self, root: str) -> Dict[str, List[SymbolEntry]]:
        """Walk *root* recursively, parse any *.py file and populate the internal dictionary.

        The dictionary maps symbol names to a list of (file_path, line_number) tuples.
        Lookup is O(1) via the internal ``_index`` dict.
        """
        self._index.clear()
        root_path = Path(root)
        if not root_path.is_dir():
            raise ValueError(f"Provided root is not a directory: {root}")

        for py_file in root_path.rglob("*.py"):
            try:
                text = py_file.read_text(encoding="utf-8")
                tree = ast.parse(text, filename=str(py_file))
                self._index_symbols(py_file, tree)
            except Exception:
                # Skip files that cannot be parsed (e.g., syntax errors)
                continue
        return self._index

    def _index_symbols(self, file_path: Path, tree: ast.AST) -> None:
        """Extract FunctionDef and ClassDef symbols and add them to the index."""
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                name = node.name
                lineno = node.lineno
                self._add_symbol(name, str(file_path), lineno)
            elif isinstance(node, ast.ClassDef):
                name = node.name
                lineno = node.lineno
                self._add_symbol(name, str(file_path), lineno)

    def _add_symbol(self, name: str, file_path: str, line_no: int) -> None:
        """Insert a symbol entry into the internal dict (fast O(1))."""
        entries = self._index.setdefault(name, [])
        entries.append((file_path, line_no))

    def lookup(self, symbol: str) -> List[SymbolEntry]:
        """Return all locations where *symbol* is defined, or an empty list."""
        return self._index.get(symbol, [])
