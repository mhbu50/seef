from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
        {
			"label": _("Company and Accounts"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "report",
					"name": "Seef General Ledger",
					"doctype": "GL Entry",
					"is_query_report": True,
				},
            ]
        }
    ]
