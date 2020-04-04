# -*- coding: utf-8 -*-
__author__ = "NightRain"
if 64 - 64: i11iIiiIii
import urllib
import urllib2
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import cookielib
import re
import json
import sys
import urlparse
import time
import base64
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
reload ( sys )
sys . setdefaultencoding ( 'utf-8' )
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
if 46 - 46: ooOoO0o * I11i - OoooooooOO
II1iII1i = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
if 97 - 97: OoooooooOO
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
if 94 - 94: i1IIi % Oo0Ooo
if 68 - 68: Ii1I / O0
class Iiii111Ii11I1 ( object ) :
 def __init__ ( self ) :
  self . MyCookie = cookielib . LWPCookieJar ( )
  self . Opener = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( self . MyCookie ) )
  self . Opener . addheaders = [ ( 'User-Agent' , II1iII1i ) ]
  urllib2 . install_opener ( self . Opener )
  if 66 - 66: iII111i
  if 30 - 30: iIii1I11I1II1 * iIii1I11I1II1 . II111iiii - oO0o
 def RequestCookie ( self , url , payload = None , cookie = None ) :
  ooO00oOoo = ''
  if 78 - 78: I11i / OoO0O00 - O0 . IiII
  if cookie : self . Opener . addheaders = cookie
  if payload :
   OOooo0000ooo = self . Opener . open ( url , urllib . urlencode ( payload ) )
  else :
   OOo000 = urllib2 . Request ( url )
   OOo000 . get_method = lambda : 'PUT'
   OOooo0000ooo = urllib2 . urlopen ( OOo000 )
   if 82 - 82: I11i . I1Ii111 / IiII % II111iiii % iIii1I11I1II1 % IiII
  ooO00oOoo = OOooo0000ooo . info ( ) . getheader ( 'set-cookie' )
  if 86 - 86: OoOoOO00 % I1IiiI
  OOooo0000ooo . close ( )
  return ooO00oOoo
  if 80 - 80: OoooooooOO . I1IiiI
  if 87 - 87: oO0o / ooOoO0o + I1Ii111 - ooOoO0o . ooOoO0o / II111iiii
 def Request ( self , url , params = None , cookie = None ) :
  if cookie : self . Opener . addheaders = cookie
  if 11 - 11: I1IiiI % o0oOOo0O0Ooo - Oo0Ooo
  if params :
   OOooo0000ooo = self . Opener . open ( url , urllib . urlencode ( params ) )
  else :
   OOooo0000ooo = self . Opener . open ( url )
   if 58 - 58: i11iIiiIii % I1Ii111
  ooO00oOoo = OOooo0000ooo . read ( )
  OOooo0000ooo . close ( )
  if 54 - 54: OOooOOo % O0 + I1IiiI - iII111i / I11i
  return ooO00oOoo
  if 31 - 31: OoO0O00 + II111iiii
  if 13 - 13: OOooOOo * oO0o * I1IiiI
  if 55 - 55: II111iiii
  if 43 - 43: OoOoOO00 - i1IIi + I1Ii111 + Ii1I
  if 17 - 17: o0oOOo0O0Ooo
