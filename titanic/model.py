class Titanic:
    def __init__(self):
        self._context = None
        self._fname = None
        self._train = None
        self._test = None
        self._testId = None

    @property
    def context(self) -> object: return self._context

    @property
    def fname(self)-> object: return self._fname

    @property
    def train(self)-> object: return self._train

    @property
    def test(self)-> object: return self._test

    @property
    def testId(self)-> object: return self._testId

    @context.setter
    def context(self, context): self._context = context

    @fname.setter
    def fname(self, fname): self._fname = fname

    @train.setter
    def train(self, train): self._train = train

    @test.setter
    def test(self, test): self.test = test

    @testID.setter
    def testId(self, testId): self.testId = testId

