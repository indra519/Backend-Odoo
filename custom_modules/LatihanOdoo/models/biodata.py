from odoo import models, fields

class Biodata (models.Model):
    _name = "odoo.biodata"

    name = fields.Char(string="Nama")
    fullname = fields.Char(string="Nama Lengkap")
    birthdate = fields.Date(string="Tanggal Lahir")
    age = fields.Integer(string="Umur")
    children = fields.Integer(string="Anak")
    photo = fields.Binary(string="Foto")
    gender = fields.Selection([('male', 'laki - laki'), ('female', 'perempuan')
    ], string="jenis_kelamin")
    education_sd = fields.Boolean(string='SD')
    education_smp = fields.Boolean(string='SMP')
    education_sltp = fields.Boolean(string='SLTP')
    education_sma = fields.Boolean(string='SMA')
    education_smk = fields.Boolean(string='SMK')
    education_smu = fields.Boolean(string='SMU')
    education_slta = fields.Boolean(string='SLTA')
    education_college = fields.Boolean(string='Kuliah')
