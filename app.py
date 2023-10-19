from base_provider import BaseProvider
from custom_provider import CustomProvider


def inherit_docstrings(subclass, base_class):
    """
    A function to inherit docstrings from a base class to a subclass.
    In addition to their own docstrings.
    """

    # Iterate over attributes (methods and properties) in the subclass
    for attr_name in dir(subclass):
        # Get the attribute with the current name
        attr = getattr(subclass, attr_name)

        # Check if the attribute in the subclass has no docstring
        # and if a corresponding attribute exists in the base class
        if not attr.__doc__ and hasattr(base_class, attr_name):
            # Get the corresponding attribute from the base class
            base_attr = getattr(base_class, attr_name)

            # Check if the base class attribute has a docstring
            if base_attr.__doc__:
                # Merge the docstrings by setting the subclass's docstring
                # to a combination of the base class and subclass docstrings
                setattr(subclass, attr_name, base_attr.__doc__ + "\n\n" + attr.__doc__)


# Inherit docstrings from the BaseProvider to CustomProvider
inherit_docstrings(CustomProvider, BaseProvider)

# Now, let's print the docstrings for CustomProvider
print(CustomProvider.__doc__)
print(CustomProvider.perform_action.__doc__)
