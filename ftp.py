# -*- coding: utf-8 -*-
'''
pip install pyftpdlib
'''

from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer

authorizer = DummyAuthorizer()
authorizer.add_user('python', '123456', 'F:\\Working~Study', perm='elradfmwM')  # user_name, passwd, dir, permissions
handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(('0.0.0.0', 8888), handler)
server.serve_forever()
