# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "express"
app_title = "Express"
app_publisher = "Accurate Systems"
app_description = "Express Sandwich App"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@accuratesystems.com.sa"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/express/css/express.css"

# include js, css files in header of web template
# web_include_css = "/assets/express/css/express.css"
# web_include_js = "/assets/express/js/express.js"

# include js in page
# page_js = {"pos": "public/js/pos.js", "point-of-sale": "public/js/pos.js","accu_pos":"public/js/pos.js"}

# include js in doctype views
doctype_js = {
    "Material Request" : "public/js/material_request.js",
    "Stock Reconciliation" : "public/js/stock_reconciliation.js",
    "Purchase Invoice" : "public/js/purchase_invoice.js",
    "Purchase Receipt" : "public/js/purchase_receipt.js",
    "Sales Invoice" : "public/js/sales_invoice.js"
    }
doctype_list_js = {
    "Stock Reconciliation" : "public/js/stock_reconciliation_list.js",
    "Purchase Invoice" : "public/js/purchase_invoice_list.js",
    "Purchase Receipt" : "public/js/purchase_receipt_list.js",
    "Sales Invoice" : "public/js/sales_invoice_list.js"
    }
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------
on_session_creation = "express.api.on_session_creation"

fixtures = [
    {
        'dt': 'Property Setter', 
        'filters':[
            ['name', 'in', [
                'Purchase Receipt Item-uom-read_only',
                'Purchase Receipt Item-read_only_onload',
                'Purchase Receipt Item-barcode-hidden'
            ]]
        ]
        }
]
# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "express.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "express.install.before_install"
# after_install = "express.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "express.notifications.get_notification_config"

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
# 		"express.tasks.all"
# 	],
# 	"daily": [
# 		"express.tasks.daily"
# 	],
# 	"hourly": [
# 		"express.tasks.hourly"
# 	],
# 	"weekly": [
# 		"express.tasks.weekly"
# 	]
# 	"monthly": [
# 		"express.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "express.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "express.event.get_events"
# }
