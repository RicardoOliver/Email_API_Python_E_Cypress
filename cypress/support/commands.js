Cypress.Commands.add('login', (username, password) => {
  return cy.api({
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
  return cy.api({
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
