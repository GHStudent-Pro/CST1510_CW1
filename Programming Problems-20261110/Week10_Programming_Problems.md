# Week 10 – SQL, Properly – Programming Problems

## Task 1: Create the Database
Using `sqlite3`, create (or recreate) a database file `lab_week9.db` and connect to it.

## Task 2: CREATE TABLE
Create a `users` table with the columns `id` (integer primary key, autoincrement), `username` (text, not null, unique), `password_hash` (text, not null) and `role` (text, default `'user'`).

## Task 3: INSERT (`add_user`)
Write `add_user(conn, username, password_hash, role='user')` using **parameterised** queries (`?` placeholders). Add three users: `alice` (admin), `bob` and `charlie`.

## Task 4: SELECT
Implement two functions:
- `get_all_users(conn)` — return all users.
- `get_user(conn, username)` — return one user (or `None` if unknown).

## Task 5: UPDATE & DELETE
Implement `update_role(conn, username, new_role)` and `delete_user(conn, username)`. Change bob's role to `moderator`, delete charlie, then print the remaining users.

## Task 6: SQL Injection Demonstration
Write an unsafe version of `get_user` that builds the query with an f-string. Compare a normal query for `alice` with the input `' OR '1'='1`, and explain why parameterised queries matter.

## Task 7: Load CSV Data with Pandas
1. Create a small CSV file `sample_incidents.csv` with columns `incident_id`, `severity`, `category`, `status`, `description` (e.g. three rows: a High Phishing incident, a Critical Ransomware incident, a Low Policy incident).
2. Load it into a DataFrame with `pd.read_csv()`.
3. Load the DataFrame into SQLite as a table called `cyber_incidents` using `to_sql()`.
4. Query the table back into a DataFrame with `pd.read_sql()`.

## Task 8: Reflection Questions
1. What is the difference between `fetchall()` and `fetchone()`?
2. What would happen if you called `DELETE FROM users` without a `WHERE` clause?
3. Why does `data.to_sql('cyber_incidents', conn, if_exists='replace')` require the `if_exists` parameter?
