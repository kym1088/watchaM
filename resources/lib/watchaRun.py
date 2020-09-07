# -*- coding: utf-8 -*-
__author__ = "NightRain"
if 64 - 64: i11iIiiIii
import os
import xbmcplugin , xbmcgui , xbmcaddon , xbmc
import sys
import urlparse
import inputstreamhelper
import datetime
import time
import base64
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
reload ( sys )
sys . setdefaultencoding ( 'utf-8' )
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
__addon__ = xbmcaddon . Addon ( )
__language__ = __addon__ . getLocalizedString
__profile__ = xbmc . translatePath ( __addon__ . getAddonInfo ( 'profile' ) )
__version__ = __addon__ . getAddonInfo ( 'version' )
__addonid__ = __addon__ . getAddonInfo ( 'id' )
__addonname__ = __addon__ . getAddonInfo ( 'name' )
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
IiiIII111iI = [
 { 'title' : '왓플 최고 인기작' , 'mode' : 'CATEGORY_LIST' , 'stype' : '-' , 'api_path' : 'staffmades/409' , 'sort' : '-' }
 , { 'title' : '최고 인기 시리즈' , 'mode' : 'CATEGORY_LIST' , 'stype' : '-' , 'api_path' : 'staffmades/410' , 'sort' : '-' }
 , { 'title' : '새로 올라온 작품' , 'mode' : 'CATEGORY_LIST' , 'stype' : '-' , 'api_path' : 'arrivals/latest' , 'sort' : '-' }
 , { 'title' : '이어보기' , 'mode' : 'CATEGORY_LIST' , 'stype' : '-' , 'api_path' : 'users/me/watchings' , 'sort' : '-' }
 , { 'title' : '장르별 분류 (평균별점순)' , 'mode' : 'SUB_GROUP' , 'stype' : 'genres' , 'api_path' : '-' , 'sort' : '2' }
 , { 'title' : '특징별 분류 (평균별점순)' , 'mode' : 'SUB_GROUP' , 'stype' : 'tags' , 'api_path' : '-' , 'sort' : '2' }
 , { 'title' : '장르별 분류 (추천순)' , 'mode' : 'SUB_GROUP' , 'stype' : 'genres' , 'api_path' : '-' , 'sort' : '1' }
 , { 'title' : '특징별 분류 (추천순)' , 'mode' : 'SUB_GROUP' , 'stype' : 'tags' , 'api_path' : '-' , 'sort' : '1' }
 , { 'title' : '-----------------' , 'mode' : 'XXX' , 'stype' : 'XXX' , 'api_path' : '-' , 'sort' : '-' }
 , { 'title' : '검색 (search)' , 'mode' : 'SEARCH' , 'stype' : '-' , 'api_path' : '-' , 'sort' : '-' }
 , { 'title' : 'Watched (시청목록)' , 'mode' : 'WATCH' , 'stype' : '-' , 'api_path' : '-' , 'sort' : '-' }
 ]
if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . OoO0O00 - I1ii11iIi11i
O0oO = [
 { 'title' : '영화 시청내역' , 'mode' : 'WATCH' , 'stype' : 'movie' }
 , { 'title' : '시리즈 시청내역' , 'mode' : 'WATCH' , 'stype' : 'seasons' }
 ]
