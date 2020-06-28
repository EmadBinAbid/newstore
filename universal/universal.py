
class Universal:
    """
    A global class to implement helper functionalities. All the methods
    in this class are either static or class methods. So this class acts
    as a static class.
    """

    newsSourcesDict = dict()

    @classmethod
    def setNewsSources(self, newsSources) -> None:
        """
        Sets news sources in static dictionary instance.

        Parameters:
        newSources (dict): A dictionary of news sources names and ids

        Returns:
        None

        """
        Universal.newsSourcesDict = newsSources

    @classmethod
    def getNewsSources(self) -> dict:
        """
        Returns the class instance of news sources dictionary object.

        Parameters:
        None

        Returns:
        dict: Dictionary of news sources

        """
        return Universal.newsSourcesDict