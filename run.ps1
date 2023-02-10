$path = Split-Path -Parent $MyInvocation.MyCommand.Path
cd $path
$env:FLASK_ENV="development"
$env:FLASK_APP="flaskr"
$env:FLASK_DEBUG=1
start http://127.0.0.1:5000
python -m flask run
