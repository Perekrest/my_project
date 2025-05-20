from typing import Optional
from .inflow_performance.ipr_model import InflowWell
from .outflow_performance.vlp_model import VLPModel
from .plotting import plot_combined

class NodalAnalysis:
    # Класс для узлового анализа скважины
    def __init__(self, ipr_well: InflowWell, vlp_model: VLPModel):
        self.ipr_well = ipr_well
        self.vlp_model = vlp_model
        self.nodal_rate: Optional[float] = None
        self.nodal_pressure: Optional[float] = None

    def calculate_nodal_point(self):
        numerator = self.ipr_well.p_e - self.vlp_model.wellhead_pressure
        denominator = (1 / self.ipr_well.k_pr) + self.vlp_model.hydraulic_loss_coeff

        if denominator <= 0:
            raise ValueError("Невозможно найти точку")

        self.nodal_rate = numerator / denominator
        self.nodal_pressure = self.ipr_well.p_e - self.nodal_rate / self.ipr_well.k_pr

        return self.nodal_rate, self.nodal_pressure

    def plot_results(self, q_max = 300):
        plot_combined(ipr_well=self.ipr_well, vlp_model=self.vlp_model, q_max=q_max)

    def get_results(self):
        return {
            'nodal_rate': self.nodal_rate,
            'nodal_pressure': self.nodal_pressure,
            'ipr_params': {
                'k_pr': self.ipr_well.k_pr,
                'p_e': self.ipr_well.p_e
            },
            'vlp_params': {
                'wellhead_pressure': self.vlp_model.wellhead_pressure,
                'hydraulic_loss_coeff': self.vlp_model.hydraulic_loss_coeff
            }
        }
