
Projeto de Automatização de Controle de Temperatura Ambiente

Descrição:
	Consiste em desenvolver um equipamento que ira gerenciar a temperatura ambiente, este gerenciamento sera realizado atraves de utilização de sensor de temperatura e umidade (DHT22) que faz a leitura dos dados em conjunto com uma Mini Computador Orange PI PC e dependendo da temperatura o Orange PI atraves da Placa Arduino efetua comandos de aumento e diminuição de temperatura no Ar Condicionado, sendo possível consultar e alterar temperatura do ar atraves de comando via chatbot telegram;

Funcionamento:
	O Mini Computador Orange PC sera a peça central do projeto sendo este responsavel por ler a temperatura dos sensores DHT22 (sera utilizado dois sensores para ter redundancia), alem de responder a solicitações via Telegram, essas solicitações poderão ser:
Verificar a temperatura;
Verificar o IP;
Cadastrar botao do controle remoto;
Setar temperatura adequada; 
Setar temperatura de alerta (minima e maxima);
	O Mini Computador Orange PC ira enviar as solicitações referentes ao controle remoto via interface serial para a Placa Arduino Uno, o Arduino sera responsavel por gravar os codigos dos botões do controle e emitir o sinal para controlar o ar condicionado. Os codigos do controle ficarão armazenados no Orange PC e serão enviados ao arduino via interface serial;
# sensor_temperatura
