
class Universal:
    newsSourcesDict = dict()

    @classmethod
    def setNewsSources(self, newsSources) -> None:
        Universal.newsSourcesDict = newsSources

    @classmethod
    def getNewsSources(self) -> dict:
        return Universal.newsSourcesDict