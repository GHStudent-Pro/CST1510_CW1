# Week 9 – Hashing and Auth – Programming Problems

Use the `bcrypt` library (`pip install bcrypt`). Keep secrets (keys, passwords) out of your code and repository.

## Task 1: Write `generate_hash()`
Write a function `generate_hash(psw)` that:
1. Encodes the password string to UTF-8 bytes
2. Generates a salt with `bcrypt.gensalt()`
3. Hashes with `bcrypt.hashpw()`
4. Returns the hash **decoded** back to a string

Test it by hashing `'Magic123'` twice and comparing the two hashes (they should differ because of different salts).

## Task 2: Write `is_valid_hash()`
Write a function `is_valid_hash(psw, hash_str)` that:
1. Encodes both the password and the stored hash to bytes
2. Uses `bcrypt.checkpw()` to compare
3. Returns `True` or `False`

Test it with a correct and a wrong password.

## Task 3: Register & Login with File I/O
Implement both functions, then test the full flow:
- `register_user(name, password, filepath='lab_users.txt')` — hash the password and append `name,hash` to the file.
- `login_user(name, password, filepath='lab_users.txt')` — return `True` if name + password match any entry in the file (return `False` if the file does not exist).

Register `alice` and `bob`, then test: alice with the correct password, alice with a wrong password, and an unknown user.

## Task 4: Reflection Questions
1. Why does `generate_hash()` return a different string each time for the same password?
2. What would happen if two users had the same password and you stored their hashes? Would the hashes be identical? Why or why not?
3. Why is it important to use `bcrypt.checkpw()` rather than comparing hash strings directly with `==`?
