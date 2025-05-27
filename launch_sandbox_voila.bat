@echo off
call venv\Scripts\activate
cd /d "%~dp0"
voila llm_sandbox.ipynb --browser
pause