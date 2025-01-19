"""
Static mappings and numeric constants for Terai and Hilly land units.

Attributes:
    TERAI_TO_SQ_M (dict): 
        A mapping of Terai land units to their approximate areas in square meters.
        Example:
            TERAI_TO_SQ_M = {
                "bigha":  6772.63,  # 1 bigha  = 6772.63 m²
                "kattha": 338.63,   # 1 kattha = 338.63  m²
                "dhur":   16.93,    # 1 dhur   = 16.93   m²
            }

    HILLY_TO_SQ_M (dict): 
        A mapping of Hilly land units to their approximate areas in square meters.
        Example:
            HILLY_TO_SQ_M = {
                "ropani": 508.72,   # 1 ropani = 508.72 m²
                "aana":   31.79,    # 1 aana   = 31.79  m²
                "paisa":  7.95,     # 1 paisa  = 7.95   m²
                "daam":   1.99,     # 1 daam   = 1.99   m²
            }
"""

TERAI_TO_SQ_M = {
    "bigha":  6772.63,  # 1 bigha  = 6772.63 m²
    "kattha": 338.63,   # 1 kattha = 338.63  m²
    "dhur":   16.93,    # 1 dhur   = 16.93   m²
}

HILLY_TO_SQ_M = {
    "ropani": 508.72,   # 1 ropani = 508.72 m²
    "aana":   31.79,    # 1 aana   = 31.79  m²
    "paisa":  7.95,     # 1 paisa  = 7.95   m²
    "daam":   1.99,     # 1 daam   = 1.99   m²
}