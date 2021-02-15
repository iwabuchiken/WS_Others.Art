
REM ==============================
REM 	browser
REM 	2019/09/16 14:18:11
REM ==============================
:web_page_keyboard_opera

REM : opera
pushd "C:\WORKS_2\Programs\opera"

rem : set urls 2020年11月17日18:27:33
rem : log files / 2020年11月17日18:27:39
rem set url_1="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=music+log&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"
set url_1="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=session+shino&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"

rem : session memo : shakuhachi : 2021年2月10日18:04:21
set url_1_2="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=session+shaku&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"


rem : video files : bamboo / 2020年11月17日18:27:39
set url_2="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=video+bamboo&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"

rem : video files : flute / 2020年11月17日18:39:02
set url_2="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=video+jap.flute&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"

start launcher.exe %url_1%
start launcher.exe %url_1_2%
start launcher.exe %url_2%

REM : log
rem 	start launcher.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=kb+log&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"
REM : video
rem 	start launcher.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=video+kb&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"
REM 	start launcher.exe "https://docs.zoho.com/sheet/open/ek7i4683eb5df87d04a23acef09182e7df623/sheets/free/ranges/A3"

rem 	start launcher.exe "https://www.youtube.com/playlist?list=PLZe1Q2NRG8YXa2FCHsE3Ji3VCOg2Ey8LS"

	goto exit_web_page_keyboard


:exit_web_page_keyboard

REM ==============================
REM 	apps : metronome
REM 	2019/10/24 15:11:38
REM ==============================
REM : metronome
rem pushd "C:\WORKS_2\Programs\opera"
rem : comment out 2020年10月11日18:13:24
rem start launcher.exe https://www.flutetunes.com/metronome/


REM 	pushd "C:\WORKS_2\Programs\opera"
REM : metronome
REM 	start launcher.exe "https://www.metronomeonline.com"
REM 	start launcher.exe "https://www.imusic-school.com/en/tools/online-metronome/"
REM : keyboard
pushd "C:\WORKS_2\Programs\opera"

start launcher.exe https://pianoplays.com
start launcher.exe https://metronom.us/en/
start launcher.exe https://www.musicca.com/jp/metronome

REM 	start launcher.exe https://www.onlinepianist.com/virtual-piano
