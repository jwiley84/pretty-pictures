Good morning, James!

I'm very sorry you're experiencing frustration with the Stripe API. Thank you for reaching out for assistance, let's see if we can get this sorted out. 

From a look at the code you've provided, you're missing a "Bearer" in the request.Headers.add section. If you modify this from: 

'request.Headers.Add("Authorization", "sk_test_W8xJYzw56NCHun0FT9iGIJeI");'

to 

'request.Headers.Add("Authorization", "Bearer sk_test_W8xJYzw56NCHun0FT9iGIJeI");'

your call should be successful.

Please let us know if you have any further questions! Thank you for choosing Stripe!

JJ
