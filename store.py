import sqlite3
from pathlib import Path

def db_path(root:Path): return root/'onboarding.db'
def init_db(root:Path):
    c=sqlite3.connect(db_path(root)); c.execute('CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,owner TEXT,completed INTEGER DEFAULT 0)'); c.commit(); c.close()
def add_item(root:Path,title:str,owner:str=''):
    c=sqlite3.connect(db_path(root)); c.execute('INSERT INTO items(title,owner,completed) VALUES (?,?,0)',(title,owner)); c.commit(); c.close()
def list_items(root:Path):
    c=sqlite3.connect(db_path(root)); r=c.execute('SELECT id,title,owner,completed FROM items ORDER BY id').fetchall(); c.close(); return r
def assign_item(root:Path,item_id:int,owner:str):
    c=sqlite3.connect(db_path(root)); c.execute('UPDATE items SET owner=? WHERE id=?',(owner,item_id)); c.commit(); c.close()
def complete_item(root:Path,item_id:int):
    c=sqlite3.connect(db_path(root)); c.execute('UPDATE items SET completed=1 WHERE id=?',(item_id,)); c.commit(); c.close()
