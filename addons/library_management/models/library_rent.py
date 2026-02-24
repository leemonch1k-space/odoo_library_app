from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryRent(models.Model):
    # _name - Table name for database (will be named as 'library_rent').
    # _description - Table description.
    _name = "library.rent"
    _description = "Library Rent Record"

    # Setting partner who rent our book. We could have a lot of partners so we are using Many2one relationship
    # Required - We must know which partner rents our books
    partner_id = fields.Many2one("res.partner", string="Client", required=True)

    # Our client could rent a lot of book, so we use Many2one relationship
    # Required - We must know which book our partner rent
    book_id = fields.Many2one("library.book", string="Book", required=True)

    # Set rent date ('context_today' automatically set current date).
    # Required - We must know when our client rented book.
    rent_date = fields.Date(
        string="Rent date",
        default=fields.Date.context_today,
        required=True
    )

    # Book could be returned after default, so we set it only after return and doesn't require this date before of it.
    return_date = fields.Date(string="Return date")

    # Here we are using @api.constrains for setting constraint on Python level.
    @api.constrains("book_id", "return_date")
    def _check_book_availability(self) -> None:
        """
        Check if the selected book is already rented and not yet returned.
        Ensures that a single book cannot be rented by multiple partners simultaneously.
        """
        for record in self:
            if not record.return_date:
                domain = [
                    ("book_id", "=", record.book_id.id),
                    ("return_date", "=", False),
                    ("id", "!=", record.id)  # removing current record data from query
                ]
                active_rents_count = self.search_count(domain)

                if active_rents_count > 0:
                    raise ValidationError(
                        f"Book '{record.book_id.name}' "
                        f"is already rented and hasn't been returned yet!"
                    )
