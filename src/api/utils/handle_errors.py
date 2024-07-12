from flask import make_response

from src.domain.commons.exceptions import InvalidInputException, InvalidStateException, QuestaoNotFoundException, \
    BusinessException, InternalErrorException
from src.api.utils.serializer import serializa_dto


class ErroResponse:

    def __init__(self, message, erro_details=None, status=500):
        self.message = message
        self.details = erro_details
        self.status = status


def handle_errors(ex: Exception):
    # status 400
    if isinstance(ex, (InvalidInputException, InvalidStateException)):
        return make_response(serializa_dto(ErroResponse(str(ex), None, 400)), 400)
    # status 404
    if isinstance(ex, QuestaoNotFoundException):
        return make_response(serializa_dto(ErroResponse(message=str(ex), status=404)), 404)
    # status: erro 500
    if isinstance(ex, (BusinessException, InternalErrorException)):
        return make_response(serializa_dto(ErroResponse(str(ex))), 500)
    # demais exceções
    return make_response(serializa_dto(ErroResponse("Erro insperado", str(ex))), 500)
