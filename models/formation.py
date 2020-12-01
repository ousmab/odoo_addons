from odoo import models,fields

class Registration(models.Model):
    _name ="registration.registration"
    description=""

    name = fields.Char(string='nom',required=True,readonly=False)
    code = fields.Char(string='Code',default='001')
    description = fields.Text(string='description')
    start_date = fields.Date("date de debut",help="date")
    end_date = fields.Date("date de fin",help="date")
    year_id = fields.Many2one("year.year",string='Année')
    cycle_id = fields.Many2one('cycle.cycle', string='Cycle')
    claim_ids = fields.One2many("claim.claim","registration_id",string="Reclammations")

class Claim(models.Model):
    _name ="claim.claim"
    description=""

    name = fields.Char(string='nom',required=True,readonly=False)
    code = fields.Char(string='Code',default='001')
    start_date = fields.Date("date de debut",help="date")
    end_date = fields.Date("date de fin",help="date")
    registration_id = fields.Many2one("registration.registration",string="Inscription")
    description = fields.Text(string='description')
    user_id = fields.Many2one('res.users',string="Responsable")
    state = fields.Selection(string='Status', selection=[('new', 'Nouvelle réclamation'), ('done', 'Validée'),('cancel', 'Annulée')])
    
  

class Year(models.Model):
    _name ="year.year"
    description=""

    name = fields.Char(string='nom',required=True,readonly=False)
    code = fields.Char(string='Code',default='001')
    start_date = fields.Date("date de debut",help="date")
    end_date = fields.Date("date de fin",help="date")
    session_ids = fields.One2many("session.session","year_id",string="Session")

class Session(models.Model):
    _name ="session.session"
    description=""

    name = fields.Char(string='nom',required=True,readonly=False)
    code = fields.Char(string='Code',default='001')
    start_date = fields.Date("date de debut",help="date")
    end_date = fields.Date("date de fin",help="date")
    year_id = fields.Many2one("year.year",string="Année")


class Cycle(models.Model):
    _name ="cycle.cycle"
    description=""

    name = fields.Char(string='nom',required=True,readonly=False)
    code = fields.Char(string='Code',default='001')
    description = fields.Text(string='description')
    level_ids = fields.One2many("level.level","cycle_id",string="Niveaux")
    reg_id = fields.One2many("registration.registration", "cycle_id", string='Registration')
    
class Level(models.Model):
    _name ="level.level"
    description=""

    name = fields.Char(string='nom',required=True,readonly=False)
    code = fields.Char(string='Code',default='001')
    description = fields.Text(string='description')
    sections_ids = fields.One2many("section.section","level_id",string="Section")
    cycle_id = fields.Many2one("cycle.cylce",string="Cycle")

class Section(models.Model):
    _name ="section.section"
    description="la classe d'enregistrement des sections"

    name = fields.Char(string='nom',required=True,readonly=False)
    code = fields.Char(string='Code',default='001')
    description = fields.Text(string='description')

    module_ids = fields.One2many("module.module","section_id",string="Module")
    level_id = fields.Many2one("level.level",string="Niveau")
    

class Module(models.Model):
    _name ="module.module"
    description="la classe d'enregistrement des modules de formation"

    name = fields.Char(string='nom du module',required=True)
    code = fields.Char(string='Code',default='001')
    description = fields.Text(string='description')
    section_id = fields.Many2one("section.section",string="Section")    



