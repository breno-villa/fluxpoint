# Requisitos

> **Status:** template. O levantamento ainda não foi feito; os itens abaixo são tópicos a preencher, não requisitos aprovados.

## 1. Objetivo e escopo

### Objetivo

TODO: descrever o problema que o teclado resolve e o público-alvo.

### Escopo inicial

TODO: o que entra nesta versão.

### Fora de escopo

TODO: o que fica para versões futuras.

## 2. Requisitos funcionais

### 2.1 Teclado

- [ ] Layout e número de teclas.
- [ ] Keymap, camadas e macros.
- [ ] Hotswap ou solda direta.
- [ ] RGB/iluminação (se houver).

### 2.2 Conectividade

- [ ] Modos entre metades: cabo, BLE ou ambos.
- [ ] Modos com o host: USB, BLE direto, dongle.
- [ ] Comportamento do dongle com uma ou duas metades.
- [ ] Troca de modo e indicação de status.
- [ ] Multi-host/pareamento (se houver).

### 2.3 Trackpoint

- [ ] Tipo de módulo e interface.
- [ ] Sensibilidade, aceleração e calibração.
- [ ] Botões e camada de scroll.

### 2.4 Display

- [ ] Tecnologia e tamanho.
- [ ] Conteúdo exibido.
- [ ] Quando liga/desliga e consumo.
- [ ] Interface de configuração.

### 2.5 Segurança / FIDO2

- [ ] Escopo: U2F, FIDO2/CTAP2, WebAuthn.
- [ ] Transportes: USB, dongle, BLE.
- [ ] Presença e verificação de usuário.
- [ ] Armazenamento de credenciais e PIN.
- [ ] Atestação e secure element.
- [ ] Modelo de ameaça e requisitos de certificação.

### 2.6 Leitor de digital

- [ ] Sensor e interface.
- [ ] Enrollment e templates.
- [ ] Anti-spoof e fallback.
- [ ] Privacidade dos dados biométricos.

### 2.7 Energia

- [ ] Bateria e autonomia alvo.
- [ ] Carregamento e proteção.
- [ ] Medição de carga.
- [ ] Deep sleep e wake.
- [ ] Comportamento com USB conectado.

### 2.8 Mecânica

- [ ] Dimensões e compatibilidade com Corne.
- [ ] Posição de trackpoint, display, digital e conectores.
- [ ] Case, montagem e acabamento.

## 3. Requisitos não funcionais

- [ ] Latência máxima aceitável (USB, BLE e dongle).
- [ ] Autonomia mínima.
- [ ] Confiabilidade e reconexão.
- [ ] Segurança e atualização de firmware.
- [ ] Custo-alvo.
- [ ] Peso e dimensões.
- [ ] Facilidade de montagem e manutenção.

## 4. Restrições

- Placa compatível com nice!nano v2 (clone) baseada em nRF52840.
- Layout baseado no Corne 3x6+3.
- Orçamento de GPIO e espaço mecânico limitados.
- Licenças e atribuições de projetos derivados.

## 5. Critérios de aceite

TODO: definir testes objetivos para cada modo e subsistema.

## 6. Perguntas abertas

- Qual o uso principal: desktop, notebook, smartphone ou todos?
- A chave de segurança precisa funcionar sem cabo?
- A digital é presença, verificação ou ambas?
- Quantas horas de bateria são aceitáveis?
- O dongle precisa ser USB-A, USB-C ou ambos?
- O projeto será aberto? Com qual licença?
