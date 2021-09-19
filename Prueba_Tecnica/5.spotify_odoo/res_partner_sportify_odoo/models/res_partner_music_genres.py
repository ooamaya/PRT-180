from odoo import models,fields,api,_
from odoo.exceptions import ValidationError,UserError

class MusicGenres(models.Model):
    _name = 'res.partner.music.genres'
    _description = "Generos de musica"

    name = fields.Char(string='Genero',required=True,copy=False)
    #active = fields.Boolean('Active', default=True, store=True, readonly=False,tracking=True)
    
    @api.model
    def create(self, vals):
        vals['name'] = vals.get('name').lower()
        result = super(MusicGenres, self).create(vals)
        return result

    @api.constrains('name')
    def unique_name(self):
        if self.name:
            name= self.name.lower()
            count_genre = self.env['res.partner.music.genres'].search_count([('name','=',name)])
            if count_genre > 1:
                raise ValidationError('Ya existe este genero de musica')