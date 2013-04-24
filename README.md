#utils

日常管理实用工具。

#1. passwdgen

因在日常工作中，有一部分是负责用户账号和权限分配，使用Lastpass自动生成密码容易导致密码繁多难以管理，且也有泄露的危险。于是动手写了一个简单的自动生成密码工具，主要使用Python的random和string标准库。

    
程序主要配置在passwdgen.py的config中，可以自定义：
    
    """password generator config"""
    config={
      'min':8,              #min length of password
      'max':32,             #max length of password
      'length':8,           #length of password to be generated
      'cs':2,               #min number of characters in password
      'ds':2,               #min number of digits in password
      'ps':2,               #min number of punctuation in password
      'users':[             #list of username to be assigned random password
         'dylanninin',
         'dylan',
         'ninin'
      ],
      'log':{
         'file':'passwdgen.log',
         'format':'%(asctime)s - %(name)s - %(levelname)s - %(message)s'
       }
    }
    
运行效果如下：
    
    $python passwdgen.py
    USERNAME    PASSWORD  
    dylanninin  U'13Dz/m  
    dylan       `9K7x\yJ  
    ninin       8x%df-06
    
为避免清空控制台导致生成的密码忘记，已经做了日志记录，passwdgen.log：
    
    2013-01-17 20:37:25,937 - root - INFO - password generation started ... ...
    2013-01-17 20:37:25,937 - root - INFO - USERNAME    PASSWORD  
    2013-01-17 20:37:25,937 - root - INFO - dylanninin  U'13Dz/m  
    2013-01-17 20:37:25,937 - root - INFO - dylan       `9K7x\yJ  
    2013-01-17 20:37:25,937 - root - INFO - ninin       8x%df-06  
    2013-01-17 20:37:25,937 - root - INFO - password generation ended ... ...

源代码：[passwordgen.py](https://github.com/dylanninin/utils/blob/master/passwdgen.py)

#2. ldapsearch

随着ldap使用的推广，很多信息已经集成到ldap服务器中，诸多应用如SVN、Apache、Web App等也开始逐步采用LDAP进行用户身份的认证以及权限管理。这里使用Python实现一个简单的LDAP查询服务，即根据用户名查询该用户在LDAP服务器上的信息。

运行效果如下：

    [dev@scripts~]$ ./ldapsearch.py  dylanninin
    共查询到1条记录。
    第1条记录：
    uid=yanxin,ou=Personnel,dc=egolife,dc=com
    cn dylanninin
    description Life is shot, I use Python!
    mobile 0
    sn gogh
    sex Male
    mail dylanninin@gmail.com
    givenName dylanninin
    uid dylanninin

源代码：[ldapsearch.py](https://github.com/dylanninin/utils/blob/master/ldapsearch.py)
