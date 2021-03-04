# Root files
if the file "newpatch.exe" is found, MTS will launch "MetinPatchUpdater.exe"
This behavour is similar to what METIN2 does when it launches PatchUpdater.exe is newpatch.exe is found

if a file called "console" is found, MTS will create a probably DEBUG console

If you create a file called "patch.exe" MTS will try to move "patch.exe" into "metin.exe"

# DDS Files
This should be MTS texture, crypted in an unknown way

# Command lines
"(-- )( --)" -> full screen
"( --)(-- )" -> windowed

# Tips
MTS seems that it can support English languages (check locale.tr client_string.txt) but it was not filled up

FLIP mode is enabled when the locale is "kor"

# Locale file
client_string.txt in main.tar

# General RE
set_locale_name (.text:0041220) seems to setup the language and internal files that MTS reads
locale_set_file (.text:0044116E) will be retrired by locale_get_name (.text:0044118)

MTS languages:
1 -> Korean
2 -> Chinese

Mutex: MetinBlockMutex
