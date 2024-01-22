## Installation


 Clone the repository and proceed with steps mentioned below

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
$env:FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```

### Server
```
$ErrorActionPreference = "Stop"

Get-ChildItem -Path . -Filter *.pyc -Recurse | Remove-Item -Force

$env:FLASK_APP = "core\server.py"

flask run
```


