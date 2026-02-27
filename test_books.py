import pytest


class TestBook:

    def test_add_new_book(self, collector):
        """Проверяет добавление новой книги"""
        collector.add_new_book('Внутри убийцы')
        assert 'Внутри убийцы' in collector.get_books_genre()

    def test_add_new_book_already_exists(self, collector):
        """Проверяет, что нельзя добавить книгу с одинаковым названием дважды"""
        collector.add_new_book('Зелёная миля')
        collector.add_new_book('Зелёная миля')
        count_books = len(collector.get_books_genre())
        assert count_books == 1

    def test_add_new_book_name_is_too_long(self, collector):
        """Проверяет, что нельзя добавить книгу с названием длиннее 40 символов"""
        collector.add_new_book('Очень длинное название книги, которое превышает сорок символов')
        assert 'Очень длинное название книги, которое превышает сорок символов' not in collector.get_books_genre()

    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Сияние', 'Ужасы'],
                                 ['Оно', 'Ужасы'],
                                 ['Дюна', 'Фантастика'],
                                 ['Внутри убийцы', 'Детективы'],
                                 ['Манюня', 'Мультфильмы'],
                                 ['Дневник Бриджит Джонс', 'Комедии']
                             ])
    def test_set_book_genre(self, collector, name, genre):
        """Проверяет установку жанра книги."""
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_not_in_genre_list(self, collector):
        """Проверяет, что нельзя установить жанр, которого нет в списке допустимых жанров"""
        collector.add_new_book('Грозовой перевал')
        collector.set_book_genre('Грозовой перевал', 'Роман')
        assert collector.get_book_genre('Грозовой перевал') == ''

    def test_get_book_genre_not_added(self, collector):
        """Проверяет, что возвращается None, если жанр для книги не был установлен"""
        assert collector.get_book_genre('Сияние') is None

    def test_get_books_with_specific_genre(self, collector):
        """Проверяет получение списка книг определенного жанра"""
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Сияние', 'Оно']

    def test_get_books_for_children(self, collector):
        """Проверяет, что возвращается список книг, подходящих для детей"""
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Манюня')
        collector.set_book_genre('Манюня', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Дюна', 'Манюня']

    def test_add_book_in_favorites(self, collector):
        """Проверяет, что книга добавляется в список избранных книг"""
        collector.add_new_book('Дневник Бриджит Джонс')
        collector.set_book_genre('Дневник Бриджит Джонс', 'Комедии')
        collector.add_book_in_favorites('Дневник Бриджит Джонс')
        assert 'Дневник Бриджит Джонс' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        """Проверяет, что книга удаляется из списка избранных книг"""
        collector.add_new_book('Институт')
        collector.set_book_genre('Институт', 'Ужасы')
        collector.add_book_in_favorites('Институт')
        collector.delete_book_from_favorites('Институт')
        assert 'Институт' not in collector.get_list_of_favorites_books()