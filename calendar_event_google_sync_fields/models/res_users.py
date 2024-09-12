from odoo import fields, models

class Users(models.Model):

    _inherit = "res.users"

    google_calendar_sync = fields.Boolean(default=False, string="Activate Google Calendar synchronization")
    google_calendar_sync_token = fields.Char(string="Google Calendar synchronization token")
