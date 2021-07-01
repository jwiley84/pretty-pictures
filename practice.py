import requests, json

def practice_GET():
    #simple GET request
    res = requests.get("https://pokeapi.co/api/v2/egg-group/13")
    #res == the result object, comes through on console as <Response [200]>
    print(res)
    #res.status_code returns the response code as an int
    print(res.status_code)

    if res: #if res will only trigger on a 200
        print("response ok")
    else: #treat it like a boolean. a 200 is True, a 404 is 
        print("try again")

    #print(res.headers) #no shit
    #print(res.text) #no shit

    output = open('testing2.json', 'w', encoding="utf-8")
    output.write(res.text)
    output.close

def practice_deserializing_JSON():
    #open the file
    f = open('testing.json', encoding="utf-8")
    
    #return the JSON obeject as a dictionary
    data = json.load(f)

    #iterate through the list
    for i in data: #for the pokeAPI results, using the JSON from testing.json
        #i is the full egg group object
        print(i["name"])
        for j in i["names"]:
            #j is the names list
            print("In {}, it's called {}".format(j["language"]["name"], j["name"]))
            #print(j["name"])

            #print(i["name"])
    

def practice_POST():
    #api_key = "pk_test_51J5di5GbgHM4rJvnQpwn1WIwn6Wlskb9sZn0HMMQwRHUrAgx22XUEgAF6PdcoGwDzPWIjwpyuE4N10CA1VMt3Rlo00vRuFcFC8"
    url = "https://api.stripe.com/v1/charges?amount=1000&currency=usd&source=tok_visa&description=test@test1.com"
    headers = {"Authorization": "Bearer sk_test_51J5di5GbgHM4rJvnSAjv9GMEP0xVewH30VlhmueVBUYLEjtafKRmTDSKN46QSKPr6oQ18mJWSXv6EMT0vsu5X67h00eonPCPNx"}
    print(url)

    res = requests.post(url, headers=headers)
    print(res.status_code)


#practice_POST()

