from frappe import _

def get_data():
    return [
        {
            "module_name": "Retails",
            "color": "#3498db",
            "icon": "octicon octicon-repo",
            "type": "module",
            "label": _("Retails")
        },
        {
            "label": _("Banking Module"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "module",
                    "name": "BankingModule",
                    "label": _("Custom Banking Module"),
                    "icon": "octicon octicon-briefcase",
                    "color": "#3498db",
                    "link": "#modules/BankingModule",
                    "category": _("Modules"),
                }
            ]
        }
    ]
