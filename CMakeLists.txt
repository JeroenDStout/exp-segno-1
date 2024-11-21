#
# Initial set-up
#

cmake_minimum_required(VERSION 3.15)

# Project
project(segno)
include(cmake/generic/project.cmake)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)

# Languages
include(cmake/generic/cxx.cmake)
include(cmake/generic/python.cmake)

# Third party
include(cmake/generic/eigen.cmake)
include(cmake/generic/nanobind.cmake)
include(cmake/generic/antlr.cmake)

# Support
include(cmake/generic/outputs.cmake)
include(cmake/generic/artefacts.cmake)
include(cmake/generic/sources.cmake)
include(cmake/generic/assets.cmake)
include(cmake/generic/publish.cmake)

# Processing
include(cmake/segno/core.cmake)

# Subprojects
add_subdirectory(src/segno)
add_subdirectory(src/exp_core)
add_subdirectory(src/exp_live)
add_subdirectory(src/exp_py)
add_subdirectory(src/repo_version)

# Publication
finalise_publish()
