"""Tiny helper endpoints for quick demos."""

import frappe


@frappe.whitelist(allow_guest=True)
def quick_hello(name: str | None = None) -> dict[str, str]:
    """Return a friendly greeting for onboarding and smoke testing.

    Args:
        name: Optional visitor name to personalize the message.

    Returns:
        A JSON-serializable dict with a greeting message.
    """

    visitor = name.strip() if name else "there"
    message = f"Hello, {visitor}! Welcome to your first Frappe app."
    return {"message": message}
