# dev-weekly-api
A collection of the weekly news letters from multiple resources like android weekly,iOSweekly,javascriptweekly,reactjsweekly,golangweekly,etc ...


## Installing Requirements
Use Virtualenv and install the packages.
```
pip install -r requirements.txt
```
## Running Flask Server
Go to the root dir and run the below line in the terminal.
```
python app.py
```
## Creating a new Database
Create a database(Used SQLite) with the table structure mentioned in *struct.sql* and update the database name in *database.py* file.
```
database.py

# Replace 'sqlite:///ramdan.db' with your path to database

engine = create_engine('sqlite:///ramdan.db', convert_unicode=True)

```

