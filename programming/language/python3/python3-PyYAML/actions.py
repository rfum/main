#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "PyYAML-%s" % get.srcVERSION()

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "examples")
    pisitools.dodoc("LICENSE", "PKG-INFO", "README")
