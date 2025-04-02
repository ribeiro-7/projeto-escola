# Escola API - Django Rest Framework

## 📚 Sobre o Projeto
Este é um projeto de API REST desenvolvido com Django Rest Framework que simula um sistema escolar. A aplicação permite o gerenciamento de alunos, cursos e matrículas, com endpoints para criar, ler, atualizar e deletar dados.

## 🚀 Tecnologias Utilizadas
- Python  
- Django  
- Django Rest Framework   

## 📁 Models
- **Alunos**: Nome, E-mail, RG, CPF, Data de Nascimento.  
- **Cursos**: Código do Curso, Descrição, Nível (básico, intermediário, avançado).  
- **Matrículas**: Período (matutino, vespertino, noturno), Aluno, Curso.  

## 🔗 Relacionamentos
- Um aluno pode se matricular em vários cursos (relacionamento muitos-para-muitos através da matrícula).
- Um curso pode ter vários alunos matriculados.

## 📌 Endpoints

### Endpoints Alunos
- `GET /alunos/` - Lista todos os alunos registrados divididos em páginas (10 alunos por página).
- `POST /alunos/` - Cria um novo aluno. **Validações:**  
  - Nome: Deve conter apenas letras.  
  - Email: Deve seguir o formato válido de email.  
  - RG: Deve conter 9 números.  
  - CPF: Deve ser um CPF válido, sem traços e pontos.  
  - Data de nascimento: Deve ser uma data válida.
- `PUT /alunos/<id_aluno>/` - Atualiza os dados de um aluno com o ID fornecido.
- `DELETE /alunos/<id_aluno>/` - Deleta o aluno com o ID fornecido.
- `GET /aluno/<id_aluno>/matriculas/` - Lista todas as matrículas cadastradas para aquele aluno.

### Endpoints Cursos
- `GET /cursos/` - Lista todos os cursos cadastrados.
- `POST /cursos/` - Cria um novo curso. **Campos:** Código do Curso, Descrição, Nível (básico, intermediário, avançado).
- `PUT /cursos/<id_curso>/` - Atualiza os dados de um curso com o ID fornecido.
- `DELETE /cursos/<id_curso>/` - Deleta o curso com o ID fornecido.
- `GET /curso/<id_curso>/matriculas/` - Lista todas as matrículas de alunos no curso fornecido.

### Endpoints Matrículas
- `GET /matriculas/` - Lista todas as matrículas cadastradas.
- `POST /matriculas/` - Cria uma nova matrícula. **Campos:** Período (matutino, vespertino, noturno), Aluno, Curso.
- `PUT /matriculas/<id_matricula>/` - Atualiza os dados de uma matrícula com o ID fornecido.
- `DELETE /matriculas/<id_matricula>/` - Deleta a matrícula com o ID fornecido.

## 📌 Validações
- Nome dos alunos: Apenas letras.
- Email dos alunos: Deve seguir o formato padrão de email.
- RG: Deve conter 9 números.
- CPF: Deve ser válido, sem traços e pontos.
- Data de nascimento: Deve ser uma data válida.
- Cursos: Nível deve ser um dos seguintes: básico, intermediário, avançado.
- Matrículas: Período deve ser um dos seguintes: matutino, vespertino, noturno.


