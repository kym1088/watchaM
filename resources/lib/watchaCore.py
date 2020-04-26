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
 def Request2 ( self , url , params = None , cookie = None ) :
  import requests
  OOooo0000ooo = requests . get ( url , headers = cookie , cookies = None )
  if 13 - 13: OOooOOo * oO0o * I1IiiI
  ooO00oOoo = OOooo0000ooo . json ( )
  return ooO00oOoo
  if 55 - 55: II111iiii
  if 43 - 43: OoOoOO00 - i1IIi + I1Ii111 + Ii1I
  if 17 - 17: o0oOOo0O0Ooo
  if 64 - 64: Ii1I % i1IIi % OoooooooOO
class i1iIIi1 ( object ) :
 def __init__ ( self ) :
  self . SESSION = Iiii111Ii11I1 ( )
  self . WATCHA_TOKEN = ''
  self . WATCHA_GUIT = ''
  self . WATCHA_GUITV = ''
  self . WATCHA_USERCD = ''
  self . API_DOMAIN = 'https://play.watcha.net'
  self . EPISODE_LIMIT = 20
  self . SEARCH_LIMIT = 30
  if 50 - 50: i11iIiiIii - Ii1I
  if 78 - 78: OoO0O00
  if 18 - 18: O0 - iII111i / iII111i + ooOoO0o % ooOoO0o - IiII
 def SaveCredential ( self , login_params ) :
  self . WATCHA_TOKEN = login_params . get ( 'watcha_token' )
  self . WATCHA_GUIT = login_params . get ( 'watcha_guit' )
  self . WATCHA_GUITV = login_params . get ( 'watcha_guitv' )
  self . WATCHA_USERCD = login_params . get ( 'watcha_usercd' )
  if 62 - 62: iII111i - IiII - OoOoOO00 % i1IIi / oO0o
 def SaveCredential_usercd ( self , usercd ) :
  self . WATCHA_USERCD = usercd
  if 77 - 77: II111iiii - II111iiii . I1IiiI / o0oOOo0O0Ooo
 def SaveCredential_guitv ( self , guitv ) :
  self . WATCHA_GUITV = guitv
  if 14 - 14: I11i % O0
 def ClearCredential ( self ) :
  self . WATCHA_TOKEN = ''
  self . WATCHA_GUIT = ''
  self . WATCHA_GUITV = ''
  self . WATCHA_USERCD = ''
  if 41 - 41: i1IIi + I1Ii111 + OOooOOo - IiII
  if 77 - 77: Oo0Ooo . IiII % ooOoO0o
 def LoadCredential ( self ) :
  IIiiIiI1 = {
 'watcha_token' : self . WATCHA_TOKEN
 , 'watcha_guit' : self . WATCHA_GUIT
 , 'watcha_guitv' : self . WATCHA_GUITV
 , 'watcha_usercd' : self . WATCHA_USERCD
 }
  return IIiiIiI1
  if 41 - 41: OoOoOO00
 def GetDefaultCookies ( self ) :
  if self . WATCHA_TOKEN :
   if self . WATCHA_GUITV :
    II = [
 ( 'user-agent' , II1iII1i )
 , ( 'x-watchaplay-client' , 'WatchaPlay-WebApp' )
 , ( 'x-watchaplay-client-language' , 'ko' )
 , ( 'x-watchaplay-client-region' , 'KR' )
 , ( 'x-watchaplay-client-version' , '1.0.0' )
 , ( 'cookie' , '%s=%s; %s=%s; %s=%s' % ( '_s_guit' , self . WATCHA_GUIT , '_s_guitv' , self . WATCHA_GUITV , '_guinness-premium_session' , self . WATCHA_TOKEN ) )
 ]
   else :
    II = [
 ( 'user-agent' , II1iII1i )
 , ( 'x-watchaplay-client' , 'WatchaPlay-WebApp' )
 , ( 'x-watchaplay-client-language' , 'ko' )
 , ( 'x-watchaplay-client-region' , 'KR' )
 , ( 'x-watchaplay-client-version' , '1.0.0' )
 , ( 'cookie' , '%s=%s; %s=%s' % ( '_s_guit' , self . WATCHA_GUIT , '_guinness-premium_session' , self . WATCHA_TOKEN ) )
 ]
  else :
   II = [
 ( 'user-agent' , II1iII1i )
 , ( 'x-watchaplay-client' , 'WatchaPlay-WebApp' )
 , ( 'x-watchaplay-client-version' , '1.0.0' )
 , ( 'x-watchaplay-client-language' , 'ko' )
 , ( 'x-watchaplay-client-region' , 'KR' )
 ]
  return II
  if 57 - 57: oO0o
 def GetDefaultCookies2 ( self ) :
  if self . WATCHA_TOKEN :
   if self . WATCHA_GUITV :
    II = {
 'user-agent' : II1iII1i
 , 'x-watchaplay-client' : 'WatchaPlay-WebApp'
 , 'x-watchaplay-client-language' : 'ko'
 , 'x-watchaplay-client-region' : 'KR'
 , 'x-watchaplay-client-version' : '1.0.0'
 , 'cookie' : '%s=%s; %s=%s; %s=%s' % ( '_s_guit' , self . WATCHA_GUIT , '_s_guitv' , self . WATCHA_GUITV , '_guinness-premium_session' , self . WATCHA_TOKEN )
 }
   else :
    II = {
 'user-agent' : II1iII1i
 , 'x-watchaplay-client' : 'WatchaPlay-WebApp'
 , 'x-watchaplay-client-language' : 'ko'
 , 'x-watchaplay-client-region' : 'KR'
 , 'x-watchaplay-client-version' : '1.0.0'
 , 'cookie' : '%s=%s; %s=%s' % ( '_s_guit' , self . WATCHA_GUIT , '_guinness-premium_session' , self . WATCHA_TOKEN )
 }
  else :
   II = {
 'user-agent' : II1iII1i
 , 'x-watchaplay-client' : 'WatchaPlay-WebApp'
 , 'x-watchaplay-client-version' : '1.0.0'
 , 'x-watchaplay-client-language' : 'ko'
 , 'x-watchaplay-client-region' : 'KR'
 }
  return II
  if 14 - 14: Oo0Ooo . I1IiiI / Ii1I
  if 38 - 38: II111iiii % i11iIiiIii . ooOoO0o - OOooOOo + Ii1I
 def makeurl ( self , domain , path , query1 = None , query2 = None ) :
  Ooooo0Oo00oO0 = domain + path
  if query1 :
   Ooooo0Oo00oO0 += '?%s' % urllib . urlencode ( query1 )
  if query2 :
   Ooooo0Oo00oO0 += '&%s' % urllib . urlencode ( query2 )
  return Ooooo0Oo00oO0
  if 12 - 12: iIii1I11I1II1 * I1IiiI . ooOoO0o % I11i + O0
  if 70 - 70: Ii1I . oO0o * ooOoO0o . Ii1I
 def GetCredential ( self , user_id , user_pw , user_pf ) :
  iII11i = False
  O0O00o0OOO0 = Ii1iIIIi1ii = '-'
  if 80 - 80: I11i * i11iIiiIii / I1Ii111
  if 9 - 9: Ii1I + oO0o % Ii1I + i1IIi . OOooOOo
  try :
   III1i1i = self . API_DOMAIN + '/api/session'
   if 26 - 26: OoooooooOO
   IiiI11Iiiii = { 'email' : user_id
 , 'password' : user_pw
 }
   if 18 - 18: o0oOOo0O0Ooo
   II = self . GetDefaultCookies ( )
   if 28 - 28: OOooOOo - IiII . IiII + OoOoOO00 - OoooooooOO + O0
   oOoOooOo0o0 = self . SESSION . RequestCookie ( III1i1i , payload = IiiI11Iiiii , cookie = II )
   if 61 - 61: o0oOOo0O0Ooo / OoO0O00 + ooOoO0o * oO0o / oO0o
   for OoOo in oOoOooOo0o0 . split ( ',' ) :
    OoOo = OoOo . strip ( )
    if OoOo . startswith ( '_guinness-premium_session' ) :
     Ii1iIIIi1ii = OoOo . split ( ';' ) [ 0 ]
     Ii1iIIIi1ii = Ii1iIIIi1ii . split ( '=' ) [ 1 ]
    if OoOo . startswith ( '_s_guit' ) :
     O0O00o0OOO0 = OoOo . split ( ';' ) [ 0 ]
     O0O00o0OOO0 = O0O00o0OOO0 . split ( '=' ) [ 1 ]
     if 18 - 18: i11iIiiIii
   if Ii1iIIIi1ii : iII11i = True
   if 46 - 46: i1IIi / I11i % OOooOOo + I1Ii111
  except Exception as O0OOO00oo :
   O0O00o0OOO0 = Ii1iIIIi1ii = ''
   if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
   if 4 - 4: II111iiii / ooOoO0o . iII111i
  IIiiIiI1 = {
 'watcha_guit' : O0O00o0OOO0
 , 'watcha_token' : Ii1iIIIi1ii
 , 'watcha_guitv' : ''
 , 'watcha_usercd' : ''
 }
  self . SaveCredential ( IIiiIiI1 )
  if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
  if 50 - 50: I1IiiI
  if 34 - 34: I1IiiI * II111iiii % iII111i * OoOoOO00 - I1IiiI
  try :
   II1III = self . GetProfilesList ( )
   iI1iI1I1i1I = II1III [ user_pf ]
   self . SaveCredential_usercd ( iI1iI1I1i1I )
   if 24 - 24: I1ii11iIi11i
  except Exception as O0OOO00oo :
   self . ClearCredential ( )
   return False
   if 56 - 56: ooOoO0o
   if 92 - 92: iII111i . I11i + o0oOOo0O0Ooo
  if user_pf != 0 :
   IiII1I11i1I1I = self . GetProfilesConvert ( iI1iI1I1i1I )
   self . SaveCredential_guitv ( IiII1I11i1I1I )
   if 83 - 83: I1ii11iIi11i / ooOoO0o
  return iII11i
  if 49 - 49: o0oOOo0O0Ooo
  if 35 - 35: OoOoOO00 - OoooooooOO / I1ii11iIi11i % i1IIi
 def GetSubGroupList ( self , stype ) :
  o00OO00OoO = [ ]
  if 60 - 60: OoO0O00 * OoOoOO00 - OoO0O00 % OoooooooOO - ooOoO0o + I1IiiI
  try :
   O00Oo000ooO0 = '/api/categories.json'
   if 100 - 100: O0 + IiII - OOooOOo + i11iIiiIii * Ii1I
   Ooooo0Oo00oO0 = self . makeurl ( self . API_DOMAIN , O00Oo000ooO0 )
   if 30 - 30: o0oOOo0O0Ooo . Ii1I - OoooooooOO
   II = self . GetDefaultCookies ( )
   if 8 - 8: i1IIi - iIii1I11I1II1 * II111iiii + i11iIiiIii / I1Ii111 % OOooOOo
   OOooo0000ooo = self . SESSION . Request ( Ooooo0Oo00oO0 , params = None , cookie = II )
   iIIIi1 = json . loads ( OOooo0000ooo )
   if 20 - 20: i1IIi + I1ii11iIi11i - ooOoO0o
   if 30 - 30: II111iiii - OOooOOo - i11iIiiIii % OoOoOO00 - II111iiii * Ii1I
   if not ( 'genres' in iIIIi1 ) : return o00OO00OoO
   if stype == 'genres' :
    oO00O0O0O = iIIIi1 [ 'genres' ]
   else :
    oO00O0O0O = iIIIi1 [ 'tags' ]
    if 31 - 31: I11i - II111iiii . I11i
    if 18 - 18: o0oOOo0O0Ooo
   for O0o0O00Oo0o0 in oO00O0O0O :
    O00O0oOO00O00 = O0o0O00Oo0o0 [ 'name' ]
    i1 = O0o0O00Oo0o0 [ 'api_path' ]
    Oo00 = O0o0O00Oo0o0 [ 'entity' ] [ 'id' ]
    if 31 - 31: I1Ii111 . OoOoOO00 / O0
    o000O0o = { 'group_name' : unicode ( O00O0oOO00O00 )
 , 'api_path' : i1
 , 'tag_id' : str ( Oo00 )
 }
    o00OO00OoO . append ( o000O0o )
    if 42 - 42: OoOoOO00
    if 41 - 41: Oo0Ooo . ooOoO0o + O0 * o0oOOo0O0Ooo % Oo0Ooo * Oo0Ooo
  except Exception as O0OOO00oo :
   print ( O0OOO00oo )
   if 19 - 19: iII111i
  return o00OO00OoO
  if 46 - 46: I1ii11iIi11i - Ii1I . iIii1I11I1II1 / I1ii11iIi11i
  if 7 - 7: i1IIi / I1IiiI * I1Ii111 . IiII . iIii1I11I1II1
  if 13 - 13: OOooOOo / i11iIiiIii
 def GetCategoryList ( self , stype , tag_id , api_path , page_int , in_sort ) :
  o00OO00OoO = [ ]
  Iiii = False
  if 75 - 75: OoOoOO00 % o0oOOo0O0Ooo % o0oOOo0O0Ooo . I1Ii111
  try :
   if 'categories' in api_path :
    O00Oo000ooO0 = '/api/categories/contents.json'
    if 5 - 5: o0oOOo0O0Ooo * ooOoO0o + OoOoOO00 . OOooOOo + OoOoOO00
    oO = { }
    if stype == 'genres' :
     oO [ 'genre' ] = tag_id
    else :
     oO [ 'tag' ] = tag_id
     if 7 - 7: o0oOOo0O0Ooo - I1IiiI
    oO [ 'order' ] = in_sort
    if page_int > 1 :
     oO [ 'page' ] = str ( page_int - 1 )
     if 100 - 100: oO0o + I11i . OOooOOo * Ii1I
    Ooooo0Oo00oO0 = self . makeurl ( self . API_DOMAIN , O00Oo000ooO0 , oO )
    if 73 - 73: i1IIi + I1IiiI
   else :
    O00Oo000ooO0 = '/api/' + api_path + '.json'
    if 46 - 46: OoO0O00 . Oo0Ooo - OoooooooOO
    if page_int > 1 :
     oO = { }
     oO [ 'page' ] = str ( page_int )
     Ooooo0Oo00oO0 = self . makeurl ( self . API_DOMAIN , O00Oo000ooO0 , oO )
    else :
     Ooooo0Oo00oO0 = self . makeurl ( self . API_DOMAIN , O00Oo000ooO0 )
     if 93 - 93: iII111i
     if 10 - 10: I11i
     if 82 - 82: I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
   if api_path == 'arrivals/latest' :
    II = self . GetDefaultCookies2 ( )
    iIIIi1 = self . SESSION . Request2 ( Ooooo0Oo00oO0 , params = None , cookie = II )
   else :
    II = self . GetDefaultCookies ( )
    OOooo0000ooo = self . SESSION . Request ( Ooooo0Oo00oO0 , params = None , cookie = II )
    iIIIi1 = json . loads ( OOooo0000ooo )
    if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
    if 37 - 37: iII111i - ooOoO0o * oO0o % i11iIiiIii - I1Ii111
    if 83 - 83: I11i / I1IiiI
   if not ( 'contents' in iIIIi1 ) : return o00OO00OoO , Iiii
   oO00O0O0O = iIIIi1 [ 'contents' ]
   Iiii = iIIIi1 [ 'meta' ] [ 'has_next' ]
   if 34 - 34: IiII
   for O0o0O00Oo0o0 in oO00O0O0O :
    oOo = O0o0O00Oo0o0 [ 'code' ]
    oOO00Oo = O0o0O00Oo0o0 [ 'content_type' ]
    i1iIIIi1i = O0o0O00Oo0o0 [ 'title' ]
    iI1iIIiiii = O0o0O00Oo0o0 [ 'story' ]
    if O0o0O00Oo0o0 [ 'thumbnail' ] != None :
     i1iI11i1ii11 = O0o0O00Oo0o0 [ 'thumbnail' ] [ 'medium' ]
    else :
     i1iI11i1ii11 = O0o0O00Oo0o0 [ 'stillcut' ] [ 'medium' ]
    OOooo0O00o = O0o0O00Oo0o0 [ 'year' ]
    oOOoOooOo = O0o0O00Oo0o0 [ 'film_rating_code' ]
    O000oo = O0o0O00Oo0o0 [ 'film_rating_short' ]
    if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
    if 45 - 45: oO0o - IiII - OoooooooOO - OoO0O00 . II111iiii / O0
    oo0o00O = { }
    oo0o00O [ 'mpaa' ] = O0o0O00Oo0o0 [ 'film_rating_long' ]
    oo0o00O [ 'year' ] = O0o0O00Oo0o0 [ 'year' ]
    oo0o00O [ 'title' ] = O0o0O00Oo0o0 [ 'title' ]
    if 51 - 51: Ii1I - OoO0O00 * iII111i
    if oOO00Oo == 'movies' :
     oo0o00O [ 'mediatype' ] = 'movie'
     oo0o00O [ 'duration' ] = O0o0O00Oo0o0 [ 'duration' ]
    else :
     oo0o00O [ 'mediatype' ] = 'episode'
     if 66 - 66: OoooooooOO + O0
     if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
    o000O0o = { 'code' : oOo
 , 'content_type' : oOO00Oo
 , 'title' : unicode ( i1iIIIi1i )
 , 'story' : unicode ( iI1iIIiiii )
 , 'thumbnail' : i1iI11i1ii11
 , 'year' : OOooo0O00o
 , 'film_rating_code' : oOOoOooOo
 , 'film_rating_short' : O000oo
 , 'info' : oo0o00O
 }
    o00OO00OoO . append ( o000O0o )
    if 41 - 41: Ii1I - O0 - O0
    if 68 - 68: OOooOOo % I1Ii111
  except Exception as O0OOO00oo :
   print ( O0OOO00oo )
   if 88 - 88: iIii1I11I1II1 - ooOoO0o + OOooOOo
  return o00OO00OoO , Iiii
  if 40 - 40: I1IiiI * Ii1I + OOooOOo % iII111i
  if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
 def GetCategoryList_morepage ( self , stype , tag_id , api_path , page_int , in_sort ) :
  Iiii = False
  if 23 - 23: O0
  if not ( 'categories' in api_path ) : return True
  if 85 - 85: Ii1I
  try :
   O00Oo000ooO0 = '/api/categories/contents.json'
   if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
   oO = { }
   if stype == 'genres' :
    oO [ 'genre' ] = tag_id
   else :
    oO [ 'tag' ] = tag_id
    if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + iII111i / OoOoOO00
   oO [ 'order' ] = in_sort
   if page_int > 1 :
    oO [ 'page' ] = str ( page_int - 1 )
    if 84 - 84: ooOoO0o * II111iiii + Oo0Ooo
   Ooooo0Oo00oO0 = self . makeurl ( self . API_DOMAIN , O00Oo000ooO0 , oO )
   if 53 - 53: iII111i % II111iiii . IiII - iIii1I11I1II1 - IiII * II111iiii
   II = self . GetDefaultCookies ( )
   if 77 - 77: iIii1I11I1II1 * OoO0O00
   OOooo0000ooo = self . SESSION . Request ( Ooooo0Oo00oO0 , params = None , cookie = II )
   iIIIi1 = json . loads ( OOooo0000ooo )
   if 95 - 95: I1IiiI + i11iIiiIii
   Iiii = iIIIi1 [ 'meta' ] [ 'has_next' ]
   if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
  except Exception as O0OOO00oo :
   print ( O0OOO00oo )
   if 80 - 80: II111iiii
  return Iiii
  if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
  if 53 - 53: II111iiii
  if 31 - 31: OoO0O00
 def GetEpisodoList ( self , program_code , page_int , orderby = 'asc' ) :
  o00OO00OoO = [ ]
  Iiii = False
  o0O = ''
  if 2 - 2: iIii1I11I1II1 / oO0o + OoO0O00 / OOooOOo
  if 9 - 9: o0oOOo0O0Ooo . ooOoO0o - Oo0Ooo - oO0o + II111iiii * i11iIiiIii
  try :
   O00Oo000ooO0 = '/api/contents/' + program_code + '/tv_episodes.json'
   oO = { 'all' : 'true' }
   if 79 - 79: oO0o % I11i % I1IiiI
   Ooooo0Oo00oO0 = self . makeurl ( self . API_DOMAIN , O00Oo000ooO0 , oO )
   II = self . GetDefaultCookies ( )
   if 5 - 5: OoooooooOO % OoOoOO00 % oO0o % iII111i
   OOooo0000ooo = self . SESSION . Request ( Ooooo0Oo00oO0 , params = None , cookie = II )
   iIIIi1 = json . loads ( OOooo0000ooo )
   if 7 - 7: II111iiii + OoooooooOO . I1Ii111 . ooOoO0o - o0oOOo0O0Ooo
   if not ( 'tv_episode_codes' in iIIIi1 ) : return o00OO00OoO , Iiii
   oO00O0O0O = iIIIi1 [ 'tv_episode_codes' ]
   if 26 - 26: Oo0Ooo / IiII % iIii1I11I1II1 / IiII + I11i
   oOO0O00oO0Ooo = len ( oO00O0O0O )
   oO0Oo0O0o = int ( oOO0O00oO0Ooo // ( self . EPISODE_LIMIT + 1 ) ) + 1
   if 99 - 99: oO0o . iII111i + ooOoO0o % oO0o . i11iIiiIii % O0
   if orderby == 'desc' :
    oOO00O = ( oOO0O00oO0Ooo - 1 ) - ( ( page_int - 1 ) * self . EPISODE_LIMIT )
   else :
    oOO00O = ( page_int - 1 ) * self . EPISODE_LIMIT
    if 77 - 77: Oo0Ooo - i1IIi - I11i . OoOoOO00
   for IiI1i in range ( self . EPISODE_LIMIT ) :
    if orderby == 'desc' :
     o0Oo00 = oOO00O - IiI1i
     if o0Oo00 < 0 : break
    else :
     o0Oo00 = oOO00O + IiI1i
     if o0Oo00 >= oOO0O00oO0Ooo : break
     if 32 - 32: o0oOOo0O0Ooo . IiII * I11i
    if o0O != '' : o0O += ','
    o0O += oO00O0O0O [ o0Oo00 ]
    if 93 - 93: o0oOOo0O0Ooo % i1IIi . Ii1I . i11iIiiIii
   if oO0Oo0O0o > page_int : Iiii = True
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
  except Exception as O0OOO00oo :
   print ( O0OOO00oo )
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
   if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
   if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
  try :
   if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
   oO = { 'codes' : o0O }
   if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
   Ooooo0Oo00oO0 = self . makeurl ( self . API_DOMAIN , O00Oo000ooO0 , oO )
   II = self . GetDefaultCookies ( )
   if 63 - 63: OoOoOO00 * iII111i
   OOooo0000ooo = self . SESSION . Request ( Ooooo0Oo00oO0 , params = None , cookie = II )
   iIIIi1 = json . loads ( OOooo0000ooo )
   if 69 - 69: O0 . OoO0O00
   if not ( 'tv_episodes' in iIIIi1 ) : return o00OO00OoO
   if 49 - 49: I1IiiI - I11i
   oO00O0O0O = iIIIi1 [ 'tv_episodes' ]
   if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
   for O0o0O00Oo0o0 in oO00O0O0O :
    oOo = O0o0O00Oo0o0 [ 'code' ]
    if 62 - 62: OoooooooOO * I1IiiI
    if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
    if O0o0O00Oo0o0 [ 'title' ] :
     i1iIIIi1i = O0o0O00Oo0o0 [ 'title' ]
    else :
     i1iIIIi1i = ''
    i1iI11i1ii11 = O0o0O00Oo0o0 [ 'stillcut' ] [ 'medium' ]
    i1OOoO = O0o0O00Oo0o0 [ 'display_number' ]
    OO0O000 = O0o0O00Oo0o0 [ 'tv_season_title' ]
    if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
    if 77 - 77: OOooOOo * iIii1I11I1II1
    oo0o00O = { }
    oo0o00O [ 'mediatype' ] = 'episode'
    oo0o00O [ 'tvshowtitle' ] = unicode ( i1iIIIi1i ) if i1iIIIi1i else unicode ( OO0O000 )
    oo0o00O [ 'title' ] = '%s %s' % ( unicode ( OO0O000 ) , unicode ( i1OOoO ) ) if i1iIIIi1i else unicode ( i1OOoO )
    oo0o00O [ 'duration' ] = O0o0O00Oo0o0 [ 'duration' ]
    try :
     if 98 - 98: I1IiiI % Ii1I * OoooooooOO
     oo0o00O [ 'episode' ] = O0o0O00Oo0o0 [ 'episode_number' ]
    except :
     None
     if 51 - 51: iIii1I11I1II1 . OoOoOO00 / oO0o + o0oOOo0O0Ooo
    o000O0o = { 'code' : oOo

    # OoooooooOO - ooOoO0o
    , 'title' : unicode ( i1iIIIi1i )
 , 'thumbnail' : i1iI11i1ii11
 , 'display_num' : unicode ( i1OOoO )
 , 'season_title' : unicode ( OO0O000 )

    , 'info' : oo0o00O
 }
    if 74 - 74: iII111i + o0oOOo0O0Ooo
    o00OO00OoO . append ( o000O0o )
    if 71 - 71: Oo0Ooo % OOooOOo
  except Exception as O0OOO00oo :
   print ( O0OOO00oo )
   if 98 - 98: I11i % i11iIiiIii % ooOoO0o + Ii1I
   if 78 - 78: I1ii11iIi11i % oO0o / iII111i - iIii1I11I1II1
  return o00OO00OoO , Iiii
  if 69 - 69: I1Ii111
  if 11 - 11: I1IiiI
  if 16 - 16: Ii1I + IiII * O0 % i1IIi . I1IiiI
 def GetSearchList ( self , search_key , page_int ) :
  Oo0OO = [ ]
  Iiii = False
  if 78 - 78: OOooOOo - OoooooooOO - I1ii11iIi11i / ooOoO0o / II111iiii
  try :
   O00Oo000ooO0 = '/api/search.json'
   if 29 - 29: I1IiiI % I1IiiI
   oO = { 'query' : search_key
 , 'page' : str ( page_int )
 , 'per' : str ( self . SEARCH_LIMIT )
 , 'exclude' : 'limited'
 }
   if 94 - 94: iIii1I11I1II1 / Oo0Ooo % iII111i * iII111i * II111iiii
   Ooooo0Oo00oO0 = self . makeurl ( self . API_DOMAIN , O00Oo000ooO0 , oO )
   if 29 - 29: OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / OOooOOo * iIii1I11I1II1
   II = self . GetDefaultCookies ( )
   if 62 - 62: OOooOOo / oO0o - OoO0O00 . I11i
   OOooo0000ooo = self . SESSION . Request ( Ooooo0Oo00oO0 , params = None , cookie = II )
   iIIIi1 = json . loads ( OOooo0000ooo )
   if 11 - 11: I1ii11iIi11i . OoO0O00 * IiII * OoooooooOO + ooOoO0o
   if not ( 'results' in iIIIi1 ) : return Oo0OO , Iiii
   oO00O0O0O = iIIIi1 [ 'results' ]
   Iiii = iIIIi1 [ 'meta' ] [ 'has_next' ]
   if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
   for O0o0O00Oo0o0 in oO00O0O0O :
    oOo = O0o0O00Oo0o0 [ 'code' ]
    oOO00Oo = O0o0O00Oo0o0 [ 'content_type' ]
    i1iIIIi1i = O0o0O00Oo0o0 [ 'title' ]
    iI1iIIiiii = O0o0O00Oo0o0 [ 'story' ]
    if O0o0O00Oo0o0 [ 'thumbnail' ] != None :
     i1iI11i1ii11 = O0o0O00Oo0o0 [ 'thumbnail' ] [ 'medium' ]
    else :
     i1iI11i1ii11 = O0o0O00Oo0o0 [ 'stillcut' ] [ 'medium' ]
    OOooo0O00o = O0o0O00Oo0o0 [ 'year' ]
    oOOoOooOo = O0o0O00Oo0o0 [ 'film_rating_code' ]
    O000oo = O0o0O00Oo0o0 [ 'film_rating_short' ]
    if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
    if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
    oo0o00O = { }
    oo0o00O [ 'mpaa' ] = O0o0O00Oo0o0 [ 'film_rating_long' ]
    oo0o00O [ 'year' ] = O0o0O00Oo0o0 [ 'year' ]
    oo0o00O [ 'title' ] = O0o0O00Oo0o0 [ 'title' ]
    if 26 - 26: Ii1I % I1ii11iIi11i
    if oOO00Oo == 'movies' :
     oo0o00O [ 'mediatype' ] = 'movie'
     oo0o00O [ 'duration' ] = O0o0O00Oo0o0 [ 'duration' ]
    else :
     oo0o00O [ 'mediatype' ] = 'episode'
     if 76 - 76: IiII * iII111i
     if 52 - 52: OOooOOo
    o000O0o = { 'code' : oOo
 , 'content_type' : oOO00Oo
 , 'title' : unicode ( i1iIIIi1i )
 , 'story' : unicode ( iI1iIIiiii )
 , 'thumbnail' : i1iI11i1ii11
 , 'year' : OOooo0O00o
 , 'film_rating_code' : oOOoOooOo
 , 'film_rating_short' : O000oo
 , 'info' : oo0o00O
 }
    Oo0OO . append ( o000O0o )
    if 19 - 19: I1IiiI
    if 25 - 25: Ii1I / ooOoO0o
  except Exception as O0OOO00oo :
   print ( O0OOO00oo )
   if 31 - 31: OOooOOo . O0 % I1IiiI . o0oOOo0O0Ooo + IiII
  return Oo0OO , Iiii
  if 71 - 71: I1Ii111 . II111iiii
  if 62 - 62: OoooooooOO . I11i
 def GetProfilesList ( self ) :
  II1III = [ ]
  if 61 - 61: OoOoOO00 - OOooOOo - i1IIi
  try :
   O00Oo000ooO0 = '/manage_profiles'
   Ooooo0Oo00oO0 = self . makeurl ( self . API_DOMAIN , O00Oo000ooO0 )
   II = self . GetDefaultCookies ( )
   OOooo0000ooo = self . SESSION . Request ( Ooooo0Oo00oO0 , params = None , cookie = II )
   if 25 - 25: O0 * I11i + I1ii11iIi11i . o0oOOo0O0Ooo . o0oOOo0O0Ooo
   if 58 - 58: I1IiiI
   if 53 - 53: i1IIi
   if 59 - 59: o0oOOo0O0Ooo
   if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
   if 73 - 73: I11i % i11iIiiIii - I1IiiI
   if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
   if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
   ii = re . findall ( '/api/users/me.{5000}' , OOooo0000ooo ) [ 0 ]
   ii = ii . replace ( '&quot;' , '' )
   II1III = re . findall ( 'Normal,code:[A-Za-z0-9]{13},name:|Virtual,code:[A-Za-z0-9]{13},name:' , ii )
   if 68 - 68: iII111i - I1IiiI / I1Ii111 / I11i
   for IiI1i in range ( len ( II1III ) ) :
    I11iiii = II1III [ IiI1i ]
    if 60 - 60: I11i . i1IIi + IiII / o0oOOo0O0Ooo . II111iiii
    if 82 - 82: I1ii11iIi11i / I1IiiI % iIii1I11I1II1 / i1IIi - I1IiiI
    if 7 - 7: I1Ii111 * OoO0O00 - ooOoO0o + OOooOOo * I1IiiI % OoO0O00
    I11iiii = I11iiii . split ( ':' ) [ 1 ]
    II1III [ IiI1i ] = I11iiii . split ( ',' ) [ 0 ]
    if 15 - 15: OoOoOO00 % I1IiiI * I11i
  except Exception as O0OOO00oo :
   print ( O0OOO00oo )
   if 81 - 81: ooOoO0o - iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * I11i
  return II1III
  if 20 - 20: oO0o % IiII
  if 19 - 19: I1ii11iIi11i % IiII + ooOoO0o / I1Ii111 . ooOoO0o
 def GetProfilesConvert ( self , usercd ) :
  IiIi1I1 = ''
  if 39 - 39: II111iiii + OoOoOO00 - ooOoO0o . OoOoOO00
  try :
   O00Oo000ooO0 = '/api/users/' + usercd + '/convert'
   Ooooo0Oo00oO0 = self . makeurl ( self . API_DOMAIN , O00Oo000ooO0 )
   if 84 - 84: OoO0O00 + i1IIi - II111iiii . I1ii11iIi11i * OoooooooOO + I1IiiI
   II = self . GetDefaultCookies ( )
   if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
   oOoOooOo0o0 = self . SESSION . RequestCookie ( Ooooo0Oo00oO0 , payload = None , cookie = II )
   if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
   for OoOo in oOoOooOo0o0 . split ( ',' ) :
    OoOo = OoOo . strip ( )
    if OoOo . startswith ( '_s_guitv' ) :
     O0O0o0oOOO = OoOo . split ( ';' ) [ 0 ]
     O0O0o0oOOO = O0O0o0oOOO . split ( '=' ) [ 1 ]
     if 67 - 67: OoOoOO00 + I1ii11iIi11i . o0oOOo0O0Ooo . II111iiii
   if O0O0o0oOOO :
    IiIi1I1 = O0O0o0oOOO
    if 98 - 98: iII111i
  except Exception as O0OOO00oo :
   IiIi1I1 = ''
   if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / II111iiii % Oo0Ooo
  return IiIi1I1
  if 38 - 38: ooOoO0o - OOooOOo / iII111i
  if 66 - 66: O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / Ii1I + I1ii11iIi11i
 def GetStreamingURL ( self , movie_code , quality_str ) :
  ooo00Ooo = Oo0o0O00 = ii1 = ''
  if 39 - 39: Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * iII111i + I1IiiI
  try :
   O00Oo000ooO0 = '/api/watch/' + movie_code + '.json'
   if 77 - 77: Ii1I + II111iiii . OoOoOO00 * I1Ii111 + OOooOOo + OOooOOo
   Ooooo0Oo00oO0 = self . makeurl ( self . API_DOMAIN , O00Oo000ooO0 )
   if 9 - 9: I11i % OoooooooOO . oO0o % I11i
   II = self . GetDefaultCookies ( )
   II . append ( ( 'x-watchaplay-client-codec-flag' , '3' ) )
   II . append ( ( 'x-watchaplay-media-devices-info' , '7' ) )
   II . append ( ( 'x-watchaplay-screen' , quality_str ) )
   if 32 - 32: i11iIiiIii
   OOooo0000ooo = self . SESSION . Request ( Ooooo0Oo00oO0 , params = None , cookie = II )
   if 31 - 31: iIii1I11I1II1 / OoO0O00 / I1ii11iIi11i
   iIIIi1 = json . loads ( OOooo0000ooo )
   if 41 - 41: Oo0Ooo
   ooo00Ooo = iIIIi1 [ 'streams' ] [ 0 ] [ 'source' ]
   if ooo00Ooo == None : return ( ooo00Ooo , Oo0o0O00 , ii1 )
   if 10 - 10: Oo0Ooo / Oo0Ooo / I1Ii111 . I1Ii111
   if 'subtitles' in iIIIi1 [ 'streams' ] [ 0 ] :
    for OOoo in iIIIi1 [ 'streams' ] [ 0 ] [ 'subtitles' ] :
     if OOoo [ 'lang' ] == 'ko' :
      Oo0o0O00 = OOoo [ 'url' ]
      break
      if 50 - 50: OoO0O00
      if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
   i1iI1 = iIIIi1 [ 'ping_payload' ]
   i11ii1ii11i = self . WATCHA_USERCD
   ooO0OoOO = '{\"merchant\":\"giitd_frograms\",\"sessionId\":\"%s\",\"userId\":\"%s\"}' % ( i1iI1 , i11ii1ii11i )
   if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
   ii1 = base64 . b64encode ( ooO0OoOO )
   if 41 - 41: i1IIi - I11i - Ii1I
   if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
  except Exception as O0OOO00oo :
   return ( ooo00Ooo , Oo0o0O00 , ii1 )
   if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + ooOoO0o
   if 44 - 44: II111iiii
  return ( ooo00Ooo , Oo0o0O00 , ii1 )
  if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
  if 35 - 35: iIii1I11I1II1
  if 42 - 42: I1Ii111 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
