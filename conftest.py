import random

import pytest


@pytest.fixture
def book_name():
    book_names = ['Гордость и предубеждение и зомби', 'Гарри Поттер и кубок огня', 'Ведьмак', 'Последнее желание',
                  'Сталкер']
    return random.choice(book_names)
