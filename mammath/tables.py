from .constants import *
from tabulate import tabulate

"""
TABLES
"""

def constants_table(category=None):
    """
    Prints a table of all constants, with the option to choose a category
    """
    headers = ["Name", "Symbol", "Value", "Unit"]

    math_constants = [
        ["pi", "π", pi, "dimensionless"],
        ["e", "ℯ", e, "dimensionless"],
        ["Golden Ratio", "ϕ", phi, "dimensionless"],
        ["Imaginary Unit", "𝑖", i, "dimensionless"],
        ["Euler-Mascheroni Constant", "γ", euler_mascheroni, "dimensionless"],
        ["Apery's Constant", "ζ_3", apery, "dimensionless"],
        ["Catalan's Constant", "G", catalan, "dimensionless"],
        ["Square Root of 2", "sqrt2", sqrt2, "dimensionless"],
        ["Square Root of 3", "sqrt3", sqrt3, "dimensionless"],
        ["Natural Logarithm of 2", "ln2", ln2, "dimensionless"],
        ["Natural Logarithm of 10", "ln10", ln10, "dimensionless"],
        ["Khinchin's Constant", "khinchin", khinchin, "dimensionless"],
        ["Twin Prime Constant", "twin_prime", twin_prime, "dimensionless"],
        ["Conway's Constant", "conways_constant", conways_constant, "dimensionless"],
        ["Feigenbaum Constant", "feigenbaum_constant", feigenbaum_constant, "dimensionless"],
        ["Glaisher's Constant", "glaisher_constant", glaisher_constant, "dimensionless"],
        ["Lehmer's Constant", "lehmer_constant", lehmer_constant, "dimensionless"],
        ["Levy's Constant", "levy_constant", levy_constant, "dimensionless"],
        ["Mills' Constant", "mills_constant", mills_constant, "dimensionless"],
        ["MrB Constant", "mrB_constant", mrB_constant, "dimensionless"],
        ["Odds Constant", "odds_constant", odds_constant, "dimensionless"],
        ["Omega Constant", "omega_constant", omega_constant, "dimensionless"],
        ["Sierpinski's Constant", "sierpinski_constant", sierpinski_constant, "dimensionless"],
        ["Thue-Morse Constant", "thue_morse_constant", thue_morse_constant, "dimensionless"],
        ["Universal Parabolic Constant", "universal_parabolic_constant", universal_parabolic_constant, "dimensionless"],
        ["Viswanath's Constant", "viswanath_constant", viswanath_constant, "dimensionless"],
    ]
    physics_constants = [
        ["Speed of Light", "𝑐", c, "m/s"],
        ["Gravitational Constant", "𝐺", G, "m³/kg/s²"],
        ["Planck Constant", "ℎ", h, "J⋅s"],
        ["Reduced Planck Constant", "ℏ", h_bar, "J⋅s"],
        ["Boltzmann Constant", "𝑘", k, "J/K"],
        ["Avogadro Constant", "𝑁_A", N_A, "1/mol"],
        ["Elementary Charge", "𝑒", e_c, "C"],
        ["Gas Constant", "𝑅", R, "J/(mol⋅K)"],
        ["Stefan-Boltzmann Constant", "σ", stefan_boltzmann, "W/(m²⋅K⁴)"],
        ["Vacuum Permittivity", "ε_0", vacuum_permittivity, "F/m"],
        ["Vacuum Permeability", "μ_0", vacuum_permeability, "H/m"],
        ["Fine Structure Constant", "α", fine_structure, "dimensionless"],
        ["Proton Mass", "m_p", proton_mass, "kg"],
        ["Neutron Mass", "m_n", neutron_mass, "kg"],
        ["Electron Mass", "m_e", electron_mass, "kg"],
        ["Bohr Radius", "a_0", bohr_radius, "m"],
        ["Rydberg Constant", "R_inf", rydberg_constant, "1/m"],
        ["Atomic Mass Constant", "m_u", atomic_mass_constant, "kg"],
        ["Faraday Constant", "F", faraday_constant, "C/mol"],
        ["Wien Displacement Constant", "b", wien_displacement, "m⋅K"],
        ["Hubble Constant", "H_0", hubble_constant, "km/(s⋅Mpc)"],
        ["Cosmological Constant", "Λ", cosmological_constant, "1/m²"],
        ["Giga Parsec", "Gpc", giga_parsec, "m"],
        ["Solar Mass", "solar_mass", solar_mass, "kg"],
        ["Solar Radius", "solar_radius", solar_radius, "m"],
        ["Solar Luminosity", "solar_luminosity", solar_luminosity, "W"],
        ["Astronomical Unit", "AU", astronomical_unit, "m"],
        ["Light Year", "ly", light_year, "m"],
        ["Parsec", "pc", parsec, "m"],
        ["Sound Speed in Air", "c_air", sound_speed_air, "m/s"],
        ["Sound Speed in Water", "c_water", sound_speed_water, "m/s"],
        ["Sound Speed in Steel", "c_steel", sound_speed_steel, "m/s"],
        ["Planck Length", "l_P", planck_length, "m"],
        ["Planck Time", "t_P", planck_time, "s"],
        ["Planck Temperature", "T_P", planck_temperature, "K"],
    ]
    mechanics_constants = [
        ["Electron Volt", "eV", electron_volt, "J"],
        ["Joule per Electronvolt", "joule_per_electronvolt", joule_per_electronvolt, "J/eV"],
        ["Newton", "N", newton, "kg⋅m/s²"],
        ["Pascal", "Pa", pascal, "N/m²"],
        ["Atmosphere", "atm", atmosphere, "Pa"],
        ["Bar", "bar", bar, "Pa"],
        ["Torr", "torr", torr, "Pa"],
        ["Dyne", "dyne", dyne, "N"],
        ["Erg", "erg", erg, "J"],
        ["Calorie", "cal", calorie, "J"],
        ["British Thermal Unit", "btu", btu, "J"],
        ["Horsepower", "hp", horsepower, "W"],
        ["Watt", "W", watt, "J/s"],
    ]
    quantum_constants = [
        ["Fine Structure Constant", "alpha", fine_structure_constant, ""],
        ["Quantum of Circulation", "h_over_4pi", quantum_of_circulation, "m^2/kg"],
        ["Quantum of Circulation Times 2", "h_over_2pi", quantum_of_circulation_times_2, "m^2/kg"],
        ["Flux Quantum", "Phi_0", flux_quantum, "Wb"],
        ["Josephson Constant", "K_J", josephson_constant, "Hz/V"],
        ["Von Klitzing Constant", "R_K", von_klitzing_constant, "ohm"],
        ["Bohr Magneton", "mu_B", bohr_magneton, "J/T"],
        ["Nuclear Magneton", "mu_N", nuclear_magneton, "J/T"],
        ["Compton Wavelength", "lambda_C", compton_wavelength, "m"],
        ["Compton Wavelength Over 2pi", "lambda_C_over_2pi", compton_wavelength_over_2pi, "m"],
        ["Classical Electron Radius", "r_e", classical_electron_radius, "m"],
        ["Hartree Energy", "E_h", hartree_energy, "J"],
        ["Conductance Quantum", "G_0", conductance_quantum, "S"],
        ["Inverse Conductance Quantum", "R_0_inv", inverse_conductance_quantum, "ohm"],
        ["Magnetic Constant", "mu_0", magnetic_constant, "N/A^2"],
        ["Electric Constant", "epsilon_0", electric_constant, "F/m"],
        ["Characteristic Impedance of Vacuum", "Z_0", characteristic_impedance_of_vacuum, "ohm"],
        ["Elementary Charge", "e", elementary_charge, "C"],
    ]
    chemistry_constants = [
        ["Electronvolt", "eV", electronvolt],
        ["Molar Volume of Ideal Gas", "V_m", V_m, "L/mol"],
        ["Molar Gas Constant", "𝑅", R, "J/mol·K"],
        ["Ion product of water", "K_w", K_w, "mol^2/L^2"],
        ["pKw of water", "pK_w", pK_w, "dimensionless"],
        ["Boltzmann constant (Chemistry)", "K_b_chem", k, "J/K"],
        ["Planck constant (Chemistry)", "h_chem", h_chem, "J·s"],
        ["Molar Mass of Air", "M_air", M_air, "kg/mol"],
        ["Density of Water", "ρ_water", ρ_water, "kg/m^3"],
        ["Gas Constant for Dry Air", "R_d", R_d, "J/kg·K"],
    ]
    geophysics_constants = [
        ["Earth Gravity", "𝑔", earth_gravity, "m/s^2"],
        ["Earth Mass", "M_E", earth_mass, "kg"],
        ["Earth Equatorial Radius", "R_E", earth_equatorial_radius, "km"],
        ["Earth Polar Radius", "R_p", earth_polar_radius, "km"],
        ["Earth Mean Radius", "R_m", earth_mean_radius, "km"],
        ["Earth Oblateness", "f", earth_oblateness, "dimensionless"],
        ["Sidereal Year", "P_sidereal", sidereal_year, "days"],
        ["Tropical Year", "P_tropical", tropical_year, "days"],
    ]
    computer_constants = [
        ["Bit", "bit", bit, "bit"],
        ["Byte", "byte", byte, "bit"],
        ["Kilobyte", "kB", kilobyte, "byte"],
        ["Megabyte", "MB", megabyte, "byte"],
        ["Gigabyte", "GB", gigabyte, "byte"],
        ["Terabyte", "TB", terabyte, "byte"],
        ["Petabyte", "PB", petabyte, "byte"],
        ["Exabyte", "EB", exabyte, "byte"],
        ["Zettabyte", "ZB", zettabyte, "byte"],
        ["Yottabyte", "YB", yottabyte, "byte"],
        ["Floating point operations per second", "fLOPS", floating_point_operations_per_second, "FLOPS"],
        ["Million instructions per second", "MIPS", million_instructions_per_second, "instructions/s"],
        ["Symbols per second", "Baud", symbols_per_second, "Baud"],
        ["Bits per second", "bps", bits_per_second, "bps"],
        ["Hertz", "Hz", hertz, "Hz"],
    ]
    constants_by_category = {
        "Mathematics": math_constants,
        "Physics": physics_constants,
        "Mechanics": mechanics_constants,
        "Quantum": quantum_constants,
        "Chemistry": chemistry_constants,
        "Geophysics": geophysics_constants,
        "Computer": computer_constants,
    }
    
    if category is None:
        for cat, constants in constants_by_category.items():
            print(f"{cat} Constants:")
            print(tabulate(constants, headers=headers))
            print("\n")
    else:
        if category in constants_by_category:
            print(f"{category} Constants:")
            print(tabulate(constants_by_category[category], headers=headers))
        else:
            print("Invalid category. Please choose a valid category ['Mathematics', 'Physics', 'Mechanics', 'Quantum', 'Chemistry', 'Geophysics', 'Computer'].")

  
    
