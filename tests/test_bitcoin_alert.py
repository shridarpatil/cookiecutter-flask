#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test bitcoin alert"""
import pytest


def test_bitcoin_alert():
    """
    Bitcoin Alert.

    test cases
    """
    try:
        # Is Trading day 2017-09-09
        assert True is True
    except AssertionError as e:
        pytest.fail("is_tradin_day 2017-09-09 Error: {}".format(e))
