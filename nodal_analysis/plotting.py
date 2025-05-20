import matplotlib.pyplot as plt
from .inflow_performance.ipr_model import InflowWell
from .outflow_performance.vlp_model import VLPModel

def plot_ipr_curve(well: InflowWell, p_w_values):
    sorted_pressures = sorted(p_w_values)
    rates = [well.k_pr * (well.p_e - pw) for pw in sorted_pressures]

    plt.figure(figsize=(10, 6))
    plt.plot(sorted_pressures, rates, 'b-', linewidth=2, marker='o')
    plt.xlabel('Забойное давление (бар)', fontsize=12)
    plt.ylabel('Дебит (м3/сут)', fontsize=12)
    plt.title('Inflow Performance Relationship (IPR)', fontsize=14)
    plt.grid()
    plt.tight_layout()
    plt.show()

def plot_vlp_curve(vlp_model: VLPModel, rates):
    pressures = vlp_model.vlp_table(rates)

    plt.figure(figsize=(10,6))
    plt.plot(rates, pressures, 'r--', linewidth=2, marker='o')
    plt.xlabel('Дебит (м3/сут)', fontsize=12)
    plt.ylabel('Забойное давление (бар)', fontsize=12)
    plt.title('Vertical Lift Performance (VLP)', fontsize=14)
    plt.grid()
    plt.tight_layout()
    plt.show()

def plot_combined(ipr_well: InflowWell, vlp_model: VLPModel, q_max = 300):
    q_values = list(range(0, q_max + 1, 10))

    # Расчет
    ipr_pressures = [ipr_well.p_e - q / ipr_well.k_pr for q in q_values]
    vlp_pressures = [vlp_model.wellhead_pressure + vlp_model.hydraulic_loss_coeff * q for q in q_values]

    # Точка пересечения
    numerator = ipr_well.p_e - vlp_model.wellhead_pressure
    denominator = (1/ipr_well.k_pr) + vlp_model.hydraulic_loss_coeff
    intersection_q = numerator / denominator
    intersection_p = ipr_well.p_e - intersection_q / ipr_well.k_pr

    # Построение графика
    plt.figure(figsize=(12, 7))
    plt.plot(q_values, ipr_pressures, 'b-', label='IPR', marker='o')
    plt.plot(q_values, vlp_pressures, 'r--', label='VLP', marker='s')

    plt.scatter(intersection_q, intersection_p, color='green', s=100, label=f'Узел\nQ={intersection_q:.1f}\nP={intersection_p:.1f}')

    plt.xlabel('Дебит (м3/сут)', fontsize=12)
    plt.ylabel('Забойное давление (бар)', fontsize=12)
    plt.title('Узловой анализ', fontsize=14)
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()
