import logging as LOG


class Score:
    def __init__(self, value=0.0):
        LOG.debug(f"{__name__} init")
        # Original Float Value
        self.value: float = value

        # Rounded Value - rounded to 2 decimal places
        self.roundedValue: float = round(self.value, 2)

        # String description of the score
        self.label: str = ''

    def setValue(self, value: float) -> None:
        """
        Set the value for the score and in turn sets the rounded value
        :param value: The value to set
        :return: None
        """
        LOG.debug(f'Setting {value} for score')
        self.value = value
        self.roundedValue = round(self.value, 2)

    def getValue(self) -> float:
        """
        Get the Value of the score
        :return: The Value
        """
        LOG.debug(f'Getting value. Value of score = {self.value}')
        return self.value

    def getRoundedValue(self) -> float:
        """
        Get the rounder value
        :return: The rounded value set to 2 decimal places
        """
        LOG.debug(
            f'Getting rounded value. Rounded value = {self.roundedValue}')
        return self.roundedValue

    def setLabel(self, label: str) -> None:
        """
        Set the label for the score
        :param label: The label for the score
        :return: None
        """
        LOG.debug(f'Setting label for score as {label}')
        self.label = label

    def getLabel(self) -> float:
        """
        Get the label of the score
        :return: The label of the score
        """
        LOG.debug(f'Getting label. Label of score = {self.label}')
        return self.label

    def __str__(self) -> str:
        returnText = f'Value  = {self.getValue()}\n'
        returnText += f'Rounded Value  = {self.getRoundedValue()}\n'
        returnText += f'Label  = {self.getLabel()}'
        return returnText

    def __eq__(self, other):
        if not isinstance(other, Score):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.value == other.value \
            and self.roundedValue == other.roundedValue \
            and self.label == other.label
