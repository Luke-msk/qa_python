# 1. Тест "test_add_new_book_one_default_rating" проверяет, что добавленной книге присвоен рейтинг 1 по умолчанию
# 2. Тест "test_add_new_book_add_one_book_twice" проверяет, что при повторном добавлении книги она не дублируется в словаре
# 3. Тест "test_set_book_rating_rating_5" проверяет, что книге устанавлен рейтинг 5
# 4. Тест "test_set_book_rating_rating_0" проверяет, что книге НЕустанавлен рейтинг 0
# 5. Тест "test_set_book_rating_rating_11" проверяет, что книге НЕустанавлен рейтинг 11
# 6. Тест "get_book_rating_by_the_name" проверяет, что выводится верный рейтинг по названию книги
# 7. Тест "test_get_books_with_specific_rating_only_5" проверяет, что выводится весь список книг с конкретным рейтингом 5
# 8. Тест "test_get_books_rating_with_different_ratings" проверяет, что выводится словарь со всеми добавленными книгами и рейтингами
# 9. Тест "test_add_book_in_favorites_add_one_book_to_favorites" проверяет, что указанная книга добавляется в избранное
# 10. Тест "test_add_book_in_favorites_add_one_book_to_favorites_twice" проверяет, что при повторном добавлении одной книги в избранное, она не дублируется в списке
# 11. Тест "test_delete_book_from_favorites_delete_one_book" проверяет, что книга удаляется из избранного
# 12. Тест "test_get_list_of_favorites_books_three_books" проверяет, что выводится весь список книг, добавленных в избранное