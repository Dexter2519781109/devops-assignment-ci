class Calculator:
    """
    Számológép példa. A projekt 'éles kódja'.
    """

    def add(self, a, b):
        """Összeadás: a + b"""
        return a + b

    def sub(self, a, b):
        """Kivonás: a - b"""
        return a - b

    def mul(self, a, b):
        """Szorzás: a * b"""
        return a * b

    def div(self, a, b):
        """
        Osztás: a / b.
        Ha b == 0, akkor hibát dob, mert 0-val nem lehet osztani.
        Teszthez.
        """
        if b == 0:
            raise ValueError("division by zero")
        return a / b