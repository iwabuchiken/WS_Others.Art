@echo off

echo killing MuseScore.exe
taskkill /im MuseScore.exe
taskkill /im MuseScore3.exe

echo killing wish.exe
taskkill /im wish.exe

echo killing Domino.exe
taskkill /im Domino.exe

echo killing javaw.exe
taskkill /im javaw.exe

echo killing thunderbird.exe
taskkill /im thunderbird.exe

echo killing chrome.exe
taskkill /im chrome.exe

taskkill /f /im filezilla.exe

taskkill /f /im sakura.exe

exit

REM pause

REM exit

