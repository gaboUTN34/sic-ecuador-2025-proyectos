#====================================================================#
#                             3. Graficos                            #
#====================================================================#
import matplotlib.pyplot as plt
import seaborn as sns

def grafico_finanzas_personales(df_finanzas, cedula):
    # Filtrar usuario específico
    usuario = df_finanzas[df_finanzas['cedula'] == cedula].iloc[0]

    # Calcular totales
    total_ingresos = sum(usuario['ingresos'].values())
    total_gastos_prio = sum(usuario['gastos_prioritarios'].values())
    total_gastos_sec = sum(usuario['gastos_secundarios'].values())
    total_gastos = total_gastos_prio + total_gastos_sec
    ahorro_actual = total_ingresos * (usuario['porcentaje_ahorro'] / 100)

    # Crear figura con dos subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Gráfico 1: Ingresos vs Gastos Totales
    categorias_ingresos_gastos = ['Ingresos', 'Gastos Totales']
    valores_ingresos_gastos = [total_ingresos, total_gastos]
    colores_ingresos_gastos = ['#2ecc71', '#e74c3c']

    ax1.pie(valores_ingresos_gastos, labels=categorias_ingresos_gastos, autopct='%1.1f%%',
            colors=colores_ingresos_gastos, startangle=90)
    ax1.set_title(f'Ingresos vs Gastos Totales\n{usuario["nombre"]} {usuario["apellido"]}')

    # Gráfico 2: Composición de Gastos (mantenemos el original)
    gastos_labels = ['Prioritarios', 'Secundarios']
    gastos_values = [total_gastos_prio, total_gastos_sec]
    ax2.pie(gastos_values, labels=gastos_labels, autopct='%1.1f%%',
            colors=['#e74c3c', '#f39c12'], startangle=90)
    ax2.set_title('Composición de Gastos')

    plt.tight_layout()
    plt.show()

def grafico_comparativo_completo(df_finanzas, cedula):
    # Filtrar usuario específico
    usuario = df_finanzas[df_finanzas['cedula'] == cedula].iloc[0]

    # Calcular totales REALES
    total_ingresos = sum(usuario['ingresos'].values())
    total_gastos_prio = sum(usuario['gastos_prioritarios'].values())
    total_gastos_sec = sum(usuario['gastos_secundarios'].values())
    total_gastos = total_gastos_prio + total_gastos_sec

    # Calcular ahorro REAL
    ahorro_real = total_ingresos - total_gastos
    porcentaje_ahorro_real = (ahorro_real / total_ingresos) * 100 if total_ingresos > 0 else 0

    # Ahorro esperado
    porcentaje_ahorro_esperado = usuario['porcentaje_ahorro']
    ahorro_esperado = total_ingresos * (porcentaje_ahorro_esperado / 100)

    # Crear gráfico único
    fig, ax = plt.subplots(figsize=(10, 6))

    # Configurar posiciones de las barras
    categorias = ['Ahorro Real', 'Ahorro Esperado']
    montos = [ahorro_real, ahorro_esperado]
    porcentajes = [porcentaje_ahorro_real, porcentaje_ahorro_esperado]
    colores = ['#2ecc71' if ahorro_real >= ahorro_esperado else '#e74c3c', '#3498db']

    # Crear barras más delgadas (reducido de 0.6 a 0.4)
    bars = ax.bar(categorias, montos, color=colores, alpha=0.8, width=0.4)

    # Personalización del gráfico
    ax.set_ylabel('Monto ($)')
    ax.set_title(f'Comparación: Ahorro Real vs Esperado\n{usuario["nombre"]} {usuario["apellido"]}')
    ax.grid(axis='y', alpha=0.3)

    # Aumentar el límite del eje Y en un 30% del valor más alto
    max_monto = max(montos)
    ax.set_ylim(0, max_monto * 1.3)

    # Añadir valores en las barras con formato combinado
    for bar, monto, porcentaje in zip(bars, montos, porcentajes):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + (max_monto * 1.3 - max_monto) * 0.1,
                f'${monto:.2f} ({porcentaje:.1f}%)',
                ha='center', va='bottom', fontweight='bold', fontsize=11)

    # Línea de referencia para el ahorro esperado
    ax.axhline(y=ahorro_esperado, color='red', linestyle='--', alpha=0.7,
               label=f'Meta: ${ahorro_esperado:.2f} ({porcentaje_ahorro_esperado}%)')

    # Añadir diferencia
    diferencia_monto = ahorro_real - ahorro_esperado
    diferencia_porcentaje = porcentaje_ahorro_real - porcentaje_ahorro_esperado

    if abs(diferencia_monto) > 0:
        color_diferencia = '#27ae60' if diferencia_monto > 0 else '#e74c3c'
        simbolo_monto = '+' if diferencia_monto > 0 else ''
        simbolo_porcentaje = '+' if diferencia_porcentaje > 0 else ''

        ax.text(0.5, max_monto * 0.8,
               f'Diferencia: {simbolo_monto}${diferencia_monto:.2f}\n({simbolo_porcentaje}{diferencia_porcentaje:.1f}%)',
               ha='center', va='center', fontsize=10, fontweight='bold',
               bbox=dict(boxstyle="round,pad=0.3", facecolor=color_diferencia, alpha=0.3))

    ax.legend()
    plt.tight_layout()
    plt.show()