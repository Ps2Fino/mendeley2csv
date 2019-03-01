set (
    CMP0048
    NEW
)

cmake_minimum_required (
    VERSION
    3.12
)

project (
    Mendeley-2-CSV
    VERSION
        0.1
    LANGUAGES
        NONE
)

install (
    FILES
        mend2csv.py
        installer-files/LICENSE.txt
    DESTINATION
        .
)

install (
    DIRECTORY
        packages
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
    mendeley2csv
)

set (
    CPACK_PACKAGE_INSTALL_DIRECTORY
    Lancophone
)

set (
    CPACK_RESOURCE_FILE_LICENSE
    ${CMAKE_SOURCE_DIR}/installer-files/LICENSE.txt
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
    Mendeley2CSV
)

set (
    CPACK_NSIS_PACKAGE_NAME
    Mendeley2CSV
)

set (
    CPACK_NSIS_MODIFY_PATH
    ON
)

set (
    CPACK_NSIS_ENABLE_UNINSTALL_BEFORE_INSTALL
    ON
)

##############################
## Zip #######################
##############################

set (
    CPACK_SOURCE_IGNORE_FILES
    "packages/__pycache__/**;packages/parsers/__pycache__/**"
)

include (CPack)