def trig_table():
    """
    Prints a table of the most useful trigonometric identities
    """
    identities = {"Quotient Identities": ["tanθ = sinθ/cosθ", "cotθ = cosθ/sinθ"],
           "Reciprocal Identities": ["cotθ = 1/tanθ", "cscθ = 1/sinθ", "sec = 1/cosθ"],
           "Pythagorean Identities": ["sin^2θ + cos^2θ = 1", "tan^2θ + 1 = sec^2θ", "1 + cot^2θ = csc^2θ"],
           "Sum Identities": ["sin(a+b) = sin(a)cos(b)+cos(a)sin(b)", "cos(a+b) = cos(a)cos(b)-sin(a)sin(b)", "tan(a+b) = (tan(a) + tan(b))/1 - tan(a)tan(b)"],
           "Difference Identities": ["sin(a-b) = sin(a)cos(b)-cos(a)sin(b)", "cos(a-b) = cos(a)cos(b)+sin(a)sin(b)", "tan(a-b) = (tan(a)-tan(b))/1 + tan(a)tan(b)"],
           "Double-Angle Formulas": ["sin(2a) = 2sin(a)cos(a)", "cos(2a) = 2cos^2 a - 1 = 1 - 2sin^2 a", "tan(2a) = 2tan(a)/1-tan^2 a"]
           }
    print(tabulate(identities, headers = "keys"))

