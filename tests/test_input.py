#!/usr/bin/env pytest -vs
"""Test for Input."""

# Third-Party Libraries
import pytest

# cisagov Libraries
import util.input as _input


class TestInput:
    """TestInput class."""

    @pytest.mark.parametrize(
        "time_in,time_out",
        [
            ("01/20/2020 13:00", "2020-01-20T13:00:00-05:00"),
            ("06/20/2020 13:00", "2020-06-20T13:00:00-04:00"),
        ],
    )
    def test_get_time_input(self, mocker, time_in, time_out):
        """Test time input."""
        mocker.patch.object(_input, "get_input")
        _input.get_input.return_value = time_in

        assert _input.get_time_input("start", "US/Eastern") == time_out
