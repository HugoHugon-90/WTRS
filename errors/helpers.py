import errors.generic_errors as gen_err


# generic print function

class ErrorHelpers:

    @staticmethod
    def error_printer(error_code, error_message):
        return f'__error__//// code: {error_code}, message: {error_message} ////__error__ \n'

    @staticmethod
    def check_type_error(obj, typ):
        if not isinstance(obj,typ):
            raise gen_err.WrongTypeError(obj, typ)