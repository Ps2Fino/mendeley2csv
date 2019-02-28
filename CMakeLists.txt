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
        license/LICENSE.txt
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

set (
    CPACK_PACKAGE_NAME
    mendeley2csv
)

if (WIN32)

set (
    CPACK_PACKAGE_INSTALL_DIRECTORY
    "Lancophone\\${CPACK_PACKAGE_NAME}"
)

endif ()

set (
    CPACK_RESOURCE_FILE_LICENSE
    ${CMAKE_SOURCE_DIR}/license/LICENSE.txt
)

set (
    CPACK_PACKAGE_HOMEPAGE_URL
    "http://github.com/Ps2Fino/mendeley2csv"
)

if (WIN32)

set (
    CPACK_PACKAGE_DESCRIPTION_FILE
    ${CMAKE_SOURCE_DIR}/cpack/description.txt
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

endif ()

include (CPack)