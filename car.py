import math

class Tire:
    """
    Represent a tire.
    """

    def __init__(self, tire_type, width, ratio, diameter, brand = '', construction='R'):
        self.brand = brand
        self.tire_type = tire_type
        self.diameter = diameter
        self.width = width
        self.ratio = ratio
        self.construction = construction
    
    def circumference(self):
        """
        The circumference of the tire in inches.

        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """
        side_wall_inches = self._side_wall_inches()
        total_diameter = side_wall_inches * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def _side_wall_inches(self):
        return (self.width * (self.ratio / 100)) / 25.4

    def __repr__(self):
        return( f'{self.tire_type}{self.width}/{self.ratio} '
                f'{self.construction}{self.diameter}' )
    pass

class SnowTire(Tire):
    def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand='', construction='R'):
        super().__init__(tire_type, width, ratio, diameter, brand, construction)
        self.chain_thickness = chain_thickness

    def circumference(self):
        """
        The circumference of a tire w/ show chains in inches.

        >>> tire = SnowTire('P', 205, 65, 15, 2)
        >>> tire.circumference()
        92.7
        """
        side_wall_inches = self._side_wall_inches()
        total_diameter = (side_wall_inches + self.chain_thickness) * 2 + self.diameter
        return round(total_diameter * math.pi, 1)
    
    def __repr__(self):
        return super().__repr__() + " (Snow)"
    pass

class Car:
    """
    Represent a car. 
    """

    def __init__(self, engine, tires):
        """
        Initialize this object.
        """
        self.engine = engine
        self.tires = tires
        pass

    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0

    def description(self):
        return f'Car(engine: {self.engine!r}, tires: {self.tires})'
    pass

