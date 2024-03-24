"""
UNIT CONVERSIONS
"""

def distance_converter(value, from_unit, to_unit):
    """
    Converts between any two distance units
    """
    units = {
        "m": 1,                       # meter
        "km": 1000,                   # kilometer
        "cm": 0.01,                   # centimeter
        "mm": 0.001,                  # millimeter
        "um": 1e-6,                   # micrometer
        "nm": 1e-9,                   # nanometer
        "angstrom": 1e-10,            # angstrom
        "mi": 1609.34,                # mile
        "yd": 0.9144,                 # yard
        "ft": 0.3048,                 # foot
        "in": 0.0254,                 # inch
        "nmi": 1852,                  # nautical mile
        "au": 149597870700,           # astronomical unit
        "ly": 9.4607e15,              # light year
        "pc": 3.08567758149137e16,    # parsec
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit. Supported units: m, km, cm, mm, um, nm, angstrom, mi, yd, ft, in, nmi, au, ly, pc")

    meters = value * units[from_unit]
    converted_value = meters / units[to_unit]

    return converted_value

def area_converter(value, from_unit, to_unit):
    """
    Converts between any two area units
    """
    units = {
        "sq_m": 1,                           # square meter
        "sq_km": 1e6,                        # square kilometer
        "sq_cm": 1e-4,                       # square centimeter
        "sq_mm": 1e-6,                       # square millimeter
        "sq_um": 1e-12,                      # square micrometer
        "sq_nm": 1e-18,                      # square nanometer
        "sq_angstrom": 1e-20,                # square angstrom
        "sq_mi": 2.589988110336e6,           # square mile
        "sq_yd": 0.83612736,                 # square yard
        "sq_ft": 0.09290304,                 # square foot
        "sq_in": 6.4516e-4,                  # square inch
        "acre": 4046.8564224,                # acre
        "hectare": 10000,                    # hectare
        "sq_nmi": 3.4299039988274e6,         # square nautical mile
        "sq_au": 2.2379529036721e22,         # square astronomical unit
        "sq_ly": 8.9505421074819e31,         # square light year
        "sq_pc": 9.5214088218406e32,         # square parsec
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit. Supported units: sq_m, sq_km, sq_cm, sq_mm, sq_um, sq_nm, sq_angstrom, sq_mi, sq_yd, sq_ft, sq_in, acre, hectare, sq_nmi, sq_au, sq_ly, sq_pc")

    sq_meters = value * units[from_unit]
    converted_value = sq_meters / units[to_unit]

    return converted_value

def volume_converter(value, from_unit, to_unit):
    """
    Converts between any two volume units
    """
    units = {
        "cu_m": 1,                          # cubic meter
        "cu_km": 1e9,                       # cubic kilometer
        "cu_cm": 1e-6,                      # cubic centimeter
        "cu_mm": 1e-9,                      # cubic millimeter
        "cu_um": 1e-18,                     # cubic micrometer
        "cu_nm": 1e-27,                     # cubic nanometer
        "cu_angstrom": 1e-30,               # cubic angstrom
        "cu_mi": 4.16818183e9,              # cubic mile
        "cu_yd": 0.764554857984,            # cubic yard
        "cu_ft": 0.028316846592,            # cubic foot
        "cu_in": 1.6387064e-5,              # cubic inch
        "l": 0.001,                         # liter
        "ml": 1e-6,                         # milliliter
        "gal": 0.00378541,                  # US gallon
        "qt": 0.000946353,                  # US quart
        "pt": 0.000473176,                  # US pint
        "cup": 0.000236588,                 # US cup
        "floz": 2.957353e-5,                # US fluid ounce
        "tbsp": 1.47867648e-5,              # US tablespoon
        "tsp": 4.92892159e-6,               # US teaspoon
        "imp_gal": 0.00454609,              # imperial gallon
        "imp_qt": 0.001136523,              # imperial quart
        "imp_pt": 0.000568261,              # imperial pint
        "imp_floz": 2.841306e-5,            # imperial fluid ounce
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit. Supported units: cu_m, cu_km, cu_cm, cu_mm, cu_um, cu_nm, cu_angstrom, cu_mi, cu_yd, cu_ft, cu_in, l, ml, gal, qt, pt, cup, floz, tbsp, tsp, imp_gal, imp_qt, imp_pt, imp_floz")

    cu_meters = value * units[from_unit]
    converted_value = cu_meters / units[to_unit]

    return converted_value

def mass_converter(value, from_unit, to_unit):
    units = {
        "kg": 1,                     # kilogram
        "g": 0.001,                  # gram
        "mg": 1e-6,                  # milligram
        "ug": 1e-9,                  # microgram
        "ng": 1e-12,                 # nanogram
        "pg": 1e-15,                 # picogram
        "lb": 0.45359237,            # pound
        "oz": 0.028349523125,        # ounce
        "st": 6.35029318,            # stone
        "ton": 907.18474,            # short ton (US ton)
        "long_ton": 1016.0469088,    # long ton (UK ton)
        "t": 1000,                   # metric ton
        "ct": 0.0002,                # carat
        "gr": 0.00006479891,         # grain
        "amu": 1.66053904e-27,       # atomic mass unit
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit. Supported units: kg, g, mg, ug, ng, pg, lb, oz, st, ton, long_ton, t, ct, gr, amu")

    kilograms = value * units[from_unit]
    converted_value = kilograms / units[to_unit]

    return converted_value

"""
END OF UNIT CONVERSIONS
"""
