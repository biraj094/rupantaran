


# This allows us easier import. Else we have to do something like this:
# from rupantaran.weight.weight import from_lal
# But now  with this we can do:
# from rupantaran.weight import from_lal

from .weight import (
    from_lal,
    from_tola,
    from_chatak,
    from_pau,
    from_dharni,
    from_sher,
    from_kg,
    from_g,
    from_lb,
    from_oz
)

__all__ = [
    'from_lal',
    'from_tola',
    'from_chatak',
    'from_pau',
    'from_dharni',
    'from_sher',
    'from_kg',
    'from_g',
    'from_lb',
    'from_oz'
] 