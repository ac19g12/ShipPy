from pint import UnitRegistry
ureg = UnitRegistry()

@ureg.wraps(None, ('=A**3', '=A', '=A', '=A'), strict=False)
def block_coeff(displacement:float,
                beam:float,
                draft:float,
                length:float) -> float:
    """The Block Coefficient, Cb, is the ratio of the volume of displacement 
    to the volume of a rectangular block whose sides are equal to the breadth
    extreme, the mean draught and length between perpendiculars.


    Parameters
    ----------
    displacement : float
        The volumeteric displacement at the draft. 
    beam : float
        breadth extreme in meters.
    draft : float
        The mean draft in meters.
    length : float
        The length between perpendiculars in meters.

    Returns
    -------
    float
        The block coefficient as a non-dimenisonal number.
    """
    return displacement / (beam * draft * length)

@ureg.wraps(None, ('=A**2', '=A', '=A'), strict=False)
def waterplane_coeff(area:float,
                     beam:float,
                     length:float) -> float:
    """The Coefficient of fineness of waterplane, Cwp, is the ratio of the
    area of the waterlane to the area of circumscribing rectangle. 
    Parameters
    ----------
    area : float
        The area of the waterplane at a draft in meters^2. 
    beam : float
        breadth extreme in meters.
    length : float
        The length between perpendiculars in meters.

    Returns
    -------
    float
        The waterplane coefficient as a non-dimenisonal number.
    """
    return area / (beam * length)

@ureg.wraps(None, ('=A**2', '=A', '=A'), strict=False)
def midship_coeff(area:float,
                beam:float,
                draft:float) -> float:
    """The midship section coefficient, Cm, is the ratio of the midship section
    area to the area of a rectangle whose sides are equal to the draught and
    the breadth extreme amidships.

    Parameters
    ----------
    area : float
        The midship area in meters^2. 
    beam : float
        breadth extreme in meters.
    draft : float
        The mean draft in meters.

    Returns
    -------
    float
        The block coefficient as a non-dimenisonal number.
    """
    return area / (beam * draft)

@ureg.wraps(None, ('=A**3', '=A**2', '=A'), strict=False)
def prismatic_coeff(displacement:float,
                midship_area:float,
                length:float) -> float:
    """The longitudinal prismatic coefficient, Cp, is the ratio of the volume
    of displacement to the volumne of a prism having a length equal to the
    length between perpendiculars and cross sectional area equal to the
    midship sectional area.

    Parameters
    ----------
    displacement : float
        The volumeteric displacement at the draft. 
    midship_area : float
        The midship area in meters^2.
    length : float
        The length between perpendiculars in meters.

    Returns
    -------
    float
        The block coefficient as a non-dimenisonal number.
    """
    return displacement / (midship_area * length)