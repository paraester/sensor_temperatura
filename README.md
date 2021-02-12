
Projeto de Automatização de Controle de Temperatura Ambiente 

Descrição:
	Consiste em desenvolver um equipamento que irá gerenciar a temperatura ambiente na  de uma sala contendo equipamentos de ar condicionado. Este gerenciamento será realizado com a utilização de sensor de temperatura e umidade (DHT22), sensor que é capaz de fazer a leitura dos dados da temperatura e umidade ambiente, em conjunto com um Mini Computador Orange PI PC. Quando alguma alteração for percebida pelo usuário e ele achar que necessita alguma intervenção, via aplicativo Telegram o usuário poderá enviar uma mensagem que o Orange PI fazendo uso da Placa Arduino efetuará os comandos de aumento e diminuição de temperatura no Ar Condicionado, sendo possível consultar e alterar temperatura do ar condicionado utilizando-se de mensagens via chatbot Telegram;

Funcionamento:
	O Mini Computador Orange PC será a peça central do projeto sendo este responsável por ler a temperatura dos sensores DHT22 (será utilizado dois sensores para ter redundância), além de responder a solicitações via Telegram, essas solicitações poderão ser:
Parte 01 – Ler e mostrar:
temperatura;
umidade
IP;
	Part 02 - 
Cadastrar os botões do controle remoto;
Setar temperatura adequada; 
Setar temperatura de alerta (mínima e máxima);
	O Mini Computador Orange PC irá enviar as solicitações referentes ao controle remoto via interface serial para a Placa Arduino Uno, o Arduino será responsavel por gravar os códigos dos botões do controle e emitir o sinal para controlar o ar condicionado. Os códigos do controle ficarão armazenados no Orange PC e serão enviados ao arduino via interface serial;
        
        
        
        
        
Algumas configurações para o sistema:

Autenticação via proxy
    pip3 install urllib3

instalar telepot para utilização telegram
    baixar o pacote telepot-12.7.tar.gz

apt-get install build-essential python-dev git scons swig

orangepi_PC_gpio_pyH3  - problemas gpio
    na pasta orangepi_PC_gpio_pyH3
    python setup.py install

Criar na pasta onde o arquivo para o programa principal estiver o arquivo dht.py


Criar o bot

no @botfather
/newbot

nome do bot umidade_temperatura
username umbot_bot
Use this token to access the HTTP API:
c:tokentokentoken
        
# sensor_temperatura #orange_pi
