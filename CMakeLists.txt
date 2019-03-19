set (
    CMP0048
    NEW
)

cmake_minimum_required (
    VERSION
    3.12
)

project (
    bib2xyz
    VERSION
        0.2.5
    LANGUAGES
        NONE
)

add_subdirectory (
    java
)

install (
    FILES
        bib2xyz.py
        license/LICENSE.txt
    DESTINATION
        .
)

install (
    DIRECTORY
        mendproc
    DESTINATION
        .
    FILES_MATCHING
    PATTERN
        "*.py"
)

##############################
## CPack specific variables ##
##############################

set (
    CPACK_GENERATOR
    ZIP
    NSIS
)

##############################
## NSIS ######################
##############################

set (
    CPACK_PACKAGE_NAME
    bib2xyz
)

set (
    CPACK_PACKAGE_DESCRIPTION_SUMMARY
    "Program for manipulating bibliographies"
)

#set (
#    CPACK_PACKAGE_EXECUTABLES
#    bib2xyz-gui;bib2xyz-gui.jar
#)

#set (
#    CPACK_TOPLEVEL_TAG
#    Lancophone
#)

#set (
#    CPACK_PACKAGE_INSTALL_DIRECTORY
#    Lancophone
#)

set (
    CPACK_RESOURCE_FILE_LICENSE
    ${CMAKE_SOURCE_DIR}/license/LICENSE.txt
)

set (
    CPACK_PACKAGE_HOMEPAGE_URL
    "http://github.com/Ps2Fino/mendeley2csv"
)

set (
    CPACK_PACKAGE_DESCRIPTION_FILE
    ${CMAKE_SOURCE_DIR}/installer-files/description.txt
)

set (
    CPACK_NSIS_DISPLAY_NAME
    bib2xyz
)

set (
    CPACK_NSIS_PACKAGE_NAME
    bib2xyz
)

set (
    CPACK_NSIS_MODIFY_PATH
    OFF
)

set (
    CPACK_NSIS_ENABLE_UNINSTALL_BEFORE_INSTALL
    OFF
)

##############################
## Zip #######################
##############################

set (
    CPACK_SOURCE_IGNORE_FILES
    "packages/__pycache__/**;packages/parsers/__pycache__/**"
)

include (CPack)