#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    random password generator
    version 1.0
    history:
    2012-12-6  dylanninin@gmail.com first release
"""
import random
import logging
from string import letters
from string import digits
from string import punctuation

"""password generator config"""
config={
  'min':8,
  'max':32,
  'length':8,
  'cs':2,
  'ds':2,
  'ps':2,
  'users':[
     'dylanninin'
  ],
  'log':{
     'file':'passwdgen.log',
     'format':'%(asctime)s - %(name)s - %(levelname)s - %(message)s'
   }
}

"""logging config"""
logging.basicConfig(filename=config['log']['file'], format=config['log']['format']
                    ,level=logging.INFO)

"""sample count unique random chars from text"""
rsample = lambda text, size: random.sample(list(text), min(size,len(text)))


def helper(text, size):
    """
        help if sample size bigger than the length of text
    """
    result = []
    r_divmod = divmod(size, len(text))
    for i in xrange(0, r_divmod[0]):
        result += rsample(text, len(text))
    result += rsample(text, r_divmod[1])
    return result


def rpwd(length, cs, ds, ps):
    """
        generate random password based on random list
    """
    password = []
    password += helper(letters, cs)
    password += helper(digits, ds)
    password += helper(punctuation, ps)
    password += helper(letters + digits + punctuation, length - cs - ds - ps)
    random.shuffle(password)
    password = ''.join(password)
    return password


def gpwds(config):
    """
        generate passwords
    """
    pwds = []
    users = config['users']
    for i in xrange(len(users)):
        pwds.append(rpwd(config['length'], config['cs'], config['ds'], config['ps']))
    return pwds



def init(config):
    """
        initialize to test the config
    """
    pmin = config['min']
    pmax = config['max']
    length = config['length']
    cs = config['cs']
    ds = config['ds']
    ps = config['ps']
    result = cs + ds + ps
    abs_result = abs(cs) + abs(ds) + abs(ps)
    if not (pmin <= length <= pmax):
        raise StandardError('length must be between min ' + str(min) + " and max " + str(max) + " !" )
    elif not result == abs_result:
        raise StandardError('cs,ds,ps must not be smaller than 0!')
    elif result > length:
        raise StandardError('cs + ds + ps must not be bigger than length ' + str(length) + ' !')


def test():
    """
        test generating passwords based on config
    """
    message = 'password generation started ... ...'
    logging.info(message)
    init(config)
    header = '%-10s\t%-10s' % ('USERNAME','PASSWORD')
    logging.info(header)
    print header
    for pwd in zip(config['users'], gpwds(config)):
        password = '%-10s\t%-10s' % (pwd[0], pwd[1])
        print password
        logging.info(password)
    message = 'password generation ended ... ...'
    logging.info(message)

if __name__ == '__main__':
    test()
