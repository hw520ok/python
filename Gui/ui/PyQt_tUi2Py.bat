@echo off
for %%i in (*.ui) do (
	E:\Python3.5.1\Lib\site-packages\PyQt5\pyuic5.bat %%i -o %%~ni.py
)

@pause
