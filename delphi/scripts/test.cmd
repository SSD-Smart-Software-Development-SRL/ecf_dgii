@echo off
setlocal
rem Run from a RAD Studio Command Prompt. No API credentials or live calls needed.
pushd "%~dp0.."
set "ECF_DELPHI_COMPILER=%~1"
if "%ECF_DELPHI_COMPILER%"=="" set "ECF_DELPHI_COMPILER=dcc32"
where "%ECF_DELPHI_COMPILER%" >nul 2>nul
if errorlevel 1 goto fail
if not exist build mkdir build
"%ECF_DELPHI_COMPILER%" -B -Q -Usrc -N0build -LEbuild -LNbuild EcfDgii.dpk
if errorlevel 1 goto fail
"%ECF_DELPHI_COMPILER%" -B -Q -Usrc -N0build -Ebuild tests\EcfDgii.Tests.dpr
if errorlevel 1 goto fail
build\EcfDgii.Tests.exe
if errorlevel 1 goto fail
"%ECF_DELPHI_COMPILER%" -B -Q -Usrc -N0build -Ebuild examples\SendEcf.dpr
if errorlevel 1 goto fail
popd
exit /b 0
:fail
popd
exit /b 1
