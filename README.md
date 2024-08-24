📧 Email API com Flask e Cypress

Desenvolvi uma API completa para envio de e-mails utilizando Flask, que inclui funcionalidades robustas para autenticação e envio de e-mails. Este projeto também conta com uma suíte de testes automatizados criados com Cypress para garantir a qualidade e a confiabilidade da aplicação.

🔧 Tecnologias Utilizadas:

    Flask: Para o desenvolvimento da API RESTful.
    JWT (JSON Web Token): Para autenticação segura.
    Cypress: Para testes automatizados de integração e e2e.
    Python: Para o desenvolvimento backend.
    JavaScript: Para a automação de testes com Cypress.

🛠 Funcionalidades Principais:

    Autenticação JWT: Implementada para proteger endpoints e garantir acesso seguro.
    Envio de E-mails: Endpoint para envio de e-mails com suporte a autenticação.
    Testes Automatizados: Testes de autenticação e envio de e-mails, com verificação de sucesso e falhas, utilizando Cypress.

🔍 Detalhes dos Testes:

    Autenticação: Testa a funcionalidade de login e valida a obtenção do token JWT.
    Envio de E-mail: Valida o envio de e-mails e o comportamento da API em casos de sucesso e erro.

💡 Destaques do Projeto:

    Código Limpo e Documentado: Estrutura clara e bem documentada para fácil manutenção e escalabilidade.
    Automação de Testes: Garantia de qualidade com testes automatizados que cobrem principais fluxos de uso.
    Configuração Flexível: Uso de variáveis de ambiente para configuração de credenciais e parâmetros sensíveis.

🔗 Link para o Repositório: 

   [ GitHub Repository](https://github.com/RicardoOliver/Email_API_Python_E_Cypress/tree/main)

Este projeto demonstrou minha habilidade em integrar desenvolvimento backend com testes automatizados, e é uma excelente adição ao meu portfólio de projetos.


EMAIL API
Descrição

Este projeto é uma API para envio de e-mails, criada com Flask. A API inclui funcionalidades para autenticação via JWT e envio de e-mails. O projeto utiliza Cypress para testes automatizados e configura um ambiente de teste completo para garantir a qualidade e a funcionalidade da aplicação.
Estrutura do Projeto

    EMAIL_API/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── app.py
    │   ├── config.py
    │   ├── routes/
    │   │   ├── __init__.py
    │   │   ├── auth.py
    │   │   └── email.py
    │   └── utils/
    │       ├── __init__.py
    │       └── auth.py
    │
    ├── tests/
    │   ├── auth.cy.js
    │   ├── post_email.cy.js
    │   └── commands.js
    │
    ├── cypress.config.js
    ├── run.py
    ├── .env
    └── README.md

Configuração do Ambiente

Clone o repositório:

    git clone https://github.com/usuario/email-api.git
    cd email-api

2.Crie um ambiente virtual e ative-o:

      python -m venv venv
      source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3.Instale as dependências do Python:

    pip install -r requirements.txt
    
4.Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis de ambiente:

    MAIL_USERNAME=seu_email@gmail.com
    MAIL_PASSWORD=sua_senha
    SECRET_KEY=sua_chave_secreta

Executando o Projeto

Inicie o servidor Flask:

    python run.py

    O servidor estará disponível em http://127.0.0.1:5000.

Testes Automatizados com Cypress
1. auth.cy.js

Este teste verifica a autenticação e a geração de um token JWT.

```
describe('Authentication', () => {
  it('should login and return a JWT token', () => {
    cy.request({
      method: 'POST',
      url: '/login',
      headers: {
        'Authorization': 'Basic ' + btoa('user:password') // Utiliza btoa no navegador
      }
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body.token).to.be.a('string');
      cy.log('Token:', response.body.token); // Registrar token para depuração
    });
  });
});
```

2. post_email.cy.js

Este arquivo testa o envio de e-mails, garantindo que o token é corretamente salvo e recuperado antes de cada teste.
```
describe('Enviar Email', () => {
  let token;

  beforeEach(() => {
    // Fazer login antes de cada teste para obter um token
    cy.login('user', 'password').then((loginToken) => {
      token = loginToken;
      cy.log('Token obtido com sucesso:', token); // Registrar token para depuração
    });
  });

  it('deve enviar um email com sucesso', () => {
    cy.sendEmail('r.c.d.29111985@gmail.com', 'Assunto de Teste', 'Este é um email de teste.')
      .then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body.status).to.eq('success');
        expect(response.body.message).to.eq('Email enviado com sucesso');
      });
  });

  it('deve falhar ao enviar um email sem token', () => {
    cy.request({
      method: 'POST',
      url: '/send_email',
      failOnStatusCode: false,
      body: {
        recipient: 'recipient@example.com',
        subject: 'Assunto de Teste',
        body: 'Este é um email de teste.'
      }
    }).then((response) => {
      expect(response.status).to.eq(403);
      expect(response.body.message).to.eq('Token de autenticação ausente ou inválido'); // Ajustar conforme a mensagem real de erro
    });
  });
});
```

3. commands.js

Define comandos personalizados para login e envio de e-mail.
```
Cypress.Commands.add('login', (username, password) => {
  return cy.request({
    method: 'POST',
    url: '/login',
    headers: {
      'Authorization': 'Basic ' + btoa(`${username}:${password}`) // Utiliza btoa no navegador
    }
  }).then((response) => {
    window.localStorage.setItem('token', response.body.token);
    return response.body.token; // return the token
  });
});

Cypress.Commands.add('sendEmail', (recipient, subject, body) => {
  const token = window.localStorage.getItem('token');
  return cy.request({
    method: 'POST',
    url: '/send_email',
    headers: {
      'Authorization': `Bearer ${token}`
    },
    body: {
      recipient,
      subject,
      body
    }
  });
});
```

4. cypress.config.js

Configuração do Cypress com a URL base ajustada para o servidor local.
```
const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    baseUrl: 'http://127.0.0.1:5000', // ou http://localhost:PORT
  },
});
```


Dicas Adicionais

    Verifique se o servidor de teste está em execução e acessível.
    Certifique-se de que o backend está retornando os dados esperados para login e envio de e-mail.
    Utilize cy.log para depuração e verifique os valores de variáveis importantes durante os testes.
    Certifique-se de que o arquivo env esteja configurado o SMTP :
    MAIL_USERNAME="adicionar seu email"
    MAIL_PASSWORD="adicionar sua senha"
    SECRET_KEY="Adicionar sua chave"



Contribuição

Sinta-se à vontade para contribuir para o projeto. Para enviar melhorias ou correções, faça um fork do repositório, faça suas alterações e envie um pull request.
Licença

Este projeto é licenciado sob a Licença MIT.




