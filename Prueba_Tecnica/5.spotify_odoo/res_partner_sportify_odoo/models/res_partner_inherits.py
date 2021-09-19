from odoo import models,fields,api,_
from odoo.exceptions import ValidationError,UserError
from .api_spotify import SpotifyApi

class search(models.Model):
    _inherit = 'res.partner'

    music_genres = fields.Many2many(string='Music Genres',comodel_name='res.partner.music.genres',ondelete='restrict')
    music_recomendations = fields.One2many('res.partner.music.recomends', 'partner_id'
                        , string='Music Recomendations'
                        , auto_join=True)
       
    def write(self, vals,context=None):
        res = super(search, self).write(vals)
        partner_genres = self.env['res.partner.music.genres'].search([('id', 'in', self.music_genres.ids)])
        for genre in partner_genres:
            genre_exist = self.env['res.partner.music.recomends'].search(['&',('music_genre_id','=', genre.id),('partner_id','=',self.id)])
            if not genre_exist:
                track = SpotifyApi(genre.name)
                recomendation = track.get_track()
                track = recomendation[0]
                artist = recomendation[1]
                url = recomendation[2]
                data = {
                        'partner_id': self.id,
                        'music_genre_id': genre.id,
                        'track': track,
                        'artist': artist,
                        'url': url
                    }
                self.env['res.partner.music.recomends'].create(data)

        partner_recomendations = self.env['res.partner.music.recomends'].search([('partner_id','=',self.id)])
        for recomendation in partner_recomendations:
            if recomendation.music_genre_id.id not in self.music_genres.ids:
                recomendation.unlink()
        
        return res