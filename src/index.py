from varasto import Varasto

def print_varasto_details(varasto, label):
    print(f"{label}: {varasto}")

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    #print("Luonnin jälkeen:")
    #print_varasto_details(mehua, "Mehuvarasto")
    #print_varasto_details(olutta, "Olutvarasto")

    #print("Olut getterit:")
    #print(f"saldo = {olutta.saldo}")
    #print(f"tilavuus = {olutta.tilavuus}")
    #print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    #print("Mehu setterit:")
    #print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    #print_varasto_details(mehua, "Mehuvarasto")
    #print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    #print_varasto_details(mehua, "Mehuvarasto")

    #print("Virhetilanteita:")
    #print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    #print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

    #print_varasto_details(olutta, "Olutvarasto")
    #print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    #print_varasto_details(olutta, "Olutvarasto")

    #print_varasto_details(mehua, "Mehuvarasto")
    #print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    #print_varasto_details(mehua, "Mehuvarasto")

    #print_varasto_details(olutta, "Olutvarasto")
    #print("olutta.ota_varastosta(1000.0)")

    olutta.ota_varastosta(1000.0)
    #saatiin = olutta.ota_varastosta(1000.0)
    #print(f"saatiin {saatiin}")

    print_varasto_details(olutta, "Olutvarasto")

    #print_varasto_details(mehua, "Mehuvarasto")
    #print("mehua.otaVarastosta(-32.9)")

    mehua.ota_varastosta(-32.9)
    #saatiin = mehua.ota_varastosta(-32.9)
    #print(f"saatiin {saatiin}")

    print_varasto_details(mehua, "Mehuvarasto")

if __name__ == "__main__":
    main()
