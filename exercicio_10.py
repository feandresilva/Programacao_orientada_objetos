# A academia FitLife precisa de um sistema para auxiliar o trabalho da recepção. 
# O sistema deverá permitir o cadastro dos alunos, armazenando informações como nome, CPF, 
# data de nascimento, telefone, endereço e número da matrícula.

# Cada aluno deverá possuir uma matrícula com informações como data de início, 
# data de vencimento e status. O status poderá indicar se a matrícula está ativa, inadimplente 
# ou cancelada. Antes de liberar o acesso à academia, a recepção deverá consultar 
# o aluno e verificar se sua matrícula permite a entrada.

# O sistema também deverá registrar as entradas e saídas dos alunos, 
# armazenando a data e o horário de cada movimentação. 
# A identificação poderá ser realizada pela carteirinha ou pelo CPF. 
# Caso o aluno esteja sem a carteirinha, a recepção deverá validar sua identidade 
# utilizando seus dados cadastrados antes de realizar uma liberação temporária.

# Crie o sistema utilizando programação orientada a objetos em Python.
# O sistema deverá salvar todos os dados em arquivos (pickle ou json), 
# e cada ação executada deverá ser salva e registrada.
# O sistema deve ser resiliente a erros e a entradas incorretas/inválidas. 
# Exiga uma autenticação (usuário e senha) para as ações administrativas do sistema 
# (adicionar aluno, alterar matrícula, registrar entrada/saída, etc).