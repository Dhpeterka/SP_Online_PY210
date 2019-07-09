#!/usr/bin/env python
"""
Test suite for all the code in mailroom object assignment.
"""

import pytest

from donor_model import *


##########
# Test initializing

def test_init():
    """
    Test we can make a donor object with the name John
    Name is required
    Make sure name can't be set.
    Make sure donation can't be set
    """
    d = Donor('John')

    assert d.name == 'John'

    with pytest.raises(AttributeError):
        d.name = 'Tom'

    with pytest.raises(AttributeError):
        d.donations = 100


def test_add_donation():
    d = Donor('John')

    # Test adding float
    d.add_donation(100.00)
    assert d.donations == [100]
    assert d.num_donations == 1

    # Test adding integer value
    d.add_donation(20)
    assert d.donations == [100, 20]
    assert d.num_donations == 2

    # Test donation amount can't be empty or zero
    with pytest.raises(TypeError):
        d.add_donation()

    # Test donation added can't be negative
    with pytest.raises(ValueError):
        d.add_donation(-100)

    # Test donation is greater than 0
    with pytest.raises(ValueError):
        d.add_donation(0)

    # Test donation has to be a number
    with pytest.raises(TypeError):
        d.add_donation('hello')


def test_tot_donated():
    d = Donor('John')

    d.add_donation(100.00)
    assert d.total_donated == 100

    d.add_donation(100.00)
    assert d.total_donated == 200


def test_average_donation():
    d = Donor('John')

    d.add_donation(100)
    assert d.average_donation == 100

    d.add_donation(50)
    assert d.average_donation == 75
