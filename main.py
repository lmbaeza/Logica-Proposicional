from src.SyntacticAnalyzer.Parser import Parser

parser = Parser()


isExit = False

while not isExit:
    print('[...] Ingrese un numero del [1, 3] para elegir un caso de prueba')
    print('[...] o "exit" si desea salir')
    print('number>', end='')
    command = input()

    if command != 'exit':
        number = int(command)
        if number>=1 and number <= 3:
            with open('./example/input-{}.txt'.format(number), 'r') as file:
                code = file.read()
                print('\nCASO DE PRUEBA #'+str(number))
                print('FILE: /example/input-{}.txt\n'.format(number))
                print('------OUTPUT------')
                parser.run(code)
        else:
            print('Numero fuera del rango [1, 3]')
    else:
        break
    print('\n'*3)
