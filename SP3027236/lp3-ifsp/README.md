LP3 IFSP

repositorio para organizar os codigos da disciplina linguagem programaçao 3.

ao chegar no laboratorio

configurar o usuario local do git

 bash
 git config --global user.name"nome"
 git config --global user.email "seuemail@email.com"
 2- fazer o clone do seu repositorio no git hub
 bash 
 git clone https://github.com/Seu_usuario/lp3-ifsp.git

 bash
 git clone
 3- abrir o repo no vscode
 code lp3-ifsp

 4- criar umtoken para realizar os pushs
 settings -> developer settings -> personal acess tokens -> tokens (classic)

  Generate new toke, selecionar a opção generate new token classic, marcar a opção scope repo

  ### antes de sair do laboratorio 
 ¨¨¨bash 
  git config --global --unset user.name
  git config --global --unset user.email

  Deletar o token no Github
  deslogar do github