from __future__ import unicode_literals
from frappe import _


def get_data():
    return [ {
        "label":
        _("Employee and Attendance"),
        "items": [{
            "type": "doctype",
            "name": "Accreditation Exchange",
            "description": _("Accreditation Exchange"),
        }, {
            "type": "doctype",
            "name": "Issuance Type",
            "description": _("Issuance Type"),
        }]
    }]
