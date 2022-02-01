from unittest import TestCase
from dominio import Usuario,Lance,Leilao

class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario('gui')
        self.lance_do_gui = Lance(self.gui,150)
        self.leilao = Leilao('celular')
    
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        yuri = Usuario('yuri')
        lance_do_yuri = Lance(yuri, 100)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 100
        maior_valor_esperado = 150

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        
        with self.assertRaises(ValueError):
            yuri = Usuario('yuri')
            lance_do_yuri = Lance(yuri, 100)
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_yuri)    

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150, self.leilao.menor_lance)
        self.assertEqual(150, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        
        yuri = Usuario('yuri')
        lance_do_yuri = Lance(yuri, 100)
        vini = Usuario('vini')
        
        lance_do_vini = Lance(vini,200)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(lance_do_vini)

        maior_valor_esperado = 200
        menor_valor_esperado = 100

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    
    #se o leilao nao tiver lancer, deve permitir propor um lance
    def test_deve_permitir_propor_lance_caso_leilao_nao_tenha_lance(self):
        self.leilao.propoe(self.lance_do_gui)
        quantidade_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(1, quantidade_lances_recebidos)

    # se o ultimo usuario for diferente, deve permitir propor o lance
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('yuri')
        lance_do_yuri = Lance(yuri, 200)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        quantidade_lances_recebidos = len(self.leilao.lances)
        self.assertEqual (2, quantidade_lances_recebidos)


    #se o ultimo usuatio fod o mesmo, nao deve permitir propor lance
    def test_nao_deve_permitir_propor_lance_caso_usuario_seja_mesmo(self):
        lance_do_gui200 = Lance(self.gui, 200)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)

