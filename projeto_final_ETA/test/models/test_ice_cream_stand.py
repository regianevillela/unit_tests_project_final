from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available(self):
        ice = IceCreamStand('Ice Cream ', 'Sorvete', ['Morango', 'Chocolate', 'Baunilha'])
        result_expected = "No momento temos os seguintes sabores de sorvete disponíveis:\nMorango\nChocolate\nBaunilha"
        result = ice.flavors_available()

        assert result_expected == result

    def test_flavors_out_of_stock(self):
        ice = IceCreamStand('Divino Sabor', 'Sorvete', [])
        result_expected = "Estamos sem estoque atualmente!"
        result = ice.flavors_available()

        assert result_expected == result

    def test_find_flavor(self):
        ice = IceCreamStand('Bacio di Latte', 'Sorvete', ['Morango', 'Chocolate', 'Baunilha'])
        result_expected = "Temos no momento o sabor Baunilha!"
        result = ice.find_flavor('Baunilha')

        assert result_expected == result

    def test_find_flavor_not_found(self):
        ice = IceCreamStand('Oggi Sorvetes', 'Sorvete', ['Morango', 'Chocolate', 'Baunilha'])
        result_expected = "Não temos no momento o sabor Cupuaçu!"
        result = ice.find_flavor('Cupuaçu')

        assert result_expected == result

    def test_find_flavor_out_of_stock(self):
        ice = IceCreamStand('Davvero', 'Sorvete', [])
        result_expected = "Estamos sem estoque atualmente!"
        result = ice.find_flavor('Rosas')

        assert result_expected == result

    def test_add_flavor(self):
        ice = IceCreamStand('Nhô Sorvetes', 'Sorvete', ['Morango', 'Chocolate', 'Cupuaçu'])
        result_expected = "Pistache adicionado ao estoque!"
        result = ice.add_flavor('Pistache')

        assert result_expected == result

    def test_add_flavor_available(self):
        ice = IceCreamStand('Cuor di Crema', 'Sorvete', ['Pistache', 'Graviola', 'Cupuaçu'])
        result_expected = "Sabor já disponivel!"
        result = ice.add_flavor('Graviola')

        assert result_expected == result

    def test_add_flavor_out_of_stock(self):
        ice = IceCreamStand('nice cream', 'Sorvete', [])
        result_expected = "Estamos sem estoque atualmente!"
        result = ice.add_flavor('Cereja')

        assert result_expected == result
