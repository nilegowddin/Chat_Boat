class FlowiseException(Exception):
    """Base exception for Flowise errors."""


class FlowiseAuthenticationError(FlowiseException):
    """Raised when Flowise authentication fails."""


class FlowiseAPIError(FlowiseException):
    """Raised when Flowise returns an unexpected error."""