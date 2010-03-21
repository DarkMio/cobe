import unittest

from cobe.tokenizers import CobeTokenizer, MegaHALTokenizer

class testMegaHALTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = MegaHALTokenizer()

    def testSplitEmpty(self):
        self.assertEquals(len(self.tokenizer.split(u"")), 0)

    def testSplitSentence(self):
        words = self.tokenizer.split(u"hi.")
        self.assertEquals(words, ["HI", "."])

    def testSplitComma(self):
        words = self.tokenizer.split(u"hi, cobe")
        self.assertEquals(words, ["HI", ", ", "COBE", "."])

    def testSplitImplicitStop(self):
        words = self.tokenizer.split(u"hi")
        self.assertEquals(words, ["HI", "."])

    def testSplitUrl(self):
        words = self.tokenizer.split(u"http://www.google.com/")
        self.assertEquals(words, ["HTTP", "://", "WWW", ".", "GOOGLE", ".", "COM", "/."])

    def testSplitApostrophe(self):
        words = self.tokenizer.split(u"hal's brain")
        self.assertEquals(words, ["HAL'S", " ", "BRAIN", "."])

        words = self.tokenizer.split(u"',','")
        self.assertEquals(words, ["'", ",", "'", ",", "'", "."])

    def testSplitApostrophe(self):
        words = self.tokenizer.split(u"hal's brain")
        self.assertEquals(words, ["HAL'S", " ", "BRAIN", "."])

    def testSplitAlphaAndNumeric(self):
        words = self.tokenizer.split(u"hal9000, test blah 12312")
        self.assertEquals(words, ["HAL", "9000", ", ", "TEST", " ", "BLAH", " ", "12312", "."])

        words = self.tokenizer.split(u"hal9000's test")
        self.assertEquals(words, ["HAL", "9000", "'S", " ", "TEST", "."])

    def testCapitalize(self):
        words = self.tokenizer.split(u"this is a test")
        self.assertEquals(u"This is a test.", self.tokenizer.join(words))

        words = self.tokenizer.split(u"A.B. Hal test test. will test")
        self.assertEquals(u"A.b. Hal test test. Will test.",
                          self.tokenizer.join(words))

        words = self.tokenizer.split(u"2nd place test")
        self.assertEquals(u"2Nd place test.", self.tokenizer.join(words))

class testCobeTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = CobeTokenizer()

    def testSplitEmpty(self):
        self.assertEquals(len(self.tokenizer.split(u"")), 0)

    def testSplitSentence(self):
        words = self.tokenizer.split(u"hi.")
        self.assertEquals(words, ["hi", "."])

    def testSplitComma(self):
        words = self.tokenizer.split(u"hi, cobe")
        self.assertEquals(words, ["hi", ", ", "cobe"])

    def testSplitUrl(self):
        words = self.tokenizer.split(u"http://www.google.com/")
        self.assertEquals(words, ["http://www.google.com/"])

    def testSplitMultipleSpaces(self):
        words = self.tokenizer.split(u"this is  a test")
        self.assertEquals(words, ["this", " ", "is", " ", "a", " ", "test"])

    def testSplitVerySadFrown(self):
        words = self.tokenizer.split(u"testing :    (")
        self.assertEquals(words, ["testing", " :    ("])

        words = self.tokenizer.split(u"testing          :    (")
        self.assertEquals(words, ["testing", " :    ("])

if __name__ == '__main__':
    unittest.main()
