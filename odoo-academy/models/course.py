# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Course(models.Model):
    _name = 'academhy.course'
    _description = 'Course'

    name = fields.Char(string='Name')
