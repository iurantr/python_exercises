class Voiture:
    """Une classe """
    compteur=0  # avant le constructteur - variable de la calsse, pas de l'instance
    def __init__(self):
        pass

    @classmethod
    def nombre_instance(cls):
        pass
    @staticmethod
    def crash():
        """This mehtod makes a CRASH"""
        return "CRASH!!!"
    # private methods et attributes par convention, préfixé par _


class Human:
    """This class models a Human"""
    def __init__(self, name):
        """Constructor"""
        self._name=name

    @property
    def _get_name(self):
        """Gets the name of the human"""
        print("We get the value of the 'name' attribute")
        return self._name

    @name.setter
    def _set_name(self, name):
        """Sets the name of the human"""
        print("We set teh value of the 'name' attribute")
        self._name = name
    @name.deleter
    def _del_name(self):
        """Deletes the name of the human"""
        print("We delete the 'name' of the human")
        del self._name
    name = property(_get_name, _set_name, _del_name)