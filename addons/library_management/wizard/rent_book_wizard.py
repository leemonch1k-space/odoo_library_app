from odoo import models, fields, api


class RentBookWizard(models.TransientModel):
    # _name - Table name for database (will be named as 'rent_book_wizard').
    # _description - Table description.
    _name = "rent.book.wizard"
    _description = "Wizard to Rent a Book"

    # Field for choosing client which rent book
    partner_id = fields.Many2one("res.partner", string="Client", required=True)

    # Field for showing current book (We are already on this book form, so it should be readonly)
    book_id = fields.Many2one(
        "library.book",
        string="Book",
        required=True,
        readonly=True
    )

    # Here we use api.model to call method when user press button, but before data store in temporary db
    @api.model
    def default_get(self, fields_list) -> dict:
        """
        This method automatically retrieves the book ID from the source form.
        res - holds the dictionary of default values for the fields.
        active_id - retrieves the ID of the record from which the wizard was launched.
        We check if active_id exists and then inject it into the 'book_id' field
        so the wizard opens with the book already selected.
        """
        res = super(RentBookWizard, self).default_get(fields_list)
        active_id = self.env.context.get("active_id")
        if active_id:
            res["book_id"] = active_id
        return res

    def action_rent_book(self) -> None:
        """
        This method creates a rental record and updates the book's availability
        when the user clicks the confirm button.
        """
        for wizard in self:
            # Creating a link between the partner and the book in the rent table
            self.env["library.rent"].create({
                "partner_id": wizard.partner_id.id,
                "book_id": wizard.book_id.id,
            })
            # Updating the book status
            wizard.book_id.is_available = False
