"""arxiv browse exceptions."""

from typing import Optional
from werkzeug.exceptions import HTTPException
from arxiv.base.exceptions import handler
from flask import render_template, make_response, Response

from arxiv import status


class AbsNotFound(HTTPException):
    """Abs not found HTTPException."""

    code = 404
    description = 'Article does not exist'

    def __init__(self, description: Optional[str] = None,
                 response: Optional[Response] = None,
                 data: dict = {}):
        """Override default to support data dict."""
        self.data = data
        super(AbsNotFound, self).__init__(description, response)


@handler(AbsNotFound)
def handle_abs_not_found(error: AbsNotFound) -> Response:
    """Render the base 404 error page."""
    rendered = render_template("abs/404.html", **error.data)
    response = make_response(rendered)
    response.status_code = status.HTTP_404_NOT_FOUND
    return response