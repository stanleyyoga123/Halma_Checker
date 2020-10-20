DIR=venv

if ! -d "$DIR"; then
    pip3 install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    clear
    python3 main.py
else
    source venv/bin/activate
    pip3 install -r requirements.txt
    clear
    python3 main.py
fi