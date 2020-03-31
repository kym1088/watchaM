# -*- coding: utf-8 -*-
__author__ = "NightRain"
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
import os
import xbmcplugin , xbmcgui , xbmcaddon
import sys
import urlparse
import inputstreamhelper
import datetime
if 46 - 46: ooOoO0o * I11i - OoooooooOO
if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO
reload ( sys )
sys . setdefaultencoding ( 'utf-8' )
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
__addon__ = xbmcaddon . Addon ( )
__language__ = __addon__ . getLocalizedString
__profile__ = xbmc . translatePath ( __addon__ . getAddonInfo ( 'profile' ) )
__version__ = __addon__ . getAddonInfo ( 'version' )
__addonid__ = __addon__ . getAddonInfo ( 'id' )
__addonname__ = __addon__ . getAddonInfo ( 'name' )
__cwd__ = xbmc . translatePath ( __addon__ . getAddonInfo ( 'path' ) )
__lib__ = os . path . join ( __cwd__ , 'resources' , 'lib' )
__data__ = os . path . join ( __cwd__ , 'resources' , 'data' )
sys . path . append ( __lib__ )
sys . path . append ( __data__ )
if 94 - 94: i1IIi % Oo0Ooo
o0oO0 = [
 { 'title' : '왓플 최고 인기작' , 'mode' : 'CATEGORY_LIST' , 'stype' : '-' , 'api_path' : 'staffmades/409' }
 , { 'title' : '최고 인기 시리즈' , 'mode' : 'CATEGORY_LIST' , 'stype' : '-' , 'api_path' : 'staffmades/410' }
 , { 'title' : '새로 올라온 작품' , 'mode' : 'CATEGORY_LIST' , 'stype' : '-' , 'api_path' : 'arrivals/latest' }
 , { 'title' : '이어보기' , 'mode' : 'CATEGORY_LIST' , 'stype' : '-' , 'api_path' : 'users/me/watchings' }
 , { 'title' : '장르별 분류 (추천순)' , 'mode' : 'SUB_GROUP' , 'stype' : 'genres' , 'api_path' : '-' }
 , { 'title' : '특징별 분류 (추천순)' , 'mode' : 'SUB_GROUP' , 'stype' : 'tags' , 'api_path' : '-' }
 , { 'title' : '-----------------' , 'mode' : 'XXX' , 'stype' : 'XXX' , 'api_path' : '-' }
 , { 'title' : '검색 (search)' , 'mode' : 'SEARCH' , 'stype' : '-' , 'api_path' : '-' }
 , { 'title' : 'Watched (시청목록)' , 'mode' : 'WATCH' , 'stype' : '-' , 'api_path' : '-' }
 ]
if 100 - 100: i1IIi
I1Ii11I1Ii1i = [
 { 'title' : '영화 시청내역' , 'mode' : 'WATCH' , 'stype' : 'movie' }
 , { 'title' : '시리즈 시청내역' , 'mode' : 'WATCH' , 'stype' : 'seasons' }
 ]
if 67 - 67: iIii1I11I1II1 . I1ii11iIi11i . oO0o / i1IIi % II111iiii - OoOoOO00
OOo = 40
Ii1IIii11 = 20
if 55 - 55: iIii1I11I1II1 - I1IiiI . Ii1I * IiII * i1IIi / iIii1I11I1II1
OOo000 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
if 82 - 82: I11i . I1Ii111 / IiII % II111iiii % iIii1I11I1II1 % IiII
oOo0oooo00o = xbmc . translatePath ( os . path . join ( __profile__ , 'temp_subtitles.vtt' ) )
if 65 - 65: o0oOOo0O0Ooo * iIii1I11I1II1 * ooOoO0o
from watchaCore import *
if 18 - 18: iIii1I11I1II1 / I11i + oO0o / Oo0Ooo - II111iiii - I11i
if 1 - 1: I11i - OOooOOo % O0 + I1IiiI - iII111i / I11i
if 31 - 31: OoO0O00 + II111iiii
if 13 - 13: OOooOOo * oO0o * I1IiiI
def oOOOO ( sting ) :
 try :
  i11iiII = xbmcgui . Dialog ( )
  if 34 - 34: OOooOOo % OoooooooOO / i1IIi . iII111i + O0
  i11iiII . notification ( __addonname__ , sting )
 except :
  None
  if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
  if 78 - 78: OoO0O00
  if 18 - 18: O0 - iII111i / iII111i + ooOoO0o % ooOoO0o - IiII
def O0O00Ooo ( string , isDebug = False ) :
 try :
  OOoooooO = string . encode ( 'utf-8' , 'ignore' )
 except :
  OOoooooO = 'addonException: addon_log'
 if isDebug : i1iIIIiI1I = xbmc . LOGDEBUG
 else : i1iIIIiI1I = xbmc . LOGNOTICE
 xbmc . log ( "[%s-%s]: %s" % ( __addonid__ , __version__ , OOoooooO ) , level = i1iIIIiI1I )
 if 70 - 70: Oo0Ooo % Oo0Ooo . IiII % OoO0O00 * o0oOOo0O0Ooo % oO0o
 if 23 - 23: i11iIiiIii + I1IiiI
 if 68 - 68: OoOoOO00 . oO0o . i11iIiiIii
 if 40 - 40: oO0o . OoOoOO00 . Oo0Ooo . i1IIi
def I11iii ( title ) :
 OO0O00 = None
 ii1 = xbmc . Keyboard ( )
 ii1 . setHeading ( title )
 xbmc . sleep ( 1000 )
 ii1 . doModal ( )
 if ( ii1 . isConfirmed ( ) ) :
  OO0O00 = ii1 . getText ( )
 return OO0O00
 if 57 - 57: Ii1I % OoooooooOO
 if 61 - 61: iII111i . iIii1I11I1II1 * I1IiiI . ooOoO0o % Oo0Ooo
 if 72 - 72: OOooOOo
 if 63 - 63: Ii1I
def O00 ( ) :
 iII11i = __addon__ . getSetting ( 'id' )
 O0O00o0OOO0 = __addon__ . getSetting ( 'pw' )
 Ii1iIIIi1ii = int ( __addon__ . getSetting ( 'selected_profile' ) )
 return ( iII11i , O0O00o0OOO0 , Ii1iIIIi1ii )
 if 80 - 80: I11i * i11iIiiIii / I1Ii111
 if 9 - 9: Ii1I + oO0o % Ii1I + i1IIi . OOooOOo
 if 31 - 31: o0oOOo0O0Ooo + I11i + I11i / II111iiii
 if 26 - 26: OoooooooOO
