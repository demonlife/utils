
    #!/usr/bin/env python
	# -*- coding:utf-8 -*-
	
	"""
	search contact information from ldap server
	history:
	2013-2-28  dylanninin@gmail.com first release
	"""
	import sys
	import ldap
	
	#argument parse
	msg = 'Error: enter any user name to be queried\nusage: ldapsearch.py username'
	if not len(sys.argv) == 2 or not sys.argv[1]:
	    print msg
	    sys.exit()
	query = sys.argv[1]
	
	#ldap settings
	url = 'ldap://ldap.egolife.com:389'
	dn = 'cn=it,ou=admin,dc=egolife,dc=com'
	pw = 'yourpassword'
	base = 'dc=egolife,dc=com'
	filters='(&(objectClass=Account)(cn=*%s*))' % query
	attrs=['*']
	
	
	#initialize and query from ldap server
	conn = ldap.initialize(url)
	conn.simple_bind(dn,pw)
	
	result = conn.search_s(base, ldap.SCOPE_SUBTREE, filters, attrs)
	
	"""
	result = [record*]
	record = (uid='user_dn',{attr*})
	attr = name:[value*]
	
	that is:
	
	result = [(uid='user_db',{cn:['cn_value1','cn_value2'],mail:['email1','email2']})]
	
	"""
	
	#output search result
	prompt = '共查询到%d条记录。' % len(result)
	print prompt
	count = 1
	for record in result:
	    prompt = '第%d条记录：' % count
	    count += 1
	    print prompt
	    print record[0]
	    for k, v in record[1].iteritems():
	        print k,
	        for e in v:
	            print e,
	        print
	    print
