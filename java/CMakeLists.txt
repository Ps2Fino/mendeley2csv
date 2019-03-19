set (
    CMP0048
    NEW
)

cmake_minimum_required (
    VERSION
    3.12
)

project (
    bib2xyz-gui
    VERSION
        0.2
    LANGUAGES
        NONE
)

find_package(Java REQUIRED)
include(UseJava)

# Set the source files
set (
    JAVA_GUI_SOURCE_FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/Main.java
)

# Set the target name for use later
set (
    JAR_GUI_PROG_NAME
    bib2xyz-gui
)

# Create the manifest file to be used for the jar
file (
    WRITE
        ${CMAKE_BINARY_DIR}/GUI.MF
        "Main-Class: Main\n"
)

###########################################################

# Add the jar file to the project

add_jar (
    ${JAR_GUI_PROG_NAME}
    SOURCES
        ${JAVA_GUI_SOURCE_FILES}
    MANIFEST
        ${CMAKE_BINARY_DIR}/GUI.MF
)

install_jar (
    ${JAR_GUI_PROG_NAME}
    DESTINATION
        .
)

## Get the location of the built jar
## See https://cmake.org/cmake/help/v3.0/module/UseJava.html for details
#get_property (
#    GUI_JAR
#    TARGET
#        ${JAR_GUI_PROG_NAME}
#    PROPERTY
#        INSTALL_FILES
#)