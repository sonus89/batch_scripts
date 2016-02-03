::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::                                                      ::
::		Cygwin64 Auto-Deploy Script		::
::		Platform: Windows			::
::		Written by Máté Gál			::
::		Date: 2015-Jan-29			::
::		Contact: mate.gal@gmail.com		::
::							::
:::::::::::::: Configuring command line ::::::::::::::::::
::                                                      ::
	color 0a										
	echo off
	prompt $g
	cls
::                                                      ::
::::::::::::::: Requesting admin rights ::::::::::::::::::
::                                                      ::
IF '%PROCESSOR_ARCHITECTURE%' EQU 'amd64' (
   >nul 2>&1 "%SYSTEMROOT%\SysWOW64\icacls.exe" "%SYSTEMROOT%\SysWOW64\config"
 ) ELSE (
   >nul 2>&1 "%SYSTEMROOT%\system32\icacls.exe" "%SYSTEMROOT%\system32\config"
)
::                                                      ::
:::::::::: Set error flag if no admin rights :::::::::::::
::                                                      ::
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )
::                                                      ::
::                                                      ::
:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B
::                                                      ::
::                                                      ::
:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
::                                                      ::
::                                                      ::
:::::::::::::::::::: Welcome text ::::::::::::::::::::::::
echo.
echo 	Welcome to Auto-Deploy Cygwin64!			
echo.													
::                                                      ::
::::::::::::::: Path vairable for Cygwin64 :::::::::::::::
::                                                      ::
set cygwin_path="c:\cygwin64"
::                                                      ::
:::::::: Appending "bin" folder to "path" env-var ::::::::
::                                                      ::
SETX /M path %path%;%cygwin_path%\bin\
::                                                      ::	
::::::::::::: Checking if folder already exist :::::::::::
::                                                      ::
IF EXIST %cygwin_path% (
rmdir /s /q %cygwin_path%
mkdir %cygwin_path%
) ELSE (
mkdir %cygwin_path%
del /s /q "%cygwin_path%\*.*"
)
::                                                      ::
:::: Download process with a native OS executable ::::::::
::                                                      ::
echo	Downloading Cygwin Setup to %cygwin_path%
pause
bitsadmin /transfer Download_Cygwin_Setup http://cygwin.com/setup-x86_64.exe %cygwin_path%\setup-x86_64.exe
::                                                      ::
::::::::::::::::::: Installation process :::::::::::::::::
::                                                      ::
cls
echo	Installing Cygwin64 basic packages to %cygwin_path%
timeout 5
::                                                      ::
:::::::::::::::: Changing working directory ::::::::::::::
cd /D  %cygwin_path%
::                                                      ::
::installing cygwin-base packages
::Ain't nobody need this shit 'cause cygsetup installs base packages anyway.. 
::%cygwin_path%\setup-x86_64.exe -q -D -n -B -s http://cygwin.mirror.constant.com -C base 
::                                                      ::
::installing gcc,wget...etc. packages
%cygwin_path%\setup-x86_64.exe -q -R %cygwin_path% -D -n -s http://cygwin.mirror.constant.com -P wget -P gcc-g++ -P make -P diffutils -P libmpfr-devel -P libgmp-devel -P libmpc-devel
::                                                      ::
sleep 5
::processing local install				::
%cygwin_path%\setup-x86_64.exe -q -L -l %cygwin_path% -P wget -P gcc-g++ -P make -P diffutils -P libmpfr-devel -P libgmp-devel -P libmpc-devel
::                                                      ::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
