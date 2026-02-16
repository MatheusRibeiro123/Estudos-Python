arquivo = open('arqText.txt','w')

arquivo.write('estudo python \n')
arquivo.write('aula pratica')
arquivo.close()

#Leitura do arquivo texto criado


leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()
