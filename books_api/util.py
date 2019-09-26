from rest_framework.response import Response


def make_status(status_code):
    if status_code < 400:
        return 'success'
    else:
        return 'some error occurred'


def make_response(response, message=None) -> Response:
    """
    :param response:
    :param message:
    :return:
    """
    data = {
        'data': response.data if hasattr(response, 'data') and response.data is not None else [],
        'status': make_status(response.status_code),
        'status_code': response.status_code,
    }
    if message is not None:
        data['message'] = message
    return Response(status=response.status_code, data=data)
