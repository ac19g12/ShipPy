import pytest

from shippy.util.coeff import block_coeff,\
      waterplane_coeff,\
          prismatic_coeff,\
              midship_coeff

def test_block():
    assert block_coeff(1,1,1,1) == 1
