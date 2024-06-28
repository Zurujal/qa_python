import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_one_book_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_similar_book_2_times_only_one_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_one_book_genre_is_empty(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ''

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_genre_added_successfully(self, genre, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_book_genre_genre_received_successfully(self, genre, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_one_book_specific_genre_received_successfully(self, genre, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre) == [book_name]

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_genre_one_book_one_genre_dictionary_received_successfully(self, genre, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_genre() == {book_name: genre}

    @pytest.mark.parametrize('genre', ['Фантастика', 'Мультфильмы', 'Комедии'])
    def test_get_books_for_children_book_with_kids_genre_book_in_list(self, genre, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert len(collector.get_books_for_children()) == 1

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_book_with_adult_genre_book_not_in_list(self, genre, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_one_book_added_successfully(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_one_book_deleted_successfully(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_one_book_received_successfully(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == [book_name]



