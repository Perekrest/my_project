class VLPModel:
        #Класс для моделирования кривой оттока
    def __init__(self, wellhead_pressure, hydraulic_loss_coeff):
        self.wellhead_pressure = wellhead_pressure
        self.hydraulic_loss_coeff = hydraulic_loss_coeff

    def vlp_table(self, rates: list):
        return [self.calculate_pwf(q) for q in rates]

    def calculate_pwf(self, rate: float):
        return self.wellhead_pressure + self.hydraulic_loss_coeff * rate
