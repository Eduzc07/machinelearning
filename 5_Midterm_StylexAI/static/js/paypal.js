// Render the PayPal button into #paypal-button-container
paypal.Buttons({
    createOrder: function(data, actions) {
    // Set up the transaction
    return actions.order.create({
      purchase_units: [{
        amount: {
          value: '1.99'
        }
      }]
    })
  },
  onApprove: function(data, actions) {
    return actions.order.capture().then(function(details) {
      alert('Transaction completed by ' + details.payer.name.given_name + "\n" +
                    'Thank you!');
      console.log("---------------------------Paid")
      console.log(data.orderID)

      $('#setting-status').text(function(i, oldText) {
          return "Account: Premium";
          // return oldText === 'Profil' ? 'New word' : oldText;
      });

      $.post({
        type: "POST",
        url: "/paypal_success",
        data: {"orderID": data.orderID}
      });
    });
  },
  // Configure environment
  // env: 'sandbox',
  // client: {
  //   sandbox: 'demo_sandbox_client_id',
  //   production: 'demo_production_client_id'
  // },

  // Configure environment
  // env: 'production',
  // client: {
  //     production: 'LIVE_CLIENT_ID' //Enter your live client ID here
  // }

  // Customize button (optional)
  locale: 'es_PE',
  style: {
      layout: 'horizontal',
      color: 'blue',
      shape: 'pill',
      label: 'pay',
      height: 40,
      tagline: false
  }
}).render('#paypal-button-container');
