#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "DevOpsAssignment"
default_task = "publish"


@init
def set_properties(project):
    project.build_depends_on("flask")
    project.build_depends_on("jsonify")
    project.build_depends_on("requests")
