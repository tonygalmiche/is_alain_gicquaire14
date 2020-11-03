# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
import datetime


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    is_cle_licence = fields.Char('Clé de licence', copy=False)


    @api.model_create_multi
    def create(self, vals):
        res = super(AccountMoveLine, self).create(vals)
        for obj in res:
            if obj.product_id.is_generer_licence:
                num_licence = "999999"
                date_achat  = datetime.date.today().strftime('%d%m%Y')
                nb_jours    = "365"
                nb_valid    = "007"
                x = num_licence+date_achat+nb_jours+nb_valid
                cle=''
                sens=1
                debut=0
                while debut<10:
                    if sens==1:
                        y=x[debut:debut+2]
                    else:
                        y=x[-debut-2:]
                        y=y[0:2]
                        debut+=2
                    cle+=y
                    sens=-sens
                obj.is_cle_licence = cle

