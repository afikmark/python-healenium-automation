from factory import DictFactory


class DictAttributes(dict):

    def __getattr__(self, item):
        return self.get(item)


class DictWithAttributes(DictFactory):
    class Meta:
        model = DictAttributes
