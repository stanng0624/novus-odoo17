from odoo import models, fields, api, _
from num2words import num2words


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def compute_amount_words(self):
        for rec in self:
            if rec.amount_total:
                amount_split = str(rec.amount_total).split(".")
                if int(amount_split[1]) == 0:
                    num_word = num2words(rec.amount_total)
                    cap_word = []
                    for i in num_word.split(" "):
                        x = i.capitalize()
                        cap_word.append(x)
                    cap_word.append(rec.currency_id.currency_unit_label)
                    rec.amount_in_word = ' '.join(cap_word)
                else:
                    num_word = num2words(int(amount_split[0]))
                    cap_word = []
                    for i in num_word.split(" "):
                        x = i.capitalize()
                        cap_word.append(x)
                    cap_word.append(rec.currency_id.currency_unit_label)
                    int_w = ' '.join(cap_word)
                    # decimal
                    num_word = num2words(int(amount_split[1]))
                    cap_dec = []
                    for i in num_word.split(" "):
                        x = i.capitalize()
                        cap_dec.append(x)
                    cap_dec.append(rec.currency_id.currency_subunit_label)
                    dec_w = ' '.join(cap_dec)
                    full_word = int_w +" and "+dec_w
                    rec.amount_in_word = full_word

    amount_in_word = fields.Char(string="Total Amount In Words", compute=compute_amount_words)
