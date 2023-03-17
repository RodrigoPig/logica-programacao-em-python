# DESAFIO: foi discutido em aula como converter de uma string, ou seja, o tipo str, para um float. 
# Como fazer o caminho inverso, converter de um float para str? 
# Reflita um pouco e tente não só apresentar o valor numérico como escrever algum texto que auxilie a leitura do usuário.
# Após este cálculo, imprima uma linha contendo o IMC da pessoa.
# altura_ao_quadrado = altura_float * altura_float 
# imc = peso_float / altura_ao_quadrado

altura_float = float(input('Informe a sua altura ex(1.80): '))
peso_float = float(input('Informe o seu peso ex(115): '))


imc = peso_float/(altura_float*altura_float)

print(f'Seu IMC é de: {imc:.2f} kg/m2')