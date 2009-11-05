# -*- coding: utf-8 -*-

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from distutils.command.build import build as _build
from distutils.command.clean import clean as _clean
import os

class my_build(_build):
    def run(self):
        _build.run(self)

        # compile edje file
        import subprocess
        result = subprocess.call( "cd ./data; edje_cc -v blipomoko.edc", shell=True )
        if result != 0:
            raise Exception( "Can't build theme files. Built edje_cc?" )

class my_clean(_clean):
    def run(self):
        _clean.run(self)

        if os.path.exists('./data/blipomoko.edj'):
            os.remove('./data/blipomoko.edj')

setup(
    name = "blipomoko",
    version = "0.1.99",
    author = "Sebastian Krzyszkowiak (dos)",
    author_email = "seba.dos1@gmail.com",
    url = "http://wiki.github.com/dos1/blipomoko",
    cmdclass = { 'build'    : my_build ,
                 'clean'    : my_clean },
    scripts = [ "blipomoko" ],
    data_files = [
        ( "blipomoko", ["data/blipomoko.edj"] ),
        ]
)
