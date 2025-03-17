first_experiment_id: int = 1

tests: list = []

sum_even = 0

try:

  if not isinstance(first_experiment_id, int):

    value = int(first_experiment_id)

  print("Gültige Test ID.")

except ValueError:

  print("Error, gib eine gültige Test ID ein")

else:

  for i in range(11):

    test_id: int = first_experiment_id + i

    test_log = {

        "Test ID:" : test_id,

        "Date:" : "13.03.2025",

        "Investigator:" : "L. Escobar"

    }

    tests.append(test_log)

 

    if test_id % 2 == 0:

      sum_even += 1

print(tests)

print("first 5 tests:", tests[:5])

print(sum_even)
