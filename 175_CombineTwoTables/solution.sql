-- regardless if there is an address for each of those people
-- we should use outer join, instead of where(inner join)

select FirstName, LastName, City, State
    from Person left join Address
    on Person.personId = Address.PersonId