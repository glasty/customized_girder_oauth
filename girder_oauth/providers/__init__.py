# -*- coding: utf-8 -*-
import collections

from .google import Google
from .globus import Globus
from .github import GitHub
from .linkedin import LinkedIn
from .bitbucket import Bitbucket
from .box import Box
from .custom import Custom
from .otherCustom import Custom2, Custom3, Custom4, Custom5, Custom6, Custom7, Custom8


def addProvider(provider):
    idMap[provider.getProviderName()] = provider


idMap = collections.OrderedDict()

addProvider(Google)
addProvider(Globus)
addProvider(GitHub)
addProvider(LinkedIn)
addProvider(Bitbucket)
addProvider(Box)
addProvider(Custom)
addProvider(Custom2)
addProvider(Custom3)
addProvider(Custom4)
addProvider(Custom5)
addProvider(Custom6)
addProvider(Custom7)
addProvider(Custom8)
