cd_dvd = []
other = []
school_supplies = []
adapter_cable = []
bijou = []
electronic = []
cover = []
dvd_tv_control = []
toy = []
fashion_accessories = []
femalle_accessories = []
hookah = []
dvd_control = []
tv_control = []
converter_control = []
DVD = []
CD = []
ps2 = []
xbox360 = []
film = []
separator = '\n'
while True:
    print('''
\033[7:31:33m OPÇÕES: \033[0:m

\033[0:32m[ 1 ] película de vidro
[ 2 ] capinha\033[0:m
\033[0:34m[ 3 ] cabo e adaptador
[ 4 ] eletrônicos\033[0:m
\033[0:36m[ 5 ] bijuteria
[ 6 ] acessórios para o corpo
[ 7 ] acessorio feminino\033[0:m
\033[0:31m[ 8 ] material escolar\033[0:m
\033[0:35m[ 9 ] narguile\033[0:m
\033[0:33m[ 10 ] controle de TV, DVD e conversor\033[0:m
\033[0:31m[ 11 ] brinquedo\033[0:m
\033[0:35m[ 12 ] CD e DVD
\033[0:35m[ 13 ] jogo de PS2 e Xbox 360\033[0:m
\033[0:33m[ 14 ] outro \033[0:m
\033[0:37m[ sair ] sair do programa
\033[0:m''')
    print('')
    op = str(input('\033[7:30:32m escolher opção principal:\033[0:m ').lower().strip())
    print('')
    if op == '1':
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')
        while True:
            a = str(input('\033[0:32mpelicula\033[:m confirme sua escolha: ').strip())
            if a == '':
                def eliminator_film(film):
                    l_film = []
                    for i in film:
                        if i not in l_film:
                            l_film.append(i)
                    l_film.sort()
                    return l_film
                print('')
                film.append(input('\033[0:32manotar pelicula: \033[:m').strip().lower().title())
                film = eliminator_film(film)
                break
            elif a == '0':
                break
            else:
                print('\033[7:30:31m digite apenas [ ENTER ] ou [ 0 ] \033[:m')
            pass
    elif op == '2':
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')
        while True:
            a = str(input('\033[:32mcapinha\033[:m confirme sua escolha: ').strip())
            if a == '':
                def eliminator_cover(cover):
                    l_cover = []
                    for i in cover:
                        if i not in l_cover:
                            l_cover.append(i)
                    l_cover.sort()
                    return l_cover
                print('')
                cover.append(input('\033[0:32manotar capinha: \033[:m').strip().lower().title())
                cover = eliminator_cover(cover)
                break
            elif a == '0':
                break
            else:
                print('\033[7:30:31m digite apenas [ ENTER ] ou [ 0 ] \033[:m')
            pass
    elif op == '3':
        print('''
[ ENTER ] para prosseguir                               
[ 0 ] para voltar
''')
        while True:
            a = str(input('\033[:34mcabo ou adaptador\033[:m confirme sua escolha: ').strip())
            if a == '':
                def eliminator_adapter_cable(adapter_cable):
                    l_adapter_cable = []
                    for i in adapter_cable:
                        if i not in l_adapter_cable:
                            l_adapter_cable.append(i)
                    l_adapter_cable.sort()
                    return l_adapter_cable
                print('')
                adapter_cable.append(input('\033[0:34manotar cabo ou adaptador: \033[:m').strip().lower())
                adapter_cable = eliminator_adapter_cable(adapter_cable)
                break
            elif a == '0':
                break
            else:
                print('\033[7:30:31m digite apenas [ ENTER ] ou [ 0 ] \033[:m')
            pass
    elif op == '4':
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')
        while True:
            a = str(input('\033[:34meletrônico\033[:m confirme sua escolha: ').strip())
            if a == '':
                def eliminator_eletronic(eletronic):
                    l_eletronic = []
                    for i in eletronic:
                        if i not in l_eletronic:
                            l_eletronic.append(i)
                    l_eletronic.sort()
                    return l_eletronic
                print('')
                electronic.append((input('\033[0:34manotar eletronico: \033[:m').strip().lower()))
                electronic = eliminator_eletronic(electronic)
                break
            elif a == '0':
                break
            else:
                print('\033[7:30:31m digite apenas [ ENTER ] ou [ 0 ] \033[:m')
            pass
    elif op == '5':
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')
        while True:
            a = str(input('\033[:36mbijuteria\033[:m confirme sua escolha: ').strip())
            if a == '':
                def eliminator_bijou(bijou):
                    l_bijou = []
                    for i in bijou:
                        if i not in l_bijou:
                            l_bijou.append(i)
                    l_bijou.sort()
                    return l_bijou
                print('')
                bijou.append(input('\033[0:36manotar bijuteria: \033[:m').strip().lower())
                bijou = eliminator_bijou(bijou)
                break
            elif a == '0':
                break
            else:
                print('\033[7:30:31m digite apenas [ ENTER ] ou [ 0 ] \033[:m')
            pass
    elif op == '6':
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')
        while True:
            a = str(input('\033[:36macessório para o corpo\033[:m confirme sua escolha: ').strip())
            if a == '':
                def eliminator_fashion_accessories(fashion_accessories):
                    l_fashion_accessories = []
                    for i in fashion_accessories:
                        if i not in l_fashion_accessories:
                            l_fashion_accessories.append(i)
                    l_fashion_accessories.sort()
                    return l_fashion_accessories
                print('')
                fashion_accessories.append(input('\033[0:36manotar acessório para o corpo: \033[:m').strip().lower())
                fashion_accessories = eliminator_fashion_accessories(fashion_accessories)
                break
            elif a == '0':
                break
            else:
                print('\033[7:30:31m digite apenas [ ENTER ] ou [ 0 ] \033[:m')
            pass
    elif op == '7':
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')
        while True:
            a = str(input('\033[:36macessório fêminino\033[:m confirme sua escolha: ').strip())
            if a == '':
                def eliminator_femalle_accessories(femalle_accessories):
                    l_femalle_accessories = []
                    for i in femalle_accessories:
                        if i not in l_femalle_accessories:
                            l_femalle_accessories.append(i)
                    l_femalle_accessories.sort()
                    return l_femalle_accessories
                print('')
                femalle_accessories.append(input('\033[0:36manotar acessório fêminino: \033[:m').strip().lower())
                femalle_accessories = eliminator_femalle_accessories(femalle_accessories)
                break
            elif a == '0':
                break
            else:
                print('\033[7:30:31m digite apenas [ ENTER ] ou [ 0 ] \033[:m')
            pass
    elif op == '8':
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')
        while True:
            a = str(input('\033[:31mmaterial escolar\033[:m confirme sua escolha: ').strip())
            if a == '':
                def eliminator_school_supplies(school_supplies):
                    l_school_supplies = []
                    for i in school_supplies:
                        if i not in l_school_supplies:
                            l_school_supplies.append(i)
                    l_school_supplies.sort()
                    return l_school_supplies
                print('')
                school_supplies.append(input('\033[0:31manotar material escolar: \033[:m').strip().lower())
                school_supplies = eliminator_school_supplies(school_supplies)
                break
            elif a == '0':
                break
            else:
                print('\033[7:30:31m digite apenas [ ENTER ] ou [ 0 ] \033[:m')
            pass
    elif op == '9':
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')
        while True:
            a = str(input('\033[:35mnarguile\033[:m confirme sua escolha: ').strip())
            if a == '':
                def eliminator_hookah(hookah):
                    l_hookah = []
                    for i in hookah:
                        if i not in l_hookah:
                            l_hookah.append(i)
                    l_hookah.sort()
                    return l_hookah
                print('')
                hookah.append(input('\033[0:35manotar narguile: \033[:m').strip().lower())
                hookah = eliminator_hookah(hookah)
                break
            elif a == '0':
                break
            else:
                print('\033[7:30:31m digite apenas [ ENTER ] ou [ 0 ] \033[:m')
            pass
    elif op == '10':
        while True:
            print('''
\033[0:33mOpções:\033[0:m

[ 1 ] TV
[ 2 ] DVD
[ 3 ] conversor
[ 0 ] para voltar às opções principais
''')
            p = str(input('\033[:33mcontrole de TV, DVD ou conversor\033[:m escolher opção: ').strip())
            if p == '1':
                def eliminator_tv_control(tv_control):
                    l_tv_control = []
                    for i in tv_control:
                        if i not in l_tv_control:
                            l_tv_control.append(i)
                        l_tv_control.sort()
                        return l_tv_control
                print('')
                tv_control.append(input('\033[0:33manotar controle de TV: \033[:m').strip().lower())
                tv_control = eliminator_tv_control(tv_control)
                break
            elif p == '2':
                def eliminator_dvd_control(dvd_control):
                    l_dvd_control = []
                    for i in dvd_control:
                        if i not in l_dvd_control:
                            l_dvd_control.append(i)
                    l_dvd_control.sort()
                    return l_dvd_control
                print('')
                dvd_control.append(input('\033[0:33manotar controle de DVD: \033[:m').strip().lower())
                dvd_control = eliminator_dvd_control(dvd_control)
                break
            elif p == '3':
                def eliminator_converter_control(converter_control):
                    l_converter_control = []
                    for i in converter_control:
                        if i not in l_converter_control:
                            l_converter_control.append(i)
                    l_converter_control.sort()
                    return l_converter_control
                print('')
                converter_control.append(input('\033[0:33manotar controle de conversor: \033[:m').strip().lower())
                converter_control = eliminator_converter_control(converter_control)
                break
            elif p == '0':
                break
            else:
                print('\033[7:30:31m DIGITE APENAS AS OPÇÕES ABAIXO. \033[0:m')
            pass
    elif op == '11':
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')
        while True:
            a = str(input('\033[:31mbrinquedo\033[:m confirme sua escolha: ').strip())
            if a == '':
                def eliminator_toy(toy):
                    l_toy = []
                    for i in toy:
                        if i not in l_toy:
                            l_toy.append(i)
                    l_toy.sort()
                    return l_toy
                print('')
                toy.append(input('\033[0:31manotar brinquedo: \033[:m').strip().lower())
                toy = eliminator_toy(toy)
                break
            elif a == '0':
                break
            else:
                print('\033[7:30:31m digite apenas [ ENTER ] ou [ 0 ] \033[:m')
            pass
    elif op == '12':
        while True:
            print('''\033[0:33mOpções:\033[0:m

[ 1 ] CD
[ 2 ] DVD
[ 0 ] para voltar às opções principais
''')
            p1 = str(input('\033[:32mCD ou DVD\033[:m escolher opção: ').strip())
            if p1 == '1':
                def eliminator_CD(CD):
                    l_CD = []
                    for i in CD:
                        if i not in l_CD:
                            l_CD.append(i)
                    l_CD.sort()
                    return l_CD
                print('')
                CD.append(input('\033[0:35manotar CD: \033[0:m').strip().lower())
                CD = eliminator_CD(CD)
                break
            elif p1 == '2':
                def eliminator_DVD(DVD):
                    l_DVD = []
                    for i in DVD:
                        if i not in l_DVD:
                            l_DVD.append(i)
                    l_DVD.sort()
                    return l_DVD
                print('')
                DVD.append(input('\033[0:35manotar DVD: \033[0:m').strip().lower())
                DVD = eliminator_DVD(DVD)
                break
            elif p1 == '0':
                break
            else:
                print('\033[7:30:31m DIGITE APENAS AS OPÇÕES ABAIXO. \033[0:m')
            pass
    elif op == '13':
        while True:
            print('''\033[0:33mOpçoes:\033[0:m

[ 1 ] PS2
[ 2 ] XBOX 360
[ 0 ] para voltar às opções principais
''')
            p2 = str(input('\033[0:35mjogo de PS2 ou XBOX 360\033[:m escolher opção: ').strip())
            if p2 == '1':
                def eliminator_ps2(ps2):
                    l_ps2 = []
                    for i in ps2:
                        if i not in l_ps2:
                            l_ps2.append(i)
                    l_ps2.sort()
                    return l_ps2
                print('')
                ps2.append(input('\033[0:35manotar jogo de PS2: \033[0:m').strip().lower())
                ps2 = eliminator_ps2(ps2)
                break
            elif p2 == '2':
                def eliminator_xbox360(xbox360):
                    l_xbox360 = []
                    for i in xbox360:
                        if i not in l_xbox360:
                            l_xbox360.append(i)
                    l_xbox360.sort()
                    return l_xbox360
                xbox360.append(input('\033[0:35manotar jogo de XBOX 360: \033[0:m').strip().lower())
                xbox360 = eliminator_xbox360(xbox360)
                break
            elif p2 == '0':
                break
            else:
                print('\033[7:30:31m DIGITE APENAS AS OPÇÕES ABAIXO. \033[0:m')
            pass
    elif op == '14':
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')
        while True:
            a = str(input('\033[:33mobjeto não listado\033[:m confirme sua escolha: ').strip())
            print('')
            if a == '':
                def eliminator_other(other):
                    l_other = []
                    for i in other:
                        if i not in l_other:
                            l_other.append(i)
                    l_other.sort()
                    return l_other
                other.append(input('\033[0:33manotar outro objeto não listado: \033[0:m').strip().lower())
                other = eliminator_other(other)
                break
            elif a == '0':
                break
            else:
                print('\033[7:30:31m digite apenas [ ENTER ] ou [ 0 ] \033[:m')
            pass
    elif op == 'sair':
        print('')
        if len(film) > 0:
            print('\033[7:30:32m PELÍCULAS \033[0:m \033[0:32m')
            film.sort()
            print(separator.join(film))
            print('\033[0:m')
        if len(cover) > 0:
            print('\033[7:30:32m CAPAS \033[0:m \033[0:32m')
            cover.sort()
            print(separator.join(cover))
            print('\033[0:m')
        if len(adapter_cable) > 0:
            print('\033[7:30:34m CABOS E ADAPTADORES \033[0:m \033[0:34m')
            adapter_cable.sort()
            print(separator.join(adapter_cable))
            print('\033[0:m')
        if len(electronic) > 0:
            print('\033[7:30:34m ELETRÔNICOS \033[0:m \033[0:34m')
            electronic.sort()
            print(separator.join(electronic))
            print('\033[0:m')
        if len(bijou) > 0:
            print('\033[7:30:36m BIJUTERIAS \033[0:m \033[0:36m')
            bijou.sort()
            print(separator.join(bijou))
            print('\033[0:m')
        if len(fashion_accessories) > 0:
            print('\033[7:30:36m ACESSÓRIOS PARA O CORPO \033[0:m \033[0:36m')
            fashion_accessories.sort()
            print(separator.join(fashion_accessories))
            print('\033[0:m')
        if len(femalle_accessories) > 0:
            print('\033[7:30:36m ACESSÓRIOS FEMENINOS \033[0:m \033[0:36m')
            femalle_accessories.sort()
            print(separator.join(femalle_accessories))
            print('\033[0:m')
        if len(school_supplies) > 0:
            print('\033[7:30:31m MATERIAL ESCOLAR \033[0:m \033[0:31m')
            school_supplies.sort()
            print(separator.join(school_supplies))
            print('\033[0:m')
        if len(hookah) > 0:
            print('\033[7:30:35m NARGUILE \033[0:m \033[0:35m')
            hookah.sort()
            print(separator.join(hookah))
            print('\033[0:m')
        if len(tv_control) > 0:
            print('\033[7:30:33m CONTROLES DE TV \033[0:m \033[0:33m')
            tv_control.sort()
            print(separator.join(tv_control))
            print('\033[0:m')
        if len(dvd_control) > 0:
            print('\033[7:30:33m CONTROLES DE DVD \033[0:m \033[0:33m')
            dvd_control.sort()
            print(separator.join(dvd_control))
            print('\033[0:m')
        if len(converter_control) > 0:
            print('\033[7:30:33m CONTROLES DE CONVERSOR \033[0:m \033[0:33m')
            converter_control.sort()
            print(separator.join(converter_control))
            print('\033[0:m')
        if len(toy) > 0:
            print('\033[7:30:31m BRINQUEDOS \033[0:m \033[0:31m')
            toy.sort()
            print(separator.join(toy))
            print('\033[0:m')
        if len(DVD) > 0:
            print('\033[7:30:35m DVD \033[0:m \033[0:35m')
            DVD.sort()
            print(separator.join(DVD))
            print('\033[0:m')
        if len(CD) > 0:
            print('\033[7:30:35m CD \033[0:m \033[0:35m')
            CD.sort()
            print(separator.join(CD))
            print('\033[0:m')
        if len(ps2) > 0:
            print('\033[7:30:35m JOGOS DE PS2 \033[0:m \033[0:35m')
            ps2.sort()
            print(separator.join(ps2))
            print('\033[0:m')
        if len(xbox360) > 0:
            print('\033[7:30:35m JOGOS DE XBOX 360 \033[0:m \033[0:35m')
            xbox360.sort()
            print(separator.join(xbox360))
            print('\033[0:m')
        if len(other) > 0:
            print('\033[7:30:33m OUTRAS COISAS \033[0:m \033[0:33m')
            other.sort()
            print(separator.join(other))
            print('\033[0:m')
        break
    else:
        print('')
        print('\033[7:30:31m DIGITE APENAS AS OPÇÕES A QUE ESTÃO ABAIXO. \033[0:m')
pass
