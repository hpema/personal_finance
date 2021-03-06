# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "personal_finance"
app_title = "Personal Finance"
app_publisher = "Hemant Pema"
app_description = "Application to manage your personal finance"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hemant@pema.co.za"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/personal_finance/css/personal_finance.css"
# app_include_js = "/assets/personal_finance/js/personal_finance.js"

# include js, css files in header of web template
# web_include_css = "/assets/personal_finance/css/personal_finance.css"
# web_include_js = "/assets/personal_finance/js/personal_finance.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "personal_finance.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "personal_finance.install.before_install"
# after_install = "personal_finance.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "personal_finance.notifications.get_notification_config"

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
# 		"personal_finance.tasks.all"
# 	],
# 	"daily": [
# 		"personal_finance.tasks.daily"
# 	],
# 	"hourly": [
# 		"personal_finance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"personal_finance.tasks.weekly"
# 	]
# 	"monthly": [
# 		"personal_finance.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "personal_finance.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "personal_finance.event.get_events"
# }

