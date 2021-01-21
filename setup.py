#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Gyula Istvan Geza Jozsa, Paolo Serra, Kshitij Thorat, Sphesihle Makhatini, NRF (Square Kilometre Array South Africa) - All Rights Reserved
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import os
from setuptools import setup

pkg='sunblocker'

build_root=os.path.dirname(__file__)

def readme():
    with open(os.path.join(build_root, 'README.md')) as f:
        return f.read()

def requirements():
    with open(os.path.join(build_root, 'requirements.txt')) as f:
        return [pname.strip() for pname in f.readlines()]

def src_pkg_dirs(pkg_name):
    mbdir = os.path.join(build_root, pkg_name)
    # Ignore
    pkg_dirs = []
    l = len(mbdir) + len(os.sep)
    exclude = ['docs', '.git', '.svn', 'CMakeFiles']
    for root, dirs, files in os.walk(mbdir, topdown=True):
        # Prune out everything we're not interested in
        # from os.walk's next yield.
        dirs[:] = [d for d in dirs if d not in exclude]

        for d in dirs:
            # Take everything after that ('src...') and
            # append a '/*.*' to it
            pkg_dirs.append(os.path.join(root[l:], d, '*.*'))
    return pkg_dirs

setup(name=pkg,
      version="1.0.1",
      description=' A (python pyrap) method to remove solar-like RFI from interferometric data',
      long_description=readme(),
      url='https://github.com/gigjozsa/sunblocker',
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Astronomy"],
      author='Gyula I. G. Jozsa, Sphesihle Makhathini, Paolo Serra, Kshitij Thorath, Ben Hugo',
      author_email='jozsa@ska.ac.za',
      license='GNU GPL v2',
      packages=[pkg],
      install_requires=requirements(),
      package_data={pkg: src_pkg_dirs(pkg)},
      include_package_data=True,
      python_requires='>=2.6',
)
