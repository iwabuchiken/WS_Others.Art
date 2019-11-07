REM ******************************* list
REM 	open folders
REM 	vlc player
REM 	browser
REM 	doc
REM 	metronome
REM *******************************


REM *******************************
REM 	open folders
REM *******************************
echo start C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\8_kb
start C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\8_kb

echo start C:\WORKS_2\WS\WS_Cake_IFM11\iphone_to_upload
start C:\WORKS_2\WS\WS_Cake_IFM11\iphone_to_upload

echo C:\WORKS_2\WS\WS_Cake_IFM11\movies_WS_Cake_IFM11\2019\6_kb
start C:\WORKS_2\WS\WS_Cake_IFM11\movies_WS_Cake_IFM11\2019\6_kb

REM *******************************
REM 	vlc player
REM 	2019/09/26 18:16:41
REM *******************************
pushd C:\Users\iwabuchiken\VLC
start vlc.exe

REM *******************************
REM 	browser
REM 	2019/09/16 14:18:11
REM *******************************
:web_page_keyboard_opera

REM : opera
	pushd "C:\WORKS_2\Programs\opera"
REM : log
	start launcher.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=kb+log&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"
REM : video
	start launcher.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=video+kb&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"
REM 	start launcher.exe "https://docs.zoho.com/sheet/open/ek7i4683eb5df87d04a23acef09182e7df623/sheets/free/ranges/A3"

	start launcher.exe "https://www.youtube.com/playlist?list=PLZe1Q2NRG8YXa2FCHsE3Ji3VCOg2Ey8LS"

	goto exit_web_page_keyboard


:exit_web_page_keyboard

REM *******************************
REM 	doc
REM 	2019/09/16 14:18:11
REM *******************************
start C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\8_kb\list_of_memos_keyboard.ods
start C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\8_kb\memos_keyboard.odt


REM *******************************
REM 	apps : metronome
REM 	2019/10/24 15:11:38
REM *******************************
	pushd "C:\WORKS_2\Programs\opera"
REM : metronome
REM 	start launcher.exe "https://www.metronomeonline.com"
	start launcher.exe "https://www.imusic-school.com/en/tools/online-metronome/"
REM : keyboard
	start launcher.exe https://pianoplays.com
REM 	start launcher.exe https://www.onlinepianist.com/virtual-piano

REM pause

REM exit
