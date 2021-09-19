from odoo import models,fields,api,_
from odoo.exceptions import ValidationError,UserError

class MusicGenres(models.Model):
    _name = 'res.partner.music.recomends'
    _description = "Recomendaciones que se le hace al cliente dependiendo los generos que tiene configurados"

    partner_id = fields.Many2one(string='Contact',comodel_name='res.partner',ondelete='cascade')
    music_genre_id = fields.Many2one(string='Genre',comodel_name='res.partner.music.genres',ondelete='cascade')
    track = fields.Char(string='Track')
    artist = fields.Char(string='Artist')
    url = fields.Char(string='URL Spotify')
    