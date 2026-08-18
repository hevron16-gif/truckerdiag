import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock

DB_PATH = Path(__file__).resolve().parent / "data" / "comments.db"
_lock = Lock()


def _connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with _lock, _connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                text TEXT NOT NULL,
                created_at TEXT NOT NULL,
                ip TEXT NOT NULL,
                is_approved INTEGER NOT NULL DEFAULT 0
            )
            """
        )


def add_comment(*, name: str, text: str, ip: str) -> dict:
    created_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    with _lock, _connect() as conn:
        cur = conn.execute(
            """
            INSERT INTO comments (name, text, created_at, ip, is_approved)
            VALUES (?, ?, ?, ?, 0)
            """,
            (name, text, created_at, ip),
        )
        return {
            "id": cur.lastrowid,
            "name": name,
            "text": text,
            "created_at": created_at,
            "ip": ip,
            "is_approved": False,
        }


def list_approved() -> list[dict]:
    with _lock, _connect() as conn:
        rows = conn.execute(
            """
            SELECT id, name, text, created_at
            FROM comments
            WHERE is_approved = 1
            ORDER BY id DESC
            """
        ).fetchall()
    return [dict(row) for row in rows]


def list_all() -> list[dict]:
    with _lock, _connect() as conn:
        rows = conn.execute(
            """
            SELECT id, name, text, created_at, ip, is_approved
            FROM comments
            ORDER BY id DESC
            """
        ).fetchall()
    out = []
    for row in rows:
        item = dict(row)
        item["is_approved"] = bool(item["is_approved"])
        out.append(item)
    return out


def approve_comment(comment_id: int) -> bool:
    with _lock, _connect() as conn:
        cur = conn.execute(
            "UPDATE comments SET is_approved = 1 WHERE id = ?",
            (comment_id,),
        )
        return cur.rowcount > 0


def delete_comment(comment_id: int) -> bool:
    with _lock, _connect() as conn:
        cur = conn.execute("DELETE FROM comments WHERE id = ?", (comment_id,))
        return cur.rowcount > 0


init_db()
