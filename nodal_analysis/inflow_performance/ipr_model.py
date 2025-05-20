class InflowWell:
    #Класс для моделирования притока в скважину
    def __init__(self, k_pr, p_e, p_w, cum_oil = 0):
        self.k_pr = k_pr
        self.p_e = p_e
        self.p_w = p_w
        self.cum_oil = cum_oil
        self.dp = p_e - p_w

    def calculate_rate(self, time):
        if self.dp > 0:
            rate = self.k_pr * self.dp
            self.cum_oil += rate * time
            return rate
        return 0.0

    def get_cum_oil(self):
        return self.cum_oil


class InvertedWell:
    # Класс для расчета забойного давления по заданному дебиту
    def __init__(self, k_pr, p_e, rate):

        self.k_pr = k_pr
        self.p_e = p_e
        self.rate = rate

    def calculate_pressure(self):
        return self.p_e - (self.rate / self.k_pr)
