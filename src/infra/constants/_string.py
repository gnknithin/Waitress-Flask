class ApplicationConstants():
    SERVICE_NAME = "waitress-flask"
    LOGGER_NAME = "waitress-flask"

class ConfigurationConstants():
    LOGGER = "logger"
    LOGGING = "logging"

class GenericConstants():
    STARTING = "STARTING"
    SHUTTING_DOWN = "SHUTTING DOWN"
    STOPPED = "STOPPED"
    SUCCESS = "success"


class MessagesConstants():
    MSG_VALIDITY_IN_CASE_OF_FAILURE = "".join(
        ["Validity of this data envelope In case of failure it will return FALSE"]
    )