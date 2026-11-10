# Week 11 – Streamlit Dashboard – Programming Problems

> **Data files:** the student data is in `DATA/students.csv`. Keep the `DATA/` folder in your project folder and load it with a path such as `pd.read_csv('DATA/students.csv')`.

Streamlit cannot run inside a Jupyter notebook: write the code into `.py` files and run them with `streamlit run Home.py`. Install with `pip install streamlit`.

## Task 1: Core Widgets
Create `demo.py` that uses: `st.set_page_config`, `st.title`, `st.subheader`, `st.write`, `st.text_input`, `st.number_input`, `st.selectbox`, `st.button` (show `st.success` when clicked), `st.columns(3)` with `st.metric` in each column, and a sidebar with a title and some text.

## Task 2: Session State Concept
Simulate `st.session_state` with a plain dictionary:
- Initialise `logged_in = False`, `username = None`, `role = None`.
- Write `simulate_login(name, role)` and `simulate_logout()`.
- Print the state before login, after login and after logout.

## Task 3: Login Page (`Home.py`)
Build a login page that:
- Initialises `logged_in`, `username` and `role` in `st.session_state`.
- Redirects to `pages/1_Dashboard.py` if already logged in.
- Uses `st.form()` with a username field, a password field (`type="password"`) and a submit button.
- Checks credentials against a hardcoded test-user dictionary (e.g. `alice` / admin and `bob` / user), sets the session state on success and shows `st.error("Invalid credentials")` on failure.

## Task 4: Protected Dashboard Page (`pages/1_Dashboard.py`)
Build a dashboard page that:
- Has an authentication guard at the top (`st.warning`, `st.switch_page("Home.py")`, `st.stop()`) when the user is not logged in.
- Shows a welcome message with the username and role.
- Builds a sample incidents DataFrame (`severity`, `category`, `status`) and shows metrics for total, open and critical incidents with `st.metric()`.
- Shows a bar chart of incidents per category (`st.bar_chart`) and the data (`st.dataframe`).
- Has a sidebar **Logout** button that clears the session state and redirects to `Home.py`.

## Task 5: Display Data

Load `DATA/students.csv` in a Streamlit page. Show the table with `st.dataframe()` and three `st.metric()` values: number of students, average grade and average attendance.

## Task 6: Interactive Filters

Add a sidebar `st.selectbox` for City (with an "All" option) and an `st.slider` for minimum grade. Show only the matching students and update the metrics to match the filter.

## Task 7: Layout: Columns and Tabs

Organise the page with `st.columns()` for the metrics and `st.tabs()` with a "Table" tab and a "Charts" tab (e.g. `st.bar_chart` of average grade per course).

## Task 8: Caching

Put the CSV loading code in a function decorated with `@st.cache_data`. Explain in a comment why this makes the app faster when widgets are changed (remember Streamlit reruns the whole script).

## Task 9: Reflection Questions
1. Why do we need `st.session_state` instead of regular variables?
2. What does `st.stop()` do in the authentication guard?
3. Why use `st.form()` instead of regular `st.text_input()` + `st.button()`?
