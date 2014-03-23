contacts={}
contacts={
'Shannon':{'phone':'202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner' },
'Anupama':{'phone':'222-222-1111', 'twitter': '@iamtheanupama', 'github':'@anupama'}}

for contact in sorted(contacts.keys()):
        #print contact,"s contact information is:"
        print "\n"
        print "{0}'s contact information is: ".format(contact)
        print "Phone: ",contacts[contact]['phone']
        print "Twitter: ",contacts[contact]['twitter']
        print "Github: ",contacts[contact]['github']
        print "\n"
