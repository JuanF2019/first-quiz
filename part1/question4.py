import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """

SELECT name,species,age FROM animals WHERE animals.animal_id NOT IN (
    SELECT DISTINCT(pet_id) FROM people_animals
);

"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """

SELECT COUNT(*) FROM (
    SELECT MAX(p.age) AS p_min_age, a.age AS pet_age
    FROM people p, people_animals pa, animals a
    WHERE p.person_id = pa.owner_id
    AND a.animal_id == pa.pet_id
    GROUP BY a.animal_id
) AS owner_min_age_and_pet_age
WHERE owner_min_age_and_pet_age.pet_age > owner_min_age_and_pet_age.p_min_age;

"""

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """
    SELECT p.name, a.name, a.species
    FROM people p, people_animals pa, animals a
    WHERE p.person_id = pa.owner_id
    AND a.animal_id == pa.pet_id
    AND p.name = "bessie"
    AND a.animal_id NOT IN (
        SELECT a2.animal_id
        FROM people p2, people_animals pa2, animals a2
        WHERE p2.person_id = pa2.owner_id
        AND a2.animal_id == pa2.pet_id 
        AND p2.name <> "bessie"
    );
"""