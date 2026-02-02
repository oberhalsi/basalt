@echo off

:: 1. Set the PYTHONPATH so Python can see your 'src' folder for imports
set PYTHONPATH=%~dp0src;%PYTHONPATH%

:: 2. If no argument is provided, jump to the shell
if "%~1"=="" goto shell

:file
:: 3. This runs when you do: basalt script.b
python "%~dp0main.py" %*
goto end

:shell
:: 4. This runs when you just type: basalt
:: 'cls' is optional, remove it if you don't want the screen cleared
cls
python "%~dp0src/shell.py"
goto end

:end
:: 5. Clean up the variable so it doesn't mess with other terminal tasks
set PYTHONPATH=