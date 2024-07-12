#ListExerc70

def leiaInt(msg): #Função para tratar a entrada diferente de inteiro.
    ok = False
    valor = 0
    while True:
        valor_de_N = str(input(msg))
        if valor_de_N.isnumeric():
            valor =int(valor_de_N)
            ok = True
        else:
            print("ERRO! Digite um número inteiro válido!")
        if ok:
            break
    return valor

#tela de menu
print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- 
|             cardápio da lanchonete            |
|------------------------------------------------
|      i.   Especificação    Código      Preço  | 
|     ii.   Cachorro Quente   100      R$ 1,20  |
|    iii.   Bauru Simples     101      R$ 1,30  |
|     iv.   Bauru com ovo     102      R$ 1,50  |
|      v.   Hambúrguer        103      R$ 1,20  |
|     vi.   Cheeseburguer     104      R$ 1,30  |
|    vii.   Refrigerante      105      R$ 1,00  |
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

#bloco de variáveis 
valor_item_100 = 0
valor_item_101 = 0
valor_item_102 = 0
valor_item_103 = 0
valor_item_104 = 0
valor_item_105 = 0
qde_item_100 = 0
qde_item_101 = 0
qde_item_102 = 0
qde_item_103 = 0
qde_item_104 = 0
qde_item_105 = 0
valor_total = 0
quantidade =0
codigo = 0

while True:
    fazer_pedido = str(input('Continuar o pedido? S/N: ').upper())
    if fazer_pedido != "S":
        break
    else:
        codigo = leiaInt("Informe o código do item: ")
        while (100 != codigo!= 101 and 102 != codigo != 103 and 104 != codigo != 105):
            print("erro")
            codigo = leiaInt("Informe o código do item: ")
        else:
            quantidade = leiaInt("Informe a quantidade: ")
            
        if codigo == 100:
            preco = 1.2
            qde_item_100 = quantidade
            valor_item_100 += qde_item_100*preco
        elif codigo == 101:
            preco = 1.3
            qde_item_101 = quantidade
            valor_item_101 += qde_item_101*preco
        elif codigo == 102:
            preco = 1.5
            qde_item_102 = quantidade
            valor_item_102 += qde_item_102*preco        
        elif codigo == 103:
            preco = 1.2
            qde_item_103 = quantidade
            valor_item_103 += qde_item_103*preco
        elif codigo == 104:
            preco = 1.3
            qde_item_104 = quantidade
            valor_item_104 += qde_item_104*preco
        elif codigo == 105:
            preco = 1.0
            qde_item_105 = quantidade
            valor_item_105 += qde_item_105*preco            

valor_total = valor_item_100+valor_item_101+valor_item_102+valor_item_103+valor_item_104+valor_item_105
print("Pedido finalizado! Abaixo descrição do seu pedido:")
print(f'''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
                   Cupom fiscal                 |         Total por item            
 ---------------------------------------------------------------------------------
       i.   Especificação    Código      Preço  |  QDe Pedida  |     Valor R$    
      ii.   Cachorro Quente   100      R$ 1,20  |      {qde_item_100}              {valor_item_100}
     iii.   Bauru Simples     101      R$ 1,30  |      {qde_item_101}              {valor_item_101}
      iv.   Bauru com ovo     102      R$ 1,50  |      {qde_item_102}              {valor_item_102}
       v.   Hambúrguer        103      R$ 1,20  |      {qde_item_103}              {valor_item_103}
      vi.   Cheeseburguer     104      R$ 1,30  |      {qde_item_104}              {valor_item_104}
     vii.   Refrigerante      105      R$ 1,00  |      {qde_item_105}              {valor_item_105}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|---------------------------------
                                                |        Total a pagar:R$ {valor_total}
                                                -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
''')