from odoo import fields, models

class CalendarEvent(models.Model):

    _inherit = "calendar.event"

    google_calendar_event_link = fields.Char(string="Google Calendar synchronized event HTML link")
    # Google Calendar doesn't use integer IDs.
    google_calendar_event_id = fields.Char(string="Google Calendar synchronized event ID")
    google_calendar_event_sync_datetime = fields.Datetime(string="Google Calendar last synchronization timestamp")