class o00ooooO0oO ( object ) :
 def __init__ ( self ) :
  self . SESSION = Iiii111Ii11I1 ( )
  self . WATCHA_TOKEN = ''
  self . WATCHA_GUIT = ''
  self . WATCHA_GUITV = ''
  self . WATCHA_USERCD = ''
  self . API_DOMAIN = 'https://play.watcha.net'
  self . EPISODE_LIMIT = 20
  self . SEARCH_LIMIT = 30
  if 63 - 63: OoOoOO00 % i1IIi
  if 66 - 66: Ii1I
  if 78 - 78: OoO0O00
 def SaveCredential ( self , login_params ) :
  self . WATCHA_TOKEN = login_params . get ( 'watcha_token' )
  self . WATCHA_GUIT = login_params . get ( 'watcha_guit' )
  self . WATCHA_GUITV = login_params . get ( 'watcha_guitv' )
  self . WATCHA_USERCD = login_params . get ( 'watcha_usercd' )
  if 18 - 18: O0 - iII111i / iII111i + ooOoO0o % ooOoO0o - IiII
 def SaveCredential_usercd ( self , usercd ) :
  self . WATCHA_USERCD = usercd
  if 62 - 62: iII111i - IiII - OoOoOO00 % i1IIi / oO0o
 def SaveCredential_guitv ( self , guitv ) :
  self . WATCHA_GUITV = guitv
  if 77 - 77: II111iiii - II111iiii . I1IiiI / o0oOOo0O0Ooo
 def ClearCredential ( self ) :
  self . WATCHA_TOKEN = ''
  self . WATCHA_GUIT = ''
  self . WATCHA_GUITV = ''
  self . WATCHA_USERCD = ''
  if 14 - 14: I11i % O0
  if 41 - 41: i1IIi + I1Ii111 + OOooOOo - IiII
 def LoadCredential ( self ) :
  oO = {
 'watcha_token' : self . WATCHA_TOKEN
 , 'watcha_guit' : self . WATCHA_GUIT
 , 'watcha_guitv' : self . WATCHA_GUITV
 , 'watcha_usercd' : self . WATCHA_USERCD
 }
  return oO
  if 76 - 76: OoO0O00 * o0oOOo0O0Ooo % i1IIi - OoO0O00 / I1IiiI . OOooOOo
 def GetDefaultCookies ( self ) :
  if self . WATCHA_TOKEN :
   if self . WATCHA_GUITV :
    iiIiIIi = [
 ( 'user-agent' , II1iII1i )
 , ( 'x-watchaplay-client' , 'WatchaPlay-WebApp' )
 , ( 'x-watchaplay-client-language' , 'ko' )
 , ( 'x-watchaplay-client-region' , 'KR' )
 , ( 'x-watchaplay-client-version' , '1.0.0' )
 , ( 'cookie' , '%s=%s; %s=%s; %s=%s' % ( '_s_guit' , self . WATCHA_GUIT , '_s_guitv' , self . WATCHA_GUITV , '_guinness-premium_session' , self . WATCHA_TOKEN ) )
 ]
   else :
    iiIiIIi = [
 ( 'user-agent' , II1iII1i )
 , ( 'x-watchaplay-client' , 'WatchaPlay-WebApp' )
 , ( 'x-watchaplay-client-language' , 'ko' )
 , ( 'x-watchaplay-client-region' , 'KR' )
 , ( 'x-watchaplay-client-version' , '1.0.0' )
 , ( 'cookie' , '%s=%s; %s=%s' % ( '_s_guit' , self . WATCHA_GUIT , '_guinness-premium_session' , self . WATCHA_TOKEN ) )
 ]
  else :
   iiIiIIi = [
 ( 'user-agent' , II1iII1i )
 , ( 'x-watchaplay-client' , 'WatchaPlay-WebApp' )
 , ( 'x-watchaplay-client-version' , '1.0.0' )
 , ( 'x-watchaplay-client-language' , 'ko' )
 , ( 'x-watchaplay-client-region' , 'KR' )
 ]
  return iiIiIIi
  if 65 - 65: OoOoOO00
  if 6 - 6: I1IiiI / Oo0Ooo % Ii1I
 def makeurl ( self , domain , path , query1 = None , query2 = None ) :
  oo = domain + path
  if query1 :
   oo += '?%s' % urllib . urlencode ( query1 )
  if query2 :
   oo += '&%s' % urllib . urlencode ( query2 )
  return oo
  if 54 - 54: OOooOOo + OOooOOo % I1Ii111 % i11iIiiIii / iIii1I11I1II1 . OOooOOo
  if 57 - 57: Ii1I % OoooooooOO
 def GetCredential ( self , user_id , user_pw , user_pf ) :
  O00 = False
  i11I1 = Ii11Ii11I = '-'
  if 43 - 43: I1IiiI - iII111i * iIii1I11I1II1
  if 97 - 97: I11i % I11i + II111iiii * iII111i
  try :
   o0o00o0 = self . API_DOMAIN + '/api/session'
   if 25 - 25: Oo0Ooo - IiII . OoooooooOO
   I11ii1 = { 'email' : user_id
 , 'password' : user_pw
 }
   if 9 - 9: Ii1I + oO0o % Ii1I + i1IIi . OOooOOo
   iiIiIIi = self . GetDefaultCookies ( )
   if 31 - 31: o0oOOo0O0Ooo + I11i + I11i / II111iiii
   iiI1 = self . SESSION . RequestCookie ( o0o00o0 , payload = I11ii1 , cookie = iiIiIIi )
   if 19 - 19: I11i + ooOoO0o
   for ooo in iiI1 . split ( ',' ) :
    ooo = ooo . strip ( )
    if ooo . startswith ( '_guinness-premium_session' ) :
     Ii11Ii11I = ooo . split ( ';' ) [ 0 ]
     Ii11Ii11I = Ii11Ii11I . split ( '=' ) [ 1 ]
    if ooo . startswith ( '_s_guit' ) :
     i11I1 = ooo . split ( ';' ) [ 0 ]
     i11I1 = i11I1 . split ( '=' ) [ 1 ]
     if 18 - 18: o0oOOo0O0Ooo
   if Ii11Ii11I : O00 = True
   if 28 - 28: OOooOOo - IiII . IiII + OoOoOO00 - OoooooooOO + O0
  except Exception as oOoOooOo0o0 :
   i11I1 = Ii11Ii11I = ''
   if 61 - 61: o0oOOo0O0Ooo / OoO0O00 + ooOoO0o * oO0o / oO0o
   if 75 - 75: i1IIi / OoooooooOO - O0 / OoOoOO00 . II111iiii - i1IIi
  oO = {
 'watcha_guit' : i11I1
 , 'watcha_token' : Ii11Ii11I
 , 'watcha_guitv' : ''
 , 'watcha_usercd' : ''
 }
  self . SaveCredential ( oO )
  if 71 - 71: OOooOOo + Ii1I * OOooOOo - OoO0O00 * o0oOOo0O0Ooo
  if 65 - 65: O0 % I1IiiI . I1ii11iIi11i % iIii1I11I1II1 / OOooOOo % I1Ii111
  if 51 - 51: i11iIiiIii . I1IiiI + II111iiii
  try :
   II111ii1II1i = self . GetProfilesList ( )
   OoOo00o = II111ii1II1i [ user_pf ]
   self . SaveCredential_usercd ( OoOo00o )
   if 70 - 70: iII111i * I1ii11iIi11i
  except Exception as oOoOooOo0o0 :
   self . ClearCredential ( )
   return False
   if 46 - 46: ooOoO0o / OoO0O00
   if 52 - 52: o0oOOo0O0Ooo - OoooooooOO + Ii1I + Ii1I - o0oOOo0O0Ooo / I1Ii111
  if user_pf != 0 :
   I1I = self . GetProfilesConvert ( OoOo00o )
   self . SaveCredential_guitv ( I1I )
   if 24 - 24: I1ii11iIi11i
  return O00
  if 56 - 56: ooOoO0o
  if 92 - 92: iII111i . I11i + o0oOOo0O0Ooo
 def GetSubGroupList ( self , stype ) :
  IiII1I11i1I1I = [ ]
  if 83 - 83: I1ii11iIi11i / ooOoO0o
  try :
   iIIIIii1 = '/api/categories.json'
   if 58 - 58: i11iIiiIii % I11i
   oo = self . makeurl ( self . API_DOMAIN , iIIIIii1 )
   if 71 - 71: OOooOOo + ooOoO0o % i11iIiiIii + I1ii11iIi11i - IiII
   iiIiIIi = self . GetDefaultCookies ( )
   if 88 - 88: OoOoOO00 - OoO0O00 % OOooOOo
   OOooo0000ooo = self . SESSION . Request ( oo , params = None , cookie = iiIiIIi )
   iI1I111Ii111i = json . loads ( OOooo0000ooo )
   if 7 - 7: ooOoO0o * OoO0O00 % oO0o . IiII
   if 45 - 45: i11iIiiIii * II111iiii % iIii1I11I1II1 + I1ii11iIi11i - Ii1I
   if not ( 'genres' in iI1I111Ii111i ) : return IiII1I11i1I1I
   if stype == 'genres' :
    iIi1iIiii111 = iI1I111Ii111i [ 'genres' ]
   else :
    iIi1iIiii111 = iI1I111Ii111i [ 'tags' ]
    if 16 - 16: I1ii11iIi11i + OoO0O00 - II111iiii
    if 85 - 85: OoOoOO00 + i1IIi
   for Oo0OoO00oOO0o in iIi1iIiii111 :
    OOO00O = Oo0OoO00oOO0o [ 'name' ]
    OOoOO0oo0ooO = Oo0OoO00oOO0o [ 'api_path' ]
    O0o0O00Oo0o0 = Oo0OoO00oOO0o [ 'entity' ] [ 'id' ]
    if 87 - 87: ooOoO0o * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
    O0ooo0O0oo0 = { 'group_name' : unicode ( OOO00O )
 , 'api_path' : OOoOO0oo0ooO
 , 'tag_id' : str ( O0o0O00Oo0o0 )
 }
    IiII1I11i1I1I . append ( O0ooo0O0oo0 )
    if 91 - 91: iIii1I11I1II1 + I1Ii111
    if 31 - 31: IiII . OoOoOO00 . OOooOOo
  except Exception as oOoOooOo0o0 :
   print ( oOoOooOo0o0 )
   if 75 - 75: I11i + OoO0O00 . OoOoOO00 . ooOoO0o + Oo0Ooo . OoO0O00
  return IiII1I11i1I1I
  if 96 - 96: OOooOOo . ooOoO0o - Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * OOooOOo
  if 65 - 65: Ii1I . iIii1I11I1II1 / O0 - Ii1I
  if 21 - 21: I1IiiI * iIii1I11I1II1
 def GetCategoryList ( self , stype , tag_id , api_path , page_int , in_sort ) :
  IiII1I11i1I1I = [ ]
  oooooOoo0ooo = False
  if 6 - 6: I11i - Ii1I + iIii1I11I1II1 - I1Ii111 - i11iIiiIii
  try :
   if 'categories' in api_path :
    iIIIIii1 = '/api/categories/contents.json'
    if 79 - 79: OoOoOO00 - O0 * OoO0O00 + OoOoOO00 % O0 * O0
    oOOo0 = { }
    if stype == 'genres' :
     oOOo0 [ 'genre' ] = tag_id
    else :
     oOOo0 [ 'tag' ] = tag_id
     if 54 - 54: O0 - IiII % OOooOOo
    oOOo0 [ 'order' ] = in_sort
    if page_int > 1 :
     oOOo0 [ 'page' ] = str ( page_int - 1 )
     if 77 - 77: OoOoOO00 / I1IiiI / OoO0O00 + OoO0O00 . OOooOOo
    oo = self . makeurl ( self . API_DOMAIN , iIIIIii1 , oOOo0 )
    if 38 - 38: I1Ii111
   else :
    iIIIIii1 = '/api/' + api_path + '.json'
    if 7 - 7: O0 . iII111i % I1ii11iIi11i - I1IiiI - iIii1I11I1II1
    if page_int > 1 :
     oOOo0 = { }
     oOOo0 [ 'page' ] = str ( page_int )
     oo = self . makeurl ( self . API_DOMAIN , iIIIIii1 , oOOo0 )
    else :
     oo = self . makeurl ( self . API_DOMAIN , iIIIIii1 )
     if 36 - 36: IiII % ooOoO0o % Oo0Ooo - I1ii11iIi11i
   iiIiIIi = self . GetDefaultCookies ( )
   if 22 - 22: iIii1I11I1II1 / Oo0Ooo * I1ii11iIi11i % iII111i
   OOooo0000ooo = self . SESSION . Request ( oo , params = None , cookie = iiIiIIi )
   iI1I111Ii111i = json . loads ( OOooo0000ooo )
   if 85 - 85: oO0o % i11iIiiIii - iII111i * OoooooooOO / I1IiiI % I1IiiI
   if not ( 'contents' in iI1I111Ii111i ) : return IiII1I11i1I1I , oooooOoo0ooo
   iIi1iIiii111 = iI1I111Ii111i [ 'contents' ]
   oooooOoo0ooo = iI1I111Ii111i [ 'meta' ] [ 'has_next' ]
   if 1 - 1: OoO0O00 - oO0o . I11i . OoO0O00 / Oo0Ooo + I11i
   for Oo0OoO00oOO0o in iIi1iIiii111 :
    Ooo = Oo0OoO00oOO0o [ 'code' ]
    OOOOo = Oo0OoO00oOO0o [ 'content_type' ]
    oo0O0oO = Oo0OoO00oOO0o [ 'title' ]
    ooooo = Oo0OoO00oOO0o [ 'story' ]
    if Oo0OoO00oOO0o [ 'thumbnail' ] != None :
     II1I = Oo0OoO00oOO0o [ 'thumbnail' ] [ 'medium' ]
    else :
     II1I = Oo0OoO00oOO0o [ 'stillcut' ] [ 'medium' ]
    O0i1II1Iiii1I11 = Oo0OoO00oOO0o [ 'year' ]
    IIII = Oo0OoO00oOO0o [ 'film_rating_code' ]
    iiIiI = Oo0OoO00oOO0o [ 'film_rating_short' ]
    if 91 - 91: iII111i % i1IIi % iIii1I11I1II1
    O0ooo0O0oo0 = { 'code' : Ooo
 , 'content_type' : OOOOo
 , 'title' : unicode ( oo0O0oO )
 , 'story' : unicode ( ooooo )
 , 'thumbnail' : II1I
 , 'year' : O0i1II1Iiii1I11
 , 'film_rating_code' : IIII
 , 'film_rating_short' : iiIiI
 }
    IiII1I11i1I1I . append ( O0ooo0O0oo0 )
    if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
    if 45 - 45: oO0o - IiII - OoooooooOO - OoO0O00 . II111iiii / O0
  except Exception as oOoOooOo0o0 :
   print ( oOoOooOo0o0 )
   if 51 - 51: O0 + iII111i
  return IiII1I11i1I1I , oooooOoo0ooo
  if 8 - 8: oO0o * OoOoOO00 - Ii1I - OoO0O00 * OOooOOo % I1IiiI
  if 48 - 48: O0
 def GetCategoryList_morepage ( self , stype , tag_id , api_path , page_int , in_sort ) :
  oooooOoo0ooo = False
  if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
  if not ( 'categories' in api_path ) : return True
  if 41 - 41: Ii1I - O0 - O0
  try :
   iIIIIii1 = '/api/categories/contents.json'
   if 68 - 68: OOooOOo % I1Ii111
   oOOo0 = { }
   if stype == 'genres' :
    oOOo0 [ 'genre' ] = tag_id
   else :
    oOOo0 [ 'tag' ] = tag_id
    if 88 - 88: iIii1I11I1II1 - ooOoO0o + OOooOOo
   oOOo0 [ 'order' ] = in_sort
   if page_int > 1 :
    oOOo0 [ 'page' ] = str ( page_int - 1 )
    if 40 - 40: I1IiiI * Ii1I + OOooOOo % iII111i
   oo = self . makeurl ( self . API_DOMAIN , iIIIIii1 , oOOo0 )
   if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
   iiIiIIi = self . GetDefaultCookies ( )
   if 23 - 23: O0
   OOooo0000ooo = self . SESSION . Request ( oo , params = None , cookie = iiIiIIi )
   iI1I111Ii111i = json . loads ( OOooo0000ooo )
   if 85 - 85: Ii1I
   oooooOoo0ooo = iI1I111Ii111i [ 'meta' ] [ 'has_next' ]
   if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
  except Exception as oOoOooOo0o0 :
   print ( oOoOooOo0o0 )
   if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + iII111i / OoOoOO00
  return oooooOoo0ooo
  if 84 - 84: ooOoO0o * II111iiii + Oo0Ooo
  if 53 - 53: iII111i % II111iiii . IiII - iIii1I11I1II1 - IiII * II111iiii
  if 77 - 77: iIii1I11I1II1 * OoO0O00
 def GetEpisodoList ( self , program_code , page_int , orderby = 'asc' ) :
  IiII1I11i1I1I = [ ]
  oooooOoo0ooo = False
  oOooOo0 = ''
  if 38 - 38: I1Ii111
  if 84 - 84: iIii1I11I1II1 % iII111i / iIii1I11I1II1 % I11i
  try :
   iIIIIii1 = '/api/contents/' + program_code + '/tv_episodes.json'
   oOOo0 = { 'all' : 'true' }
   if 45 - 45: O0
   oo = self . makeurl ( self . API_DOMAIN , iIIIIii1 , oOOo0 )
   iiIiIIi = self . GetDefaultCookies ( )
   if 26 - 26: I11i - iIii1I11I1II1 - I1IiiI / OoO0O00 . OoOoOO00 % iIii1I11I1II1
   OOooo0000ooo = self . SESSION . Request ( oo , params = None , cookie = iiIiIIi )
   iI1I111Ii111i = json . loads ( OOooo0000ooo )
   if 91 - 91: o0oOOo0O0Ooo . iIii1I11I1II1 / oO0o + i1IIi
   if not ( 'tv_episode_codes' in iI1I111Ii111i ) : return IiII1I11i1I1I , oooooOoo0ooo
   iIi1iIiii111 = iI1I111Ii111i [ 'tv_episode_codes' ]
   if 42 - 42: ooOoO0o . o0oOOo0O0Ooo . ooOoO0o - I1ii11iIi11i
   i1ii1I1I1 = len ( iIi1iIiii111 )
   oOoO0O0o0Oooo = int ( i1ii1I1I1 // ( self . EPISODE_LIMIT + 1 ) ) + 1
   if 5 - 5: ooOoO0o - II111iiii - OoooooooOO % Ii1I + I1IiiI * iIii1I11I1II1
   if orderby == 'desc' :
    I1I1II1I11 = ( i1ii1I1I1 - 1 ) - ( ( page_int - 1 ) * self . EPISODE_LIMIT )
   else :
    I1I1II1I11 = ( page_int - 1 ) * self . EPISODE_LIMIT
    if 8 - 8: o0oOOo0O0Ooo % O0 / I1IiiI - oO0o
   for Ii1I1i in range ( self . EPISODE_LIMIT ) :
    if orderby == 'desc' :
     OO = I1I1II1I11 - Ii1I1i
     if OO < 0 : break
    else :
     OO = I1I1II1I11 + Ii1I1i
     if OO >= i1ii1I1I1 : break
     if 37 - 37: ooOoO0o % oO0o . i11iIiiIii % Ii1I . Oo0Ooo
    if oOooOo0 != '' : oOooOo0 += ','
    oOooOo0 += iIi1iIiii111 [ OO ]
    if 39 - 39: OOooOOo - Oo0Ooo * I1ii11iIi11i % o0oOOo0O0Ooo
   if oOoO0O0o0Oooo > page_int : oooooOoo0ooo = True
   if 40 - 40: iIii1I11I1II1 / OoOoOO00 % I1ii11iIi11i + II111iiii
  except Exception as oOoOooOo0o0 :
   print ( oOoOooOo0o0 )
   if 27 - 27: II111iiii * OoOoOO00 * iIii1I11I1II1
   if 86 - 86: OoO0O00 * OOooOOo . iII111i
   if 32 - 32: o0oOOo0O0Ooo . IiII * I11i
  try :
   if 93 - 93: o0oOOo0O0Ooo % i1IIi . Ii1I . i11iIiiIii
   oOOo0 = { 'codes' : oOooOo0 }
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
   oo = self . makeurl ( self . API_DOMAIN , iIIIIii1 , oOOo0 )
   iiIiIIi = self . GetDefaultCookies ( )
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
   OOooo0000ooo = self . SESSION . Request ( oo , params = None , cookie = iiIiIIi )
   iI1I111Ii111i = json . loads ( OOooo0000ooo )
   if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
   if not ( 'tv_episodes' in iI1I111Ii111i ) : return IiII1I11i1I1I
   if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
   iIi1iIiii111 = iI1I111Ii111i [ 'tv_episodes' ]
   if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
   for Oo0OoO00oOO0o in iIi1iIiii111 :
    Ooo = Oo0OoO00oOO0o [ 'code' ]
    if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
    if 63 - 63: OoOoOO00 * iII111i
    if Oo0OoO00oOO0o [ 'title' ] :
     oo0O0oO = Oo0OoO00oOO0o [ 'title' ]
    else :
     oo0O0oO = ''
    II1I = Oo0OoO00oOO0o [ 'stillcut' ] [ 'medium' ]
    ooiIi1 = Oo0OoO00oOO0o [ 'display_number' ]
    OoOOoOooooOOo = Oo0OoO00oOO0o [ 'tv_season_title' ]
    if 87 - 87: I1IiiI
    if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
    O0ooo0O0oo0 = { 'code' : Ooo

    # i11iIiiIii / o0oOOo0O0Ooo * ooOoO0o
    , 'title' : unicode ( oo0O0oO )
 , 'thumbnail' : II1I
 , 'display_num' : unicode ( ooiIi1 )
 , 'season_title' : unicode ( OoOOoOooooOOo )

    }
    if 22 - 22: OoOoOO00 . OOooOOo * OoOoOO00
    IiII1I11i1I1I . append ( O0ooo0O0oo0 )
    if 54 - 54: IiII + Ii1I % OoO0O00 + OoooooooOO - O0 - o0oOOo0O0Ooo
  except Exception as oOoOooOo0o0 :
   print ( oOoOooOo0o0 )
   if 77 - 77: OOooOOo * iIii1I11I1II1
   if 98 - 98: I1IiiI % Ii1I * OoooooooOO
  return IiII1I11i1I1I , oooooOoo0ooo
  if 51 - 51: iIii1I11I1II1 . OoOoOO00 / oO0o + o0oOOo0O0Ooo
  if 33 - 33: ooOoO0o . II111iiii % iII111i + o0oOOo0O0Ooo
  if 71 - 71: Oo0Ooo % OOooOOo
 def GetSearchList ( self , search_key , page_int ) :
  O00oO000O0O = [ ]
  oooooOoo0ooo = False
  if 18 - 18: iII111i - OOooOOo . I1Ii111 . iIii1I11I1II1
  try :
   iIIIIii1 = '/api/search.json'
   if 2 - 2: OOooOOo . OoO0O00
   oOOo0 = { 'query' : search_key
 , 'page' : str ( page_int )
 , 'per' : str ( self . SEARCH_LIMIT )
 , 'exclude' : 'limited'
 }
   if 78 - 78: I11i * iIii1I11I1II1 . I1IiiI / o0oOOo0O0Ooo - OoooooooOO / I1Ii111
   oo = self . makeurl ( self . API_DOMAIN , iIIIIii1 , oOOo0 )
   if 35 - 35: I11i % OOooOOo - oO0o
   iiIiIIi = self . GetDefaultCookies ( )
   if 20 - 20: i1IIi - ooOoO0o
   OOooo0000ooo = self . SESSION . Request ( oo , params = None , cookie = iiIiIIi )
   iI1I111Ii111i = json . loads ( OOooo0000ooo )
   if 30 - 30: I11i / I1IiiI
   if not ( 'results' in iI1I111Ii111i ) : return O00oO000O0O , oooooOoo0ooo
   iIi1iIiii111 = iI1I111Ii111i [ 'results' ]
   oooooOoo0ooo = iI1I111Ii111i [ 'meta' ] [ 'has_next' ]
   if 35 - 35: II111iiii % OOooOOo . ooOoO0o + ooOoO0o % II111iiii % II111iiii
   for Oo0OoO00oOO0o in iIi1iIiii111 :
    Ooo = Oo0OoO00oOO0o [ 'code' ]
    OOOOo = Oo0OoO00oOO0o [ 'content_type' ]
    oo0O0oO = Oo0OoO00oOO0o [ 'title' ]
    ooooo = Oo0OoO00oOO0o [ 'story' ]
    if Oo0OoO00oOO0o [ 'thumbnail' ] != None :
     II1I = Oo0OoO00oOO0o [ 'thumbnail' ] [ 'medium' ]
    else :
     II1I = Oo0OoO00oOO0o [ 'stillcut' ] [ 'medium' ]
    O0i1II1Iiii1I11 = Oo0OoO00oOO0o [ 'year' ]
    IIII = Oo0OoO00oOO0o [ 'film_rating_code' ]
    iiIiI = Oo0OoO00oOO0o [ 'film_rating_short' ]
    if 72 - 72: II111iiii + i1IIi + o0oOOo0O0Ooo
    O0ooo0O0oo0 = { 'code' : Ooo
 , 'content_type' : OOOOo
 , 'title' : unicode ( oo0O0oO )
 , 'story' : unicode ( ooooo )
 , 'thumbnail' : II1I
 , 'year' : O0i1II1Iiii1I11
 , 'film_rating_code' : IIII
 , 'film_rating_short' : iiIiI
 }
    O00oO000O0O . append ( O0ooo0O0oo0 )
    if 94 - 94: oO0o . i1IIi - o0oOOo0O0Ooo % O0 - OoO0O00
    if 72 - 72: Ii1I
  except Exception as oOoOooOo0o0 :
   print ( oOoOooOo0o0 )
   if 1 - 1: OoO0O00 * IiII * OoooooooOO + ooOoO0o
  return O00oO000O0O , oooooOoo0ooo
  if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
  if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
 def GetProfilesList ( self ) :
  II111ii1II1i = [ ]
  if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
  try :
   iIIIIii1 = '/manage_profiles'
   oo = self . makeurl ( self . API_DOMAIN , iIIIIii1 )
   iiIiIIi = self . GetDefaultCookies ( )
   OOooo0000ooo = self . SESSION . Request ( oo , params = None , cookie = iiIiIIi )
   if 26 - 26: Ii1I % I1ii11iIi11i
   if 76 - 76: IiII * iII111i
   if 52 - 52: OOooOOo
   if 19 - 19: I1IiiI
   if 25 - 25: Ii1I / ooOoO0o
   if 31 - 31: OOooOOo . O0 % I1IiiI . o0oOOo0O0Ooo + IiII
   if 71 - 71: I1Ii111 . II111iiii
   if 62 - 62: OoooooooOO . I11i
   oOOOoo00 = re . findall ( '/api/users/me.{5000}' , OOooo0000ooo ) [ 0 ]
   oOOOoo00 = oOOOoo00 . replace ( '&quot;' , '' )
   II111ii1II1i = re . findall ( 'Normal,code:[A-Za-z0-9]{13},name:|Virtual,code:[A-Za-z0-9]{13},name:' , oOOOoo00 )
   if 9 - 9: O0 % O0 - o0oOOo0O0Ooo
   for Ii1I1i in range ( len ( II111ii1II1i ) ) :
    OoO = II111ii1II1i [ Ii1I1i ]
    if 12 - 12: O0 - o0oOOo0O0Ooo
    if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
    if 73 - 73: I11i % i11iIiiIii - I1IiiI
    OoO = OoO . split ( ':' ) [ 1 ]
    II111ii1II1i [ Ii1I1i ] = OoO . split ( ',' ) [ 0 ]
    if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
  except Exception as oOoOooOo0o0 :
   print ( oOoOooOo0o0 )
   if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
  return II111ii1II1i
  if 23 - 23: i11iIiiIii
  if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
 def GetProfilesConvert ( self , usercd ) :
  o0ooooO0o0O = ''
  if 24 - 24: O0 * o0oOOo0O0Ooo
  try :
   iIIIIii1 = '/api/users/' + usercd + '/convert'
   oo = self . makeurl ( self . API_DOMAIN , iIIIIii1 )
   if 29 - 29: I1IiiI % OOooOOo - I1IiiI / OOooOOo . i1IIi
   iiIiIIi = self . GetDefaultCookies ( )
   if 31 - 31: I1Ii111
   iiI1 = self . SESSION . RequestCookie ( oo , payload = None , cookie = iiIiIIi )
   if 88 - 88: OoO0O00 - ooOoO0o + OOooOOo * I1IiiI % iIii1I11I1II1 + Oo0Ooo
   for ooo in iiI1 . split ( ',' ) :
    ooo = ooo . strip ( )
    if ooo . startswith ( '_s_guitv' ) :
     oo000O0OoooO = ooo . split ( ';' ) [ 0 ]
     oo000O0OoooO = oo000O0OoooO . split ( '=' ) [ 1 ]
     if 93 - 93: I11i . II111iiii / oO0o % OoooooooOO * I11i % I1ii11iIi11i
   if oo000O0OoooO :
    o0ooooO0o0O = oo000O0OoooO
    if 48 - 48: ooOoO0o / I1Ii111 . iIii1I11I1II1 * OoOoOO00 * oO0o / i1IIi
  except Exception as oOoOooOo0o0 :
   o0ooooO0o0O = ''
   if 92 - 92: Oo0Ooo % Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
  return o0ooooO0o0O
  if 10 - 10: iII111i + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / I1Ii111 / I1ii11iIi11i
  if 42 - 42: I1IiiI
 def GetStreamingURL ( self , movie_code , quality_str ) :
  II1i11I = ii1I1IIii11 = O0o0oO = ''
  if 38 - 38: oO0o % OoOoOO00 + I1ii11iIi11i . i11iIiiIii
  try :
   iIIIIii1 = '/api/watch/' + movie_code + '.json'
   if 53 - 53: i11iIiiIii * iII111i
   oo = self . makeurl ( self . API_DOMAIN , iIIIIii1 )
   if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / II111iiii % Oo0Ooo
   iiIiIIi = self . GetDefaultCookies ( )
   iiIiIIi . append ( ( 'x-watchaplay-client-codec-flag' , '3' ) )
   iiIiIIi . append ( ( 'x-watchaplay-media-devices-info' , '7' ) )
   iiIiIIi . append ( ( 'x-watchaplay-screen' , quality_str ) )
   if 38 - 38: ooOoO0o - OOooOOo / iII111i
   OOooo0000ooo = self . SESSION . Request ( oo , params = None , cookie = iiIiIIi )
   if 66 - 66: O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / Ii1I + I1ii11iIi11i
   iI1I111Ii111i = json . loads ( OOooo0000ooo )
   if 86 - 86: o0oOOo0O0Ooo
   II1i11I = iI1I111Ii111i [ 'streams' ] [ 0 ] [ 'source' ]
   if II1i11I == None : return ( II1i11I , ii1I1IIii11 , O0o0oO )
   if 5 - 5: IiII * OoOoOO00
   if 'subtitles' in iI1I111Ii111i [ 'streams' ] [ 0 ] :
    for i1Ii1i1I11Iii in iI1I111Ii111i [ 'streams' ] [ 0 ] [ 'subtitles' ] :
     if i1Ii1i1I11Iii [ 'lang' ] == 'ko' :
      ii1I1IIii11 = i1Ii1i1I11Iii [ 'url' ]
      break
      if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
      if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
   II1I1Ii = iI1I111Ii111i [ 'ping_payload' ]
   Ooo0O0oooo = self . WATCHA_USERCD
   iiI = '{\"merchant\":\"giitd_frograms\",\"sessionId\":\"%s\",\"userId\":\"%s\"}' % ( II1I1Ii , Ooo0O0oooo )
   if 56 - 56: Oo0Ooo . I1ii11iIi11i . I1IiiI
   O0o0oO = base64 . b64encode ( iiI )
   if 39 - 39: O0 + I1Ii111
   if 91 - 91: OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoOoOO00 + O0
  except Exception as oOoOooOo0o0 :
   return ( II1i11I , ii1I1IIii11 , O0o0oO )
   if 26 - 26: I1ii11iIi11i - OoooooooOO
   if 11 - 11: I1IiiI * oO0o
  return ( II1i11I , ii1I1IIii11 , O0o0oO )
  if 81 - 81: iII111i + IiII
  if 98 - 98: I1IiiI
  if 95 - 95: ooOoO0o / ooOoO0o
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
