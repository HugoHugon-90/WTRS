# file errors
FILE_NOT_FOUND_CODE = "file_error_00001"
FILE_NOT_FOUND_MESSAGE = "File not found"

FILE_CANT_OPEN_CODE = "file_error_00002"
FILE_CANT_OPEN_MESSAGE = "Failed to open the file"

# input errors
JSON_MANDATORY_FIELDS_NOT_FOUND_CODE = "input_error_00001"
JSON_MANDATORY_FIELDS_NOT_FOUND_MESSAGE = "One or more mandatory json fields are missing"

INPUT_CONFIGURATION_ILL_DEFINED_CODE = "input_error_00002"
INPUT_CONFIGURATION_ILL_DEFINED_MESSAGE = "The field input_configuration must be one of these:\n" \
                                          "'parallel', 'perpendicular', 'oblique' or an empty string"

RAY_PARAMS_CONFIGURATION_ILL_DEFINED_CODE = "input_error_00003"
RAY_PARAMS_CONFIGURATION_ILL_DEFINED_MESSAGE = "If the field 'input_configuration' is not defined, " \
                                               "the field 'k0_angle_degrees' must be defined"

TURBULENCE_AMPLITUDE_ILL_DEFINED_CODE = "input_error_00004"
TURBULENCE_AMPLITUDE_ILL_DEFINED_MESSAGE = "Turbulence amplitude must lie within the interval [0, 0.15]"

AT_LEAST_ONE_PLOT_PARAM_CODE = "input_error_00005"
AT_LEAST_ONE_PLOT_PARAM_MESSAGE = "At least one input parameter must be defined to plot as a result (e.g. 'x': true)"

MONTE_CARLO_WITH_MORE_THAN_ONE_PLOT_PARAM_CODE = "input_error_00006"
MONTE_CARLO_WITH_MORE_THAN_ONE_PLOT_PARAM_MESSAGE = "In order to compare with MonteCarlo, only one plot parameter " \
                                                    "must be chosen (e.g. 'x': true)"

MONTE_CARLO_NOT_ALLOWED_PARAMETER_CODE = "input_error_00007"
MONTE_CARLO_NOT_ALLOWED_PARAMETER_MESSAGE = "For now, only x, y,kx ,ky ,dxdx ,dydy ,dkxdkx ,and " \
                                            "dkydky are allowed for Monte Carlo calculations"

# run-time errors
TYPE_ILL_DEFINED_CODE = "runtime_error_00001"
TYPE_ILL_DEFINED_MESSAGE = "This field was somewhere instanced with the wrong type"





