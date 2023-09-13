from odoo import http
# import logging #Esta libreria se usa para 

# Cuando se hace un cambio en el controlador hay que hacerle restart al contenedor.

# _logger = logging.getLogger(__name__)

class Books(http.Controller):

    @http.route("/library/books")
    def list(self, **kwargs):
        libros = http.request.env["library.book"]
        books = libros.search([])

        # Esto se usa para probar 
        # _logger.warning("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
        # _logger.warning(books)

        # return None

        return http.request.render(
            "library_app.book_list_template",
            {"book": books}
        )