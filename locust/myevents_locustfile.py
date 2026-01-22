from database import get_db

def my_events_logic(user):
    db = get_db()
    db.row_factory = None

    # Optimised: direct DB fetch, no extra loops
    my_events = db.execute(
        "SELECT * FROM events WHERE user = ?",
        (user,)
    ).fetchall()

    return my_events
