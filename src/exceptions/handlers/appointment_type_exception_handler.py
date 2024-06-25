from typing import Callable
from urllib.request import Request

from fastapi.responses import JSONResponse

from exceptions.appointment_type_exceptions import AppointmentTypeException


class AppointmentTypeExceptionHandler:
    def create_exception_handler(status_code: int) -> Callable[[Request, AppointmentTypeException], JSONResponse]:
        detail = {}
        async def exception_handler(_: Request, exception: AppointmentTypeException) -> JSONResponse:
            if exception.message: detail["message"] = exception.message
            if exception.name: detail["message"] = "{detail['message']} [{exception.name}]"
            return JSONResponse(status_code = status_code, content = {"detail": detail["message"]})
        return exception_handler