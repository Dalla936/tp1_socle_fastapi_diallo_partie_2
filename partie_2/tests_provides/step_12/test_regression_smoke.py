from __future__ import annotations

def test_should_import_application_layers():
    # Arrange / Act
    import app.api
    import app.services
    import app.repositories

    # Assert (1 assertion métier)
    assert True
