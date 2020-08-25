celular = 299.99
chaleira = 23.87
gnomo_de_jardim = 66.66
adesivos_unicornio = 1.42
frete = 12.34
iof = 0.0638
dolar_real_hoje = 5.59

total_dolar = celular + chaleira + gnomo_de_jardim + adesivos_unicornio * 6 + frete
conversao_real = total_dolar * dolar_real_hoje
iof_a_pagar = conversao_real * iof

print(
    f"Joseferson ira pagar US$ {total_dolar:.2f}, que convertendo para real, da R$ {conversao_real:.2f}")
print(f"Também precisara pagar R$ {iof_a_pagar:.2f} de IOF")
