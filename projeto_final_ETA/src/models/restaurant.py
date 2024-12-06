class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """
        Imprima uma descrição simples da instância do restaurante.
        """

        ###print(f"Esse restaurante se chama {self.restaurant_name} e serve {self.cuisine_type}.")    ### Corrigindo a ordem das variaveis
        ###print(f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto.")

        return f"Esse restaurante se chama {self.restaurant_name} e serve {self.cuisine_type}." \
               f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto."

    def open_restaurant(self):
        """
        Imprima uma mensagem indicando que o restaurante está aberto para negócios.
        """
        if not self.open:
            self.open = True                                        ### Estava False. Alterando para True (BUG)
            self.number_served = 0                                  ### Estava -2. Alterando para 0 (BUG)
            return f"{self.restaurant_name} agora está aberto!"     ###print(f"{self.restaurant_name} agora está aberto!")
        else:
            return f"{self.restaurant_name} já está aberto!"        ###print(f"{self.restaurant_name} já está aberto!")

    def close_restaurant(self):
        """
        Imprima uma mensagem indicando que o restaurante está fechado para negócios.
        """
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"    ###print(f"{self.restaurant_name} agora está fechado!")
        else:
            return f"{self.restaurant_name} já está fechado!"       ###print(f"{self.restaurant_name} já está fechado!")

    def set_number_served(self, total_customers):
        """
        Defina o número total de pessoas atendidas por este restaurante até o momento.
        """
        if self.open:
            self.number_served = total_customers
            return self.number_served                           ### adicionando return da variavel self.number_served
        else:
            return f"{self.restaurant_name} está fechado!"      ###print(f"{self.restaurant_name} está fechado!")

    def increment_number_served(self, more_customers):
        """
        Aumenta número total de clientes atendidos por este restaurante.
        """
        if self.open:
            self.number_served += more_customers                ### Estava apenas com o =. Alterando para += (BUG)
            return self.number_served                           ### adicionando return da variavel self.number_served
        else:
            return f"{self.restaurant_name} está fechado!"      ###print(f"{self.restaurant_name} está fechado!")