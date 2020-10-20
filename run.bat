@echo off
IF not exist venv ( 
    python -m venv venv 
    venv\Scripts\activate 
    echo Installing Dependencies
    pip install -r requirements.txt
    cls
    python main.py
    pause
) ELSE (
    venv\Scripts\activate
    cls
    python main.py
    pause
)