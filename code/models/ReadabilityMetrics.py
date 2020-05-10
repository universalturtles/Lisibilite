import logging as LOG
from models.Score import Score


class ReadabilityMetrics:
    def __init__(self):
        LOG.debug(f"{__name__} init")
        self.fres: Score = Score(0.0)  # Flesch Reading Ease Score
        self.fkgl: Score = Score(0.0)  # Flesch-Kincaid Grade Level
        self.gfi: Score = Score(0.0)  # Gunning Fog Index
        self.ari: Score = Score(0.0)  # Automated Readability Index
        self.smog: Score = Score(0.0)  # Simple Measure of Gobbledygook
        self.cli: Score = Score(0.0)  # Coleman-Liau Index
        self.lws: Score = Score(0.0)  # Linsear Write Score
        self.fry: Score = Score(0.0)  # Fry Readability Formula
        self.fres_desc = "Flesch Reading Ease Score"
        self.fkgl_desc = "Flesch-Kincaid Grade Level"
        self.gfi_desc = "Gunning Fog Index"
        self.ari_desc = "Automated Readability Index"
        self.smog_desc = "Simple Measure of Gobbledygook"
        self.cli_desc = "Coleman-Liau Index"
        self.lws_desc = "Linsear Write Score"
        self.fry_desc = "Fry Readability Formula"




    def setFRES(self, fres: float) -> None:
        """
        Set the FRES Score
        :param fres: The FRES score value
        :return: None
        """
        LOG.debug(f'Setting {self.fres_desc} as {fres}')
        self.fres = Score(fres)

    def getFRES(self) -> Score:
        """
        Get the FRES Score
        :return: The FRES Score
        """
        LOG.debug(f'Getting {self.fres_desc}. FRES Score = {self.fres}')
        return self.fres

    def setFKGL(self, fkgl: float) -> None:
        """
        Set the FKGL Score
        :param fkgl: The FKGL score value
        :return: None
        """
        LOG.debug(f'Setting {self.fkgl_desc} as {fkgl}')
        self.fkgl = Score(fkgl)

    def getFKGL(self) -> Score:
        """
        Get the FKGL Score
        :return: The FKGL Score
        """
        LOG.debug(f'Getting {self.fkgl_desc}. FKGL Score = {self.fkgl}')
        return self.fkgl

    def setGFI(self, gfi: float) -> None:
        """
        Set the GFI Score
        :param gfi: Set the GFI Score
        :return: None
        """
        LOG.debug(f'Setting {self.gfi_desc} as {gfi}')
        self.gfi = Score(gfi)

    def getGFI(self) -> Score:
        """
        Get the GFI Score
        :return: The GFI Score
        """
        LOG.debug(f'Getting {self.gfi_desc}. FKGL Score = {self.gfi}')
        return self.gfi

    def setARI(self, ari: float) -> None:
        """
        Set the ARI Score
        :param ari: Set the ARI Score
        :return: None
        """
        LOG.debug(f'Setting {self.ari_desc} as {ari}')
        self.ari = Score(ari)

    def getARI(self) -> Score:
        """
        Get the ARI Score
        :return: The ARI Score
        """
        LOG.debug(f'Getting {self.ari_desc}. FKGL Score = {self.ari}')
        return self.ari

    def setSMOG(self, smog: float) -> None:
        """
        Set the SMOG Score
        :param smog: Set the SMOG Score
        :return: None
        """
        LOG.debug(f'Setting {self.smog_desc} as {smog}')
        self.smog = Score(smog)

    def getSMOG(self) -> Score:
        """
        Get the SMOG Score
        :return: The SMOG Score
        """
        LOG.debug(f'Getting {self.smog_desc}. SMOG Score = {self.smog}')
        return self.smog

    def setCLI(self, cli: float) -> None:
        """
        Set the CLI Score
        :param cli: Set the CLI Score
        :return: None
        """
        LOG.debug(f'Setting {self.cli_desc} as {cli}')
        self.cli = Score(cli)

    def getCLI(self) -> Score:
        """
        Get the CLI Score
        :return: The CLI Score
        """
        LOG.debug(f'Getting {self.cli_desc}. CLI Score = {self.cli}')
        return self.cli

    def setLWS(self, lws: float) -> None:
        """
        Set the LWS Score
        :param lws: Set the LWS Score
        :return: None
        """
        LOG.debug(f'Setting {self.lws_desc} as {lws}')
        self.lws = Score(lws)

    def getLWS(self) -> Score:
        """
        Get the LWS Score
        :return: The LWS Score
        """
        LOG.debug(f'Getting {self.lws_desc}. LWS Score = {self.lws}')
        return self.lws

    def setFRY(self, fry: float) -> None:
        """
        Set the FRY Score
        :param fry: Set the FRY Score
        :return: None
        """
        LOG.debug(f'Setting {self.fry_desc} as {fry}')
        self.fry = Score(fry)

    def getFRY(self) -> Score:
        """
        Get the FRY Score
        :return: The FRY Score
        """
        LOG.debug(f'Getting {self.fry_desc}. FRY Score = {self.fry}')
        return self.fry

    def __str__(self) -> str:
        returnText = f'{self.ari_desc}  = {self.getARI()}\n'
        returnText += f'{self.cli_desc}  = {self.getCLI()}\n'
        returnText += f'{self.fkgl_desc}  = {self.getFKGL()}\n'
        returnText += f'{self.fres_desc}  = {self.getFRES()}\n'
        returnText += f'{self.fry_desc}  = {self.getFRY()}\n'
        returnText += f'{self.gfi_desc}  = {self.getGFI()}\n'
        returnText += f'{self.lws_desc}  = {self.getLWS()}\n'
        returnText += f'{self.smog_desc}  = {self.getSMOG()}'
        return returnText

    def __eq__(self, other):
        if not isinstance(other, ReadabilityMetrics):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.fres == other.fres and \
               self.fkgl == other.fkgl and \
               self.gfi == other.gfi and \
               self.ari == other.ari and \
               self.smog == other.smog and \
               self.cli == other.cli and \
               self.lws == other.lws and \
               self.fry == other.fry