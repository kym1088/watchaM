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
  ooOOoooooo = datetime . datetime . now ( ) . date ( )
  II1I = xbmcgui . Window ( 10000 ) . getProperty ( 'WATCHA_M_LOGINTIME' )
  if II1I == None or II1I == '' : II1I = '1900-01-01'
  try :
   II1I = datetime . datetime . strptime ( II1I , '%Y-%m-%d' ) . date ( )
  except TypeError :
   II1I = datetime . datetime ( * ( time . strptime ( II1I , '%Y-%m-%d' ) [ 0 : 6 ] ) ) . date ( )
   if 84 - 84: O00oOoOoO0o0O . i11iIiiIii . O00oOoOoO0o0O * I1ii11iIi11i - I11i
   if 42 - 42: i11iIiiIii
   if 33 - 33: iii1I1I - O0 * i1IIi * o0oOOo0O0Ooo - Oo0Ooo
  if xbmcgui . Window ( 10000 ) . getProperty ( 'WATCHA_M_LOGINWAIT' ) == 'TRUE' :
   iiIiI = 0
   while True :
    iiIiI += 1
    if 91 - 91: iii1I1I % i1IIi % iIii1I11I1II1
    time . sleep ( 0.05 )
    if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
    if 45 - 45: oO0o - O00oOoOoO0o0O - OoooooooOO - OoO0O00 . II111iiii / O0
    if II1I >= ooOOoooooo : return
    if iiIiI > 600 : return
  else :
   xbmcgui . Window ( 10000 ) . setProperty ( 'WATCHA_M_LOGINWAIT' , 'TRUE' )
   if 51 - 51: O0 + iii1I1I
   if 8 - 8: oO0o * OoOoOO00 - Ii1I - OoO0O00 * OOooOOo % I1IiiI
  if II1I >= ooOOoooooo :
   xbmcgui . Window ( 10000 ) . setProperty ( 'WATCHA_M_LOGINWAIT' , 'FALSE' )
   return
   if 48 - 48: O0
   if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
  if not self . WatchaObj . GetCredential ( oO , iIi1IIIi1 , O0oOoOOOoOO ) :
   self . addon_noti ( __language__ ( 30103 ) . encode ( 'utf8' ) )
   xbmcgui . Window ( 10000 ) . setProperty ( 'WATCHA_M_LOGINWAIT' , 'FALSE' )
   sys . exit ( )
   if 41 - 41: Ii1I - O0 - O0
   if 68 - 68: OOooOOo % O0oo0OO0
  self . set_winCredential ( self . WatchaObj . LoadCredential ( ) )
  if 88 - 88: iIii1I11I1II1 - Oo0ooO0oo0oO + OOooOOo
  self . cookiefile_save ( )
  xbmcgui . Window ( 10000 ) . setProperty ( 'WATCHA_M_LOGINWAIT' , 'FALSE' )
  if 40 - 40: I1IiiI * Ii1I + OOooOOo % iii1I1I
  if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + O0oo0OO0 / OoOoOO00
  if 23 - 23: O0
  if 85 - 85: Ii1I
  if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
  if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + iii1I1I / OoOoOO00
 def dp_SubGroup_List ( self , args ) :
  if 84 - 84: Oo0ooO0oo0oO * II111iiii + Oo0Ooo
  self . WatchaObj . SaveCredential ( self . get_winCredential ( ) )
  if 53 - 53: iii1I1I % II111iiii . O00oOoOoO0o0O - iIii1I11I1II1 - O00oOoOoO0o0O * II111iiii
  ooO0oOOooOo0 = args . get ( 'stype' )
  i1I1ii11i1Iii = int ( args . get ( 'page' ) )
  I1IiiiiI = args . get ( 'sort' )
  if 80 - 80: O0oo0OO0 . i11iIiiIii - o0oOOo0O0Ooo
  iIiIIi1 = self . WatchaObj . GetSubGroupList ( ooO0oOOooOo0 )
  if 7 - 7: Oo0ooO0oo0oO - Oo0Ooo - oO0o + Oo0ooO0oo0oO
  if 26 - 26: Ii1I
  if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
  if 47 - 47: iii1I1I - Ii1I . II111iiii + OoooooooOO . i11iIiiIii
  if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
  if 87 - 87: Oo0Ooo . O00oOoOoO0o0O
  if 75 - 75: Oo0ooO0oo0oO + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iii1I1I
  if 55 - 55: OOooOOo . I1IiiI
  if 61 - 61: Oo0Ooo % O00oOoOoO0o0O . Oo0Ooo
  if 100 - 100: O0oo0OO0 * O0
  if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
  if 79 - 79: O0
  if 78 - 78: I1ii11iIi11i + OOooOOo - O0oo0OO0
  if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
  if 57 - 57: OoO0O00 / Oo0ooO0oo0oO
  if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
  if 7 - 7: O00oOoOoO0o0O * O0oo0OO0 % Ii1I - o0oOOo0O0Ooo
  i1i = Iiii111Ii11I1 if ooO0oOOooOo0 == 'genres' else ooO0oooOoO0
  if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
  O00o0OO0 = len ( iIiIIi1 )
  IIi1I1iiiii = int ( O00o0OO0 // ( i1i + 1 ) ) + 1
  o00oOOooOOo0o = ( i1I1ii11i1Iii - 1 ) * i1i
  if 66 - 66: iii1I1I - iii1I1I - i11iIiiIii . I1ii11iIi11i - OOooOOo
  for oOOo0O00o in range ( i1i ) :
   iIiIi11 = o00oOOooOOo0o + oOOo0O00o
   if iIiIi11 >= O00o0OO0 : break
   if 87 - 87: Oo0Ooo . I1IiiI - II111iiii + O0 / Oo0Ooo / oO0o
   oooo000 = iIiIIi1 [ iIiIi11 ] . get ( 'group_name' )
   IiI = iIiIIi1 [ iIiIi11 ] . get ( 'api_path' )
   IIIii1I = iIiIIi1 [ iIiIi11 ] . get ( 'tag_id' )
   if 97 - 97: O0 + OoOoOO00
   II = { 'mode' : 'CATEGORY_LIST'
 , 'api_path' : IiI
 , 'tag_id' : IIIii1I
 , 'stype' : ooO0oOOooOo0
 , 'page' : '1'
 , 'sort' : I1IiiiiI
 }
   if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
   self . add_dir ( oooo000 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = II )
   if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
  if IIi1I1iiiii > i1I1ii11i1Iii :
   II = { }
   II [ 'mode' ] = 'SUB_GROUP'
   II [ 'stype' ] = ooO0oOOooOo0
   II [ 'api_path' ] = args . get ( 'api_path' )
   II [ 'page' ] = str ( i1I1ii11i1Iii + 1 )
   II [ 'sort' ] = I1IiiiiI
   oooo000 = '[B]%s >>[/B]' % '다음 페이지'
   o0o0O0O00oOOo = str ( i1I1ii11i1Iii + 1 )
   self . add_dir ( oooo000 , sublabel = o0o0O0O00oOOo , img = '' , infoLabels = None , isFolder = True , params = II )
   if 14 - 14: OoOoOO00 + oO0o
   if 52 - 52: OoooooooOO - Oo0ooO0oo0oO
  if len ( iIiIIi1 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = True )
  if 74 - 74: iii1I1I + o0oOOo0O0Ooo
  if 71 - 71: Oo0Ooo % OOooOOo
  if 98 - 98: I11i % i11iIiiIii % Oo0ooO0oo0oO + Ii1I
  if 78 - 78: I1ii11iIi11i % oO0o / iii1I1I - iIii1I11I1II1
 def play_VIDEO ( self , args ) :
  if 69 - 69: O0oo0OO0
  self . WatchaObj . SaveCredential ( self . get_winCredential ( ) )
  if 11 - 11: I1IiiI
  if 16 - 16: Ii1I + O00oOoOoO0o0O * O0 % i1IIi . I1IiiI
  if 67 - 67: OoooooooOO / I1IiiI * Ii1I + I11i
  if 65 - 65: OoooooooOO - I1ii11iIi11i / Oo0ooO0oo0oO / II111iiii / i1IIi
  if 71 - 71: O0oo0OO0 + Ii1I
  if 28 - 28: OOooOOo
  if 38 - 38: Oo0ooO0oo0oO % II111iiii % I11i / OoO0O00 + OoOoOO00 / i1IIi
  if 54 - 54: iIii1I11I1II1 % I1ii11iIi11i - OOooOOo / oO0o - OoO0O00 . I11i
  IIo0Oo0oO0oOO00 = args . get ( 'movie_code' )
  oo00OO0000oO = args . get ( 'season_code' )
  oooo000 = args . get ( 'title' )
  I1II1 = args . get ( 'thumbnail' )
  oooO = self . get_selQuality ( )
  if 26 - 26: Ii1I % I1ii11iIi11i
  if 76 - 76: O00oOoOoO0o0O * iii1I1I
  self . addon_log ( IIo0Oo0oO0oOO00 + ' - ' + oo00OO0000oO , False )
  ooooooo00o , o0oooOO00 , iiIiii1IIIII = self . WatchaObj . GetStreamingURL ( IIo0Oo0oO0oOO00 , oooO )
  if 67 - 67: Ii1I / O00oOoOoO0o0O
  if 9 - 9: O0 % O0 - o0oOOo0O0Ooo
  if ooooooo00o == '' :
   self . addon_noti ( __language__ ( 30302 ) . encode ( 'utf8' ) )
   return
   if 51 - 51: I1IiiI . iIii1I11I1II1 - I1ii11iIi11i / O0
   if 52 - 52: o0oOOo0O0Ooo + O0 + iii1I1I + Oo0Ooo % iii1I1I
   if 75 - 75: I1IiiI . Oo0ooO0oo0oO . O0 * O0oo0OO0
   if 4 - 4: Ii1I % oO0o * OoO0O00
  o0O0OOOOoOO0 = ooooooo00o
  self . addon_log ( o0O0OOOOoOO0 , False )
  if 23 - 23: i11iIiiIii
  if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
  o0ooooO0o0O = xbmcgui . ListItem ( path = o0O0OOOOoOO0 )
  if 24 - 24: O0 * o0oOOo0O0Ooo
  if iiIiii1IIIII :
   IiI1iiiIii = iiIiii1IIIII
   I1III1111iIi = 'https://lic.drmtoday.com/license-proxy-widevine/cenc/?specConform=true'
   I1i111I = 'mpd'
   Ooo = 'com.widevine.alpha'
   if 65 - 65: O0 * OoooooooOO % OOooOOo / O00oOoOoO0o0O - Ii1I / I11i
   oo0o00o0OoOo = inputstreamhelper . Helper ( I1i111I , drm = Ooo )
   if 92 - 92: Oo0Ooo % Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
   if oo0o00o0OoOo . check_inputstream ( ) :
    if 10 - 10: iii1I1I + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / O0oo0OO0 / I1ii11iIi11i
    iI1II = { 'Host' : 'lic.drmtoday.com'
 , 'origin' : 'https://play.watcha.net'
 , 'referer' : 'https://play.watcha.net/watch/' + IIo0Oo0oO0oOO00
 , 'dt-custom-data' : IiI1iiiIii
 , 'Sec-Fetch-Dest' : 'empty'
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'cross-site'
 , 'user-agent' : Ii1IIii11
 , 'Content-Type' : 'application/octet-stream'
 }
    o0OOo0o0O0O = I1III1111iIi + '|' + urllib . urlencode ( iI1II ) + '|R{SSM}|'
    if 65 - 65: i11iIiiIii
    self . addon_log ( o0OOo0o0O0O )
    if 85 - 85: Ii1I % iii1I1I + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
    o0ooooO0o0O . setProperty ( 'inputstreamaddon' , oo0o00o0OoOo . inputstream_addon )
    o0ooooO0o0O . setProperty ( 'inputstream.adaptive.manifest_type' , I1i111I )
    o0ooooO0o0O . setProperty ( 'inputstream.adaptive.license_type' , Ooo )
    o0ooooO0o0O . setProperty ( 'inputstream.adaptive.license_key' , o0OOo0o0O0O )
    if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
    if 28 - 28: iii1I1I . iii1I1I % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iii1I1I
    if 27 - 27: OoO0O00 + Oo0ooO0oo0oO - i1IIi
    if 69 - 69: O00oOoOoO0o0O - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
    if 79 - 79: O0 * i11iIiiIii - O00oOoOoO0o0O / O00oOoOoO0o0O
  if o0oooOO00 :
   try :
    import urllib2
    i1 = open ( Oooo0000 , 'wb' )
    O0I11Iiii1I = urllib2 . urlopen ( o0oooOO00 )
    while True :
     oo00O0oO0O0 = O0I11Iiii1I . readline ( )
     oo00O0oO0O0 = re . sub ( r'(\d\d:\d\d).(\d\d\d) --> (\d\d:\d\d).(\d\d\d)(?:[ \-\w]+:[\w\%\d:]+)*\n' , r'00:\1.\2 --> 00:\3.\4\n' , oo00O0oO0O0 )
     if not oo00O0oO0O0 : break
     i1 . write ( oo00O0oO0O0 )
     if 96 - 96: i11iIiiIii % Oo0ooO0oo0oO / OoOoOO00
    i1 . close ( )
    o0ooooO0o0O . setSubtitles ( [ Oooo0000 , o0oooOO00 ] )
   except :
    o0ooooO0o0O . setSubtitles ( [ o0oooOO00 ] )
    if 36 - 36: OOooOOo + O0 - Ii1I - O0 % I11i . oO0o
    if 74 - 74: i11iIiiIii . I1IiiI
  xbmcplugin . setResolvedUrl ( self . _addon_handle , True , o0ooooO0o0O )
  if 36 - 36: OoooooooOO . OoO0O00
  if 56 - 56: Oo0Ooo . I1ii11iIi11i . I1IiiI
  if 39 - 39: O0 + O0oo0OO0
  try :
   ooO0oOOooOo0 = 'movie' if oo00OO0000oO == '-' else 'seasons'
   II = { 'code' : IIo0Oo0oO0oOO00 if ooO0oOOooOo0 == 'movie' else oo00OO0000oO
 , 'img' : I1II1
 , 'title' : oooo000
 , 'videoid' : IIo0Oo0oO0oOO00
   }
   self . Save_Watched_List ( ooO0oOOooOo0 , II )
  except :
   None
   if 91 - 91: OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoOoOO00 + O0
   if 26 - 26: I1ii11iIi11i - OoooooooOO
   if 11 - 11: I1IiiI * oO0o
   if 81 - 81: iii1I1I + O00oOoOoO0o0O
   if 98 - 98: I1IiiI
 def dp_Category_List ( self , args ) :
  if 95 - 95: Oo0ooO0oo0oO / Oo0ooO0oo0oO
  self . WatchaObj . SaveCredential ( self . get_winCredential ( ) )
  if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
  ooO0oOOooOo0 = args . get ( 'stype' )
  IIIii1I = args . get ( 'tag_id' )
  IiI = args . get ( 'api_path' )
  i1I1ii11i1Iii = int ( args . get ( 'page' ) )
  I1IiiiiI = args . get ( 'sort' )
  if 55 - 55: Oo0ooO0oo0oO - I11i + II111iiii + iii1I1I % Ii1I
  iiI11i1II , OO0O0OOo0O = self . WatchaObj . GetCategoryList ( ooO0oOOooOo0 , IIIii1I , IiI , i1I1ii11i1Iii , I1IiiiiI )
  if 36 - 36: Oo0ooO0oo0oO . Oo0Ooo % Oo0ooO0oo0oO % OoO0O00
  if 2 - 2: o0oOOo0O0Ooo - I1ii11iIi11i
  for o0OOOo in iiI11i1II :
   IIo0Oo0oO0oOO00 = o0OOOo . get ( 'code' )
   oooo000 = o0OOOo . get ( 'title' )
   ii1iiIiIII1ii = o0OOOo . get ( 'content_type' )
   oO0o0oooO0oO = o0OOOo . get ( 'story' )
   I1II1 = o0OOOo . get ( 'thumbnail' )
   IiIiII1 = o0OOOo . get ( 'year' )
   Iii1iiIi1II = o0OOOo . get ( 'film_rating_code' )
   OO0O00oOo = o0OOOo . get ( 'film_rating_short' )
   if 14 - 14: I1IiiI
   if ii1iiIiIII1ii == 'movies' :
    Oo0ooOo0o = False
    IIiIiI1I = 'MOVIE'
    OooOoOo = ''
    oo00OO0000oO = '-'
   else :
    Oo0ooOo0o = True
    IIiIiI1I = 'EPISODE'
    OooOoOo = 'Series'
    oo00OO0000oO = IIo0Oo0oO0oOO00
    if 14 - 14: o0oOOo0O0Ooo * OOooOOo + iii1I1I + O0 + i11iIiiIii
   oOoO0 = o0OOOo . get ( 'info' )
   oOoO0 [ 'plot' ] = '%s (%s)\n년도 : %s\n\n%s' % ( oooo000 , OO0O00oOo , IiIiII1 , oO0o0oooO0oO )
   if 77 - 77: iIii1I11I1II1 . iii1I1I % iii1I1I + i11iIiiIii
   if Iii1iiIi1II >= 19 :
    oooo000 += '  (%s년 - %s)' % ( IiIiII1 , str ( OO0O00oOo ) )
   else :
    oooo000 += '  (%s년)' % ( IiIiII1 )
    if 72 - 72: iIii1I11I1II1 * Ii1I % Oo0ooO0oo0oO / OoO0O00
    if 35 - 35: Oo0ooO0oo0oO + i1IIi % I1ii11iIi11i % I11i + oO0o
   II = { 'mode' : IIiIiI1I
 , 'movie_code' : IIo0Oo0oO0oOO00
 , 'page' : '1'
 , 'season_code' : oo00OO0000oO
   , 'title' : oooo000
 , 'thumbnail' : I1II1
 }
   if 17 - 17: i1IIi
   self . add_dir ( oooo000 , sublabel = OooOoOo , img = I1II1 , infoLabels = oOoO0 , isFolder = Oo0ooOo0o , params = II )
   if 21 - 21: Oo0Ooo
   if 29 - 29: I11i / II111iiii / Oo0ooO0oo0oO * OOooOOo
  if OO0O0OOo0O :
   if self . WatchaObj . GetCategoryList_morepage ( ooO0oOOooOo0 , IIIii1I , IiI , i1I1ii11i1Iii + 1 , I1IiiiiI ) :
    II = { }
    II [ 'mode' ] = 'CATEGORY_LIST'
    II [ 'stype' ] = ooO0oOOooOo0
    II [ 'tag_id' ] = IIIii1I
    II [ 'api_path' ] = IiI
    II [ 'page' ] = str ( i1I1ii11i1Iii + 1 )
    II [ 'sort' ] = I1IiiiiI
    oooo000 = '[B]%s >>[/B]' % '다음 페이지'
    o0o0O0O00oOOo = str ( i1I1ii11i1Iii + 1 )
    self . add_dir ( oooo000 , sublabel = o0o0O0O00oOOo , img = '' , infoLabels = None , isFolder = True , params = II )
    if 10 - 10: O0oo0OO0 % O00oOoOoO0o0O * O00oOoOoO0o0O . I11i / Ii1I % OOooOOo
  if len ( iiI11i1II ) > 0 :
   if IiI == 'arrivals/latest' :
    xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = True )
   else :
    xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
    if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
    if 28 - 28: Oo0ooO0oo0oO + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
    if 54 - 54: i1IIi + II111iiii
    if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
    if 5 - 5: Ii1I
 def dp_Episode_List ( self , args ) :
  if 46 - 46: O00oOoOoO0o0O
  self . WatchaObj . SaveCredential ( self . get_winCredential ( ) )
  if 45 - 45: Oo0ooO0oo0oO
  IIi = args . get ( 'movie_code' )
  i1I1ii11i1Iii = int ( args . get ( 'page' ) )
  oo00OO0000oO = args . get ( 'season_code' )
  if 94 - 94: II111iiii - Oo0Ooo
  if 91 - 91: Oo0Ooo
  iiI11i1II , OO0O0OOo0O = self . WatchaObj . GetEpisodoList ( IIi , i1I1ii11i1Iii , orderby = self . get_winEpisodeOrderby ( ) )
  if 31 - 31: OOooOOo / i11iIiiIii % iIii1I11I1II1 + OOooOOo / i11iIiiIii
  if 70 - 70: OoO0O00 * O0 . I11i + I1IiiI . O00oOoOoO0o0O
  for o0OOOo in iiI11i1II :
   IIo0Oo0oO0oOO00 = o0OOOo . get ( 'code' )
   oooo000 = o0OOOo . get ( 'title' )
   I1II1 = o0OOOo . get ( 'thumbnail' )
   Ii1iIiII1Ii = o0OOOo . get ( 'display_num' )
   Iii1II1iiiiI = o0OOOo . get ( 'season_title' )
   if 61 - 61: OOooOOo % OOooOOo * o0oOOo0O0Ooo / o0oOOo0O0Ooo
   oOoO0 = o0OOOo . get ( 'info' )
   oOoO0 [ 'plot' ] = '%s\n%s\n\n%s' % ( Iii1II1iiiiI , Ii1iIiII1Ii , oooo000 )
   if 75 - 75: O00oOoOoO0o0O . Oo0ooO0oo0oO
   oooo000 = '(%s) %s' % ( Ii1iIiII1Ii , oooo000 )
   if 50 - 50: OoOoOO00
   II = { 'mode' : 'MOVIE'
 , 'movie_code' : IIo0Oo0oO0oOO00
 , 'season_code' : oo00OO0000oO
   # Oo0ooO0oo0oO - O0oo0OO0 * O00oOoOoO0o0O . I1ii11iIi11i
   , 'title' : '%s < %s >' % ( oooo000 , Iii1II1iiiiI )
 , 'thumbnail' : I1II1
 }
   if 37 - 37: Oo0ooO0oo0oO % i11iIiiIii % II111iiii . O0 . Ii1I
   self . add_dir ( oooo000 , sublabel = Iii1II1iiiiI , img = I1II1 , infoLabels = oOoO0 , isFolder = False , params = II )
   if 51 - 51: OoO0O00 - O0 % oO0o - II111iiii
  if i1I1ii11i1Iii == 1 :
   oOoO0 = { 'plot' : '정렬순서를 변경합니다.' }
   II = { }
   II [ 'mode' ] = 'ORDER_BY'
   if self . get_winEpisodeOrderby ( ) == 'desc' :
    oooo000 = '정렬순서변경 : 최신화부터 -> 1회부터'
    II [ 'orderby' ] = 'asc'
   else :
    oooo000 = '정렬순서변경 : 1회부터 -> 최신화부터'
    II [ 'orderby' ] = 'desc'
   self . add_dir ( oooo000 , sublabel = '' , img = '' , infoLabels = oOoO0 , isFolder = False , params = II )
   if 31 - 31: iii1I1I / Oo0Ooo - iii1I1I - OOooOOo
  if OO0O0OOo0O :
   if 7 - 7: iii1I1I % O0 . OoOoOO00 + I1IiiI - I11i
   II [ 'mode' ] = 'EPISODE'
   II [ 'movie_code' ] = IIi
   II [ 'page' ] = str ( i1I1ii11i1Iii + 1 )
   oooo000 = '[B]%s >>[/B]' % '다음 페이지'
   o0o0O0O00oOOo = str ( i1I1ii11i1Iii + 1 )
   self . add_dir ( oooo000 , sublabel = o0o0O0O00oOOo , img = '' , infoLabels = None , isFolder = True , params = II )
   if 75 - 75: I11i
   if 71 - 71: Oo0ooO0oo0oO
  if len ( iiI11i1II ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = True )
  if 53 - 53: OoooooooOO % Ii1I . O00oOoOoO0o0O / i11iIiiIii % iii1I1I
  if 28 - 28: I11i
  if 58 - 58: OoOoOO00
  if 37 - 37: Oo0Ooo - iIii1I11I1II1 / I1ii11iIi11i
  if 73 - 73: i11iIiiIii - O00oOoOoO0o0O
  if 25 - 25: OoooooooOO + O00oOoOoO0o0O * I1ii11iIi11i
  if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + O0oo0OO0
 def dp_Search_List ( self , args ) :
  if 18 - 18: Oo0ooO0oo0oO * OoOoOO00 . iii1I1I / I1ii11iIi11i / i11iIiiIii
  self . WatchaObj . SaveCredential ( self . get_winCredential ( ) )
  if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
  i1I1ii11i1Iii = int ( args . get ( 'page' ) )
  if 91 - 91: i11iIiiIii / i1IIi + iii1I1I + Oo0ooO0oo0oO * i11iIiiIii
  if 'search_key' in args :
   OoOoOo00o0 = args . get ( 'search_key' )
  else :
   OoOoOo00o0 = self . get_keyboard_input ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
   if not OoOoOo00o0 : return
   if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . iii1I1I
   if 8 - 8: Oo0ooO0oo0oO + II111iiii / iii1I1I / I11i
  iiI11i1II , OO0O0OOo0O = self . WatchaObj . GetSearchList ( OoOoOo00o0 , i1I1ii11i1Iii )
  if len ( iiI11i1II ) == 0 : return
  if 74 - 74: O0 / i1IIi
  if 78 - 78: OoooooooOO . OoO0O00 + Oo0ooO0oo0oO - i1IIi
  for o0OOOo in iiI11i1II :
   IIo0Oo0oO0oOO00 = o0OOOo . get ( 'code' )
   oooo000 = o0OOOo . get ( 'title' )
   ii1iiIiIII1ii = o0OOOo . get ( 'content_type' )
   oO0o0oooO0oO = o0OOOo . get ( 'story' )
   I1II1 = o0OOOo . get ( 'thumbnail' )
   IiIiII1 = o0OOOo . get ( 'year' )
   Iii1iiIi1II = o0OOOo . get ( 'film_rating_code' )
   OO0O00oOo = o0OOOo . get ( 'film_rating_short' )
   if 31 - 31: OoooooooOO . OOooOOo
   if ii1iiIiIII1ii == 'movies' :
    Oo0ooOo0o = False
    IIiIiI1I = 'MOVIE'
    OooOoOo = ''
    oo00OO0000oO = '-'
   else :
    Oo0ooOo0o = True
    IIiIiI1I = 'EPISODE'
    OooOoOo = 'Series'
    oo00OO0000oO = IIo0Oo0oO0oOO00
    if 83 - 83: iii1I1I . O0 / Oo0Ooo / OOooOOo - II111iiii
   oOoO0 = o0OOOo . get ( 'info' )
   oOoO0 [ 'plot' ] = '%s (%s)\n년도 : %s\n\n%s' % ( oooo000 , OO0O00oOo , IiIiII1 , oO0o0oooO0oO )
   if 100 - 100: OoO0O00
   if Iii1iiIi1II >= 19 :
    oooo000 += '  (%s년 - %s)' % ( IiIiII1 , str ( OO0O00oOo ) )
   else :
    oooo000 += '  (%s년)' % ( IiIiII1 )
    if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iii1I1I . iIii1I11I1II1 * iii1I1I
   II = { 'mode' : IIiIiI1I
 , 'movie_code' : IIo0Oo0oO0oOO00
 , 'page' : '1'
 , 'season_code' : oo00OO0000oO
   , 'title' : oooo000
 , 'thumbnail' : I1II1
 }
   if 38 - 38: I1ii11iIi11i - iii1I1I / O0 . O0oo0OO0
   self . add_dir ( oooo000 , sublabel = OooOoOo , img = I1II1 , infoLabels = oOoO0 , isFolder = Oo0ooOo0o , params = II )
   if 45 - 45: O0oo0OO0
   if 83 - 83: OoOoOO00 . OoooooooOO
  if OO0O0OOo0O :
   II = { }
   II [ 'mode' ] = 'SEARCH'
   II [ 'search_key' ] = OoOoOo00o0
   II [ 'page' ] = str ( i1I1ii11i1Iii + 1 )
   oooo000 = '[B]%s >>[/B]' % '다음 페이지'
   o0o0O0O00oOOo = str ( i1I1ii11i1Iii + 1 )
   self . add_dir ( oooo000 , sublabel = o0o0O0O00oOOo , img = '' , infoLabels = None , isFolder = True , params = II )
   if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / O00oOoOoO0o0O / i11iIiiIii
  if len ( iiI11i1II ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 62 - 62: OoO0O00 / I1ii11iIi11i
  if 7 - 7: OoooooooOO . O00oOoOoO0o0O
  if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
  if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
  if 100 - 100: Oo0ooO0oo0oO % iIii1I11I1II1 * II111iiii - iii1I1I
  if 92 - 92: Oo0ooO0oo0oO
 def Delete_Watched_List ( self , stype ) :
  try :
   II11iI111i1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   with open ( II11iI111i1 , 'w' ) as Oo00OoOo :
    Oo00OoOo . write ( '' )
  except :
   None
   if 24 - 24: i11iIiiIii - O0oo0OO0
   if 21 - 21: I11i
   if 92 - 92: i11iIiiIii / O0oo0OO0 - iii1I1I % Oo0ooO0oo0oO * O0oo0OO0 + Oo0Ooo
   if 11 - 11: OoooooooOO . O0oo0OO0
 def dp_WatchList_Delete ( self , args ) :
  ooO0oOOooOo0 = args . get ( 'stype' )
  if 80 - 80: OoooooooOO - OOooOOo * Ii1I * I1ii11iIi11i / I1IiiI / OOooOOo
  oOOOO = xbmcgui . Dialog ( )
  I111IIIiIii = oOOOO . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if I111IIIiIii == False : sys . exit ( )
  if 13 - 13: O0oo0OO0 * Oo0ooO0oo0oO + i11iIiiIii * O0oo0OO0 - Oo0ooO0oo0oO
  self . Delete_Watched_List ( ooO0oOOooOo0 )
  if 23 - 23: iIii1I11I1II1 * i1IIi % OoooooooOO * O00oOoOoO0o0O
  xbmc . executebuiltin ( "Container.Refresh" )
  if 9 - 9: O00oOoOoO0o0O - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
  if 39 - 39: O00oOoOoO0o0O * Oo0Ooo + iIii1I11I1II1 - O00oOoOoO0o0O + OOooOOo
  if 69 - 69: O0
  if 85 - 85: Oo0ooO0oo0oO / O0
 def Load_Watched_List ( self , stype ) :
  try :
   II11iI111i1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   with open ( II11iI111i1 , 'r' ) as Oo00OoOo :
    iI1iIIIi1i = Oo00OoOo . readlines ( )
  except :
   iI1iIIIi1i = [ ]
   if 89 - 89: iIii1I11I1II1
  return iI1iIIIi1i
  if 21 - 21: I11i % I11i
  if 27 - 27: i11iIiiIii / I1ii11iIi11i
  if 84 - 84: Oo0Ooo
  if 43 - 43: oO0o - OoooooooOO
 def Save_Watched_List ( self , stype , in_params ) :
  try :
   II11iI111i1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   ii1iI = self . Load_Watched_List ( stype )
   if 49 - 49: o0oOOo0O0Ooo . O00oOoOoO0o0O / OoO0O00 + II111iiii
   with open ( II11iI111i1 , 'w' ) as Oo00OoOo :
    ii11i = urllib . urlencode ( in_params )
    ii11i = ii11i . encode ( 'utf-8' ) + '\n'
    Oo00OoOo . write ( ii11i )
    if 35 - 35: I1ii11iIi11i * iii1I1I - OoO0O00 % o0oOOo0O0Ooo
    oOo00O000Oo0 = 0
    for I1iI1I1I1i11i in ii1iI :
     iiI11 = dict ( urlparse . parse_qsl ( I1iI1I1I1i11i ) )
     if 63 - 63: OoO0O00 + I1ii11iIi11i . O0oo0OO0 % O0oo0OO0
     oOOOOIi = in_params . get ( 'code' )
     Ii1ii111i1 = iiI11 . get ( 'code' )
     if stype == 'seasons' and self . get_settings_direct_replay ( ) == True :
      oOOOOIi = in_params . get ( 'videoid' )
      Ii1ii111i1 = iiI11 . get ( 'videoid' ) if Ii1ii111i1 != None else '-'
      if 31 - 31: OOooOOo + O0
     if oOOOOIi != Ii1ii111i1 :
      Oo00OoOo . write ( I1iI1I1I1i11i )
      oOo00O000Oo0 += 1
      if oOo00O000Oo0 >= 50 : break
  except :
   None
   if 87 - 87: Oo0ooO0oo0oO
   if 45 - 45: OoO0O00 / OoooooooOO - iii1I1I / Ii1I % O00oOoOoO0o0O
   if 83 - 83: I1IiiI . iIii1I11I1II1 - O00oOoOoO0o0O * i11iIiiIii
   if 20 - 20: i1IIi * O0oo0OO0 + II111iiii % o0oOOo0O0Ooo % oO0o
   if 13 - 13: Oo0Ooo
 def dp_Watch_List ( self , args ) :
  ooO0oOOooOo0 = args . get ( 'stype' )
  oOoOooOo0o0 = self . get_settings_direct_replay ( )
  if 60 - 60: I1ii11iIi11i * I1IiiI
  if ooO0oOOooOo0 == '-' :
   for I1iIiI11I1 in O0oO :
    oooo000 = I1iIiI11I1 . get ( 'title' )
    if 27 - 27: Ii1I . i11iIiiIii % O0oo0OO0
    II = { 'mode' : I1iIiI11I1 . get ( 'mode' )
 , 'stype' : I1iIiI11I1 . get ( 'stype' )
 }
    if 65 - 65: II111iiii . I1IiiI % oO0o * OoO0O00
    self . add_dir ( oooo000 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = II )
   if len ( O0oO ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
   if 38 - 38: OoOoOO00 / iii1I1I % Oo0Ooo
  else :
   I1IIIiii1 = self . Load_Watched_List ( ooO0oOOooOo0 )
   if 65 - 65: I11i / II111iiii * Ii1I . iii1I1I * oO0o % OOooOOo
   for O0oOOo0Oo in I1IIIiii1 :
    o000O000 = dict ( urlparse . parse_qsl ( O0oOOo0Oo ) )
    if 19 - 19: iIii1I11I1II1
    IIo0Oo0oO0oOO00 = o000O000 . get ( 'code' )
    oooo000 = o000O000 . get ( 'title' )
    I1II1 = o000O000 . get ( 'img' )
    Ii1IiI1i1ii = o000O000 . get ( 'videoid' )
    if 30 - 30: O00oOoOoO0o0O + O0oo0OO0 - O00oOoOoO0o0O . O00oOoOoO0o0O - II111iiii + O0
    oOoO0 = { }
    oOoO0 [ 'plot' ] = oooo000
    if 86 - 86: i1IIi
    if ooO0oOOooOo0 == 'movie' :
     II = { 'mode' : 'MOVIE'
 , 'page' : '1'
 , 'movie_code' : IIo0Oo0oO0oOO00
 , 'season_code' : '-'
 , 'title' : oooo000
 , 'thumbnail' : I1II1
 }
     Oo0ooOo0o = False
    else :
     if oOoOooOo0o0 == False or Ii1IiI1i1ii == None :
      II = { 'mode' : 'EPISODE'
 , 'page' : '1'
 , 'movie_code' : IIo0Oo0oO0oOO00
 , 'season_code' : IIo0Oo0oO0oOO00
 , 'title' : oooo000
 , 'thumbnail' : I1II1
 }
      Oo0ooOo0o = True
     else :
      II = { 'mode' : 'MOVIE'
 , 'movie_code' : Ii1IiI1i1ii
 , 'season_code' : IIo0Oo0oO0oOO00
 , 'title' : oooo000
 , 'thumbnail' : I1II1
 }
      Oo0ooOo0o = False
      if 41 - 41: OoOoOO00 * I11i / OoOoOO00 % oO0o
    self . add_dir ( oooo000 , sublabel = '' , img = I1II1 , infoLabels = oOoO0 , isFolder = Oo0ooOo0o , params = II )
    if 18 - 18: II111iiii . OoooooooOO % OoOoOO00 % Ii1I
   oOoO0 = { 'plot' : '시청목록을 삭제합니다.' }
   oooo000 = '*** 시청목록 삭제 ***'
   II = { 'mode' : 'MYVIEW_REMOVE'
 , 'stype' : ooO0oOOooOo0
 }
   self . add_dir ( oooo000 , sublabel = '' , img = '' , infoLabels = oOoO0 , isFolder = False , params = II )
   if 9 - 9: OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
   xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
   if 2 - 2: OoooooooOO % OOooOOo
   if 63 - 63: I1IiiI % iIii1I11I1II1
   if 39 - 39: iii1I1I / II111iiii / I1ii11iIi11i % I1IiiI
   if 89 - 89: O0oo0OO0 + OoooooooOO + O0oo0OO0 * i1IIi + iIii1I11I1II1 % I11i
 def logout ( self ) :
  oOOOO = xbmcgui . Dialog ( )
  I111IIIiIii = oOOOO . yesno ( __language__ ( 30910 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if I111IIIiIii == False : sys . exit ( )
  if 59 - 59: OOooOOo + i11iIiiIii
  self . wininfo_clear ( )
  if 88 - 88: i11iIiiIii - Oo0ooO0oo0oO
  if 67 - 67: OOooOOo . Oo0Ooo + OoOoOO00 - OoooooooOO
  if os . path . isfile ( i11 ) : os . remove ( i11 )
  if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iii1I1I
  self . addon_noti ( __language__ ( 30909 ) . encode ( 'utf-8' ) )
  if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - I11i
  if 30 - 30: OoOoOO00
  if 21 - 21: i11iIiiIii / O0oo0OO0 % OOooOOo * O0 . I11i - iIii1I11I1II1
  if 26 - 26: II111iiii * OoOoOO00
 def wininfo_clear ( self ) :
  if 10 - 10: II111iiii . iii1I1I
  II111ii1II1i = xbmcgui . Window ( 10000 )
  II111ii1II1i . setProperty ( 'WATCHA_M_TOKEN' , '' )
  II111ii1II1i . setProperty ( 'WATCHA_M_GUIT' , '' )
  II111ii1II1i . setProperty ( 'WATCHA_M_GUITV' , '' )
  II111ii1II1i . setProperty ( 'WATCHA_M_USERCD' , '' )
  II111ii1II1i . setProperty ( 'WATCHA_M_LOGINTIME' , '' )
  if 32 - 32: Ii1I . O00oOoOoO0o0O . OoooooooOO - OoO0O00 + oO0o
  if 88 - 88: iii1I1I
  if 19 - 19: II111iiii * O00oOoOoO0o0O + Ii1I
  if 65 - 65: OOooOOo . O0oo0OO0 . OoO0O00 . iii1I1I - OOooOOo
 def cookiefile_save ( self ) :
  ii111i = datetime . datetime . now ( )
  oooo00 = ii111i + datetime . timedelta ( days = int ( __addon__ . getSetting ( 'cache_ttl' ) ) )
  if 77 - 77: Oo0ooO0oo0oO - I1IiiI % I11i - O0
  II111ii1II1i = xbmcgui . Window ( 10000 )
  o0O0O0 = { 'watcha_token' : II111ii1II1i . getProperty ( 'WATCHA_M_TOKEN' )
 , 'watcha_guit' : II111ii1II1i . getProperty ( 'WATCHA_M_GUIT' )
 , 'watcha_guitv' : II111ii1II1i . getProperty ( 'WATCHA_M_GUITV' )
 , 'watcha_usercd' : II111ii1II1i . getProperty ( 'WATCHA_M_USERCD' )
 , 'watcha_id' : base64 . standard_b64encode ( __addon__ . getSetting ( 'id' ) . encode ( ) ) . decode ( 'utf-8' )
 , 'watcha_pw' : base64 . standard_b64encode ( __addon__ . getSetting ( 'pw' ) . encode ( ) ) . decode ( 'utf-8' )
 , 'watcha_profile' : __addon__ . getSetting ( 'selected_profile' )
 , 'watcha_limitdate' : oooo00 . strftime ( '%Y-%m-%d' )
 }
  if 6 - 6: iii1I1I . O00oOoOoO0o0O * OoOoOO00 . i1IIi
  try :
   with open ( i11 , 'w' ) as Oo00OoOo :
    json . dump ( o0O0O0 , Oo00OoOo )
  except Exception as oOOo :
   print ( oOOo )
   if 46 - 46: O00oOoOoO0o0O + iIii1I11I1II1 + OOooOOo + OoO0O00 . I1ii11iIi11i
   if 1 - 1: oO0o
   if 62 - 62: i1IIi - OOooOOo
   if 96 - 96: i1IIi . I1ii11iIi11i + oO0o
 def cookiefile_check ( self ) :
  if 48 - 48: iIii1I11I1II1 % i1IIi % iii1I1I + Oo0ooO0oo0oO
  if 30 - 30: i11iIiiIii % iIii1I11I1II1 . I11i % iIii1I11I1II1
  o0O0O0 = { }
  try :
   with open ( i11 , 'r' ) as Oo00OoOo :
    o0O0O0 = json . load ( Oo00OoOo )
  except Exception as oOOo :
   self . wininfo_clear ( )
   return False
   if 62 - 62: Oo0Ooo * OoOoOO00
   if 79 - 79: OoO0O00 . iii1I1I * Ii1I - OOooOOo + Oo0ooO0oo0oO
   if 14 - 14: i11iIiiIii - iii1I1I * OoOoOO00
  oO = __addon__ . getSetting ( 'id' )
  iIi1IIIi1 = __addon__ . getSetting ( 'pw' )
  OO0o = __addon__ . getSetting ( 'selected_profile' )
  o0O0O0 [ 'watcha_id' ] = base64 . standard_b64decode ( o0O0O0 [ 'watcha_id' ] ) . decode ( 'utf-8' )
  o0O0O0 [ 'watcha_pw' ] = base64 . standard_b64decode ( o0O0O0 [ 'watcha_pw' ] ) . decode ( 'utf-8' )
  if oO != o0O0O0 [ 'watcha_id' ] or iIi1IIIi1 != o0O0O0 [ 'watcha_pw' ] or OO0o != o0O0O0 [ 'watcha_profile' ] :
   self . wininfo_clear ( )
   return False
   if 39 - 39: o0oOOo0O0Ooo * Oo0ooO0oo0oO + Ii1I * II111iiii
   if 97 - 97: iIii1I11I1II1 + I11i + II111iiii % O00oOoOoO0o0O % O0oo0OO0 % oO0o
  ooOOoooooo = datetime . datetime . now ( ) . date ( )
  II11I = o0O0O0 [ 'watcha_limitdate' ]
  try :
   II1I = datetime . datetime . strptime ( II11I , '%Y-%m-%d' ) . date ( )
  except TypeError :
   II1I = datetime . datetime ( * ( time . strptime ( II11I , '%Y-%m-%d' ) [ 0 : 6 ] ) ) . date ( )
   if 96 - 96: I1IiiI % Oo0Ooo . I1ii11iIi11i + OOooOOo
  if II1I < ooOOoooooo :
   self . wininfo_clear ( )
   return False
   if 42 - 42: II111iiii * iii1I1I * i11iIiiIii - OOooOOo . OoooooooOO
   if 76 - 76: II111iiii
  II111ii1II1i = xbmcgui . Window ( 10000 )
  II111ii1II1i . setProperty ( 'WATCHA_M_TOKEN' , o0O0O0 [ 'watcha_token' ] )
  II111ii1II1i . setProperty ( 'WATCHA_M_GUIT' , o0O0O0 [ 'watcha_guit' ] )
  II111ii1II1i . setProperty ( 'WATCHA_M_GUITV' , o0O0O0 [ 'watcha_guitv' ] )
  II111ii1II1i . setProperty ( 'WATCHA_M_USERCD' , o0O0O0 [ 'watcha_usercd' ] )
  II111ii1II1i . setProperty ( 'WATCHA_M_LOGINTIME' , II11I )
  if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
  return True
  if 24 - 24: II111iiii % O0oo0OO0 - Oo0ooO0oo0oO + I1IiiI * I1ii11iIi11i
  if 2 - 2: Ii1I - O00oOoOoO0o0O
  if 83 - 83: oO0o % o0oOOo0O0Ooo % Ii1I - II111iiii * OOooOOo / OoooooooOO
  if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
  if 71 - 71: OoooooooOO
 def watcha_main ( self ) :
  iIIIII1iiiiII = self . main_params . get ( 'mode' , None )
  if 54 - 54: i1IIi
  self . login_main ( )
  if 22 - 22: i1IIi + Ii1I
  if iIIIII1iiiiII is None :
   self . dp_Main_List ( )
   if 54 - 54: Oo0ooO0oo0oO % OOooOOo . O0oo0OO0 + oO0o - OOooOOo * I1IiiI
  elif iIIIII1iiiiII == 'SUB_GROUP' :
   self . dp_SubGroup_List ( self . main_params )
   if 92 - 92: o0oOOo0O0Ooo + O0oo0OO0 / Oo0Ooo % OoO0O00 % O00oOoOoO0o0O . OoooooooOO
  elif iIIIII1iiiiII == 'CATEGORY_LIST' :
   self . dp_Category_List ( self . main_params )
   if 52 - 52: Oo0ooO0oo0oO / i11iIiiIii - OOooOOo . O00oOoOoO0o0O % iIii1I11I1II1 + o0oOOo0O0Ooo
  elif iIIIII1iiiiII == 'EPISODE' :
   self . dp_Episode_List ( self . main_params )
   if 71 - 71: oO0o % I11i * OoOoOO00 . O0 / Ii1I . I1ii11iIi11i
  elif iIIIII1iiiiII == 'ORDER_BY' :
   self . dp_setEpOrderby ( self . main_params )
   if 58 - 58: Oo0Ooo / oO0o
  elif iIIIII1iiiiII == 'SEARCH' :
   self . dp_Search_List ( self . main_params )
   if 44 - 44: OOooOOo
  elif iIIIII1iiiiII == 'MOVIE' :
   self . play_VIDEO ( self . main_params )
   if 54 - 54: Ii1I - I11i - O0oo0OO0 . iIii1I11I1II1
   time . sleep ( 0.1 )
   if 79 - 79: Ii1I . OoO0O00
  elif iIIIII1iiiiII == 'WATCH' :
   self . dp_Watch_List ( self . main_params )
   if 40 - 40: o0oOOo0O0Ooo + Oo0Ooo . o0oOOo0O0Ooo % Oo0ooO0oo0oO
  elif iIIIII1iiiiII == 'MYVIEW_REMOVE' :
   self . dp_WatchList_Delete ( self . main_params )
   if 15 - 15: Ii1I * Oo0Ooo % I1ii11iIi11i * iIii1I11I1II1 - i11iIiiIii
  elif iIIIII1iiiiII == 'LOGOUT' :
   self . logout ( )
   if 60 - 60: I1IiiI * O0oo0OO0 % OoO0O00 + oO0o
   if 52 - 52: i1IIi
   if 84 - 84: Ii1I / O00oOoOoO0o0O
   if 86 - 86: OoOoOO00 * II111iiii - O0 . OoOoOO00 % iIii1I11I1II1 / OOooOOo
   if 11 - 11: I1IiiI * oO0o + I1ii11iIi11i / I1ii11iIi11i
   if 37 - 37: i11iIiiIii + i1IIi
  else :
   None
   if 23 - 23: iii1I1I + I11i . OoOoOO00 * I1IiiI + I1ii11iIi11i
   if 18 - 18: O00oOoOoO0o0O * o0oOOo0O0Ooo . O00oOoOoO0o0O / O0
   if 8 - 8: o0oOOo0O0Ooo
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
