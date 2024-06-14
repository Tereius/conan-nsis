#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conan import ConanFile
from conan.tools.files import get, copy
import json, os

required_conan_version = ">=2.0"

class NsisConan(ConanFile):

    jsonInfo = json.load(open("info.json", 'r'))
    # ---Package reference---
    name = jsonInfo["projectName"]
    version = jsonInfo["version"]
    user = jsonInfo["domain"]
    channel = "stable"
    # ---Metadata---
    description = jsonInfo["projectDescription"]
    license = jsonInfo["license"]
    author = jsonInfo["vendor"]
    topics = jsonInfo["topics"]
    homepage = jsonInfo["homepage"]
    url = jsonInfo["repository"]
    # ---Requirements---
    requires = []
    tool_requires = []
    # ---Sources---
    exports = ["info.json"]
    exports_sources = []
    # ---Binary model---
    settings = "os", "arch"
    options = {}
    default_options = {}
    # ---Build---
    generators = []
    # ---Folders---
    no_copy_source = False


    def source(self):
        source_url = "https://sourceforge.net/projects/nsis/files/NSIS%203/" + self.version + "/nsis-" + self.version + ".zip/download?use_mirror=autoselect"
        get(self, source_url, filename="nsis-%s.zip" % self.version)

    def package(self):
        copy(self, pattern="*", dst=self.package_folder, src="nsis-%s" % self.version)

    def package_info(self):
        self.output.info('Prepending to PATH environment variable: %s' % self.package_folder)
        self.buildenv_info.prepend_path("PATH", self.package_folder)
