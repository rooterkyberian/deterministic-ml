def test_apiver_exports(apiver_module):
    assert sorted(name for name in dir(apiver_module) if not name.startswith("_")) == [
        "set_deterministic",
        "set_deterministic_pytorch",
    ]
