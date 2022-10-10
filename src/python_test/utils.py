"""
Utility functions.
"""

# --- Imports

# Standard library
import datetime

# External packages
from slugify import slugify


# --- Utility functions


def get_experiment_name(description: str, include_timestamp: bool = False) -> str:
    """
    Get standard experiment name.

    Parameters
    ----------
    description: brief description

    include_timestamp: when True, include a timestamp in the experiment name

    Return value
    ------------
    experiment name
    """
    description_slugified = slugify(description, separator="_")

    datestamp = datetime.date.today().isoformat()
    if include_timestamp:
        timestamp = datetime.datetime.now().strftime("-%H%M%S")
    else:
        timestamp = ""

    experiment_name = f"{datestamp}{timestamp}-{description_slugified}"

    return experiment_name


def add(x, y):
    """
    Add x and y.
    """
    return x + y


def multiply(x, y):
    """
    Multiply x and y.
    """
    return x * y


def axpy(a, x, y):
    """
    Return ax + y.
    """
    return a * x + y


def diff(x, y):
    """
    Difference of x and y.
    """
    return x - y


def diff2(x, y):
    """
    Difference of x and y.
    """
    return x - y
