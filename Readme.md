# Paint Game - Trabalho de Sistemas Operacionais

Este aplicativo de pintura é um projeto desenvolvido para a disciplina de Sistemas Operacionais. Ele utiliza conceitos avançados de programação concorrente, como semáforos e threads, para gerenciar o acesso a recursos compartilhados e garantir a integridade do processo de desenho.

## Integrantes do Grupo

- João Marcos Azevedo Cruz
- Marcos André Barros Meneses
- Paulo Eduardo Teixeira Barbosa
- João Victor Albernaz

Preencha os nomes dos integrantes do grupo acima.

## Funcionalidades

- **Diferentes cores de pincel**: Escolha entre uma variedade de cores para desenhar.
- **Diferentes tamanhos de pincel**: Ajuste o tamanho do pincel para criar linhas finas ou grossas.
- **Opções de pincel**: Utilize ferramentas como linha, oval e borracha para desenhar.
- **Salvar o desenho**: Guarde sua obra de arte no seu dispositivo.
- **Limpar a tela**: Comece um novo desenho com uma tela limpa.

## Concorrência com Semaforos e Threads

O aplicativo implementa semáforos para controlar o acesso à área de desenho e à função de salvamento de imagens. Isso previne condições de corrida e garante que as operações não interfiram umas nas outras. As threads permitem que o desenho e o salvamento ocorram simultaneamente sem bloquear a interface do usuário.

- **Semaforos**: Utilizados para sincronizar o acesso a recursos compartilhados.
- **Threads**: Criam múltiplas linhas de execução para operações concorrentes.

## Como Usar

1. Clone este repositório para o seu computador local.
2. Navegue até o diretório onde o arquivo `main.py` está localizado.
3. Execute o arquivo `main.py` usando Python 3.

## Dependências

Este projeto depende da biblioteca Python PIL (Pillow), que pode ser instalada usando pip:

```bash
pip install pillow
