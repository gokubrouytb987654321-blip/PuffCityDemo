@echo off
setlocal
cd /d "%~dp0"
if not exist "%LocalAppData%\Programs\Python\Python313\python.exe" (
  echo Python 3.13 introuvable. Utilise le lanceur py -3.13.
)
py -3.13 -m PyInstaller --noconfirm --clean --onefile --windowed --name PuffCity --add-data "index.html;PuffHouse" --add-data "PuffCity.html;PuffHouse" --add-data "Plugins;PuffHouse\Plugins" launcher.py
if errorlevel 1 (
  echo.
  echo Echec de compilation. Verifie que PyInstaller est installe :
  echo py -3.13 -m pip install pyinstaller
  pause
  exit /b 1
)
copy /y "dist\PuffCity.exe" ".\PuffCity.exe" >nul
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
del /q PuffCity.spec 2>nul
echo.
echo PuffCity.exe cree avec succes.
pause