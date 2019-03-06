from __future__ import unicode_literals
from frappe import _


def get_data():
    return [{
        "label":
        _("Recruitment"),
        "items": [{
            "type": "doctype",
            "name": "Job Contract",
            "description": _("Job Contract"),
        }, {
            "type": "doctype",
            "name": "Joining Work",
            "description": _("Joining Work"),
        }]
    }, {
        "label":
        _("Leaves and Holiday"),
        "items": [{
            "type": "doctype",
            "name": "Vacation Settlement",
            "description": _("Vacation Settlement"),
        }]
    }, {
        "label":
        _("Expense Claims"),
        "items": [{
            "type": "doctype",
            "name": "Mandate Form",
            "description": _("Mandate Form"),
        }]
    }, {
        "label":
        _("Employee Document"),
        "items": [{
            "type": "doctype",
            "name": "Issuance Documents",
            "description": _("Issuance Documents"),
        }]
    }, {
        "label":
        _("Violation"),
        "items": [{
            "type": "doctype",
            "name": "Violation",
            "description": _("Violation"),
        }, {
            "type": "doctype",
            "name": "Violation Type",
            "description": _("Violation Type"),
        }]
    }, {
        "label":
        _("Employee and Attendance"),
        "items": [{
            "type": "doctype",
            "name": "Receipt Custody",
            "description": _("Receipt Custody"),
        }, {
            "type": "doctype",
            "name": "Employee Certificate",
            "description": _("Employee Certificate"),
        }, {
            "type": "doctype",
            "name": "Experience Certificate",
            "description": _("Experience Certificate"),
        }, {
            "type": "doctype",
            "name": "Final Settlement",
            "description": _("Final Settlement"),
        }]
    }]
