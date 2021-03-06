"""Test cases for SOHO Map subclasses.
This particular test file pertains to LASCOMap.
@Author: Pritish C. (VaticanCameos)
"""

import os
import glob

import sunpy.data.test
from sunpy.map import Map
from sunpy.map.sources.soho import LASCOMap

path = sunpy.data.test.rootdir
fitspath = glob.glob(os.path.join(path, "lasco_c2_25299383_s.fts"))
lasco = Map(fitspath)

# LASCO Tests


def test_fitstoLASCO():
    """Tests the creation of LASCOMap using FITS."""
    assert isinstance(lasco, LASCOMap)


def test_is_datasource_for():
    """Test the is_datasource_for method of LASCOMap.
    Note that header data to be provided as an argument
    can be a MetaDict object."""
    assert lasco.is_datasource_for(lasco.data, lasco.meta)


def test_measurement():
    """Tests the measurement property of the LASCOMap object."""
    assert lasco.measurement == "white-light"


def test_observatory():
    """Tests the observatory property of the LASCOMap object."""
    assert lasco.observatory == "SOHO"


def test_norm_clip():
    # Tests that the default normalizer has clipping disabled
    assert not lasco.plot_settings['norm'].clip
