from base_provider import BaseProvider


class CustomProvider(BaseProvider):
    """
    CustomProvider inherits from BaseProvider.
    """

    def __init__(self):
        super().__init__()

    def perform_action(self):
        """
        This is the custom action method for CustomProvider.
        It overrides the base action method.
        """
        pass
