# -*- encoding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2021. All rights reserved.

from odoo import fields, models, _
import json


class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_total_tax(self):
        tax = json.loads(self.tax_totals_json)
        return tax
