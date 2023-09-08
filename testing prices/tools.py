class to_use:

    ## Price
    def get_profit(final_price):

        remove_tva = 1.19
        
        def calculate_base_price(final_price, percentage):
            return final_price / (1 + percentage)

        table = [
            (4.99, 1.0),
            (9.99, 1.0),
            (14.99, 0.9),
            (24.99, 0.9),
            (29.99, 0.9),
            (34.99, 0.8),
            (39.99, 0.65),
            (49.99, 0.6),
            (54.99, 0.58),
            (64.99, 0.5),
            (74.99, 0.45),
            (89.99, 0.43),
            (99.99, 0.37),
            (124.99, 0.32),
            (144.99, 0.29),
            (174.99, 0.28),
            (199.99, 0.27),
            (229.99, 0.26),
            (299.99, 0.25),
            (399.99, 0.24),
            (499.99, 0.23),
            (649.99, 0.22),
            (749.99, 0.21),
            (799.99, 0.20),
            (899.99, 0.19),
            (999.99, 0.18),
            (1999.99, 0.17),
            (4999.99, 0.12),
            (float('inf'), 0.10)
        ]

        for price, percentage in table:
            base_price = calculate_base_price(final_price, percentage)
            if base_price <= price:
                return (final_price - base_price)/remove_tva
            