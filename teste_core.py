from core.financeiro import registrar_movimento, listar_movimentos

registrar_movimento(
    tipo="entrada",
    valor=3000,
    categoria="trabalho",
    origem_entrada="salario"
)

registrar_movimento(
    tipo="saida",
    valor=1200,
    categoria="moradia",
    tipo_gasto="fixo"
)

print("\nMOVIMENTOS REGISTRADOS:")
for m in listar_movimentos():
    print(m)