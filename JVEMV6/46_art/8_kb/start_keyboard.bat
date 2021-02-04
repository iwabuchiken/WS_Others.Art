REM ============================== list
REM 	open folders
REM 	vlc player
REM 	browser
REM 	doc
REM 	metronome
REM 	console
REM 	mind map
REM 	musescore3
REM ==============================


REM ==============================
REM 	open folders
REM ==============================
echo start C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\8_kb
start C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\8_kb

echo start C:\WORKS_2\WS\WS_Cake_IFM11\iphone_to_upload
start C:\WORKS_2\WS\WS_Cake_IFM11\iphone_to_upload

rem echo C:\WORKS_2\WS\WS_Cake_IFM11\movies_WS_Cake_IFM11\2019\6_kb
rem start C:\WORKS_2\WS\WS_Cake_IFM11\movies_WS_Cake_IFM11\2019\6_kb
rem 2020�N9��10��18:16:28

echo C:\WORKS_2\WS\WS_Cake_IFM11\movies_WS_Cake_IFM11\2019\a_15_flute
start C:\WORKS_2\WS\WS_Cake_IFM11\movies_WS_Cake_IFM11\2019\a_15_flute

REM ==============================
REM 	vlc player
REM 	2019/09/26 18:16:41
REM ==============================
pushd C:\Users\iwabuchiken\VLC
start vlc.exe

REM ==============================
REM 	browser
REM 	2019/09/16 14:18:11
REM ==============================
:web_page_keyboard_opera

REM : opera
pushd "C:\WORKS_2\Programs\opera"

rem : set urls 2020�N11��17��18:27:33
rem : log files / 2020�N11��17��18:27:39
rem set url_1="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=music+log&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"
set url_1="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=session+shino&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"

rem : video files : bamboo / 2020�N11��17��18:27:39
set url_2="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=video+bamboo&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"

rem : video files : flute / 2020�N11��17��18:39:02
set url_2="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=video+jap.flute&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"

start launcher.exe %url_1%
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
rem : comment out 2020�N10��11��18:13:24
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

REM ==============================
REM 	console
REM 	2020�N7��22��19:08:10
REM ==============================
pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\8_kb
start start_command_prompot.bat

REM ==============================
REM 	mind map
REM 	2020�N7��20��18:35:01
REM ==============================
rem : comment in 2020�N10��25��18:13:20
pushd "C:\WORKS_2\WS\FM_2_20171104_225946\Projects\JVEMV6\46 Art\8 kb"
start 3_music-types.mm

rem : comment in 2020�N10��21��19:08:01
start "C:\WORKS_2\WS\FM_2_20171104_225946\Projects\JVEMV6\46 Art\8 kb\3_music-types.mm"

REM ==============================
REM 	musescore3
REM 	2020�N8��13��18:35:12
REM ==============================
rem commet out 2020�N9��4��18:18:30
rem commet in	2020�N9��24��18:28:09
rem commet out : 2021�N2��3��17:55:18
rem start C:\WORKS_2\Programs\musescore\ms_3.2.3.7635\bin\MuseScore3.exe

REM ==============================
REM 	doc
REM 	2019/09/16 14:18:11
REM ==============================
REM start C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\8_kb\list_of_memos_keyboard.ods
REM start C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\8_kb\memos_keyboard.odt
rem C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\8_kb\log_keyboard.odt
rem "C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\8_kb\46#8.[kb].[admin].ods"

rem C:\WORKS_2\WS\WS_Cake_IFM11\movies_WS_Cake_IFM11\2019\6_kb\log_kb.txt
rem "C:\WORKS_2\WS\WS_Cake_IFM11\movies_WS_Cake_IFM11\2019\6_kb\log_kb.txt"
rem C:\WORKS_2\shortcuts_docs\log_kb.txt
rem start C:\WORKS_2\shortcuts_docs\log_kb.txt
rem start "C:\WORKS_2\shortcuts_docs\log_[flute].txt"

rem : comment out : 2021�N1��10��18:02:07
rem set text_1="C:\WORKS_2\shortcuts_docs\log_[flute].txt"

rem : comment out : 2021�N1��10��18:02:07
rem C:\WORKS_2\Programs\sakura\sakura.exe %text_1%



REM pause

REM exit
