# Explicações sobre Separadores e Terminadores:


### Explicando o comando SEP:

O comando __*sep=""*__ é utilizado como forma de separador. Sempre que uma virgula é adicionada ao programa. Um bom exemplo é o uso de CPF, print(555, 435, 518, 90). Concatenado com o comando de separação, nossa intenção é a adição de um ponto como separador entre os números. 

O comando então deverá ficar assim: __print(555, 435, 518, 90, sep=".")__
O resultado: 565.435.518.90. 

### Explicando o comando END:

Usaremos como dado explicativo a versão anterior do nosso print, que exibia o CPF de uma pessoa. O formato padrão e correto de um CPF é com um traço ao final, exibindo os últimos dois digitos. O comando END adiciona um comando ao final da exibição de um print. Para o CPF permanecer no padrão correto, seria necessário que estivesse assim;

__print(555, 435, 518, sep=".", end="-")__
__print(90)
