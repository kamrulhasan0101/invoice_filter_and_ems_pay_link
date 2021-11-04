# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class StudentPayslip(models.Model):
    _inherit = "student.payslip"
    _description = "Student PaySlip"

    def invoice_link(self):
        """View number of invoice of student"""
        return {
            'type': 'ir.actions.act_url',
            'url': 'my/invoices',
            'target': 'self',
        }

    def view_invoice(self):
        """View number of invoice of student"""
        invoice_obj = self.env["account.move"]
        for rec in self:
            invoices_rec = invoice_obj.search(
                [("student_payslip_id", "=", rec.id)]
            )
            action = rec.env.ref(
                "account.action_move_out_invoice_type"
            ).read()[0]
            if len(invoices_rec) > 1:
                action["domain"] = [("id", "in", invoices_rec.ids)]
            elif len(invoices_rec) == 1:
                action["views"] = [
                    (rec.env.ref("account.view_move_form").id, "form")
                ]
                action["res_id"] = invoices_rec.ids[0]
            else:
                action = {"type": "ir.actions.act_window_close"}
        return action
