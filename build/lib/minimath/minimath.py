from .algebra import Algebra
from .basic import Basic
from .geometry import Geometry


class MiniMath(Basic, Algebra, Geometry):
    pass
