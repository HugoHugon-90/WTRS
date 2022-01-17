import errors.constants as const

def error_printer(error_code, error_message):
    return f'__error__//// code: {error_code}, message: {error_message} ////__error__ \n'

class WrongTypeError(TypeError):

    def __init__(self, *args):

        self.arg_len = len(args)
        self.field = None
        self.should_be_type = None

        if self.arg_len > 1:
            self.field = args[0]
            self.should_be_type = args[1]

    def __str__(self):
        error = error_printer(const.TYPE_ILL_DEFINED_CODE, const.TYPE_ILL_DEFINED_MESSAGE)
        if self.arg_len > 1:
            return error + f"field: '{self.field}' is of type '{type(self.field)}', " \
                           f"but should be of type '{self.should_be_type}'"
        else:
            return error