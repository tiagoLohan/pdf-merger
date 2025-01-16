# 📄 Projeto: Juntador de PDFs com Python

Este projeto é um script simples para juntar múltiplos arquivos PDF em um único documento. Ele utiliza a biblioteca **PyPDF2** e a interface do **Tkinter** para facilitar a seleção da pasta de arquivos. Além disso, inclui um executável para facilitar o uso, mesmo para quem não tem Python instalado.

---

## 🚀 Funcionalidades

- 📂 Seleção de uma pasta com arquivos PDF.
- 🔄 Ordenação automática dos PDFs da pasta selecionada.
- 📑 Junção dos arquivos em um único PDF, nomeado com base na pasta escolhida.
- 🖥️ **Geração de um executável** para facilitar a utilização.
- ✅ Mensagem de sucesso no terminal ao finalizar o processo.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 🐍
- **Bibliotecas:**
  - [PyPDF2](https://pypi.org/project/PyPDF2/) - Manipulação de PDFs.
  - [Tkinter](https://docs.python.org/3/library/tkinter.html) - Interface para seleção de pasta.
  - [OS](https://docs.python.org/3/library/os.html) - Manipulação de arquivos e diretórios.
- **Ferramenta para Executável:** [PyInstaller](https://pyinstaller.org/).

---

## 📂 Estrutura do Projeto

1. **Seleção de Pasta:** Uma janela é aberta para escolher a pasta onde os arquivos PDF estão localizados.
2. **Ordenação e Validação:** Filtragem e ordenação de arquivos para garantir a junção correta.
3. **Geração do PDF Final:** Criação de um único arquivo PDF nomeado com base no nome da pasta selecionada.
4. **Executável:** Um arquivo `.exe` criado para facilitar o uso do projeto, dispensando a necessidade de instalar Python e bibliotecas.

---

## 📅 Próximos Passos

- Melhorar a interface gráfica com uma janela mais amigável.
- Adicionar suporte a diferentes formatos de arquivos além de PDFs.
- Implementar a possibilidade de personalizar o nome do arquivo final.
