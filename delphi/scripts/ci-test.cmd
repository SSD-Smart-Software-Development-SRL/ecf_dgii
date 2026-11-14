@echo off
setlocal
rem Repository variable DELPHI_RSVARS points to the licensed installation on the runner.
if not defined DELPHI_RSVARS (
  echo ERROR: Set repository variable DELPHI_RSVARS to the full path of rsvars.bat.
  exit /b 1
)
if not exist "%DELPHI_RSVARS%" (
  echo ERROR: The configured rsvars.bat does not exist on this runner.
  exit /b 1
)
call "%DELPHI_RSVARS%"
if errorlevel 1 exit /b 1
call "%~dp0test.cmd" dcc32
if errorlevel 1 exit /b 1
call "%~dp0test.cmd" dcc64
if errorlevel 1 exit /b 1
exit /b 0
