#  Nangate15 plugin for Hammer.
#
#  See LICENSE for licence details.

import sys
import re
import os, shutil
from pathlib import Path
from typing import NamedTuple, List, Optional, Tuple, Dict, Set, Any
import importlib

import hammer.tech
from hammer.tech import HammerTechnology
from hammer.vlsi import HammerTool, HammerPlaceAndRouteTool, TCLTool, HammerDRCTool, HammerLVSTool, HammerToolHookAction

import hammer.tech.specialcells as specialcells
from hammer.tech.specialcells import CellType, SpecialCell

class Nangate15Tech(HammerTechnology):
    """
    Override the HammerTechnology used in `hammer_tech.py`
    This class is loaded by function `load_from_json`, and will pass the `try` in `importlib`.
    """

tech = Nangate15Tech()
