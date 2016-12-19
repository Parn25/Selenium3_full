import pytest
from aplication import Aplication
#Тест добаления трех продуктов и удаления их из корзине
@pytest.fixture
def app(request):
    app = Aplication()
    request.addfinalizer(app.quit)
    return app
def test_add_del_product(app):
    app.st_open()#Открываем стартовую страницу
    app.add_duck("Yellow Duck")#Добавляем продукт
    app.add_duck("Green Duck")
    app.add_duck("Blue Duck")
    app.d_all_duck()#Elfkztv dct ghjlerns

