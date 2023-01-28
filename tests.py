from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_one_default_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        assert collector.books_rating.get('Гордость и предубеждение') == 1

    def test_add_new_book_add_one_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_rating_5(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 5)
        assert collector.books_rating.get('Война и мир') == 5

    def test_set_book_rating_rating_0(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 0)
        assert collector.books_rating.get('Война и мир') != 0

    def test_set_book_rating_rating_11(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 11)
        assert collector.books_rating.get('Война и мир') != 11

    def get_book_rating_by_the_name(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 4)
        collector.add_new_book('Алые паруса')
        collector.set_book_rating('Алые паруса', 5)
        assert collector.get_book_rating('Война и мир') == 4

    def test_get_books_with_specific_rating_only_5(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 4)
        collector.add_new_book('Алые паруса')
        collector.set_book_rating('Алые паруса', 5)
        collector.add_new_book('Д’Артаньян и три мушкетёра')
        collector.set_book_rating('Д’Артаньян и три мушкетёра', 5)
        collector.add_new_book('Цветы для Элджернона')
        collector.set_book_rating('Цветы для Элджернона', 10)
        assert collector.get_books_with_specific_rating(5) == ['Алые паруса', 'Д’Артаньян и три мушкетёра']

    def test_get_books_rating_with_different_ratings(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Алые паруса')
        collector.set_book_rating('Алые паруса', 5)
        collector.add_new_book('Д’Артаньян и три мушкетёра')
        collector.add_new_book('Цветы для Элджернона')
        collector.set_book_rating('Цветы для Элджернона', 10)
        assert collector.get_books_rating() == {'Война и мир' : 1, 'Алые паруса' : 5, 'Д’Артаньян и три мушкетёра' : 1, 'Цветы для Элджернона': 10}

    def test_add_book_in_favorites_add_one_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Алые паруса')
        collector.add_book_in_favorites('Алые паруса')
        assert 'Алые паруса' in collector.favorites

    def test_add_book_in_favorites_add_one_book_to_favorites_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Алые паруса')
        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('Алые паруса')
        collector.delete_book_from_favorites('Алые паруса')
        assert 'Алые паруса' not in collector.favorites

    def test_get_list_of_favorites_books_three_books(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Алые паруса')
        collector.add_new_book('Д’Артаньян и три мушкетёра')
        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('Алые паруса')
        collector.add_book_in_favorites('Д’Артаньян и три мушкетёра')
        assert collector.favorites == ['Война и мир', 'Алые паруса', 'Д’Артаньян и три мушкетёра']