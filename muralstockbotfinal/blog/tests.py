from test_title import solution

#  Teste : Se titulo de mensagens forem iguais , retorne Error
class Testtitle(solution):
    def test_title_n(self):

        self.assertEqual(solution('o-vento'), 'o-vento')
