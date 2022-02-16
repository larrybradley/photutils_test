# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Tests for the ellipse module.
"""

from astropy.coordinates import SkyCoord
import astropy.units as u
import numpy as np
import pytest

from .test_aperture_common import BaseTestAperture
from ..ellipse import (EllipticalAperture, EllipticalAnnulus,
                       SkyEllipticalAperture, SkyEllipticalAnnulus)


POSITIONS = [(10, 20), (30, 40), (50, 60), (70, 80)]
RA, DEC = np.transpose(POSITIONS)
SKYCOORD = SkyCoord(ra=RA, dec=DEC, unit='deg')
UNIT = u.arcsec
RADII = (0.0, -1.0, -np.inf)


class TestEllipticalAperture(BaseTestAperture):
    aperture = EllipticalAperture(POSITIONS, a=10., b=5., theta=np.pi/2.)

    @staticmethod
    @pytest.mark.parametrize('radius', RADII)
    def test_invalid_params(radius):
        with pytest.raises(ValueError):
            EllipticalAperture(POSITIONS, a=radius, b=5., theta=np.pi/2.)
        with pytest.raises(ValueError):
            EllipticalAperture(POSITIONS, a=10., b=radius, theta=np.pi/2.)


class TestEllipticalAnnulus(BaseTestAperture):
    aperture = EllipticalAnnulus(POSITIONS, a_in=10., a_out=20., b_out=17,
                                 theta=np.pi/3)

    @staticmethod
    @pytest.mark.parametrize('radius', RADII)
    def test_invalid_params(radius):
        with pytest.raises(ValueError):
            EllipticalAnnulus(POSITIONS, a_in=radius, a_out=20., b_out=17,
                              theta=np.pi/3)
        with pytest.raises(ValueError):
            EllipticalAnnulus(POSITIONS, a_in=10., a_out=radius, b_out=17,
                              theta=np.pi/3)
        with pytest.raises(ValueError):
            EllipticalAnnulus(POSITIONS, a_in=10., a_out=20., b_out=radius,
                              theta=np.pi/3)
        with pytest.raises(ValueError):
            EllipticalAnnulus(POSITIONS, a_in=10., a_out=20., b_out=17,
                              b_in=radius, theta=np.pi/3)


class TestSkyEllipticalAperture(BaseTestAperture):
    aperture = SkyEllipticalAperture(SKYCOORD, a=10.*UNIT, b=5.*UNIT,
                                     theta=30*u.deg)

    @staticmethod
    @pytest.mark.parametrize('radius', RADII)
    def test_invalid_params(radius):
        with pytest.raises(ValueError):
            SkyEllipticalAperture(SKYCOORD, a=radius*UNIT, b=5.*UNIT,
                                  theta=30*u.deg)
        with pytest.raises(ValueError):
            SkyEllipticalAperture(SKYCOORD, a=10.*UNIT, b=radius*UNIT,
                                  theta=30*u.deg)


class TestSkyEllipticalAnnulus(BaseTestAperture):
    aperture = SkyEllipticalAnnulus(SKYCOORD, a_in=10.*UNIT, a_out=20.*UNIT,
                                    b_out=17.*UNIT, theta=60*u.deg)

    @staticmethod
    @pytest.mark.parametrize('radius', RADII)
    def test_invalid_params(radius):
        with pytest.raises(ValueError):
            SkyEllipticalAnnulus(SKYCOORD, a_in=radius*UNIT, a_out=20.*UNIT,
                                 b_out=17.*UNIT, theta=60*u.deg)
        with pytest.raises(ValueError):
            SkyEllipticalAnnulus(SKYCOORD, a_in=10.*UNIT, a_out=radius*UNIT,
                                 b_out=17.*UNIT, theta=60*u.deg)
        with pytest.raises(ValueError):
            SkyEllipticalAnnulus(SKYCOORD, a_in=10.*UNIT, a_out=20.*UNIT,
                                 b_out=radius*UNIT, theta=60*u.deg)
        with pytest.raises(ValueError):
            SkyEllipticalAnnulus(SKYCOORD, a_in=10.*UNIT, a_out=20.*UNIT,
                                 b_out=17.*UNIT, b_in=radius*UNIT,
                                 theta=60*u.deg)
