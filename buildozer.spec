[app]

# (str) Title of your application
title = Resistor Calculator

# (str) Package name
package.name = resistorcalculator

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (str) Application version
version = 0.1

# (str) The main Python file to use as the entry point
entrypoint = main.py

# (list) Application requirements
requirements = python3,kivy

# (str) Presplash image
presplash.filename = presplash.png

# (str) Icon file
icon.filename = icon.png

# (bool) Whether to include the debug symbols
debug = True

# (list) Permissions your app needs
android.permissions = INTERNET

# (int) Target API level
android.api = 33

# (int) Minimum API your app supports
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (int) Build tools version
android.build_tools_version = 33.0.0

# (list) Android archs you want to support
android.arch = armeabi-v7a, arm64-v8a

