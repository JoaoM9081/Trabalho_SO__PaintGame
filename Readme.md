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

## Visão Geral do Código

O aplicativo de pintura foi desenvolvido em Python, uma linguagem de programação de alto nível conhecida por sua legibilidade e simplicidade. Utilizamos a biblioteca Tkinter para criar a interface gráfica do usuário (GUI), permitindo interações intuitivas com o aplicativo.

### Estrutura do Projeto

O projeto é estruturado da seguinte maneira:

- `main.py`: Contém a lógica principal do aplicativo, incluindo a inicialização da janela principal, configuração dos pincéis e gerenciamento de eventos.
- `icons/`: Um diretório que armazena ícones usados na interface do usuário, como ícones de pincel e botões de ação.

### Bibliotecas Utilizadas

- **Tkinter**: Uma biblioteca padrão do Python para desenvolvimento de interfaces gráficas. É usada para criar todos os elementos visuais do aplicativo, como botões, menus e a área de desenho.
- **colorchooser**: Um módulo do Tkinter que fornece uma caixa de diálogo para escolher cores.
- **PIL (Pillow)**: Especificamente, o módulo `ImageGrab` é usado para capturar a área de desenho e salvá-la como um arquivo de imagem.
- **threading**: Este módulo é utilizado para criar threads que permitem a execução concorrente de tarefas, como desenhar e salvar imagens simultaneamente.
- **time**: Utilizado para gerenciar pequenas pausas na execução das threads para simular trabalho intensivo e evitar condições de corrida.

### Concorrência

Para garantir que a interface do usuário permaneça responsiva e que as operações de desenho e salvamento sejam realizadas corretamente, utilizamos threads e semáforos:

- **Threads**: Permitem que múltiplas operações sejam executadas em paralelo. Por exemplo, enquanto uma imagem está sendo salva, o usuário ainda pode desenhar na tela.
- **Semaforos**: São mecanismos de sincronização que controlam o acesso a recursos compartilhados. No nosso caso, eles previnem que múltiplas threads executem operações conflitantes ao mesmo tempo.

## Como Usar

1. Clone este repositório para o seu computador local.
2. Navegue até o diretório onde o arquivo `main.py` está localizado.
3. Execute o arquivo `main.py` usando Python 3.

## Dependências

Este projeto depende da biblioteca Python PIL (Pillow), que pode ser instalada usando pip:

```bash
pip install pillow
