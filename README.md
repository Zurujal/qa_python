# qa_python

Описание тестов

Метод add_new_book
test_add_new_book_one_book_added - Проверяем, что мы можем успешно добавить книгу.
test_add_new_book_similar_book_2_times_only_one_added - Проверяем, что при попытке добавить
книгу с одним и тем же названием дважды - добавляется только одна книга.
test_add_new_book_one_book_genre_is_empty - Проверяем, что при добавлении книги жанр остается
пустым.

Метод set_book_genre
test_set_book_genre_genre_added_successfully - Проверяем, что можем успешно присвоить книге жанр.

Метод get_book_genre
test_get_book_genre_genre_received_successfully - Проверяем, что можем успешно получить жанр книги.

Метод get_books_with_specific_genre
test_get_books_with_specific_genre_one_book_specific_genre_received_successfully - Проверяем,
что можем успешно получить список названий книг конкретного жанра.

Метод get_books_genre
test_get_books_genre_one_book_one_genre_dictionary_received_successfully - Проверяем, что можем
успешно получить словарь вида - Название книги: жанр книги.

Метод get_books_for_children
test_get_books_for_children_book_with_kids_genre_book_in_list - Проверяем, что метод возвращает
книги с "детскими" жанрами.
test_get_books_for_children_book_with_adult_genre_book_not_in_list - Проверяем, что метод не 
возвращает книги с "взрослыми" жанрами.

Метод add_book_in_favorites
test_add_book_in_favorites_one_book_added_successfully - Проверяем, что книга добавляется в
избранное.

Метод delete_book_from_favorites
test_delete_book_from_favorites_one_book_deleted_successfully - Проверяем. что книга удаляется
из избранного.

Метод get_list_of_favorites_books
test_get_list_of_favorites_books_one_book_received_successfully - Проверяем, что метод возвращает
список избранных книг.Ы