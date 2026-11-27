import sqlite3

def init_fts_vault(db_path: str = ':memory:'):
    con = sqlite3.connect(db_path)
    con.execute('CREATE VIRTUAL TABLE IF NOT EXISTS tools USING fts5(name, spec)')
    con.execute('INSERT INTO tools VALUES (?, ?)', ('lead-harvester', 'Async B2B pipeline'))
    return con.execute('SELECT * FROM tools WHERE tools MATCH ?', ('Async',)).fetchall()

if __name__ == '__main__':
    print('MCP Vault Active:', init_fts_vault())
