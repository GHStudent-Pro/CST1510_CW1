# Task 2: Scientific Calculator (Unit Conversion Chart)
# Note: the chart has two typos. 1 inch is 2.54 cm (not 2.43), and its
# "1 ft = 0.028 m" line is really 1 cubic foot = 0.028 cubic metres.
# The correct values are used below.


# ---------------------------------------------------------------- length
def m_to_ft(m):
    """Convert metres to feet."""
    return m * 3.281


def ft_to_m(ft):
    """Convert feet to metres."""
    return ft / 3.281


def in_to_cm(inches):
    """Convert inches to centimetres."""
    return inches * 2.54


def cm_to_in(cm):
    """Convert centimetres to inches."""
    return cm / 2.54


def mi_to_km(mi):
    """Convert miles to kilometres."""
    return mi * 1.609


def km_to_mi(km):
    """Convert kilometres to miles."""
    return km / 1.609


# ----------------------------------------------------------- temperature
def c_to_f(c):
    """Convert Celsius to Fahrenheit."""
    return 9 / 5 * c + 32


def f_to_c(f):
    """Convert Fahrenheit to Celsius."""
    return 5 / 9 * (f - 32)


def c_to_k(c):
    """Convert Celsius to Kelvin."""
    return c + 273.15


def f_to_k(f):
    """Convert Fahrenheit to Kelvin."""
    return 5 / 9 * (f - 32) + 273.15


# ------------------------------------------------------------------ mass
def kg_to_lb(kg):
    """Convert kilograms to pounds."""
    return kg * 2.2


def lb_to_kg(lb):
    """Convert pounds to kilograms."""
    return lb / 2.2


def oz_to_g(oz):
    """Convert ounces to grams."""
    return oz * 28.35


def g_to_oz(g):
    """Convert grams to ounces."""
    return g / 28.35


# ---------------------------------------------------------------- volume
def ml_to_cc(ml):
    """Convert millilitres to cubic centimetres."""
    return ml * 1


def cup_to_ml(cup):
    """Convert cups to millilitres."""
    return cup * 237


def gal_to_cup(gal):
    """Convert gallons to cups."""
    return gal * 16


def m3_to_ft3(m3):
    """Convert cubic metres to cubic feet."""
    return m3 * 35.31


def ft3_to_m3(ft3):
    """Convert cubic feet to cubic metres."""
    return ft3 * 0.028


# -------------------------------------------------------------- pressure
def atm_to_kpa(atm):
    """Convert atmospheres to kilopascals."""
    return atm * 101.3


def atm_to_mmhg(atm):
    """Convert atmospheres to millimetres of mercury."""
    return atm * 760


def bar_to_pa(bar):
    """Convert bar to pascals."""
    return bar * 10 ** 5


def psi_to_mbar(psi):
    """Convert psi to millibar."""
    return psi * 68.948


# ---------------------------------------------------------------- energy
def j_to_kcal(j):
    """Convert joules to kilocalories."""
    return j * 2.39e-4


def ev_to_j(ev):
    """Convert electronvolts to joules."""
    return ev * 1.602e-19


CONVERSIONS = {
    "length": {"1": ("m -> ft", m_to_ft), "2": ("ft -> m", ft_to_m),
               "3": ("in -> cm", in_to_cm), "4": ("cm -> in", cm_to_in),
               "5": ("mi -> km", mi_to_km), "6": ("km -> mi", km_to_mi)},
    "temperature": {"1": ("C -> F", c_to_f), "2": ("F -> C", f_to_c),
                    "3": ("C -> K", c_to_k), "4": ("F -> K", f_to_k)},
    "mass": {"1": ("kg -> lb", kg_to_lb), "2": ("lb -> kg", lb_to_kg),
             "3": ("oz -> g", oz_to_g), "4": ("g -> oz", g_to_oz)},
    "volume": {"1": ("ml -> cc", ml_to_cc), "2": ("cup -> ml", cup_to_ml),
               "3": ("gal -> cup", gal_to_cup), "4": ("m3 -> ft3", m3_to_ft3),
               "5": ("ft3 -> m3", ft3_to_m3)},
    "pressure": {"1": ("atm -> kPa", atm_to_kpa), "2": ("atm -> mmHg", atm_to_mmhg),
                 "3": ("bar -> Pa", bar_to_pa), "4": ("psi -> mbar", psi_to_mbar)},
    "energy": {"1": ("J -> kcal", j_to_kcal), "2": ("eV -> J", ev_to_j)},
}


def choose(prompt, options):
    """Keep asking until the user types one of the options."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print("Not a valid choice, try again.")


def main():
    """Run the converter until the user quits."""
    while True:
        print("\nTypes:", ", ".join(CONVERSIONS), "(or quit)")
        unit_type = choose("Choose a type: ", list(CONVERSIONS) + ["quit"])
        if unit_type == "quit":
            break
        options = CONVERSIONS[unit_type]
        for key, (label, _) in options.items():
            print(f"  {key}) {label}")
        key = choose("Choose a conversion: ", list(options))
        label, convert = options[key]
        try:
            value = float(input("Enter the value: "))
        except ValueError:
            print("That was not a number.")
            continue
        print(f"Result ({label}): {convert(value):.6g}")


if __name__ == "__main__":
    main()
