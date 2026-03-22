# Пример переменных
lucky_number = 7            # int — immutable
pi = 3.14                   # float — immutable
one_is_a_prime_number = True  # bool — immutable
name = "Jessica"            # str — immutable

my_favourite_films = ["Inception", "Pulp Fiction"]  # list — mutable
profile_info = {"age": 20, "city": "Lviv"}         # dict — mutable
marks = [5, 4, 3]                                  # list — mutable
collection_of_coins = {1, 2, 5}                    # set — mutable

# Сортируем переменные по типу (mutable / immutable)
sorted_variables = {
    "immutable": [
        lucky_number,
        pi,
        one_is_a_prime_number,
        name,
    ],
    "mutable": [
        my_favourite_films,
        profile_info,
        marks,
        collection_of_coins,
    ],
}
