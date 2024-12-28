peca1_data = input().split()
peca1 = int(peca1_data[0])
qtd_pcs_1 = int(peca1_data[1])
valor_unit_pc1 = float(peca1_data[2])


peca2_data = input().split()
peca2 = int(peca2_data[0])
qtd_pcs_2 = int(peca2_data[1])
valor_unit_pc2 = float(peca2_data[2])


total = (qtd_pcs_1 * valor_unit_pc1) + (qtd_pcs_2 * valor_unit_pc2)


print(f"VALOR A PAGAR: R$ {total:.2f}")
