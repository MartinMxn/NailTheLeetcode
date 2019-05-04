select Person.Firstname, Person.Lastname, Address.City, Address.State
From Person
Left Join Address on Person.PersonId = Address.PersonId
