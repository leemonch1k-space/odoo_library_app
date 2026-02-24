import json
from odoo import http
from odoo.http import request


class LibraryController(http.Controller):

    @http.route(
        "/library/books",
        type="http",
        auth="user",
        methods=["GET"],
        csrf=False
    )
    def get_books(self) -> http.Response:
        """
        Controller for receiving book list.
        Return JSON with book title and book status
        (available or not available)
        """
        books = request.env["library.book"].search([])

        books_data = []
        for book in books:
            books_data.append({
                "id": book.id,
                "name": book.name,
                "author": book.author or "Unknown",
                "is_available": book.is_available,
                "published_date": str(book.published_date)
                if book.published_date
                else None
            })

        return request.make_response(
            json.dumps(books_data),
            headers=[("Content-Type", "application/json")]
        )
