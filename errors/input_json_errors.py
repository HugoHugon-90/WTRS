import errors.constants as const
from errors.helpers import ErrorHelpers


class FieldNotFoundError(Exception):

    def __init__(self, *args):

        self.key = None
        self.upper_key = None
        self.arg_len = len(args)
        if args:
            self.key = args[0]
        if self.arg_len > 1:
            self.upper_key = args[1]

    def __str__(self):
        error = ErrorHelpers.error_printer(const.JSON_MANDATORY_FIELDS_NOT_FOUND_CODE,
                                           const.JSON_MANDATORY_FIELDS_NOT_FOUND_MESSAGE)
        if self.arg_len == 1:
            return error + f"field: '{self.key}' is mandatory in the file 'input.json'"
        if self.arg_len > 1:
            return error + f"field: '{self.key}' is mandatory inside the field '{self.upper_key}' " \
                           f"in the file 'input.json'"
        else:
            return error


class WrongRayParamsError(Exception):

    def __str__(self):
        error = ErrorHelpers.error_printer(const.RAY_PARAMS_CONFIGURATION_ILL_DEFINED_CODE,
                                           const.RAY_PARAMS_CONFIGURATION_ILL_DEFINED_MESSAGE)
        return error


class TurbAmpIllDefinedError(Exception):

    def __str__(self):
        error = ErrorHelpers.error_printer(const.TURBULENCE_AMPLITUDE_ILL_DEFINED_CODE,
                                           const.TURBULENCE_AMPLITUDE_ILL_DEFINED_MESSAGE)
        return error


class WrongInputConfigurationError(Exception):

    def __init__(self, *args):

        self.inputConfiguration = None
        if args:
            self.inputConfiguration = args[0]

    def __str__(self):
        error = ErrorHelpers.error_printer(const.INPUT_CONFIGURATION_ILL_DEFINED_CODE,
                                           const.INPUT_CONFIGURATION_ILL_DEFINED_MESSAGE)
        if self.inputConfiguration:
            return error + f" The field 'input_type' = '{self.inputConfiguration}' is invalid"
        else:
            return error


class WrongInputWaveVectorError(Exception):

    def __init__(self, *args):

        self.inputType = None
        if args:
            self.inputType = args[0]

    def __str__(self):
        error = ErrorHelpers.error_printer(const.INPUT_CONFIGURATION_ILL_DEFINED_CODE,
                                           const.INPUT_CONFIGURATION_ILL_DEFINED_MESSAGE)
        if self.inputType:
            return error + f" The field 'input_type' = '{self.inputType}' is invalid"
        else:
            return error


class AtLeastOnePlotQuantitieError(Exception):

    def __str__(self):
        error = ErrorHelpers.error_printer(const.AT_LEAST_ONE_PLOT_PARAM_CODE,
                                           const.AT_LEAST_ONE_PLOT_PARAM_MESSAGE)
        return error


class MonteCarloWithMoreThanOnePlotQuantitiesError(Exception):

    def __str__(self):
        error = ErrorHelpers.error_printer(const.MONTE_CARLO_WITH_MORE_THAN_ONE_PLOT_PARAM_CODE,
                                           const.MONTE_CARLO_WITH_MORE_THAN_ONE_PLOT_PARAM_MESSAGE)
        return error
