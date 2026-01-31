@echo off
setlocal enabledelayedexpansion

echo ============================= test session starts =============================
echo platform %OS% -- Python 3.x -- Basalt
echo rootdir: %CD%
echo.

set PASSED=0
set FAILED=0
set TOTAL=0

:: Count total files for percentage calculation
for %%f in (tests\*.b) do set /a TOTAL+=1
set CURRENT=0

for %%f in (tests\*.b) do (
    set /a CURRENT+=1
    set FILENAME=%%~nf
    
    set /a "PERCENT=(!CURRENT!*100)/!TOTAL!"

    set "DISP_NAME=tests/!FILENAME!.b ........................................."
    set "DISP_NAME=!DISP_NAME:~0,40!"

    python main.py tests\!FILENAME!.b > tests\!FILENAME!.actual 2>nul

    fc tests\!FILENAME!.actual tests\!FILENAME!.expected > nul 2>&1
    
    if !errorlevel! equ 0 (
        echo !DISP_NAME! PASSED [!PERCENT!%%]
        set /a PASSED+=1
        del tests\!FILENAME!.actual
    ) else (
        echo !DISP_NAME! FAILED [!PERCENT!%%]
        set /a FAILED+=1
    )
)

echo.
if %FAILED% equ 0 (
    echo ========================== %PASSED% passed in 0.05s ==========================
) else (
    echo ==================== %FAILED% failed, %PASSED% passed in 0.05s ====================
)