def algebraic_identities_table():
    """
    Prints a table of commonly used algebraic identities
    """
    identities = {
        "Basic Identities": [
            "a^2 - b^2 = (a - b)(a + b)",
            "(a + b)^2 = a^2 + 2ab + b^2",
            "(a - b)^2 = a^2 - 2ab + b^2"
        ],
        "Sum and Difference of Cubes": [
            "a^3 + b^3 = (a + b)(a^2 - ab + b^2)",
            "a^3 - b^3 = (a - b)(a^2 + ab + b^2)"
        ],
        "Polynomial Identities": [
            "(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca",
            "(a + b + c)^3 = a^3 + b^3 + c^3 + 3(a + b)(b + c)(c + a)"
        ]
    }
    print(tabulate(identities, headers="keys"))

def calculus_formulas_table():
    """
    Prints a table of fundamental calculus formulas
    """
    formulas = {
        "Derivatives": [
            "d/dx [c] = 0",
            "d/dx [x^n] = nx^(n-1)",
            "d/dx [sin(x)] = cos(x)",
            "d/dx [cos(x)] = -sin(x)",
            "d/dx [e^x] = e^x",
            "d/dx [ln(x)] = 1/x"
        ],
        "Integrals": [
            "∫ c dx = cx + C",
            "∫ x^n dx = (x^(n+1))/(n+1) + C (n ≠ -1)",
            "∫ e^x dx = e^x + C",
            "∫ 1/x dx = ln|x| + C",
            "∫ sin(x) dx = -cos(x) + C",
            "∫ cos(x) dx = sin(x) + C"
        ],
        "Limits": [
            "lim (x→a) c = c",
            "lim (x→a) x = a",
            "lim (x→0) (sin(x)/x) = 1",
            "lim (x→∞) (1/x) = 0",
            "lim (x→∞) (1/x^n) = 0 (n > 0)"
        ]
    }
    print(tabulate(formulas, headers="keys"))

"""
END OF TABLES
"""
