[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android packaging)
package.domain = org.example

# (list) Source files to include (let it include python and kv files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Add other dependencies here separated by commas (e.g., requests)
requirements = python3,kivy

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 0