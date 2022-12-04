from .day import build_zone, CleaningZone
from hypothesis import given, strategies as st, assume, settings, HealthCheck


def test_input():
    zones, count = build_zone("test.txt")
    assert count == 2


@given(zone_1_start=st.integers(min_value=1), zone_1_end=st.integers(), zone_2_start=st.integers(), zone_2_end=st.integers())
@settings(max_examples=500, suppress_health_check=[HealthCheck.filter_too_much])
def test_contains(zone_1_start, zone_1_end, zone_2_start, zone_2_end):
    assume(zone_1_start <= zone_1_end)
    assume(zone_1_start <= zone_2_start)
    assume(zone_2_end <= zone_1_end)
    assume(zone_2_start <= zone_2_end)

    zone_1 = CleaningZone(f"{zone_1_start}-{zone_1_end}")
    zone_2 = CleaningZone(f"{zone_2_start}-{zone_2_end}")
    assert zone_1.contains(zone_1)
    assert zone_1.contains(zone_2)


@given(zone_1_start=st.integers(min_value=1), zone_1_end=st.integers(), zone_2_start=st.integers(), zone_2_end=st.integers())
@settings(max_examples=500, suppress_health_check=[HealthCheck.filter_too_much])
def test_overlap(zone_1_start, zone_1_end, zone_2_start, zone_2_end):
    assume(zone_1_start <= zone_1_end)
    assume(zone_1_start <= zone_2_start)
    assume(zone_2_start <= zone_2_end)
    assume(zone_1_end <= zone_2_end)

    zone_1 = CleaningZone(f"{zone_1_start}-{zone_1_end}")
    zone_2 = CleaningZone(f"{zone_2_start}-{zone_2_end}")
    assert zone_1.overlap(zone_1)
    assert zone_2.overlap(zone_2)
