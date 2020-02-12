class Car:
    """
    Some text that describe the object. 
    """

    def __init__(self, engine, tires):
        """
        Initialize this object.
        """
        print('__init__ called')
        self.name = 'unnamed'
        self.model = 'unknown'
        self.engine = engine
        self.tires = tires
        print('__init__ completed')
        pass
    pass

