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
