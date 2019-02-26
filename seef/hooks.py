# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "seef"
app_title = "seef App"
app_publisher = "Accurate Systems"
app_description = "seef customization"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@accuratesystems.com.sa"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/seef/css/seef.css"
# app_include_js = "/assets/seef/js/seef.js"

# include js, css files in header of web template
# web_include_css = "/assets/seef/css/seef.css"
# web_include_js = "/assets/seef/js/seef.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Journal Entry" : "public/js/journal_entry.js"}
# doctype_list_js = {"Purchase Invoice" : "public/js/purchase_invoice.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "seef.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "seef.install.before_install"
# after_install = "seef.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "seef.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"seef.tasks.all"
# 	],
# 	"daily": [
# 		"seef.tasks.daily"
# 	],
# 	"hourly": [
# 		"seef.tasks.hourly"
# 	],
# 	"weekly": [
# 		"seef.tasks.weekly"
# 	]
# 	"monthly": [
# 		"seef.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "seef.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "seef.event.get_events"
# }

