from dominio import Usuario,Lance,Leilao,Avaliador

gui = Usuario('gui')
yuri = Usuario('yuri')

lance_do_yuri = Lance(yuri, 100)
lance_do_gui = Lance(gui,150)

leilao = Leilao('celular')


leilao.lances.append(lance_do_yuri)
leilao.lances.append(lance_do_gui)

for lance in leilao.lances:
    print('o usuário {} deu um lance de {}'.format(lance.usuario.nome, lance.valor))

avaliador = Avaliador()
avaliador.avalia(leilao)

print("O menor lance foi de {} e o maior lance foi de {}".format(avaliador.menor_lance, avaliador.maior_lance))