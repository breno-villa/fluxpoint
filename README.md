# Corne Hybrid (nome provisório)

Teclado split 3x6+3 baseado no Corne, com múltiplos modos de conexão e periféricos integrados.

> **Status:** esqueleto inicial. Requisitos, arquitetura e decisões de hardware/firmware ainda estão em definição. Nada aqui deve ser tratado como especificação fechada.

## Ideias iniciais

- Layout Corne 3x6+3 (42 teclas), uma placa por metade.
- Comunicação entre as metades por cabo ou sem fio.
- Conexão com o host por USB, BLE direto ou dongle.
- Dongle capaz de receber de uma ou das duas metades.
- Trackpoint estilo ThinkPad.
- Chave de segurança FIDO2/CTAP2 implementada no firmware.
- Leitor de digital como presença/verificação de usuário da chave.
- Display de baixo consumo, ligado apenas quando necessário (bateria, conexão, status).
- Bateria recarregável em cada metade.

## Hardware base

- Placa compatível com **nice!nano v2** (clone), baseada no **nRF52840**.
- O pinout e as características elétricas do clone precisam ser confirmados antes do PCB.

## Estrutura do repositório

```text
.
├── docs/          # requisitos, arquitetura e decisões
├── hardware/      # PCB, case e diagramas
├── firmware/      # configuração ZMK, módulos e dongle
└── tools/         # scripts auxiliares
```

## Documentos

- [`docs/architecture.md`](docs/architecture.md) — rascunho da arquitetura e dos modos de conexão.
- [`docs/requirements.md`](docs/requirements.md) — template para o levantamento de requisitos.

## Próximos passos

1. Levantar requisitos e critérios de aceite.
2. Fechar o orçamento de pinos e a topologia de energia.
3. Validar o suporte de firmware para split com cabo, dongle e múltiplos transportes.
4. Fazer provas de conceito de trackpoint, display, digital e FIDO2.
5. Definir PCB, case e BOM.

## Licença

A definir. O projeto é inspirado no [Corne (crkbd)](https://github.com/foostan/crkbd); se forem usados PCB, case ou outros arquivos derivados, a licença e a atribuição originais serão preservadas.
