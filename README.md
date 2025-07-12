# LavaNotifica - Simulação Visual (Versão Tkinter)

Clique na imagem abaixo para assistir ao vídeo no YouTube:

<a href="https://youtu.be/95hWp7qxDCk" target="_blank">
  <img src="https://img.youtube.com/vi/95hWp7qxDCk/hqdefault.jpg" alt="Assista ao vídeo no YouTube" />
</a>

---

 **Simulação gráfica do sistema LavaNotifica**, um projeto de automação embarcada desenvolvido para notificar usuários, via Telegram, sobre o fim do ciclo de lavagem de máquinas coletivas. Esta versão reproduz visualmente o funcionamento do sistema utilizando Python, para fim didático de apresentação e validação de lógica.

---

## Sobre o Projeto Original

O **LavaNotifica** surgiu como uma solução para a **moradia estudantil Brejão (UFLA)**, onde o uso coletivo de lavanderias frequentemente gera esquecimentos, filas e conflitos. O sistema real consiste em sensores de vibração SW-420 acoplados às máquinas de lavar, conectados a um microcontrolador ESP8266, que envia **notificações automáticas via Telegram** ao detectar inatividade prolongada (fim do ciclo).

A simulação aqui representada permite **visualizar esse comportamento em tempo real**, simulando o sensor de vibração e o envio de mensagens no celular de forma gráfica.

---

## Objetivos da Simulação

- Reproduzir a lógica de funcionamento do sistema embarcado.
- Visualizar a detecção de atividade/inatividade da máquina de lavar.
- Simular o envio de notificação ao "celular" do usuário.
- Servir como ferramenta de apoio para **demonstrações didáticas e apresentações técnicas**.

---

## Interface

A interface gráfica inclui:

- **Máquina de Lavar** com estados visuais: `Funcionando` ou `Parada`;
- **Sensor SW-420** que alterna entre `ativo` (vibração detectada) e `inativo`;
- **Celular** com notificação visível ao fim de um ciclo;
- **Botão** para alternar a simulação da vibração;
- **Indicador de tempo de inatividade** da máquina.

---

## Como Executar

### Requisitos

- Python 3.6+
- Biblioteca Tkinter (já incluída na maioria das distribuições Python)

### Execução

Clone o repositório e execute o arquivo:

```bash
python3 run.py
```

## Estrutura do Código

**Componente	Descrição**

- **draw_machine()**:	Desenha a máquina de lavar e atualiza seu estado visual.
- **draw_sensor()**:	Representa o sensor SW-420 e indica se está ativo ou não.
- **draw_cellphone()**:	Simula um celular com área de notificação.
- **toggle_sensor()**:	Alterna entre vibração ativa/inativa, simulando início e fim do ciclo.
update_loop()	Lógica contínua que atualiza os estados da máquina e exibe notificações.

## Lógica de Funcionamento
1. Sensor ativo (vibração): máquina funcionando → tempo de inatividade zera.

2. Sensor inativo: tempo de inatividade é contado.

3. Se o tempo inativo ≥ 10 segundos → notificação é exibida.

4. A notificação fica visível por 5 segundos antes de desaparecer.

## Documentações

<a href="./Projeto_LavaNotifica.pdf" target="_blank">
  Clique para abrir o relatório técnico (PDF)
</a>
<br><br>
<a href="https://github.com/joseabrantesjr/LavaNotifica/blob/main/run.py" target="_blank">
  Clique para abrir o código-fonte da simulação (run.py) no GitHub
</a>

## Possibilidades Futuras
Adição de interface de autenticação;

Registro de histórico de lavagens;

Versão web para controle e visualização remota;

Integração com banco de dados de uso;

Simulação com múltiplas máquinas.
