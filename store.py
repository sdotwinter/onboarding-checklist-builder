import sqlite3
from pathlib import Path

def db_path(root: Path) -> Path:
    return root / "onboarding.db"

def init_db(root: Path) -> None:
    conn = sqlite3.connect(db_path(root))
    conn.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, owner TEXT NOT NULL DEFAULT '', completed INTEGER NOT NULL DEFAULT 0)")
    conn.commit(); conn.close()

def add_item(root: Path, title: str, owner: str = "") -> None:
    conn = sqlite3.connect(db_path(root)); conn.execute("INSERT INTO items(title,owner,completed) VALUES (?,?,0)",(title,owner)); conn.commit(); conn.close()

def list_items(root: Path):
    conn = sqlite3.connect(db_path(root)); rows=conn.execute("SELECT id,title,owner,completed FROM items ORDER BY id").fetchall(); conn.close(); return rows

def assign_item(root: Path, item_id: int, owner: str) -> None:
    conn = sqlite3.connect(db_path(root)); conn.execute("UPDATE items SET owner=? WHERE id=?",(owner,item_id)); conn.commit(); conn.close()

def complete_item(root: Path, item_id: int) -> None:
    conn = sqlite3.connect(db_path(root)); conn.execute("UPDATE items SET completed=1 WHERE id=?",(item_id,)); conn.commit(); conn.close()
