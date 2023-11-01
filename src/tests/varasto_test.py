import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_pos_tilavuus(self):
        varasto = Varasto(10)  
        self.assertEqual(varasto.tilavuus, 10)

    def test_konstruktori_neg_tilavuus(self):
        varasto = Varasto(-2)
        self.assertEqual(varasto.tilavuus, 0.0)

    def test_konstruktori_neg_alku_saldo(self):
        varasto = Varasto(10, -5)  
        self.assertEqual(varasto.saldo, 0.0)

    def test_konstruktori_alku_saldo_grt_tilavuus(self):
        varasto = Varasto(10, 15)  
        self.assertEqual(varasto.saldo, 10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
        
    def test_lisays_lisaa_ei_onnistu_jos_isompi_kuin_varasto(self):
        self.varasto.lisaa_varastoon(12)
        
        # varastossa on tilaa 10 ja koska 12 ei mahdu siihen, niin saldo jää 10:ksi
        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
    
    def test_yliottaminen(self):
        self.varasto.lisaa_varastoon(10)

        # varastossa on tilaa ja lisätään 10 ja yritetään ottaa 12. Sitten saa 10 vaan
        self.assertAlmostEqual(self.varasto.ota_varastosta(12), 10)
    
    def test_neg_lisays(self):
        self.assertAlmostEqual(self.varasto.lisaa_varastoon(-2), None)

    def test_neg_ottaminen(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-2), 0.0)

    def test_str_saldo_tilaa(self):
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(self.varasto.__str__(), "saldo = 5, vielä tilaa 5")
