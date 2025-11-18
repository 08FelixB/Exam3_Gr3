import pytest
from debogue_moi import *


def test_ajouter_apres_dernier(rendez_vous, nom, duree):
    assert ajouter_apres_dernier(rendez_vous, nom, duree) == rendez_vous







