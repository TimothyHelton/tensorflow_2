# PGAdmin Setup
1. From the main directory call `make pgadmin`
    - The default browser will open to `localhost:5000`
1. Enter the **PGAdmin** default user and password.
    - These variable are set in the `envfile`.
1. Click `Add New Server`.
    - General Name: Enter the <project_name>
    - Connection Host: Enter <project_name>_postgres
    - Connection Username and Password: Enter **Postgres** username and password
      from the `envfile`.

# PyCharm Setup
1. Database -> New -> Data Source -> PostgreSQL
1. Name: <project_name>_postgres@localhost
1. Host: localhost
1. Port: 5432
1. Database: <project_name>
1. User: **Postgres** username
1. Password: **Postgres** password

# SNAKEVIZ Execution
1. Create profile file
    - Jupyter Notebook
        - `%prun -D profile.prof enter_cmd_or_file`
    - Command Line
        - `python -m cProfile -o profile.prof program.py`
1. Start server **from the command line** on port 10000
    - `snakeviz profile.prof --hostname 0.0.0.0 --port 10000 -s`
1. Open host web browser
    - `http://0.0.0.0:10000/snakeviz/`

# Memory Profiler
1. Open Jupyter Notebook
1. Load Extension
    - `%load_ext memory_profiler`
1. Run profiler
    - `%memit enter_code_here`
