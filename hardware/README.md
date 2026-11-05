# Hardware

## Estrutura

- `pcb/` — projetos KiCad das placas (esquerda, direita e dongle).
- `case/` — modelo mecânico (CAD/STEP).
- `diagrams/` — diagramas de bloco, pinout e ligações.

## Base

- Placa compatível com nice!nano v2 (clone), nRF52840.
- Layout Corne 3x6+3, 42 teclas.

## Cuidados iniciais

- Confirmar o pinout e a capacidade de corrente do clone antes de projetar o PCB.
- Fechar o orçamento de GPIOs: matriz, trackpoint, display, digital, bateria e detecção de USB.
- Definir o conector entre as metades e a proteção contra hot-plug/backfeed.
- Definir a topologia de energia (uma bateria por metade, carregamento e VBUS).
- Se o PCB/case for derivado do Corne, preservar licença e atribuição.

## TODO

- [ ] Esquemático
- [ ] Pinout
- [ ] BOM
- [ ] PCB
- [ ] Case
- [ ] Testes de bring-up
