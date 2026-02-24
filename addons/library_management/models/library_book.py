from odoo import models, fields


class LibraryBook(models.Model):
    # _name - Table name for database (will be named as 'library_book').
    # _description - Table description.
    _name = "library.book"
    _description = "Library Book model"

    # required field because book can't be without title. Type 'Char' because title shouldn't be long text.
    name = fields.Char(string="Book title", required=True)

    # Book author. Type Char because title shouldn't be long text. Some books might not have an author
    author = fields.Char(string="Author")

    # Date of publication. Type 'Date' to save data in date format. Some old books could not have published date, so we doesn't require it.
    published_date = fields.Date(string="Publication date")

    # Book status. Book available by default because in most cases if we add something we already have it.
    is_available = fields.Boolean(string="Is available", default=True)
