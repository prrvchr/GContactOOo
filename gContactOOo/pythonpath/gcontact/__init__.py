#!
# -*- coding: utf-8 -*-

"""
╔════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                    ║
║   Copyright (c) 2020 https://prrvchr.github.io                                     ║
║                                                                                    ║
║   Permission is hereby granted, free of charge, to any person obtaining            ║
║   a copy of this software and associated documentation files (the "Software"),     ║
║   to deal in the Software without restriction, including without limitation        ║
║   the rights to use, copy, modify, merge, publish, distribute, sublicense,         ║
║   and/or sell copies of the Software, and to permit persons to whom the Software   ║
║   is furnished to do so, subject to the following conditions:                      ║
║                                                                                    ║
║   The above copyright notice and this permission notice shall be included in       ║
║   all copies or substantial portions of the Software.                              ║
║                                                                                    ║
║   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,                  ║
║   EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES                  ║
║   OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.        ║
║   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY             ║
║   CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,             ║
║   TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE       ║
║   OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                                    ║
║                                                                                    ║
╚════════════════════════════════════════════════════════════════════════════════════╝
"""

import traceback
try:
    from .user import User
    from .datasource import DataSource
    from .dataparser import DataParser
    from .connection import Connection
    from .provider import Provider
    from .replicator import Replicator

    from .configuration import g_identifier
    from .configuration import g_extension
    from .configuration import g_host
    from .configuration import g_url

    from .dbinit import getDataSourceUrl

    from .dbconfig import g_path

    from .dbtools import getDataSourceConnection
    from .dbtools import getDataBaseInfo
    from .dbtools import getDataSourceLocation
    from .dbtools import getDataSourceJavaInfo
    from .dbtools import getSqlException

    from .logger import getLoggerSetting
    from .logger import getLoggerUrl
    from .logger import setLoggerSetting
    from .logger import clearLogger
    from .logger import logMessage
    from .logger import getMessage

except Exception as e:
    print("gcontact.__init__() ERROR: %s - %s" % (e, traceback.print_exc()))