def IiiI11Iiiii ( ) :
 try :
  ii1I1i1I = [ '4096x2160/1' , '1920x1080/1' , '1280x720/1' ]
  if 88 - 88: OoO0O00 + O0 / OoOoOO00 * iII111i
  iiiIi1i1I = int ( __addon__ . getSetting ( 'selected_quality' ) )
  return ii1I1i1I [ iiiIi1i1I ]
 except :
  None
  if 80 - 80: OoOoOO00 - OoO0O00
 return 1080
 if 87 - 87: oO0o / I11i - i1IIi * OOooOOo / OoooooooOO . O0
 if 1 - 1: II111iiii - I11i / I11i
 if 46 - 46: Ii1I * OOooOOo - OoO0O00 * oO0o - I1Ii111
 if 83 - 83: OoooooooOO
def Iii111II ( credential ) :
 iiii11I = xbmcgui . Window ( 10000 )
 iiii11I . setProperty ( 'WATCHA_M_TOKEN' , credential . get ( 'watcha_token' ) )
 iiii11I . setProperty ( 'WATCHA_M_GUIT' , credential . get ( 'watcha_guit' ) )
 iiii11I . setProperty ( 'WATCHA_M_GUITV' , credential . get ( 'watcha_guitv' ) )
 iiii11I . setProperty ( 'WATCHA_M_USERCD' , credential . get ( 'watcha_usercd' ) )
 iiii11I . setProperty ( 'WATCHA_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) )
 if 96 - 96: II111iiii % Ii1I . OOooOOo + OoooooooOO * oO0o - OoOoOO00
 if 10 - 10: OOooOOo / I1IiiI * OOooOOo
def IIIii1II1II ( ) :
 iiii11I = xbmcgui . Window ( 10000 )
 i1I1iI = {
 'watcha_token' : iiii11I . getProperty ( 'WATCHA_M_TOKEN' )
 , 'watcha_guit' : iiii11I . getProperty ( 'WATCHA_M_GUIT' )
 , 'watcha_guitv' : iiii11I . getProperty ( 'WATCHA_M_GUITV' )
 , 'watcha_usercd' : iiii11I . getProperty ( 'WATCHA_M_USERCD' )
 }
 return i1I1iI
 if 93 - 93: iIii1I11I1II1 % oO0o * i1IIi
def Ii11Ii1I ( orderby ) :
 iiii11I = xbmcgui . Window ( 10000 )
 iiii11I . setProperty ( 'WATCHA_M_ORDERBY' , orderby )
 if 72 - 72: iII111i / i1IIi * Oo0Ooo - I1Ii111
def Oo0O0O0ooO0O ( ) :
 iiii11I = xbmcgui . Window ( 10000 )
 return iiii11I . getProperty ( 'WATCHA_M_ORDERBY' )
 if 15 - 15: I1ii11iIi11i + OoOoOO00 - OoooooooOO / OOooOOo
 if 58 - 58: i11iIiiIii % I11i
 if 71 - 71: OOooOOo + ooOoO0o % i11iIiiIii + I1ii11iIi11i - IiII
def oO0OOoO0 ( args ) :
 I111Ii111 = args . get ( 'orderby' )
 if 4 - 4: oO0o
 Ii11Ii1I ( I111Ii111 )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 93 - 93: OoO0O00 % oO0o . OoO0O00 * I1Ii111 % Ii1I . II111iiii
 if 38 - 38: o0oOOo0O0Ooo
 if 57 - 57: O0 / oO0o * I1Ii111 / OoOoOO00 . II111iiii
def i11iIIIIIi1 ( ) :
 iiII1i1 = urlparse . parse_qs ( sys . argv [ 2 ] [ 1 : ] )
 for o00oOO0o in iiII1i1 . keys ( ) :
  iiII1i1 [ o00oOO0o ] = iiII1i1 [ o00oOO0o ] [ 0 ]
 return iiII1i1
 if 80 - 80: oO0o + OOooOOo - OOooOOo % iII111i
 if 63 - 63: I1IiiI - I1ii11iIi11i + O0 % I11i / iIii1I11I1II1 / o0oOOo0O0Ooo
 if 98 - 98: iII111i * iII111i / iII111i + I11i
def ii111111I1iII ( label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
 O00ooo0O0 = '%s?%s' % ( sys . argv [ 0 ] , urllib . urlencode ( params ) )
 if 23 - 23: iII111i
 if sublabel : oo0oOo = '%s < %s >' % ( label , sublabel )
 else : oo0oOo = label
 if not img : img = 'DefaultFolder.png'
 if 89 - 89: OoOoOO00
 OO0oOoOO0oOO0 = xbmcgui . ListItem ( oo0oOo , thumbnailImage = img )
 if infoLabels : OO0oOoOO0oOO0 . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder : OO0oOoOO0oOO0 . setProperty ( 'IsPlayable' , 'true' )
 if 86 - 86: OOooOOo
 xbmcplugin . addDirectoryItem ( OOoo0O , O00ooo0O0 , OO0oOoOO0oOO0 , isFolder )
 if 67 - 67: i11iIiiIii - i1IIi % I1ii11iIi11i . O0
 if 77 - 77: IiII / I1IiiI
 if 15 - 15: IiII . iIii1I11I1II1 . OoooooooOO / i11iIiiIii - Ii1I . i1IIi
 if 33 - 33: I11i . o0oOOo0O0Ooo
 if 75 - 75: o0oOOo0O0Ooo % o0oOOo0O0Ooo . I1Ii111
def III1iII1I1ii ( ) :
 if 61 - 61: II111iiii
 for O0OOO in o0oO0 :
  oo0oOo = O0OOO . get ( 'title' )
  if 10 - 10: OOooOOo * I11i % OoOoOO00 / I1IiiI / OoOoOO00
  iIIi1i1 = { 'mode' : O0OOO . get ( 'mode' )
 , 'stype' : O0OOO . get ( 'stype' )
 , 'api_path' : O0OOO . get ( 'api_path' )
 , 'page' : '1'
 }
  if 10 - 10: I11i
  if O0OOO . get ( 'mode' ) == 'XXX' :
   iIIi1i1 [ 'mode' ] = 'XXX'
   OOooOO000 = False
  else :
   OOooOO000 = True
   if 97 - 97: I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
  ii111111I1iII ( oo0oOo , sublabel = '' , img = '' , infoLabels = None , isFolder = OOooOO000 , params = iIIi1i1 )
 if len ( o0oO0 ) > 0 : xbmcplugin . endOfDirectory ( OOoo0O )
 if 37 - 37: iII111i - ooOoO0o * oO0o % i11iIiiIii - I1Ii111
 if 83 - 83: I11i / I1IiiI
 if 34 - 34: IiII
 if 57 - 57: oO0o . I11i . i1IIi
def i11Iii ( ) :
 ( IiIIIi1iIi , ooOOoooooo , II1I ) = O00 ( )
 if 84 - 84: IiII . i11iIiiIii . IiII * I1ii11iIi11i - I11i
 if 42 - 42: i11iIiiIii
 if not ( IiIIIi1iIi and ooOOoooooo ) :
  i11iiII = xbmcgui . Dialog ( )
  I11i1iIII = i11iiII . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
  if I11i1iIII == True :
   __addon__ . openSettings ( )
   sys . exit ( )
   if 32 - 32: OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
   if 91 - 91: iII111i % i1IIi % iIii1I11I1II1
 if xbmcgui . Window ( 10000 ) . getProperty ( 'WATCHA_M_LOGINWAIT' ) == 'TRUE' :
  IIi1I11I1II = 0
  while True :
   IIi1I11I1II += 1
   xbmc . sleep ( 250 )
   if xbmcgui . Window ( 10000 ) . getProperty ( 'WATCHA_M_LOGINWAIT' ) == 'FALSE' or IIi1I11I1II > 500 :
    break
    if 63 - 63: OoooooooOO - OoO0O00 . II111iiii / o0oOOo0O0Ooo . OoOoOO00 / O0
 o0OOOO00O0Oo = xbmcgui . Window ( 10000 ) . getProperty ( 'WATCHA_M_LOGINTIME' )
 if 48 - 48: O0
 if o0OOOO00O0Oo != '' :
  if o0OOOO00O0Oo == datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) :
   return
   if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
 xbmcgui . Window ( 10000 ) . setProperty ( 'WATCHA_M_LOGINWAIT' , 'TRUE' )
 if 41 - 41: Ii1I - O0 - O0
 if 68 - 68: OOooOOo % I1Ii111
 if not ooO00OO0 . GetCredential ( IiIIIi1iIi , ooOOoooooo , II1I ) :
  oOOOO ( __language__ ( 30103 ) . encode ( 'utf8' ) )
  xbmcgui . Window ( 10000 ) . setProperty ( 'WATCHA_M_LOGINWAIT' , 'FALSE' )
  sys . exit ( )
  if 31 - 31: iII111i % iII111i % I11i
  if 69 - 69: OoO0O00 - Oo0Ooo + i1IIi / I1Ii111
 Iii111II ( ooO00OO0 . LoadCredential ( ) )
 Ii11Ii1I ( 'asc' )
 xbmcgui . Window ( 10000 ) . setProperty ( 'WATCHA_M_LOGINWAIT' , 'FALSE' )
 if 49 - 49: O0 . iII111i
 if 11 - 11: IiII * I1IiiI . iIii1I11I1II1 % OoooooooOO + iII111i
 if 78 - 78: OoO0O00 . OOooOOo + OoO0O00 / I11i / OoO0O00
 if 54 - 54: OoOoOO00 % iII111i
 if 37 - 37: OoOoOO00 * Oo0Ooo / ooOoO0o - iII111i % II111iiii . oO0o
def O00I1iI1 ( args ) :
 if 23 - 23: i11iIiiIii + o0oOOo0O0Ooo . i1IIi
 ooO00OO0 . SaveCredential ( IIIii1II1II ( ) )
 if 100 - 100: I1Ii111 . oO0o * Ii1I
 i1i1Iiii1I1 = args . get ( 'stype' )
 oooO0 = int ( args . get ( 'page' ) )
 if 46 - 46: I1Ii111
 oooOOoOO = ooO00OO0 . GetSubGroupList ( i1i1Iiii1I1 )
 if 9 - 9: o0oOOo0O0Ooo . ooOoO0o - Oo0Ooo - oO0o + II111iiii * i11iIiiIii
 if 79 - 79: oO0o % I11i % I1IiiI
 if 5 - 5: OoooooooOO % OoOoOO00 % oO0o % iII111i
 if 7 - 7: II111iiii + OoooooooOO . I1Ii111 . ooOoO0o - o0oOOo0O0Ooo
 if 26 - 26: Oo0Ooo / IiII % iIii1I11I1II1 / IiII + I11i
 if 90 - 90: OoOoOO00 * I1Ii111 + o0oOOo0O0Ooo
 if 81 - 81: oO0o . o0oOOo0O0Ooo % O0 / I1IiiI - oO0o
 if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * I1Ii111 * O0
 if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
 if 79 - 79: O0
 if 78 - 78: I1ii11iIi11i + OOooOOo - I1Ii111
 if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
 if 57 - 57: OoO0O00 / ooOoO0o
 if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
 if 7 - 7: IiII * I1Ii111 % Ii1I - o0oOOo0O0Ooo
 if 13 - 13: Ii1I . i11iIiiIii
 if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
 O00o0OO0 = OOo if i1i1Iiii1I1 == 'genres' else Ii1IIii11
 if 35 - 35: oO0o % ooOoO0o / I1Ii111 + iIii1I11I1II1 . OoooooooOO . I1IiiI
 o00oOOooOOo0o = len ( oooOOoOO )
 O0O0ooOOO = int ( o00oOOooOOo0o // ( O00o0OO0 + 1 ) ) + 1
 oOOo0O00o = ( oooO0 - 1 ) * O00o0OO0
 if 8 - 8: OoO0O00
 for o00oOO0o in range ( O00o0OO0 ) :
  ii1111iII = oOOo0O00o + o00oOO0o
  if ii1111iII >= o00oOOooOOo0o : break
  if 32 - 32: i1IIi / II111iiii . Oo0Ooo
  oo0oOo = oooOOoOO [ ii1111iII ] . get ( 'group_name' )
  oooOo0OOOoo0 = oooOOoOO [ ii1111iII ] . get ( 'api_path' )
  OOoO = oooOOoOO [ ii1111iII ] . get ( 'tag_id' )
  if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
  iIIi1i1 = { 'mode' : 'CATEGORY_LIST'
 , 'api_path' : oooOo0OOOoo0
 , 'tag_id' : OOoO
 , 'stype' : i1i1Iiii1I1
 , 'page' : '1'
 }
  if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
  ii111111I1iII ( oo0oOo , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if 77 - 77: OOooOOo * iIii1I11I1II1
 if O0O0ooOOO > oooO0 :
  iIIi1i1 = { }
  iIIi1i1 [ 'mode' ] = 'SUB_GROUP'
  iIIi1i1 [ 'stype' ] = i1i1Iiii1I1
  iIIi1i1 [ 'api_path' ] = args . get ( 'api_path' )
  iIIi1i1 [ 'page' ] = str ( oooO0 + 1 )
  oo0oOo = '[B]%s >>[/B]' % '다음 페이지'
  oO00oOOoooO = str ( oooO0 + 1 )
  ii111111I1iII ( oo0oOo , sublabel = oO00oOOoooO , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if 46 - 46: I1IiiI - OoooooooOO - I11i * II111iiii
  if 34 - 34: I11i - iII111i / OOooOOo + I1ii11iIi11i * Ii1I
 if len ( oooOOoOO ) > 0 : xbmcplugin . endOfDirectory ( OOoo0O , cacheToDisc = True )
 if 73 - 73: OoOoOO00 . Ii1I * I1ii11iIi11i % I1ii11iIi11i % OoooooooOO
 if 63 - 63: iIii1I11I1II1 * i11iIiiIii % iIii1I11I1II1 * i11iIiiIii
 if 32 - 32: OOooOOo
 if 42 - 42: IiII * O0 % i1IIi . OOooOOo / o0oOOo0O0Ooo
def iII11I1IiiIi ( args ) :
 if 98 - 98: i1IIi / I11i
 ooO00OO0 . SaveCredential ( IIIii1II1II ( ) )
 if 32 - 32: Ii1I * iIii1I11I1II1 / OOooOOo
 if 38 - 38: ooOoO0o % II111iiii % I11i / OoO0O00 + OoOoOO00 / i1IIi
 if 54 - 54: iIii1I11I1II1 % I1ii11iIi11i - OOooOOo / oO0o - OoO0O00 . I11i
 if 11 - 11: I1ii11iIi11i . OoO0O00 * IiII * OoooooooOO + ooOoO0o
 if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
 if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
 if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
 if 26 - 26: Ii1I % I1ii11iIi11i
 o00Oo0oooooo = args . get ( 'movie_code' )
 O0oO0 = args . get ( 'season_code' )
 oo0oOo = args . get ( 'title' )
 iII11 = args . get ( 'thumbnail' )
 iiIiii1IIIII = IiiI11Iiiii ( )
 if 67 - 67: Ii1I / IiII
 if 9 - 9: O0 % O0 - o0oOOo0O0Ooo
 O0O00Ooo ( o00Oo0oooooo + ' - ' + O0oO0 , False )
 OoO , iiI1IIIi , II11IiIi11 = ooO00OO0 . GetStreamingURL ( o00Oo0oooooo , iiIiii1IIIII )
 if 7 - 7: OoO0O00 . Ii1I % oO0o * ooOoO0o + IiII + I1Ii111
 if 38 - 38: o0oOOo0O0Ooo - I1IiiI - o0oOOo0O0Ooo / I11i - i1IIi
 if OoO == '' :
  oOOOO ( __language__ ( 30302 ) . encode ( 'utf8' ) )
  return
  if 1 - 1: II111iiii
  if 68 - 68: iII111i - I1IiiI / I1Ii111 / I11i
  if 12 - 12: Ii1I + i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . I11i
  if 5 - 5: i1IIi + IiII / o0oOOo0O0Ooo . iII111i / I11i
 IiiiIiii11 = OoO
 O0O00Ooo ( IiiiIiii11 , False )
 if 92 - 92: OoOoOO00 + I1Ii111 * Ii1I % I1IiiI
 if 42 - 42: Oo0Ooo
 oo000O0OoooO = xbmcgui . ListItem ( path = IiiiIiii11 )
 if 93 - 93: I11i . II111iiii / oO0o % OoooooooOO * I11i % I1ii11iIi11i
 if II11IiIi11 :
  I1i11 = II11IiIi11
  IiIi1I1 = 'https://lic.drmtoday.com/license-proxy-widevine/cenc/?specConform=true'
  IiIIi1 = 'mpd'
  IIIIiii1IIii = 'com.widevine.alpha'
  if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
  oOOoo0000O0o0 = inputstreamhelper . Helper ( IiIIi1 , drm = IIIIiii1IIii )
  if 1 - 1: oO0o + oO0o % OoOoOO00 + i11iIiiIii
  if oOOoo0000O0o0 . check_inputstream ( ) :
   if 56 - 56: o0oOOo0O0Ooo
   I1 = { 'Host' : 'lic.drmtoday.com'
 , 'origin' : 'https://play.watcha.net'
 , 'referer' : 'https://play.watcha.net/watch/' + o00Oo0oooooo
 , 'dt-custom-data' : I1i11
 , 'Sec-Fetch-Dest' : 'empty'
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'cross-site'
 , 'user-agent' : OOo000
 , 'Content-Type' : 'application/octet-stream'
 }
   OooooO0oOOOO = IiIi1I1 + '|' + urllib . urlencode ( I1 ) + '|R{SSM}|'
   if 100 - 100: iII111i % OOooOOo
   O0O00Ooo ( OooooO0oOOOO )
   if 86 - 86: Oo0Ooo . O0 - OoooooooOO . OoO0O00 + Ii1I
   oo000O0OoooO . setProperty ( 'inputstreamaddon' , oOOoo0000O0o0 . inputstream_addon )
   oo000O0OoooO . setProperty ( 'inputstream.adaptive.manifest_type' , IiIIi1 )
   oo000O0OoooO . setProperty ( 'inputstream.adaptive.license_type' , IIIIiii1IIii )
   oo000O0OoooO . setProperty ( 'inputstream.adaptive.license_key' , OooooO0oOOOO )
   if 57 - 57: o0oOOo0O0Ooo . i1IIi . IiII * i11iIiiIii + I1Ii111 . IiII
   if 57 - 57: I1Ii111
   if 32 - 32: Ii1I - Oo0Ooo % OoooooooOO . iII111i / IiII + I1IiiI
   if 76 - 76: ooOoO0o
   if 73 - 73: O0 * iII111i + Ii1I + ooOoO0o
 if iiI1IIIi :
  oo000O0OoooO . setSubtitles ( [ iiI1IIIi ] )
  if 40 - 40: II111iiii . OoOoOO00 * I1Ii111 + OOooOOo + OOooOOo
  if 9 - 9: I11i % OoooooooOO . oO0o % I11i
  if 32 - 32: i11iIiiIii
  if 31 - 31: iIii1I11I1II1 / OoO0O00 / I1ii11iIi11i
  if 41 - 41: Oo0Ooo
  if 10 - 10: Oo0Ooo / Oo0Ooo / I1Ii111 . I1Ii111
  if 98 - 98: Oo0Ooo / I1IiiI . O0 + OoO0O00
  if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
  if 20 - 20: I1IiiI
  if 95 - 95: iII111i - I1IiiI
  if 34 - 34: ooOoO0o * I1IiiI . i1IIi * ooOoO0o / ooOoO0o
  if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
  if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
 xbmcplugin . setResolvedUrl ( OOoo0O , True , oo000O0OoooO )
 if 41 - 41: i1IIi - I11i - Ii1I
 if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
 if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + ooOoO0o
 i1i1Iiii1I1 = 'movie' if O0oO0 == '-' else 'seasons'
 iIIi1i1 = { 'code' : o00Oo0oooooo if i1i1Iiii1I1 == 'movie' else O0oO0
 , 'img' : iII11
 , 'title' : oo0oOo
 }
 iIIII ( i1i1Iiii1I1 , iIIi1i1 )
 if 45 - 45: I1ii11iIi11i % I1IiiI - i11iIiiIii
 if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * I1IiiI
 if 46 - 46: OoOoOO00 + OoO0O00
 if 70 - 70: iII111i / iIii1I11I1II1
 if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / I1ii11iIi11i
def ooOOoO ( args ) :
 if 20 - 20: I11i + Ii1I / O0 % iIii1I11I1II1
 ooO00OO0 . SaveCredential ( IIIii1II1II ( ) )
 if 88 - 88: OoOoOO00 / II111iiii
 i1i1Iiii1I1 = args . get ( 'stype' )
 OOoO = args . get ( 'tag_id' )
 oooOo0OOOoo0 = args . get ( 'api_path' )
 oooO0 = int ( args . get ( 'page' ) )
 if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - iII111i + oO0o
 OOooo , iIIiIiI1I1 = ooO00OO0 . GetCategoryList ( i1i1Iiii1I1 , OOoO , oooOo0OOOoo0 , oooO0 )
 if 56 - 56: I1IiiI . O0 + Oo0Ooo
 if 1 - 1: iII111i
 for O0O0Ooo in OOooo :
  o00Oo0oooooo = O0O0Ooo . get ( 'code' )
  oo0oOo = O0O0Ooo . get ( 'title' )
  oOoO0 = O0O0Ooo . get ( 'content_type' )
  Oo0 = O0O0Ooo . get ( 'story' )
  iII11 = O0O0Ooo . get ( 'thumbnail' )
  oo0O0o00o0O = O0O0Ooo . get ( 'year' )
  I11i1II = O0O0Ooo . get ( 'film_rating_code' )
  Ooo = O0O0Ooo . get ( 'film_rating_short' )
  if 21 - 21: Oo0Ooo
  if oOoO0 == 'movies' :
   OOooOO000 = False
   I1ii1 = 'MOVIE'
   O00Oo0o0000OOoO = ''
   O0oO0 = '-'
  else :
   OOooOO000 = True
   I1ii1 = 'EPISODE'
   O00Oo0o0000OOoO = 'Series'
   O0oO0 = o00Oo0oooooo
   if 46 - 46: O0 * II111iiii - Oo0Ooo * ooOoO0o
  i11IIIiIiIi = { }
  i11IIIiIiIi [ 'plot' ] = '%s (%s)\n년도 : %s\n\n%s' % ( oo0oOo , Ooo , oo0O0o00o0O , Oo0 )
  if 27 - 27: I1ii11iIi11i + OoOoOO00 - OOooOOo + O0 . Ii1I
  if I11i1II >= 19 :
   oo0oOo += '  (%s년 - %s)' % ( oo0O0o00o0O , str ( Ooo ) )
  else :
   oo0oOo += '  (%s년)' % ( oo0O0o00o0O )
   if 46 - 46: IiII
   if 45 - 45: ooOoO0o
  iIIi1i1 = { 'mode' : I1ii1
 , 'movie_code' : o00Oo0oooooo
 , 'page' : '1'
 , 'season_code' : O0oO0
  , 'title' : oo0oOo
 , 'thumbnail' : iII11
 }
  if 21 - 21: oO0o . I1Ii111 . OOooOOo / Oo0Ooo / I1Ii111
  ii111111I1iII ( oo0oOo , sublabel = O00Oo0o0000OOoO , img = iII11 , infoLabels = i11IIIiIiIi , isFolder = OOooOO000 , params = iIIi1i1 )
  if 17 - 17: OOooOOo / OOooOOo / I11i
  if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
 if iIIiIiI1I1 :
  if ooO00OO0 . GetCategoryList_morepage ( i1i1Iiii1I1 , OOoO , oooOo0OOOoo0 , oooO0 + 1 ) :
   iIIi1i1 = { }
   iIIi1i1 [ 'mode' ] = 'CATEGORY_LIST'
   iIIi1i1 [ 'stype' ] = i1i1Iiii1I1
   iIIi1i1 [ 'tag_id' ] = OOoO
   iIIi1i1 [ 'api_path' ] = oooOo0OOOoo0
   iIIi1i1 [ 'page' ] = str ( oooO0 + 1 )
   oo0oOo = '[B]%s >>[/B]' % '다음 페이지'
   oO00oOOoooO = str ( oooO0 + 1 )
   ii111111I1iII ( oo0oOo , sublabel = oO00oOOoooO , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 82 - 82: iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % IiII / Ii1I . Ii1I
 if len ( OOooo ) > 0 : xbmcplugin . endOfDirectory ( OOoo0O , cacheToDisc = False )
 if 14 - 14: o0oOOo0O0Ooo . OOooOOo . I11i + OoooooooOO - OOooOOo + IiII
 if 9 - 9: Ii1I
 if 59 - 59: I1IiiI * II111iiii . O0
 if 56 - 56: Ii1I - iII111i % I1IiiI - o0oOOo0O0Ooo
 if 51 - 51: O0 / ooOoO0o * iIii1I11I1II1 + I1ii11iIi11i + o0oOOo0O0Ooo
def Oo0OO0000oooo ( args ) :
 if 7 - 7: oO0o - OoO0O00 - O0 % oO0o - II111iiii
 ooO00OO0 . SaveCredential ( IIIii1II1II ( ) )
 if 31 - 31: iII111i / Oo0Ooo - iII111i - OOooOOo
 I1iiIIIi11 = args . get ( 'movie_code' )
 oooO0 = int ( args . get ( 'page' ) )
 O0oO0 = args . get ( 'season_code' )
 if 12 - 12: OoooooooOO % o0oOOo0O0Ooo * I11i % iIii1I11I1II1 / Ii1I
 if 27 - 27: i11iIiiIii % II111iiii % I11i . O0 - Oo0Ooo + OoOoOO00
 OOooo , iIIiIiI1I1 = ooO00OO0 . GetEpisodoList ( I1iiIIIi11 , oooO0 , orderby = Oo0O0O0ooO0O ( ) )
 if 57 - 57: iIii1I11I1II1 / I11i - i1IIi
 if 51 - 51: IiII
 for O0O0Ooo in OOooo :
  o00Oo0oooooo = O0O0Ooo . get ( 'code' )
  oo0oOo = O0O0Ooo . get ( 'title' )
  iII11 = O0O0Ooo . get ( 'thumbnail' )
  ii11I1 = O0O0Ooo . get ( 'display_num' )
  oO0oo = O0O0Ooo . get ( 'season_title' )
  if 38 - 38: OoooooooOO * ooOoO0o % O0 * OoOoOO00
  i11IIIiIiIi = { }
  i11IIIiIiIi [ 'plot' ] = '%s\n%s\n\n%s' % ( oO0oo , ii11I1 , oo0oOo )
  if 29 - 29: I1ii11iIi11i / i1IIi . I1IiiI - OoOoOO00 - OoOoOO00 - Ii1I
  oo0oOo = '(%s) %s' % ( ii11I1 , oo0oOo )
  if 20 - 20: i1IIi % OoO0O00 . I1IiiI / IiII * i11iIiiIii * OOooOOo
  iIIi1i1 = { 'mode' : 'MOVIE'
 , 'movie_code' : o00Oo0oooooo
 , 'season_code' : O0oO0
  # iIii1I11I1II1 % i1IIi - O0 + I11i * I1Ii111 . IiII
  , 'title' : '%s < %s >' % ( oo0oOo , oO0oo )
 , 'thumbnail' : iII11
 }
  if 52 - 52: ooOoO0o + O0 . iII111i . I1ii11iIi11i . OoO0O00
  ii111111I1iII ( oo0oOo , sublabel = oO0oo , img = iII11 , infoLabels = i11IIIiIiIi , isFolder = False , params = iIIi1i1 )
  if 97 - 97: I1IiiI / iII111i
 if oooO0 == 1 :
  i11IIIiIiIi = { 'plot' : '정렬순서를 변경합니다.' }
  iIIi1i1 = { }
  iIIi1i1 [ 'mode' ] = 'ORDER_BY'
  if Oo0O0O0ooO0O ( ) == 'desc' :
   oo0oOo = '정렬순서변경 : 최신화부터 -> 1회부터'
   iIIi1i1 [ 'orderby' ] = 'asc'
  else :
   oo0oOo = '정렬순서변경 : 1회부터 -> 최신화부터'
   iIIi1i1 [ 'orderby' ] = 'desc'
  ii111111I1iII ( oo0oOo , sublabel = '' , img = '' , infoLabels = i11IIIiIiIi , isFolder = False , params = iIIi1i1 )
  if 71 - 71: II111iiii / i1IIi . I1ii11iIi11i % OoooooooOO . OoOoOO00
 if iIIiIiI1I1 :
  if 41 - 41: i1IIi * II111iiii / OoooooooOO . OOooOOo
  iIIi1i1 [ 'mode' ] = 'EPISODE'
  iIIi1i1 [ 'movie_code' ] = I1iiIIIi11
  iIIi1i1 [ 'page' ] = str ( oooO0 + 1 )
  oo0oOo = '[B]%s >>[/B]' % '다음 페이지'
  oO00oOOoooO = str ( oooO0 + 1 )
  ii111111I1iII ( oo0oOo , sublabel = oO00oOOoooO , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
 if len ( OOooo ) > 0 : xbmcplugin . endOfDirectory ( OOoo0O , cacheToDisc = False )
 if 100 - 100: OoO0O00
 if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
 if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
 if 45 - 45: I1Ii111
 if 83 - 83: OoOoOO00 . OoooooooOO
 if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
def oOOoo ( args ) :
 if 14 - 14: o0oOOo0O0Ooo * oO0o
 ooO00OO0 . SaveCredential ( IIIii1II1II ( ) )
 if 81 - 81: Ii1I * o0oOOo0O0Ooo + I1Ii111 + Oo0Ooo - OoooooooOO
 oooO0 = int ( args . get ( 'page' ) )
 if 32 - 32: Ii1I * O0
 if 'search_key' in args :
  O00oOo00o0o = args . get ( 'search_key' )
 else :
  O00oOo00o0o = I11iii ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
  if not O00oOo00o0o : return
  if 85 - 85: iII111i + OoooooooOO * iII111i - I1Ii111 % i11iIiiIii
  if 71 - 71: I1ii11iIi11i - ooOoO0o / OoOoOO00 * OoOoOO00 / i1IIi . i1IIi
 OOooo , iIIiIiI1I1 = ooO00OO0 . GetSearchList ( O00oOo00o0o , oooO0 )
 if len ( OOooo ) == 0 : return
 if 53 - 53: I1Ii111
 if 21 - 21: I11i
 for O0O0Ooo in OOooo :
  o00Oo0oooooo = O0O0Ooo . get ( 'code' )
  oo0oOo = O0O0Ooo . get ( 'title' )
  oOoO0 = O0O0Ooo . get ( 'content_type' )
  Oo0 = O0O0Ooo . get ( 'story' )
  iII11 = O0O0Ooo . get ( 'thumbnail' )
  oo0O0o00o0O = O0O0Ooo . get ( 'year' )
  I11i1II = O0O0Ooo . get ( 'film_rating_code' )
  Ooo = O0O0Ooo . get ( 'film_rating_short' )
  if 92 - 92: i11iIiiIii / I1Ii111 - iII111i % ooOoO0o * I1Ii111 + Oo0Ooo
  if oOoO0 == 'movies' :
   OOooOO000 = False
   I1ii1 = 'MOVIE'
   O00Oo0o0000OOoO = ''
   O0oO0 = '-'
  else :
   OOooOO000 = True
   I1ii1 = 'EPISODE'
   O00Oo0o0000OOoO = 'Series'
   O0oO0 = o00Oo0oooooo
   if 11 - 11: OoooooooOO . I1Ii111
  i11IIIiIiIi = { }
  i11IIIiIiIi [ 'plot' ] = '%s (%s)\n년도 : %s\n\n%s' % ( oo0oOo , Ooo , oo0O0o00o0O , Oo0 )
  if 80 - 80: OoooooooOO - OOooOOo * Ii1I * I1ii11iIi11i / I1IiiI / OOooOOo
  if I11i1II >= 19 :
   oo0oOo += '  (%s년 - %s)' % ( oo0O0o00o0O , str ( Ooo ) )
  else :
   oo0oOo += '  (%s년)' % ( oo0O0o00o0O )
   if 13 - 13: I1Ii111 * ooOoO0o + i11iIiiIii * I1Ii111 - ooOoO0o
  iIIi1i1 = { 'mode' : I1ii1
 , 'movie_code' : o00Oo0oooooo
 , 'page' : '1'
 , 'season_code' : O0oO0
  , 'title' : oo0oOo
 , 'thumbnail' : iII11
 }
  if 23 - 23: iIii1I11I1II1 * i1IIi % OoooooooOO * IiII
  ii111111I1iII ( oo0oOo , sublabel = O00Oo0o0000OOoO , img = iII11 , infoLabels = i11IIIiIiIi , isFolder = OOooOO000 , params = iIIi1i1 )
  if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
  if 39 - 39: IiII * Oo0Ooo + iIii1I11I1II1 - IiII + OOooOOo
 if iIIiIiI1I1 :
  iIIi1i1 = { }
  iIIi1i1 [ 'mode' ] = 'SEARCH'
  iIIi1i1 [ 'search_key' ] = O00oOo00o0o
  iIIi1i1 [ 'page' ] = str ( oooO0 + 1 )
  oo0oOo = '[B]%s >>[/B]' % '다음 페이지'
  oO00oOOoooO = str ( oooO0 + 1 )
  ii111111I1iII ( oo0oOo , sublabel = oO00oOOoooO , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if 69 - 69: O0
 if len ( OOooo ) > 0 : xbmcplugin . endOfDirectory ( OOoo0O )
 if 85 - 85: ooOoO0o / O0
 if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
 if 62 - 62: I1Ii111 . IiII . OoooooooOO
 if 11 - 11: OOooOOo / I11i
 if 73 - 73: i1IIi / i11iIiiIii
 if 58 - 58: Oo0Ooo . II111iiii + oO0o - i11iIiiIii / II111iiii / O0
def oOOoOo ( stype ) :
 try :
  ooOooo0 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  with open ( ooOooo0 , 'w' ) as oO0OO0 :
   oO0OO0 . write ( '' )
 except :
  None
  if 82 - 82: IiII - IiII + OoOoOO00
  if 8 - 8: o0oOOo0O0Ooo % iII111i * oO0o % Ii1I . ooOoO0o / ooOoO0o
  if 81 - 81: OoO0O00
  if 99 - 99: oO0o * II111iiii * I1Ii111
def oOooO0 ( args ) :
 i1i1Iiii1I1 = args . get ( 'stype' )
 if 79 - 79: OoO0O00 - iIii1I11I1II1 + Ii1I - I1Ii111
 i11iiII = xbmcgui . Dialog ( )
 I11i1iIII = i11iiII . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
 if I11i1iIII == False : sys . exit ( )
 if 93 - 93: II111iiii . I1IiiI - Oo0Ooo + OoOoOO00
 oOOoOo ( i1i1Iiii1I1 )
 if 61 - 61: II111iiii
 xbmc . executebuiltin ( "Container.Refresh" )
 if 15 - 15: i11iIiiIii % I1IiiI * I11i / I1Ii111
 if 90 - 90: iII111i
 if 31 - 31: OOooOOo + O0
 if 87 - 87: ooOoO0o
def IIIii ( stype ) :
 try :
  ooOooo0 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  with open ( ooOooo0 , 'r' ) as oO0OO0 :
   O00OooOo00o = oO0OO0 . readlines ( )
 except :
  O00OooOo00o = [ ]
  if 20 - 20: i1IIi * I1Ii111 + II111iiii % o0oOOo0O0Ooo % oO0o
 return O00OooOo00o
 if 13 - 13: Oo0Ooo
 if 60 - 60: I1ii11iIi11i * I1IiiI
 if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
 if 41 - 41: Ii1I
def iIIII ( stype , in_params ) :
 try :
  ooOooo0 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  oOOoo0o0OOOO = IIIii ( stype )
  if 26 - 26: iII111i % iIii1I11I1II1 + o0oOOo0O0Ooo
  with open ( ooOooo0 , 'w' ) as oO0OO0 :
   OOOooo = urllib . urlencode ( in_params )
   OOOooo = OOOooo . encode ( 'utf-8' ) + '\n'
   oO0OO0 . write ( OOOooo )
   if 99 - 99: II111iiii * IiII % iIii1I11I1II1 / Ii1I
   OOO00O0oOOo = 0
   for O0oO in oOOoo0o0OOOO :
    OO000oooo0 = dict ( urlparse . parse_qsl ( O0oO ) )
    if in_params . get ( 'code' ) != OO000oooo0 . get ( 'code' ) :
     oO0OO0 . write ( O0oO )
     OOO00O0oOOo += 1
     if OOO00O0oOOo >= 50 : break
 except :
  None
  if 77 - 77: I1IiiI % O0
  if 36 - 36: Ii1I / II111iiii / IiII / IiII + I1ii11iIi11i
  if 95 - 95: IiII
  if 51 - 51: II111iiii + IiII . i1IIi . I1ii11iIi11i + OoOoOO00 * I1IiiI
  if 72 - 72: oO0o + oO0o / II111iiii . OoooooooOO % Ii1I
def III ( args ) :
 i1i1Iiii1I1 = args . get ( 'stype' )
 if 41 - 41: i11iIiiIii + Oo0Ooo / I1IiiI . OoooooooOO % oO0o % i1IIi
 if i1i1Iiii1I1 == '-' :
  for oOO in I1Ii11I1Ii1i :
   oo0oOo = oOO . get ( 'title' )
   if 17 - 17: II111iiii / I1ii11iIi11i % IiII + I1IiiI * I1Ii111
   iIIi1i1 = { 'mode' : oOO . get ( 'mode' )
 , 'stype' : oOO . get ( 'stype' )
 }
   if 36 - 36: I1Ii111 * OoO0O00
   ii111111I1iII ( oo0oOo , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if len ( I1Ii11I1Ii1i ) > 0 : xbmcplugin . endOfDirectory ( OOoo0O )
  if 23 - 23: I11i . OoooooooOO - OOooOOo + IiII . II111iiii
 else :
  oOOo0OOOOo0Oo = IIIii ( i1i1Iiii1I1 )
  if 67 - 67: oO0o / iII111i . I11i . iIii1I11I1II1
  for iiiI in oOOo0OOOOo0Oo :
   IiIi1 = dict ( urlparse . parse_qsl ( iiiI ) )
   if 34 - 34: OOooOOo
   o00Oo0oooooo = IiIi1 . get ( 'code' )
   oo0oOo = IiIi1 . get ( 'title' )
   iII11 = IiIi1 . get ( 'img' )
   if 91 - 91: iIii1I11I1II1 % o0oOOo0O0Ooo . iIii1I11I1II1 % i1IIi / II111iiii * OoOoOO00
   i11IIIiIiIi = { }
   i11IIIiIiIi [ 'plot' ] = oo0oOo
   if 10 - 10: II111iiii . iII111i
   if i1i1Iiii1I1 == 'movie' :
    iIIi1i1 = { 'mode' : 'MOVIE'
 , 'page' : '1'
 , 'movie_code' : o00Oo0oooooo
 , 'season_code' : '-'
 , 'title' : oo0oOo
 , 'thumbnail' : iII11
 }
    OOooOO000 = False
   else :
    iIIi1i1 = { 'mode' : 'EPISODE'
 , 'page' : '1'
 , 'movie_code' : o00Oo0oooooo
 , 'season_code' : o00Oo0oooooo
 , 'title' : oo0oOo
 , 'thumbnail' : iII11
 }
    OOooOO000 = True
    if 32 - 32: Ii1I . IiII . OoooooooOO - OoO0O00 + oO0o
   ii111111I1iII ( oo0oOo , sublabel = '' , img = iII11 , infoLabels = i11IIIiIiIi , isFolder = OOooOO000 , params = iIIi1i1 )
   if 88 - 88: iII111i
  i11IIIiIiIi = { 'plot' : '시청목록을 삭제합니다.' }
  oo0oOo = '*** 시청목록 삭제 ***'
  iIIi1i1 = { 'mode' : 'MYVIEW_REMOVE'
 , 'stype' : i1i1Iiii1I1
 }
  if 19 - 19: II111iiii * IiII + Ii1I
  ii111111I1iII ( oo0oOo , sublabel = '' , img = '' , infoLabels = i11IIIiIiIi , isFolder = False , params = iIIi1i1 )
  if 65 - 65: OOooOOo . I1Ii111 . OoO0O00 . iII111i - OOooOOo
  xbmcplugin . endOfDirectory ( OOoo0O , cacheToDisc = False )
  if 19 - 19: i11iIiiIii + iII111i % ooOoO0o
  if 14 - 14: OoO0O00 . II111iiii . I11i / Ii1I % I1ii11iIi11i - ooOoO0o
  if 67 - 67: I11i - OOooOOo . i1IIi
  if 35 - 35: iII111i + ooOoO0o - oO0o . iII111i . IiII
  if 87 - 87: OoOoOO00
  if 25 - 25: i1IIi . OoO0O00 - OoOoOO00 / OoO0O00 % OoO0O00 * iIii1I11I1II1
  if 50 - 50: OoO0O00 . i11iIiiIii - oO0o . oO0o
  if 31 - 31: OOooOOo / Oo0Ooo * i1IIi . OoOoOO00
ooO00OO0 = o00ooooO0oO ( )
OOoo0O = int ( sys . argv [ 1 ] )
if 57 - 57: OOooOOo + iIii1I11I1II1 % i1IIi % I1IiiI
iIIi1i1 = i11iIIIIIi1 ( )
OO0oo = iIIi1i1 . get ( 'mode' , None )
if 15 - 15: iIii1I11I1II1 % OoooooooOO - Oo0Ooo * Ii1I + I11i
i11Iii ( )
if 11 - 11: iII111i * Ii1I - OoOoOO00
if OO0oo is None :
 III1iII1I1ii ( )
 if 66 - 66: OoOoOO00 . i11iIiiIii - iII111i * o0oOOo0O0Ooo + OoooooooOO * I1ii11iIi11i
elif OO0oo == 'SUB_GROUP' :
 O00I1iI1 ( iIIi1i1 )
 if 74 - 74: Oo0Ooo
elif OO0oo == 'CATEGORY_LIST' :
 ooOOoO ( iIIi1i1 )
 if 61 - 61: Oo0Ooo - I1Ii111 * II111iiii % ooOoO0o * iIii1I11I1II1 + OoO0O00
elif OO0oo == 'EPISODE' :
 Oo0OO0000oooo ( iIIi1i1 )
 if 71 - 71: I11i / I11i * oO0o * oO0o / II111iiii
elif OO0oo == 'ORDER_BY' :
 oO0OOoO0 ( iIIi1i1 )
 if 35 - 35: OOooOOo * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo . OoOoOO00
elif OO0oo == 'SEARCH' :
 oOOoo ( iIIi1i1 )
 if 58 - 58: I11i + II111iiii * iII111i * i11iIiiIii - iIii1I11I1II1
elif OO0oo == 'MOVIE' :
 iII11I1IiiIi ( iIIi1i1 )
 xbmc . sleep ( 200 )
 if 68 - 68: OoooooooOO % II111iiii
elif OO0oo == 'WATCH' :
 III ( iIIi1i1 )
 if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
elif OO0oo == 'MYVIEW_REMOVE' :
 oOooO0 ( iIIi1i1 )
 if 24 - 24: II111iiii % I1Ii111 - ooOoO0o + I1IiiI * I1ii11iIi11i
else :
 None
 if 2 - 2: Ii1I - IiII
 if 83 - 83: oO0o % o0oOOo0O0Ooo % Ii1I - II111iiii * OOooOOo / OoooooooOO
 if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
