from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
        {
			"label": _("Stock Reports"),
			"items": [
                {
					"type": "report",
					"is_query_report": True,
					"name": "Seef Stock Ledger",
					"doctype": "Stock Ledger Entry",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Seef Stock Balance",
					"doctype": "Stock Ledger Entry"
				},
            ]
        }
    ]