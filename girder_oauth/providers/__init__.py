# -*- coding: utf-8 -*-
import collections

from .google import Google
from .globus import Globus
from .github import GitHub
from .linkedin import LinkedIn
from .bitbucket import Bitbucket
from .box import Box
from .custom import Custom
from .custom2 import Custom2
from .custom3 import Custom3
from .custom4 import Custom4
from .custom5 import Custom5


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



