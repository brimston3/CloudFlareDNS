#!/usr/bin/env python

import os,re
import urllib
import sys
import json

cloudflareEmail="EMAIL@EXAMPLE.COM" #CF Login Email Address
cloudflareAPIkey="cloudflareapikeylowercase"    #API Key as shown on https://www.cloudflare.com/my-account
baseDomain='yourdomain.com' #Domain Name as shown on https://www.cloudflare.com/my-websites.html
recordType='A'      #See "Type" Column on https://www.cloudflare.com/dns-settings?z=example.com
recordName='yoursubdomain'  #See "Name" Column on https://www.cloudflare.com/dns-settings?z=example.com

#Find the CloudFlare ID of your (sub)domain based on the recordName and recordType
data={'a': 'rec_load_all','tkn': cloudflareAPIkey,'email': cloudflareEmail,'z': baseDomain}
data = urllib.urlencode(data)
try:
  f = urllib.urlopen("https://www.cloudflare.com/api_json.html", data)

  CFR = json.loads(f.read())
  matching_CF_recids = map((lambda r: r['rec_id']), filter((lambda o: o['display_name'] == recordName and o['type'] == recordType),CFR['response']['recs']['objs']))
  if len(matching_CF_recids) == 0 or matching_CF_recids[0] == "error" or CFR['msg'] is not None:
    recordID = CFR['msg']
  else:
    recordID = matching_CF_recids[0]
    
  print "CF Record:",recordID
  
  f = urllib.urlopen("http://ip-api.com/json")
  ip = json.loads(f.read())['query']
  print "IP Address:",ip
  
  #Update with Cloudflare
  data={'a': 'rec_edit','tkn': cloudflareAPIkey,'id': recordID,'email': cloudflareEmail,'z': baseDomain,'type': recordType,'name': recordName,'content': ip,'service_mode': '0','ttl': '1'}
  data = urllib.urlencode(data)
  f = urllib.urlopen("https://www.cloudflare.com/api_json.html", data)
  CFR = json.loads(f.read())
  print "Update:", CFR['result']
  
except:
  sys.exit(-1)
