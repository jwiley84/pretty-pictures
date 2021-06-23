Good morning, Donald!

Glad to see it's working for you so far! Let's get you on track to get and review all your charges. From your code snippet, it appears you're using Ruby, so I'll continue with that language:

The code snippet you listed: 

'charges = Stripe::Charge.list() '

is set to return with default optional parameters, unless you set them manually. The parameter of 'limit' has a default of 10, which is what you're running into. By adding a new limit as a parameter as follows:

'charges = Stripe::Charge.list({limit: 3})'

you can change that amount. 'limit' as a paramter can accept any integer between 1 and 100. Of course, this still doesn't quiet solve what you need, as 100 is still under the 1000 you want to look at. In this case, we can look at auto-pagination feature offered in the API. The following code snipped will retrieve all 1000 charges, and add them to a list:

'''
charge_amts = []
charges = Stripe::Charge.list({limit: 100})
charges.auto_paging_each do |charge|
    charge_amts << charge.id
end
'''

For more examples, I recommend taking a look at this video for pagination with stripe-ruby: 

https://www.youtube.com/watch?v=mawDqjFzTIQ&list=PLy1nL-pvL2M50RmP6ie-gdcSnfOuQCRYk&ab_channel=StripeDevelopers

Please let us know if you have any further questions! Thank you for choosing Stripe!

JJ



Summary: I'm aware the cx asked for a list with both charge id and charge amount, but I know less than 0% of the Ruby language, and have no idea how do add both to a list. If I was using Python or C#, I would know, but in this case, I would reach out for assistance for someone who actually knows Ruby for help 

