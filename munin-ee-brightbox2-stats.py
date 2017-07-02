#!/usr/bin/env python

import requests
import md5
import re
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('brightbox.cfg')

host = config.get('brightbox','host')
user = config.get('brightbox','user')
password = config.get('brightbox','password')

pc = md5.new(password).hexdigest()
print pc

endpoint = "http://%s/login.cgi" % (host)

post_data = { 'usr': user, 'pws': pc, 'GO':'status.htm'}

r = requests.post(endpoint, data = post_data)

print endpoint
print r.text

urn_re = "new_urn\ \=\ '(.*)'"
urn = re.search(urn_re,r.text).group(1)
cookies = dict(urn=urn)
print urn


endpoint = "http://%s/cgi/cgi_dsl_status.js" % (host)
print endpoint
r = requests.get(endpoint,cookies=cookies)
print r.text


endpoint = "http://%s/status_conn.xml" % (host)
print endpoint
r = requests.get(endpoint,cookies=cookies)
print r.text

endpoint = "http://%s/logout.cgi" % (host)
print endpoint
r = requests.post(endpoint,cookies=cookies)
print r.text