if 68 - 68: Ii1I / O0
Iiii111Ii11I1 = 40
ooO0oooOoO0 = 20
if 21 - 21: OoOoOO00 / iii1I1I * OoO0O00 . II111iiii
Ii1IIii11 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
Oooo0000 = xbmc . translatePath ( os . path . join ( __profile__ , 'temp_subtitles.vtt' ) )
i11 = xbmc . translatePath ( os . path . join ( __profile__ , 'watcha_cookies.json' ) )
if 41 - 41: O0oo0OO0 . Oo0ooO0oo0oO * O00oOoOoO0o0O % i11iIiiIii
if 74 - 74: iii1I1I * O00oOoOoO0o0O
from watchaCore import *
if 82 - 82: iIii1I11I1II1 % O00oOoOoO0o0O
if 86 - 86: OoOoOO00 % I1IiiI
class oo ( object ) :
 def __init__ ( self , in_addonurl , in_handle , in_params ) :
  if 33 - 33: II111iiii * Oo0Ooo - o0oOOo0O0Ooo * iIii1I11I1II1 * OoooooooOO * Oo0ooO0oo0oO
  if 27 - 27: OoO0O00
  if 73 - 73: o0oOOo0O0Ooo - Oo0Ooo
  if 58 - 58: i11iIiiIii % O0oo0OO0
  self . _addon_url = in_addonurl
  self . _addon_handle = in_handle
  self . main_params = in_params
  self . WatchaObj = i1iIIi1 ( )
  if 54 - 54: OOooOOo % O0 + I1IiiI - iii1I1I / I11i
  if 31 - 31: OoO0O00 + II111iiii
  if 13 - 13: OOooOOo * oO0o * I1IiiI
 def addon_noti ( self , sting ) :
  try :
   oOOOO = xbmcgui . Dialog ( )
   if 45 - 45: O0oo0OO0 + Ii1I
   oOOOO . notification ( __addonname__ , sting )
  except :
   None
   if 17 - 17: o0oOOo0O0Ooo
   if 64 - 64: Ii1I % i1IIi % OoooooooOO
   if 3 - 3: iii1I1I + O0
 def addon_log ( self , string , isDebug = False ) :
  try :
   I1Ii = string . encode ( 'utf-8' , 'ignore' )
  except :
   I1Ii = 'addonException: addon_log'
  if isDebug : o0oOo0Ooo0O = xbmc . LOGDEBUG
  else : o0oOo0Ooo0O = xbmc . LOGNOTICE
  xbmc . log ( "[%s-%s]: %s" % ( __addonid__ , __version__ , I1Ii ) , level = o0oOo0Ooo0O )
  if 81 - 81: I1ii11iIi11i * O00oOoOoO0o0O * I11i - iii1I1I - o0oOOo0O0Ooo
  if 90 - 90: II111iiii + oO0o / o0oOOo0O0Ooo % II111iiii - O0
  if 29 - 29: o0oOOo0O0Ooo / iIii1I11I1II1
  if 24 - 24: O0 % o0oOOo0O0Ooo + i1IIi + O0oo0OO0 + I1ii11iIi11i
 def get_keyboard_input ( self , title ) :
  OOoO000O0OO = None
  iiI1IiI = xbmc . Keyboard ( )
  iiI1IiI . setHeading ( title )
  xbmc . sleep ( 1000 )
  iiI1IiI . doModal ( )
  if ( iiI1IiI . isConfirmed ( ) ) :
   OOoO000O0OO = iiI1IiI . getText ( )
  return OOoO000O0OO
  if 13 - 13: Oo0Ooo . i11iIiiIii - iIii1I11I1II1 - OoOoOO00
  if 6 - 6: I1IiiI / Oo0Ooo % Ii1I
  if 84 - 84: i11iIiiIii . o0oOOo0O0Ooo
  if 100 - 100: Ii1I - Ii1I - O0oo0OO0
 def get_settings_login_info ( self ) :
  ii1 = __addon__ . getSetting ( 'id' )
  o0oO0o00oo = __addon__ . getSetting ( 'pw' )
  II1i1Ii11Ii11 = int ( __addon__ . getSetting ( 'selected_profile' ) )
  return ( ii1 , o0oO0o00oo , II1i1Ii11Ii11 )
  if 35 - 35: o0oOOo0O0Ooo + iii1I1I + iii1I1I
  if 11 - 11: iii1I1I - OoO0O00 % Oo0ooO0oo0oO % iii1I1I / OoOoOO00 - OoO0O00
  if 74 - 74: iii1I1I * O0
  if 89 - 89: oO0o + Oo0Ooo
 def get_selQuality ( self ) :
  try :
   if 3 - 3: i1IIi / I1IiiI % I11i * i11iIiiIii / O0 * I11i
   III1ii1iII = [ '3840x2160/1.25' , '1920x1080/1.25' , '1280x720/1.25' ]
   if 54 - 54: I1IiiI % II111iiii % II111iiii
   iI1 = int ( __addon__ . getSetting ( 'selected_quality' ) )
   return III1ii1iII [ iI1 ]
  except :
   None
   if 19 - 19: I11i + Oo0ooO0oo0oO
  return 1080
  if 53 - 53: OoooooooOO . i1IIi
  if 18 - 18: o0oOOo0O0Ooo
  if 28 - 28: OOooOOo - O00oOoOoO0o0O . O00oOoOoO0o0O + OoOoOO00 - OoooooooOO + O0
 def get_settings_direct_replay ( self ) :
  oOoOooOo0o0 = int ( __addon__ . getSetting ( 'direct_replay' ) )
  if oOoOooOo0o0 == 0 :
   return False
  else :
   return True
   if 61 - 61: o0oOOo0O0Ooo / OoO0O00 + Oo0ooO0oo0oO * oO0o / oO0o
   if 75 - 75: i1IIi / OoooooooOO - O0 / OoOoOO00 . II111iiii - i1IIi
   if 71 - 71: OOooOOo + Ii1I * OOooOOo - OoO0O00 * o0oOOo0O0Ooo
   if 65 - 65: O0 % I1IiiI . I1ii11iIi11i % iIii1I11I1II1 / OOooOOo % O0oo0OO0
   if 51 - 51: i11iIiiIii . I1IiiI + II111iiii
 def set_winCredential ( self , credential ) :
  II111ii1II1i = xbmcgui . Window ( 10000 )
  II111ii1II1i . setProperty ( 'WATCHA_M_TOKEN' , credential . get ( 'watcha_token' ) )
  II111ii1II1i . setProperty ( 'WATCHA_M_GUIT' , credential . get ( 'watcha_guit' ) )
  II111ii1II1i . setProperty ( 'WATCHA_M_GUITV' , credential . get ( 'watcha_guitv' ) )
  II111ii1II1i . setProperty ( 'WATCHA_M_USERCD' , credential . get ( 'watcha_usercd' ) )
  II111ii1II1i . setProperty ( 'WATCHA_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) )
  if 59 - 59: O0 + I1IiiI + O00oOoOoO0o0O % I1IiiI
  if 70 - 70: iii1I1I * I1ii11iIi11i
 def get_winCredential ( self ) :
  II111ii1II1i = xbmcgui . Window ( 10000 )
  i1II1 = {
 'watcha_token' : II111ii1II1i . getProperty ( 'WATCHA_M_TOKEN' )
 , 'watcha_guit' : II111ii1II1i . getProperty ( 'WATCHA_M_GUIT' )
 , 'watcha_guitv' : II111ii1II1i . getProperty ( 'WATCHA_M_GUITV' )
 , 'watcha_usercd' : II111ii1II1i . getProperty ( 'WATCHA_M_USERCD' )
 }
  return i1II1
  if 66 - 66: OoooooooOO + Ii1I + Ii1I - i1IIi
 def set_winEpisodeOrderby ( self , orderby ) :
  II111ii1II1i = xbmcgui . Window ( 10000 )
  II111ii1II1i . setProperty ( 'WATCHA_M_ORDERBY' , orderby )
  if 55 - 55: OOooOOo + Oo0ooO0oo0oO . i1IIi - I1ii11iIi11i . O0 - Oo0ooO0oo0oO
 def get_winEpisodeOrderby ( self ) :
  II111ii1II1i = xbmcgui . Window ( 10000 )
  return II111ii1II1i . getProperty ( 'WATCHA_M_ORDERBY' )
  if 92 - 92: iii1I1I . I11i + o0oOOo0O0Ooo
  if 28 - 28: i1IIi * Oo0Ooo - o0oOOo0O0Ooo * O00oOoOoO0o0O * Ii1I / OoO0O00
  if 94 - 94: II111iiii % I1ii11iIi11i / OoOoOO00 * iIii1I11I1II1
 def dp_setEpOrderby ( self , args ) :
  oOOoo0Oo = args . get ( 'orderby' )
  if 78 - 78: I11i
  self . set_winEpisodeOrderby ( oOOoo0Oo )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 71 - 71: OOooOOo + Oo0ooO0oo0oO % i11iIiiIii + I1ii11iIi11i - O00oOoOoO0o0O
  if 88 - 88: OoOoOO00 - OoO0O00 % OOooOOo
  if 16 - 16: I1IiiI * oO0o % O00oOoOoO0o0O
  if 86 - 86: I1IiiI + Ii1I % i11iIiiIii * oO0o . Oo0ooO0oo0oO * I11i
 def add_dir ( self , label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
  i1I11i1iI = '%s?%s' % ( self . _addon_url , urllib . urlencode ( params ) )
  if 15 - 15: Ii1I - O0 / oO0o * i1IIi
  if sublabel : oooo000 = '%s < %s >' % ( label , sublabel )
  else : oooo000 = label
  if not img : img = 'DefaultFolder.png'
  if 16 - 16: I1ii11iIi11i + OoO0O00 - II111iiii
  if 85 - 85: OoOoOO00 + i1IIi
  Oo0OoO00oOO0o = xbmcgui . ListItem ( oooo000 )
  Oo0OoO00oOO0o . setArt ( { 'thumbnailImage' : img , 'icon' : img , 'poster' : img } )
  if 80 - 80: oO0o + OOooOOo - OOooOOo % iii1I1I
  if infoLabels : Oo0OoO00oOO0o . setInfo ( type = "Video" , infoLabels = infoLabels )
  if not isFolder : Oo0OoO00oOO0o . setProperty ( 'IsPlayable' , 'true' )
  if 63 - 63: I1IiiI - I1ii11iIi11i + O0 % I11i / iIii1I11I1II1 / o0oOOo0O0Ooo
  xbmcplugin . addDirectoryItem ( self . _addon_handle , i1I11i1iI , Oo0OoO00oOO0o , isFolder )
  if 98 - 98: iii1I1I * iii1I1I / iii1I1I + I11i
  if 34 - 34: Oo0ooO0oo0oO
  if 15 - 15: I11i * Oo0ooO0oo0oO * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
  if 68 - 68: O0oo0OO0 % i1IIi . O00oOoOoO0o0O . I1ii11iIi11i
  if 92 - 92: iii1I1I . O0oo0OO0
 def dp_Main_List ( self ) :
  if 31 - 31: O0oo0OO0 . OoOoOO00 / O0
  for o000O0o in IiiIII111iI :
   oooo000 = o000O0o . get ( 'title' )
   if 42 - 42: OoOoOO00
   II = { 'mode' : o000O0o . get ( 'mode' )
 , 'stype' : o000O0o . get ( 'stype' )
 , 'api_path' : o000O0o . get ( 'api_path' )
 , 'page' : '1'
 , 'sort' : o000O0o . get ( 'sort' )
 , 'tag_id' : '-'
 }
   if 45 - 45: O0 * o0oOOo0O0Ooo % Oo0Ooo * OoooooooOO + iii1I1I . OoOoOO00
   if o000O0o . get ( 'mode' ) == 'XXX' :
    II [ 'mode' ] = 'XXX'
    Oo0ooOo0o = False
   else :
    Oo0ooOo0o = True
    if 22 - 22: iIii1I11I1II1 / i11iIiiIii * iIii1I11I1II1 * II111iiii . OOooOOo / i11iIiiIii
   self . add_dir ( oooo000 , sublabel = '' , img = '' , infoLabels = None , isFolder = Oo0ooOo0o , params = II )
  if len ( IiiIII111iI ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
  if 52 - 52: o0oOOo0O0Ooo
  if 95 - 95: Ii1I
  if 87 - 87: Oo0ooO0oo0oO + OoOoOO00 . OOooOOo + OoOoOO00
 def login_main ( self ) :
  ( oO , iIi1IIIi1 , O0oOoOOOoOO ) = self . get_settings_login_info ( )
  if 38 - 38: O0oo0OO0
  if 7 - 7: O0 . iii1I1I % I1ii11iIi11i - I1IiiI - iIii1I11I1II1
  if not ( oO and iIi1IIIi1 ) :
   oOOOO = xbmcgui . Dialog ( )
   I111IIIiIii = oOOOO . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
   if I111IIIiIii == True :
    __addon__ . openSettings ( )
    sys . exit ( )
    if 85 - 85: I1ii11iIi11i % iii1I1I % Oo0ooO0oo0oO
    if 82 - 82: i11iIiiIii - iii1I1I * OoooooooOO / I11i
  if self . get_winEpisodeOrderby ( ) == '' :
   self . set_winEpisodeOrderby ( 'asc' )
   if 31 - 31: O00oOoOoO0o0O . OoO0O00 - iIii1I11I1II1
   if 64 - 64: I11i
  if self . cookiefile_check ( ) : return
  if 22 - 22: Oo0Ooo + Ii1I % I1ii11iIi11i
  if 9 - 9: OoooooooOO
  if 62 - 62: OOooOOo / OoO0O00 + Ii1I / OoO0O00 . II111iiii
  if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
  if 31 - 31: II111iiii . I1IiiI
  if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % iii1I1I * O00oOoOoO0o0O . i11iIiiIii
  if 2 - 2: I1ii11iIi11i * I11i - iIii1I11I1II1 + I1IiiI . oO0o % iii1I1I
  if 92 - 92: iii1I1I
  if 25 - 25: Oo0Ooo - I1IiiI / OoooooooOO / o0oOOo0O0Ooo
  if 12 - 12: I1IiiI * iii1I1I % i1IIi % iIii1I11I1II1
  if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
  III1IiiI = int ( datetime . datetime . now ( ) . strftime ( '%Y%m%d' ) )
  iI = xbmcgui . Window ( 10000 ) . getProperty ( 'WATCHA_M_LOGINTIME' )
  if iI == None or iI == '' : iI = int ( '19000101' )
  if 32 - 32: iii1I1I . O00oOoOoO0o0O . O00oOoOoO0o0O
  if 62 - 62: I1ii11iIi11i + O00oOoOoO0o0O % iii1I1I + OOooOOo
  if 33 - 33: O0 . O00oOoOoO0o0O . I1IiiI
  if xbmcgui . Window ( 10000 ) . getProperty ( 'WATCHA_M_LOGINWAIT' ) == 'TRUE' :
   OoOO = 0
   while True :
    OoOO += 1
    if 53 - 53: Oo0Ooo
    time . sleep ( 0.05 )
    if 29 - 29: I1ii11iIi11i + oO0o % O0
    if iI >= III1IiiI : return
    if OoOO > 600 : return
  else :
   xbmcgui . Window ( 10000 ) . setProperty ( 'WATCHA_M_LOGINWAIT' , 'TRUE' )
   if 10 - 10: I11i / O0oo0OO0 - I1IiiI * iIii1I11I1II1 - I1IiiI
  if iI >= III1IiiI :
   xbmcgui . Window ( 10000 ) . setProperty ( 'WATCHA_M_LOGINWAIT' , 'FALSE' )
   return
   if 97 - 97: I1ii11iIi11i + I1IiiI * Ii1I + OOooOOo % iii1I1I
   if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + O0oo0OO0 / OoOoOO00
  if not self . WatchaObj . GetCredential ( oO , iIi1IIIi1 , O0oOoOOOoOO ) :
   self . addon_noti ( __language__ ( 30103 ) . encode ( 'utf8' ) )
   xbmcgui . Window ( 10000 ) . setProperty ( 'WATCHA_M_LOGINWAIT' , 'FALSE' )
   sys . exit ( )
   if 23 - 23: O0
   if 85 - 85: Ii1I
  self . set_winCredential ( self . WatchaObj . LoadCredential ( ) )
  self . cookiefile_save ( )
  xbmcgui . Window ( 10000 ) . setProperty ( 'WATCHA_M_LOGINWAIT' , 'FALSE' )
  if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
  if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + iii1I1I / OoOoOO00
  if 84 - 84: Oo0ooO0oo0oO * II111iiii + Oo0Ooo
  if 53 - 53: iii1I1I % II111iiii . O00oOoOoO0o0O - iIii1I11I1II1 - O00oOoOoO0o0O * II111iiii
  if 77 - 77: iIii1I11I1II1 * OoO0O00
  if 95 - 95: I1IiiI + i11iIiiIii
 def dp_SubGroup_List ( self , args ) :
  if 6 - 6: Oo0ooO0oo0oO / i11iIiiIii + iii1I1I * oO0o
  self . WatchaObj . SaveCredential ( self . get_winCredential ( ) )
  if 80 - 80: II111iiii
  O0O = args . get ( 'stype' )
  i1I1I = int ( args . get ( 'page' ) )
  iiI1I = args . get ( 'sort' )
  if 12 - 12: i11iIiiIii - i1IIi - OoO0O00 . i1IIi - OOooOOo + O0
  oO0OOOO0 = self . WatchaObj . GetSubGroupList ( O0O )
  if 26 - 26: Ii1I
  I11iiI1i1 = Iiii111Ii11I1 if O0O == 'genres' else ooO0oooOoO0
  if 47 - 47: iii1I1I - Ii1I . II111iiii + OoooooooOO . i11iIiiIii
  OOo0oO00ooO00 = len ( oO0OOOO0 )
  oOO0O00oO0Ooo = int ( OOo0oO00ooO00 // ( I11iiI1i1 + 1 ) ) + 1
  oO0Oo0O0o = ( i1I1I - 1 ) * I11iiI1i1
  if 99 - 99: oO0o . iii1I1I + Oo0ooO0oo0oO % oO0o . i11iIiiIii % O0
  for oOO00O in range ( I11iiI1i1 ) :
   OOOoo0OO = oO0Oo0O0o + oOO00O
   if OOOoo0OO >= OOo0oO00ooO00 : break
   if 57 - 57: OoO0O00 / Oo0ooO0oo0oO
   oooo000 = oO0OOOO0 [ OOOoo0OO ] . get ( 'group_name' )
   Ii1I1Ii = oO0OOOO0 [ OOOoo0OO ] . get ( 'api_path' )
   OOoO0 = oO0OOOO0 [ OOOoo0OO ] . get ( 'tag_id' )
   if 86 - 86: oO0o * o0oOOo0O0Ooo % i1IIi . Ii1I . i11iIiiIii
   II = { 'mode' : 'CATEGORY_LIST'
 , 'api_path' : Ii1I1Ii
 , 'tag_id' : OOoO0
 , 'stype' : O0O
 , 'page' : '1'
 , 'sort' : iiI1I
 }
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
   self . add_dir ( oooo000 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = II )
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
  if oOO0O00oO0Ooo > i1I1I :
   II = { }
   II [ 'mode' ] = 'SUB_GROUP'
   II [ 'stype' ] = O0O
   II [ 'api_path' ] = args . get ( 'api_path' )
   II [ 'page' ] = str ( i1I1I + 1 )
   II [ 'sort' ] = iiI1I
   oooo000 = '[B]%s >>[/B]' % '다음 페이지'
   Oo0O0oooo = str ( i1I1I + 1 )
   self . add_dir ( oooo000 , sublabel = Oo0O0oooo , img = '' , infoLabels = None , isFolder = True , params = II )
   if 33 - 33: O0oo0OO0 + iii1I1I * oO0o / iIii1I11I1II1 - I1IiiI
   if 54 - 54: O0oo0OO0 / OOooOOo . oO0o % iii1I1I
  if len ( oO0OOOO0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = True )
  if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
  if 63 - 63: OoOoOO00 * iii1I1I
  if 69 - 69: O0 . OoO0O00
  if 49 - 49: I1IiiI - I11i
 def play_VIDEO ( self , args ) :
  if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
  self . WatchaObj . SaveCredential ( self . get_winCredential ( ) )
  if 62 - 62: OoooooooOO * I1IiiI
  if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
  if 50 - 50: O0oo0OO0 . o0oOOo0O0Ooo
  if 97 - 97: O0 + OoOoOO00
  if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
  if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
  o0o0O0O00oOOo = args . get ( 'movie_code' )
  iIIIiIi = args . get ( 'season_code' )
  oooo000 = args . get ( 'title' )
  OO0O0 = args . get ( 'thumbnail' )
  I11I11 = self . get_selQuality ( )
  if 69 - 69: OoOoOO00
  if 97 - 97: I1ii11iIi11i % I1ii11iIi11i % oO0o / iii1I1I - iIii1I11I1II1
  self . addon_log ( o0o0O0O00oOOo + ' - ' + iIIIiIi , False )
  ooooo0O0000oo , iIii1II11 , OooOo0ooo = self . WatchaObj . GetStreamingURL ( o0o0O0O00oOOo , I11I11 )
  if 71 - 71: O0oo0OO0 + Ii1I
  if 28 - 28: OOooOOo
  if ooooo0O0000oo == '' :
   self . addon_noti ( __language__ ( 30302 ) . encode ( 'utf8' ) )
   return
   if 38 - 38: Oo0ooO0oo0oO % II111iiii % I11i / OoO0O00 + OoOoOO00 / i1IIi
   if 54 - 54: iIii1I11I1II1 % I1ii11iIi11i - OOooOOo / oO0o - OoO0O00 . I11i
   if 11 - 11: I1ii11iIi11i . OoO0O00 * O00oOoOoO0o0O * OoooooooOO + Oo0ooO0oo0oO
   if 33 - 33: O0 * o0oOOo0O0Ooo - O0oo0OO0 % O0oo0OO0
  I11I = ooooo0O0000oo
  self . addon_log ( I11I , False )
  if 50 - 50: O0oo0OO0 * i11iIiiIii * iIii1I11I1II1 - II111iiii * o0oOOo0O0Ooo * OoOoOO00
  if 94 - 94: OoooooooOO + OoooooooOO . II111iiii + I11i / I1ii11iIi11i % Ii1I
  I1Ii1iiiiii1 = xbmcgui . ListItem ( path = I11I )
  if 96 - 96: i11iIiiIii % OOooOOo
  if OooOo0ooo :
   ooO = OooOo0ooo
   Ooo0oOooo0 = 'https://lic.drmtoday.com/license-proxy-widevine/cenc/?specConform=true'
   oOOOoo00 = 'mpd'
   iiIiIIIiiI = 'com.widevine.alpha'
   if 12 - 12: O0 - o0oOOo0O0Ooo
   oOoO00O0 = inputstreamhelper . Helper ( oOOOoo00 , drm = iiIiIIIiiI )
   if 75 - 75: I1IiiI . Oo0ooO0oo0oO . O0 * O0oo0OO0
   if oOoO00O0 . check_inputstream ( ) :
    if 4 - 4: Ii1I % oO0o * OoO0O00
    o0O0OOOOoOO0 = { 'Host' : 'lic.drmtoday.com'
 , 'origin' : 'https://play.watcha.net'
 , 'referer' : 'https://play.watcha.net/watch/' + o0o0O0O00oOOo
 , 'dt-custom-data' : ooO
 , 'Sec-Fetch-Dest' : 'empty'
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'cross-site'
 , 'user-agent' : Ii1IIii11
 , 'Content-Type' : 'application/octet-stream'
 }
    ii = Ooo0oOooo0 + '|' + urllib . urlencode ( o0O0OOOOoOO0 ) + '|R{SSM}|'
    if 68 - 68: iii1I1I - I1IiiI / O0oo0OO0 / I11i
    self . addon_log ( ii )
    if 12 - 12: Ii1I + i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . I11i
    I1Ii1iiiiii1 . setProperty ( 'inputstreamaddon' , oOoO00O0 . inputstream_addon )
    I1Ii1iiiiii1 . setProperty ( 'inputstream.adaptive.manifest_type' , oOOOoo00 )
    I1Ii1iiiiii1 . setProperty ( 'inputstream.adaptive.license_type' , iiIiIIIiiI )
    I1Ii1iiiiii1 . setProperty ( 'inputstream.adaptive.license_key' , ii )
    if 5 - 5: i1IIi + O00oOoOoO0o0O / o0oOOo0O0Ooo . iii1I1I / I11i
    if 32 - 32: I1IiiI % iIii1I11I1II1 / i1IIi - I1IiiI
    if 7 - 7: O0oo0OO0 * OoO0O00 - Oo0ooO0oo0oO + OOooOOo * I1IiiI % OoO0O00
    if 15 - 15: OoOoOO00 % I1IiiI * I11i
    if 81 - 81: Oo0ooO0oo0oO - iIii1I11I1II1 - i1IIi / O0oo0OO0 - O0 * I11i
  if iIii1II11 :
   try :
    import urllib2
    iI1i11II1i = open ( Oooo0000 , 'wb' )
    o0o0OoOo0O0OO = urllib2 . urlopen ( iIii1II11 )
    while True :
     iIi1I11I = o0o0OoOo0O0OO . readline ( )
     iIi1I11I = re . sub ( r'(\d\d:\d\d).(\d\d\d) --> (\d\d:\d\d).(\d\d\d)(?:[ \-\w]+:[\w\%\d:]+)*\n' , r'00:\1.\2 --> 00:\3.\4\n' , iIi1I11I )
     if not iIi1I11I : break
     iI1i11II1i . write ( iIi1I11I )
     if 42 - 42: iIii1I11I1II1 / O0oo0OO0 / OoO0O00 - OoooooooOO
    iI1i11II1i . close ( )
    I1Ii1iiiiii1 . setSubtitles ( [ Oooo0000 , iIii1II11 ] )
   except :
    I1Ii1iiiiii1 . setSubtitles ( [ iIii1II11 ] )
    if 33 - 33: OoOoOO00 * OOooOOo - II111iiii
    if 83 - 83: OoOoOO00 - Ii1I / I11i / O0oo0OO0 + oO0o - O0
  xbmcplugin . setResolvedUrl ( self . _addon_handle , True , I1Ii1iiiiii1 )
  if 4 - 4: OOooOOo * OoO0O00 % i1IIi * i11iIiiIii % Oo0Ooo - oO0o
  if 67 - 67: OoOoOO00 + I1ii11iIi11i . o0oOOo0O0Ooo . II111iiii
  if 98 - 98: iii1I1I
  try :
   O0O = 'movie' if iIIIiIi == '-' else 'seasons'
   II = { 'code' : o0o0O0O00oOOo if O0O == 'movie' else iIIIiIi
 , 'img' : OO0O0
 , 'title' : oooo000
 , 'videoid' : o0o0O0O00oOOo
   }
   self . Save_Watched_List ( O0O , II )
  except :
   None
   if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / II111iiii % Oo0Ooo
   if 38 - 38: Oo0ooO0oo0oO - OOooOOo / iii1I1I
   if 66 - 66: O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / Ii1I + I1ii11iIi11i
   if 86 - 86: o0oOOo0O0Ooo
   if 5 - 5: O00oOoOoO0o0O * OoOoOO00
 def dp_Category_List ( self , args ) :
  if 5 - 5: O0oo0OO0
  self . WatchaObj . SaveCredential ( self . get_winCredential ( ) )
  if 90 - 90: O0oo0OO0 . Oo0ooO0oo0oO / Ii1I - I11i
  O0O = args . get ( 'stype' )
  OOoO0 = args . get ( 'tag_id' )
  Ii1I1Ii = args . get ( 'api_path' )
  i1I1I = int ( args . get ( 'page' ) )
  iiI1I = args . get ( 'sort' )
  if 40 - 40: OoooooooOO
  I1i1i1 , OoO0O00O0oo0O = self . WatchaObj . GetCategoryList ( O0O , OOoO0 , Ii1I1Ii , i1I1I , iiI1I )
  if 36 - 36: OOooOOo + O0 - Ii1I - O0 % I11i . oO0o
  if 74 - 74: i11iIiiIii . I1IiiI
  for iiI in I1i1i1 :
   o0o0O0O00oOOo = iiI . get ( 'code' )
   oooo000 = iiI . get ( 'title' )
   oOIIiIi = iiI . get ( 'content_type' )
   OOoOooOoOOOoo = iiI . get ( 'story' )
   OO0O0 = iiI . get ( 'thumbnail' )
   Iiii1iI1i = iiI . get ( 'year' )
   I1ii1ii11i1I = iiI . get ( 'film_rating_code' )
   o0OoOO = iiI . get ( 'film_rating_short' )
   if 55 - 55: Oo0ooO0oo0oO - I11i + II111iiii + iii1I1I % Ii1I
   if oOIIiIi == 'movies' :
    Oo0ooOo0o = False
    iiI11i1II = 'MOVIE'
    OO0O0OOo0O = ''
    iIIIiIi = '-'
   else :
    Oo0ooOo0o = True
    iiI11i1II = 'EPISODE'
    OO0O0OOo0O = 'Series'
    iIIIiIi = o0o0O0O00oOOo
    if 36 - 36: Oo0ooO0oo0oO . Oo0Ooo % Oo0ooO0oo0oO % OoO0O00
   iIIIII1I = iiI . get ( 'info' )
   iIIIII1I [ 'plot' ] = '%s (%s)\n년도 : %s\n\n%s' % ( oooo000 , o0OoOO , Iiii1iI1i , OOoOooOoOOOoo )
   if 51 - 51: iIii1I11I1II1 . Oo0ooO0oo0oO + iIii1I11I1II1
   if I1ii1ii11i1I >= 19 :
    oooo000 += '  (%s년 - %s)' % ( Iiii1iI1i , str ( o0OoOO ) )
   else :
    oooo000 += '  (%s년)' % ( Iiii1iI1i )
    if 95 - 95: I1IiiI
    if 46 - 46: OoOoOO00 + OoO0O00
   II = { 'mode' : iiI11i1II
 , 'movie_code' : o0o0O0O00oOOo
 , 'page' : '1'
 , 'season_code' : iIIIiIi
   , 'title' : oooo000
 , 'thumbnail' : OO0O0
 }
   if 70 - 70: iii1I1I / iIii1I11I1II1
   self . add_dir ( oooo000 , sublabel = OO0O0OOo0O , img = OO0O0 , infoLabels = iIIIII1I , isFolder = Oo0ooOo0o , params = II )
   if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / I1ii11iIi11i
   if 96 - 96: OoooooooOO + oO0o
  if OoO0O00O0oo0O :
   if self . WatchaObj . GetCategoryList_morepage ( O0O , OOoO0 , Ii1I1Ii , i1I1I + 1 , iiI1I ) :
    II = { }
    II [ 'mode' ] = 'CATEGORY_LIST'
    II [ 'stype' ] = O0O
    II [ 'tag_id' ] = OOoO0
    II [ 'api_path' ] = Ii1I1Ii
    II [ 'page' ] = str ( i1I1I + 1 )
    II [ 'sort' ] = iiI1I
    oooo000 = '[B]%s >>[/B]' % '다음 페이지'
    Oo0O0oooo = str ( i1I1I + 1 )
    self . add_dir ( oooo000 , sublabel = Oo0O0oooo , img = '' , infoLabels = None , isFolder = True , params = II )
    if 44 - 44: oO0o
  if len ( I1i1i1 ) > 0 :
   if Ii1I1Ii == 'arrivals/latest' :
    xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = True )
   else :
    xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
    if 20 - 20: I11i + Ii1I / O0 % iIii1I11I1II1
    if 88 - 88: OoOoOO00 / II111iiii
    if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - iii1I1I + oO0o
    if 82 - 82: oO0o / iIii1I11I1II1 . I1IiiI . OOooOOo / o0oOOo0O0Ooo
    if 42 - 42: Oo0Ooo
 def dp_Episode_List ( self , args ) :
  if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
  self . WatchaObj . SaveCredential ( self . get_winCredential ( ) )
  if 46 - 46: Oo0Ooo
  i1II1I1Iii1 = args . get ( 'movie_code' )
  i1I1I = int ( args . get ( 'page' ) )
  iIIIiIi = args . get ( 'season_code' )
  if 30 - 30: OoooooooOO - OoOoOO00
  if 75 - 75: iIii1I11I1II1 - Ii1I . Oo0Ooo % i11iIiiIii % I11i
  I1i1i1 , OoO0O00O0oo0O = self . WatchaObj . GetEpisodoList ( i1II1I1Iii1 , i1I1I , orderby = self . get_winEpisodeOrderby ( ) )
  if 55 - 55: iii1I1I . II111iiii % OoO0O00 * iii1I1I + Oo0ooO0oo0oO + Ii1I
  if 24 - 24: Oo0Ooo - oO0o % iIii1I11I1II1 . i1IIi / O0
  for iiI in I1i1i1 :
   o0o0O0O00oOOo = iiI . get ( 'code' )
   oooo000 = iiI . get ( 'title' )
   OO0O0 = iiI . get ( 'thumbnail' )
   ii1ii111 = iiI . get ( 'display_num' )
   I111i1i1111 = iiI . get ( 'season_title' )
   if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
   iIIIII1I = iiI . get ( 'info' )
   iIIIII1I [ 'plot' ] = '%s\n%s\n\n%s' % ( I111i1i1111 , ii1ii111 , oooo000 )
   if 28 - 28: Oo0ooO0oo0oO + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
   oooo000 = '(%s) %s' % ( ii1ii111 , oooo000 )
   if 54 - 54: i1IIi + II111iiii
   II = { 'mode' : 'MOVIE'
 , 'movie_code' : o0o0O0O00oOOo
 , 'season_code' : iIIIiIi
   # I1ii11iIi11i + OoOoOO00 - OOooOOo + O0 . Ii1I
   , 'title' : '%s < %s >' % ( oooo000 , I111i1i1111 )
 , 'thumbnail' : OO0O0
 }
   if 46 - 46: O00oOoOoO0o0O
   self . add_dir ( oooo000 , sublabel = I111i1i1111 , img = OO0O0 , infoLabels = iIIIII1I , isFolder = False , params = II )
   if 45 - 45: Oo0ooO0oo0oO
  if i1I1I == 1 :
   iIIIII1I = { 'plot' : '정렬순서를 변경합니다.' }
   II = { }
   II [ 'mode' ] = 'ORDER_BY'
   if self . get_winEpisodeOrderby ( ) == 'desc' :
    oooo000 = '정렬순서변경 : 최신화부터 -> 1회부터'
    II [ 'orderby' ] = 'asc'
   else :
    oooo000 = '정렬순서변경 : 1회부터 -> 최신화부터'
    II [ 'orderby' ] = 'desc'
   self . add_dir ( oooo000 , sublabel = '' , img = '' , infoLabels = iIIIII1I , isFolder = False , params = II )
   if 21 - 21: oO0o . O0oo0OO0 . OOooOOo / Oo0Ooo / O0oo0OO0
  if OoO0O00O0oo0O :
   if 17 - 17: OOooOOo / OOooOOo / I11i
   II [ 'mode' ] = 'EPISODE'
   II [ 'movie_code' ] = i1II1I1Iii1
   II [ 'page' ] = str ( i1I1I + 1 )
   oooo000 = '[B]%s >>[/B]' % '다음 페이지'
   Oo0O0oooo = str ( i1I1I + 1 )
   self . add_dir ( oooo000 , sublabel = Oo0O0oooo , img = '' , infoLabels = None , isFolder = True , params = II )
   if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
   if 82 - 82: iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % O00oOoOoO0o0O / Ii1I . Ii1I
  if len ( I1i1i1 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = True )
  if 14 - 14: o0oOOo0O0Ooo . OOooOOo . I11i + OoooooooOO - OOooOOo + O00oOoOoO0o0O
  if 9 - 9: Ii1I
  if 59 - 59: I1IiiI * II111iiii . O0
  if 56 - 56: Ii1I - iii1I1I % I1IiiI - o0oOOo0O0Ooo
  if 51 - 51: O0 / Oo0ooO0oo0oO * iIii1I11I1II1 + I1ii11iIi11i + o0oOOo0O0Ooo
  if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * OOooOOo + Oo0ooO0oo0oO % i11iIiiIii % O0
  if 27 - 27: O0
 def dp_Search_List ( self , args ) :
  if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
  self . WatchaObj . SaveCredential ( self . get_winCredential ( ) )
  if 28 - 28: i1IIi - iii1I1I
  i1I1I = int ( args . get ( 'page' ) )
  if 54 - 54: iii1I1I - O0 % OOooOOo
  if 'search_key' in args :
   Oo = args . get ( 'search_key' )
  else :
   Oo = self . get_keyboard_input ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
   if not Oo : return
   if 44 - 44: I1IiiI - I11i % iIii1I11I1II1
   if 71 - 71: Oo0ooO0oo0oO . Ii1I - OoooooooOO % Ii1I . II111iiii
  I1i1i1 , OoO0O00O0oo0O = self . WatchaObj . GetSearchList ( Oo , i1I1I )
  if len ( I1i1i1 ) == 0 : return
  if 89 - 89: iii1I1I . O0 / I1ii11iIi11i % OoOoOO00 . Oo0Ooo
  if 50 - 50: II111iiii + I1ii11iIi11i . i1IIi % o0oOOo0O0Ooo
  for iiI in I1i1i1 :
   o0o0O0O00oOOo = iiI . get ( 'code' )
   oooo000 = iiI . get ( 'title' )
   oOIIiIi = iiI . get ( 'content_type' )
   OOoOooOoOOOoo = iiI . get ( 'story' )
   OO0O0 = iiI . get ( 'thumbnail' )
   Iiii1iI1i = iiI . get ( 'year' )
   I1ii1ii11i1I = iiI . get ( 'film_rating_code' )
   o0OoOO = iiI . get ( 'film_rating_short' )
   if 5 - 5: OoOoOO00 / OoooooooOO + O00oOoOoO0o0O * O0oo0OO0 - OoO0O00 % I1IiiI
   if oOIIiIi == 'movies' :
    Oo0ooOo0o = False
    iiI11i1II = 'MOVIE'
    OO0O0OOo0O = ''
    iIIIiIi = '-'
   else :
    Oo0ooOo0o = True
    iiI11i1II = 'EPISODE'
    OO0O0OOo0O = 'Series'
    iIIIiIi = o0o0O0O00oOOo
    if 42 - 42: O0 / o0oOOo0O0Ooo + OoooooooOO * Oo0ooO0oo0oO % Oo0ooO0oo0oO
   iIIIII1I = iiI . get ( 'info' )
   iIIIII1I [ 'plot' ] = '%s (%s)\n년도 : %s\n\n%s' % ( oooo000 , o0OoOO , Iiii1iI1i , OOoOooOoOOOoo )
   if 7 - 7: iii1I1I / I1ii11iIi11i / i11iIiiIii
   if I1ii1ii11i1I >= 19 :
    oooo000 += '  (%s년 - %s)' % ( Iiii1iI1i , str ( o0OoOO ) )
   else :
    oooo000 += '  (%s년)' % ( Iiii1iI1i )
    if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
   II = { 'mode' : iiI11i1II
 , 'movie_code' : o0o0O0O00oOOo
 , 'page' : '1'
 , 'season_code' : iIIIiIi
   , 'title' : oooo000
 , 'thumbnail' : OO0O0
 }
   if 91 - 91: i11iIiiIii / i1IIi + iii1I1I + Oo0ooO0oo0oO * i11iIiiIii
   self . add_dir ( oooo000 , sublabel = OO0O0OOo0O , img = OO0O0 , infoLabels = iIIIII1I , isFolder = Oo0ooOo0o , params = II )
   if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + I11i * O0oo0OO0 . O00oOoOoO0o0O
   if 52 - 52: Oo0ooO0oo0oO + O0 . iii1I1I . I1ii11iIi11i . OoO0O00
  if OoO0O00O0oo0O :
   II = { }
   II [ 'mode' ] = 'SEARCH'
   II [ 'search_key' ] = Oo
   II [ 'page' ] = str ( i1I1I + 1 )
   oooo000 = '[B]%s >>[/B]' % '다음 페이지'
   Oo0O0oooo = str ( i1I1I + 1 )
   self . add_dir ( oooo000 , sublabel = Oo0O0oooo , img = '' , infoLabels = None , isFolder = True , params = II )
   if 97 - 97: I1IiiI / iii1I1I
  if len ( I1i1i1 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 71 - 71: II111iiii / i1IIi . I1ii11iIi11i % OoooooooOO . OoOoOO00
  if 41 - 41: i1IIi * II111iiii / OoooooooOO . OOooOOo
  if 83 - 83: iii1I1I . O0 / Oo0Ooo / OOooOOo - II111iiii
  if 100 - 100: OoO0O00
  if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iii1I1I . iIii1I11I1II1 * iii1I1I
  if 38 - 38: I1ii11iIi11i - iii1I1I / O0 . O0oo0OO0
 def Delete_Watched_List ( self , stype ) :
  try :
   i1iiIiI1Ii1i = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   with open ( i1iiIiI1Ii1i , 'w' ) as i1iIi :
    i1iIi . write ( '' )
  except :
   None
   if 30 - 30: O0 - iIii1I11I1II1 / OoooooooOO
   if 89 - 89: iii1I1I - Oo0ooO0oo0oO % Oo0Ooo % o0oOOo0O0Ooo
   if 49 - 49: Oo0Ooo - I1IiiI / O00oOoOoO0o0O / O0 % o0oOOo0O0Ooo * Ii1I
   if 100 - 100: OOooOOo . iii1I1I / O0 * i1IIi * Ii1I * Oo0Ooo
 def dp_WatchList_Delete ( self , args ) :
  O0O = args . get ( 'stype' )
  if 84 - 84: I1ii11iIi11i / OOooOOo % i11iIiiIii * O0oo0OO0 % I1ii11iIi11i - OoooooooOO
  oOOOO = xbmcgui . Dialog ( )
  I111IIIiIii = oOOOO . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if I111IIIiIii == False : sys . exit ( )
  if 99 - 99: I1IiiI + O0 + i1IIi / i11iIiiIii - i1IIi * iIii1I11I1II1
  self . Delete_Watched_List ( O0O )
  if 72 - 72: I1IiiI * I1ii11iIi11i . Ii1I * O00oOoOoO0o0O * Oo0Ooo * O0oo0OO0
  xbmc . executebuiltin ( "Container.Refresh" )
  if 40 - 40: I1IiiI
  if 14 - 14: O0oo0OO0
  if 80 - 80: OoooooooOO - OOooOOo * Ii1I * I1ii11iIi11i / I1IiiI / OOooOOo
  if 13 - 13: O0oo0OO0 * Oo0ooO0oo0oO + i11iIiiIii * O0oo0OO0 - Oo0ooO0oo0oO
 def Load_Watched_List ( self , stype ) :
  try :
   i1iiIiI1Ii1i = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   with open ( i1iiIiI1Ii1i , 'r' ) as i1iIi :
    Ii1i1i1i1I1Ii = i1iIi . readlines ( )
  except :
   Ii1i1i1i1I1Ii = [ ]
   if 25 - 25: II111iiii
  return Ii1i1i1i1I1Ii
  if 11 - 11: Oo0Ooo
  if 74 - 74: OoOoOO00 * o0oOOo0O0Ooo + OoOoOO00 . OOooOOo * OoooooooOO % O0
  if 85 - 85: Oo0ooO0oo0oO / O0
  if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
 def Save_Watched_List ( self , stype , in_params ) :
  try :
   i1iiIiI1Ii1i = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   o0 = self . Load_Watched_List ( stype )
   if 17 - 17: iIii1I11I1II1 . OoooooooOO / I11i % II111iiii % i1IIi / i11iIiiIii
   with open ( i1iiIiI1Ii1i , 'w' ) as i1iIi :
    OOO = urllib . urlencode ( in_params )
    OOO = OOO . encode ( 'utf-8' ) + '\n'
    i1iIi . write ( OOO )
    if 30 - 30: OoooooooOO - OoooooooOO . O0 / iii1I1I
    iIiIi1I = 0
    for iiii11i in o0 :
     III11II1I1Ii1 = dict ( urlparse . parse_qsl ( iiii11i ) )
     if 72 - 72: iii1I1I * oO0o % Ii1I . OoooooooOO
     OoO0O0O0o00 = in_params . get ( 'code' )
     iiiI11 = III11II1I1Ii1 . get ( 'code' )
     if stype == 'seasons' and self . get_settings_direct_replay ( ) == True :
      OoO0O0O0o00 = in_params . get ( 'videoid' )
      iiiI11 = III11II1I1Ii1 . get ( 'videoid' ) if iiiI11 != None else '-'
      if 63 - 63: OoO0O00 + I1ii11iIi11i . O0oo0OO0 % O0oo0OO0
     if OoO0O0O0o00 != iiiI11 :
      i1iIi . write ( iiii11i )
      iIiIi1I += 1
      if iIiIi1I >= 50 : break
  except :
   None
   if 57 - 57: II111iiii
   if 54 - 54: Oo0Ooo + oO0o + i11iIiiIii
   if 28 - 28: oO0o
   if 70 - 70: O00oOoOoO0o0O
   if 34 - 34: O0oo0OO0 % O00oOoOoO0o0O
 def dp_Watch_List ( self , args ) :
  O0O = args . get ( 'stype' )
  oOoOooOo0o0 = self . get_settings_direct_replay ( )
  if 3 - 3: II111iiii / OOooOOo + O00oOoOoO0o0O . Oo0ooO0oo0oO . OoO0O00
  if O0O == '-' :
   for oOoo000 in O0oO :
    oooo000 = oOoo000 . get ( 'title' )
    if 87 - 87: OoooooooOO - o0oOOo0O0Ooo / O00oOoOoO0o0O . i11iIiiIii * OoooooooOO
    II = { 'mode' : oOoo000 . get ( 'mode' )
 , 'stype' : oOoo000 . get ( 'stype' )
 }
    if 84 - 84: OoOoOO00 / I11i * iii1I1I / oO0o - i11iIiiIii . Oo0Ooo
    self . add_dir ( oooo000 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = II )
   if len ( O0oO ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
   if 60 - 60: I1ii11iIi11i * I1IiiI
  else :
   I1iIiI11I1 = self . Load_Watched_List ( O0O )
   if 27 - 27: Ii1I . i11iIiiIii % O0oo0OO0
   for OooOOOOoO00OoOO in I1iIiI11I1 :
    oOooo0O0o = dict ( urlparse . parse_qsl ( OooOOOOoO00OoOO ) )
    if 72 - 72: iIii1I11I1II1 / O00oOoOoO0o0O % iii1I1I % OOooOOo - I11i % OOooOOo
    o0o0O0O00oOOo = oOooo0O0o . get ( 'code' )
    oooo000 = oOooo0O0o . get ( 'title' )
    OO0O0 = oOooo0O0o . get ( 'img' )
    oOo0Oo0 = oOooo0O0o . get ( 'videoid' )
    if 23 - 23: O0oo0OO0 % o0oOOo0O0Ooo % iii1I1I * O00oOoOoO0o0O
    iIIIII1I = { }
    iIIIII1I [ 'plot' ] = oooo000
    if 19 - 19: iIii1I11I1II1
    if O0O == 'movie' :
     II = { 'mode' : 'MOVIE'
 , 'page' : '1'
 , 'movie_code' : o0o0O0O00oOOo
 , 'season_code' : '-'
 , 'title' : oooo000
 , 'thumbnail' : OO0O0
 }
     Oo0ooOo0o = False
    else :
     if oOoOooOo0o0 == False or oOo0Oo0 == None :
      II = { 'mode' : 'EPISODE'
 , 'page' : '1'
 , 'movie_code' : o0o0O0O00oOOo
 , 'season_code' : o0o0O0O00oOOo
 , 'title' : oooo000
 , 'thumbnail' : OO0O0
 }
      Oo0ooOo0o = True
     else :
      II = { 'mode' : 'MOVIE'
 , 'movie_code' : oOo0Oo0
 , 'season_code' : o0o0O0O00oOOo
 , 'title' : oooo000
 , 'thumbnail' : OO0O0
 }
      Oo0ooOo0o = False
      if 26 - 26: OoooooooOO % I1IiiI % Oo0Ooo . I1IiiI % Ii1I
    self . add_dir ( oooo000 , sublabel = '' , img = OO0O0 , infoLabels = iIIIII1I , isFolder = Oo0ooOo0o , params = II )
    if 34 - 34: O00oOoOoO0o0O / OoOoOO00
   iIIIII1I = { 'plot' : '시청목록을 삭제합니다.' }
   oooo000 = '*** 시청목록 삭제 ***'
   II = { 'mode' : 'MYVIEW_REMOVE'
 , 'stype' : O0O
 }
   self . add_dir ( oooo000 , sublabel = '' , img = '' , infoLabels = iIIIII1I , isFolder = False , params = II )
   if 87 - 87: O0 * o0oOOo0O0Ooo * Oo0Ooo * II111iiii
   xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
   if 6 - 6: i1IIi . I1ii11iIi11i + OoOoOO00 * I11i / OoOoOO00 % oO0o
   if 18 - 18: II111iiii . OoooooooOO % OoOoOO00 % Ii1I
   if 9 - 9: OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
   if 2 - 2: OoooooooOO % OOooOOo
 def logout ( self ) :
  oOOOO = xbmcgui . Dialog ( )
  I111IIIiIii = oOOOO . yesno ( __language__ ( 30910 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if I111IIIiIii == False : sys . exit ( )
  if 63 - 63: I1IiiI % iIii1I11I1II1
  self . wininfo_clear ( )
  if 39 - 39: iii1I1I / II111iiii / I1ii11iIi11i % I1IiiI
  if 89 - 89: O0oo0OO0 + OoooooooOO + O0oo0OO0 * i1IIi + iIii1I11I1II1 % I11i
  if os . path . isfile ( i11 ) : os . remove ( i11 )
  if 59 - 59: OOooOOo + i11iIiiIii
  self . addon_noti ( __language__ ( 30909 ) . encode ( 'utf-8' ) )
  if 88 - 88: i11iIiiIii - Oo0ooO0oo0oO
  if 67 - 67: OOooOOo . Oo0Ooo + OoOoOO00 - OoooooooOO
  if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iii1I1I
  if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - I11i
 def wininfo_clear ( self ) :
  if 30 - 30: OoOoOO00
  II111ii1II1i = xbmcgui . Window ( 10000 )
  II111ii1II1i . setProperty ( 'WATCHA_M_TOKEN' , '' )
  II111ii1II1i . setProperty ( 'WATCHA_M_GUIT' , '' )
  II111ii1II1i . setProperty ( 'WATCHA_M_GUITV' , '' )
  II111ii1II1i . setProperty ( 'WATCHA_M_USERCD' , '' )
  II111ii1II1i . setProperty ( 'WATCHA_M_LOGINTIME' , '' )
  if 21 - 21: i11iIiiIii / O0oo0OO0 % OOooOOo * O0 . I11i - iIii1I11I1II1
  if 26 - 26: II111iiii * OoOoOO00
  if 10 - 10: II111iiii . iii1I1I
  if 32 - 32: Ii1I . O00oOoOoO0o0O . OoooooooOO - OoO0O00 + oO0o
 def cookiefile_save ( self ) :
  ooO0oO00O0o = datetime . datetime . now ( )
  ooOO00oOOo000 = ooO0oO00O0o + datetime . timedelta ( days = int ( __addon__ . getSetting ( 'cache_ttl' ) ) )
  if 14 - 14: OoO0O00 . II111iiii . I11i / Ii1I % I1ii11iIi11i - Oo0ooO0oo0oO
  II111ii1II1i = xbmcgui . Window ( 10000 )
  o0oOoO0O = { 'watcha_token' : II111ii1II1i . getProperty ( 'WATCHA_M_TOKEN' )
 , 'watcha_guit' : II111ii1II1i . getProperty ( 'WATCHA_M_GUIT' )
 , 'watcha_guitv' : II111ii1II1i . getProperty ( 'WATCHA_M_GUITV' )
 , 'watcha_usercd' : II111ii1II1i . getProperty ( 'WATCHA_M_USERCD' )
 , 'watcha_id' : base64 . standard_b64encode ( __addon__ . getSetting ( 'id' ) . encode ( ) ) . decode ( 'utf-8' )
 , 'watcha_pw' : base64 . standard_b64encode ( __addon__ . getSetting ( 'pw' ) . encode ( ) ) . decode ( 'utf-8' )
 , 'watcha_profile' : __addon__ . getSetting ( 'selected_profile' )
 , 'watcha_limitdate' : ooOO00oOOo000 . strftime ( '%Y-%m-%d' )
 }
  if 84 - 84: O0 * OoooooooOO - O00oOoOoO0o0O * O00oOoOoO0o0O
  try :
   with open ( i11 , 'w' ) as i1iIi :
    json . dump ( o0oOoO0O , i1iIi )
  except Exception as i1ii :
   print ( i1ii )
   if 65 - 65: OoOoOO00 / OoO0O00 % O00oOoOoO0o0O
   if 45 - 45: OoOoOO00
   if 66 - 66: OoO0O00
   if 56 - 56: O0
 def cookiefile_check ( self ) :
  if 61 - 61: o0oOOo0O0Ooo / OOooOOo / Oo0Ooo * O0
  if 23 - 23: oO0o - OOooOOo + I11i
  o0oOoO0O = { }
  try :
   with open ( i11 , 'r' ) as i1iIi :
    o0oOoO0O = json . load ( i1iIi )
  except Exception as i1ii :
   self . wininfo_clear ( )
   return False
   if 12 - 12: I1IiiI / Oo0ooO0oo0oO % o0oOOo0O0Ooo / i11iIiiIii % OoooooooOO
   if 15 - 15: iIii1I11I1II1 % OoooooooOO - Oo0Ooo * Ii1I + I11i
   if 11 - 11: iii1I1I * Ii1I - OoOoOO00
  oO = __addon__ . getSetting ( 'id' )
  iIi1IIIi1 = __addon__ . getSetting ( 'pw' )
  OOOIII1iI1iII1I = __addon__ . getSetting ( 'selected_profile' )
  o0oOoO0O [ 'watcha_id' ] = base64 . standard_b64decode ( o0oOoO0O [ 'watcha_id' ] ) . decode ( 'utf-8' )
  o0oOoO0O [ 'watcha_pw' ] = base64 . standard_b64decode ( o0oOoO0O [ 'watcha_pw' ] ) . decode ( 'utf-8' )
  if oO != o0oOoO0O [ 'watcha_id' ] or iIi1IIIi1 != o0oOoO0O [ 'watcha_pw' ] or OOOIII1iI1iII1I != o0oOoO0O [ 'watcha_profile' ] :
   self . wininfo_clear ( )
   return False
   if 39 - 39: Ii1I * Oo0ooO0oo0oO / OoOoOO00 * OoO0O00 . I11i % II111iiii
   if 71 - 71: O0oo0OO0 % i1IIi - II111iiii - OOooOOo + OOooOOo * Oo0ooO0oo0oO
   if 51 - 51: iIii1I11I1II1 / OoOoOO00 + OOooOOo - I11i + iii1I1I
   if 29 - 29: o0oOOo0O0Ooo % iIii1I11I1II1 . OoooooooOO % OoooooooOO % II111iiii / iii1I1I
   if 70 - 70: i11iIiiIii % iii1I1I
   if 11 - 11: O00oOoOoO0o0O % I1ii11iIi11i % Ii1I / II111iiii % O0oo0OO0 - Oo0Ooo
   if 96 - 96: I1ii11iIi11i / II111iiii . Ii1I - iii1I1I * I11i * oO0o
   if 76 - 76: Ii1I - II111iiii * OOooOOo / OoooooooOO
   if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
   if 71 - 71: OoooooooOO
  III1IiiI = int ( datetime . datetime . now ( ) . strftime ( '%Y%m%d' ) )
  iIIIII1iiiiII = o0oOoO0O [ 'watcha_limitdate' ]
  iI = int ( re . sub ( '-' , '' , iIIIII1iiiiII ) )
  if 54 - 54: i1IIi
  if 22 - 22: i1IIi + Ii1I
  if iI < III1IiiI :
   self . wininfo_clear ( )
   return False
   if 54 - 54: Oo0ooO0oo0oO % OOooOOo . O0oo0OO0 + oO0o - OOooOOo * I1IiiI
   if 92 - 92: o0oOOo0O0Ooo + O0oo0OO0 / Oo0Ooo % OoO0O00 % O00oOoOoO0o0O . OoooooooOO
  II111ii1II1i = xbmcgui . Window ( 10000 )
  II111ii1II1i . setProperty ( 'WATCHA_M_TOKEN' , o0oOoO0O [ 'watcha_token' ] )
  II111ii1II1i . setProperty ( 'WATCHA_M_GUIT' , o0oOoO0O [ 'watcha_guit' ] )
  II111ii1II1i . setProperty ( 'WATCHA_M_GUITV' , o0oOoO0O [ 'watcha_guitv' ] )
  II111ii1II1i . setProperty ( 'WATCHA_M_USERCD' , o0oOoO0O [ 'watcha_usercd' ] )
  II111ii1II1i . setProperty ( 'WATCHA_M_LOGINTIME' , iIIIII1iiiiII )
  if 52 - 52: Oo0ooO0oo0oO / i11iIiiIii - OOooOOo . O00oOoOoO0o0O % iIii1I11I1II1 + o0oOOo0O0Ooo
  return True
  if 71 - 71: oO0o % I11i * OoOoOO00 . O0 / Ii1I . I1ii11iIi11i
  if 58 - 58: Oo0Ooo / oO0o
  if 44 - 44: OOooOOo
  if 54 - 54: Ii1I - I11i - O0oo0OO0 . iIii1I11I1II1
  if 79 - 79: Ii1I . OoO0O00
 def watcha_main ( self ) :
  IIiI1I1 = self . main_params . get ( 'mode' , None )
  if 15 - 15: Ii1I * Oo0Ooo % I1ii11iIi11i * iIii1I11I1II1 - i11iIiiIii
  self . login_main ( )
  if 60 - 60: I1IiiI * O0oo0OO0 % OoO0O00 + oO0o
  if IIiI1I1 is None :
   self . dp_Main_List ( )
   if 52 - 52: i1IIi
  elif IIiI1I1 == 'SUB_GROUP' :
   self . dp_SubGroup_List ( self . main_params )
   if 84 - 84: Ii1I / O00oOoOoO0o0O
  elif IIiI1I1 == 'CATEGORY_LIST' :
   self . dp_Category_List ( self . main_params )
   if 86 - 86: OoOoOO00 * II111iiii - O0 . OoOoOO00 % iIii1I11I1II1 / OOooOOo
  elif IIiI1I1 == 'EPISODE' :
   self . dp_Episode_List ( self . main_params )
   if 11 - 11: I1IiiI * oO0o + I1ii11iIi11i / I1ii11iIi11i
  elif IIiI1I1 == 'ORDER_BY' :
   self . dp_setEpOrderby ( self . main_params )
   if 37 - 37: i11iIiiIii + i1IIi
  elif IIiI1I1 == 'SEARCH' :
   self . dp_Search_List ( self . main_params )
   if 23 - 23: iii1I1I + I11i . OoOoOO00 * I1IiiI + I1ii11iIi11i
  elif IIiI1I1 == 'MOVIE' :
   self . play_VIDEO ( self . main_params )
   if 18 - 18: O00oOoOoO0o0O * o0oOOo0O0Ooo . O00oOoOoO0o0O / O0
   time . sleep ( 0.1 )
   if 8 - 8: o0oOOo0O0Ooo
  elif IIiI1I1 == 'WATCH' :
   self . dp_Watch_List ( self . main_params )
   if 4 - 4: I1ii11iIi11i + I1ii11iIi11i * Oo0ooO0oo0oO - OoOoOO00
  elif IIiI1I1 == 'MYVIEW_REMOVE' :
   self . dp_WatchList_Delete ( self . main_params )
   if 78 - 78: Ii1I / II111iiii % OoOoOO00
  elif IIiI1I1 == 'LOGOUT' :
   self . logout ( )
   if 52 - 52: OOooOOo - iii1I1I * oO0o
   if 17 - 17: OoooooooOO + OOooOOo * I11i * OoOoOO00
   if 36 - 36: O0 + Oo0Ooo
   if 5 - 5: Oo0Ooo * OoOoOO00
   if 46 - 46: Oo0ooO0oo0oO
   if 33 - 33: iii1I1I - II111iiii * OoooooooOO - Oo0Ooo - OOooOOo
  else :
   None
   if 84 - 84: O0oo0OO0 + Oo0Ooo - OoOoOO00 * OoOoOO00
   if 61 - 61: OoooooooOO . oO0o . OoooooooOO / Oo0Ooo
   if 72 - 72: i1IIi
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
