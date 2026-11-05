# Firmware

Base proposta: **ZMK/Zephyr**, a confirmar durante o levantamento de requisitos.

## Estrutura

- `zmk-config/` — configuração do teclado (keymap, `build.yaml`, `west.yml`).
- `modules/` — módulos Zephyr customizados (trackpoint, display, digital, FIDO2).
- `dongle/` — firmware do receptor.

## Pontos a validar

- Suporte atual do ZMK a split com cabo, dongle e múltiplos transportes.
- Coexistência de HID de teclado/mouse com FIDO2 no mesmo MCU.
- Fingerprint como *user presence* e/ou *user verification*.
- Orçamento de GPIO e gerenciamento de energia.
- Estratégia de build, flash e atualização.
- Necessidade de secure element ou MCU dedicado para a chave de segurança.

## TODO

- [ ] Definir a base de firmware.
- [ ] Criar o `west.yml` e o `build.yaml`.
- [ ] Implementar o keymap inicial.
- [ ] Provar o dongle.
- [ ] Provar os drivers dos periféricos.
