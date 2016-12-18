import pytest
from aplication import Aplication

@pytest.fixture
def app(request):
    app = Aplication()
    request.addfinalizer(app.quit)
    return app
def test_add_del_product(app):
    app.st_open()
    app.add_duck("Yellow Duck")
    app.add_duck("Green Duck")
    app.add_duck("Blue Duck")
    app.d_all_duck()

