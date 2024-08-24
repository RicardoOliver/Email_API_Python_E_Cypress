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
    cy.sendEmail('kafeha4155@inpsur.com', 'Assunto de Teste', 'Este é um email de teste.')
      .then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body.status).to.eq('success');
      });
  });
});

