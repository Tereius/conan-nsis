#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class NsisConan(ConanFile):
    name = "NSIS"
    version = "3.03"
    url = "https://github.com/Tereius/conan-nsis"
    homepage = "https://sourceforge.net/projects/nsis"
    description = "NSIS (Nullsoft Scriptable Install System) is a professional open source system to create Windows installers."
    license = "https://www.zlib.net/zlib_license.html"
    settings = {"os": ["Windows"]}

    def source(self):
        source_url = "https://sourceforge.net/projects/nsis/files/NSIS%203/3.03/nsis-3.03.zip/download?use_mirror=netcologne#"
        tools.get(source_url, filename="nsis-%s.zip" % self.version)

    def package(self):
        self.copy(pattern="*", src="nsis-%s" % self.version)

    def package_info(self):
        self.output.info('Adding NSIS binaries to PATH: %s' % self.package_folder)
        self.env_info.PATH.append(self.package_folder)
