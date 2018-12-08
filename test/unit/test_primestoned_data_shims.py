import pytest
import sys
import os
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), '../../lib')))
import primestonelib


@pytest.fixture
def sentinel_proposal_hex():
    return '5b2270726f706f73616c222c207b22656e645f65706f6368223a20313439313032323830302c20226e616d65223a2022626565722d7265696d62757273656d656e742d37222c20227061796d656e745f61646472657373223a2022795965384b77796155753559737753596d4233713372797838585455753979375569222c20227061796d656e745f616d6f756e74223a20372e30303030303030302c202273746172745f65706f6368223a20313438333235303430302c202275726c223a202268747470733a2f2f6461736863656e7472616c2e636f6d2f626565722d7265696d62757273656d656e742d37227d5d'


@pytest.fixture
def sentinel_superblock_hex():
    return '5b227375706572626c6f636b222c207b226576656e745f626c6f636b5f686569676874223a2036323530302c20227061796d656e745f616464726573736573223a2022795965384b77796155753559737753596d42337133727978385854557539793755697c795443363268755234595145506e39414a486a6e517878726548536267416f617456222c20227061796d656e745f616d6f756e7473223a2022357c33227d5d'


@pytest.fixture
def primestoned_proposal_hex():
    return '5b5b2270726f706f73616c222c207b22656e645f65706f6368223a20313439313336383430302c20226e616d65223a2022626565722d7265696d62757273656d656e742d39222c20227061796d656e745f61646472657373223a2022795965384b77796155753559737753596d4233713372797838585455753979375569222c20227061796d656e745f616d6f756e74223a2034392e30303030303030302c202273746172745f65706f6368223a20313438333235303430302c202274797065223a20312c202275726c223a202268747470733a2f2f7777772e6461736863656e7472616c2e6f72672f702f626565722d7265696d62757273656d656e742d39227d5d5d'


@pytest.fixture
def primestoned_superblock_hex():
    return '5b5b2274726967676572222c207b226576656e745f626c6f636b5f686569676874223a2036323530302c20227061796d656e745f616464726573736573223a2022795965384b77796155753559737753596d42337133727978385854557539793755697c795443363268755234595145506e39414a486a6e517878726548536267416f617456222c20227061796d656e745f616d6f756e7473223a2022357c33222c202274797065223a20327d5d5d'

# ========================================================================


def test_SHIM_deserialise_from_primestoned(primestoned_proposal_hex, primestoned_superblock_hex):
    assert primestonelib.SHIM_deserialise_from_primestoned(primestoned_proposal_hex) == '5b2270726f706f73616c222c207b22656e645f65706f6368223a20313439313336383430302c20226e616d65223a2022626565722d7265696d62757273656d656e742d39222c20227061796d656e745f61646472657373223a2022795965384b77796155753559737753596d4233713372797838585455753979375569222c20227061796d656e745f616d6f756e74223a2034392e30303030303030302c202273746172745f65706f6368223a20313438333235303430302c202275726c223a202268747470733a2f2f7777772e6461736863656e7472616c2e6f72672f702f626565722d7265696d62757273656d656e742d39227d5d'
    assert primestonelib.SHIM_deserialise_from_primestoned(primestoned_superblock_hex) == '5b227375706572626c6f636b222c207b226576656e745f626c6f636b5f686569676874223a2036323530302c20227061796d656e745f616464726573736573223a2022795965384b77796155753559737753596d42337133727978385854557539793755697c795443363268755234595145506e39414a486a6e517878726548536267416f617456222c20227061796d656e745f616d6f756e7473223a2022357c33227d5d'


def test_SHIM_serialise_for_primestoned(sentinel_proposal_hex, sentinel_superblock_hex):
    assert primestonelib.SHIM_serialise_for_primestoned(sentinel_proposal_hex) == '5b5b2270726f706f73616c222c207b22656e645f65706f6368223a20313439313032323830302c20226e616d65223a2022626565722d7265696d62757273656d656e742d37222c20227061796d656e745f61646472657373223a2022795965384b77796155753559737753596d4233713372797838585455753979375569222c20227061796d656e745f616d6f756e74223a20372e30303030303030302c202273746172745f65706f6368223a20313438333235303430302c202274797065223a20312c202275726c223a202268747470733a2f2f6461736863656e7472616c2e636f6d2f626565722d7265696d62757273656d656e742d37227d5d5d'
    assert primestonelib.SHIM_serialise_for_primestoned(sentinel_superblock_hex) == '5b5b2274726967676572222c207b226576656e745f626c6f636b5f686569676874223a2036323530302c20227061796d656e745f616464726573736573223a2022795965384b77796155753559737753596d42337133727978385854557539793755697c795443363268755234595145506e39414a486a6e517878726548536267416f617456222c20227061796d656e745f616d6f756e7473223a2022357c33222c202274797065223a20327d5d5d'
