import csv

from mrjob.job import MRJob
from mrjob.step import MRStep


class VLookUP(MRJob):

    def mapper(self, key, value):
        result = next(csv.reader([value], quotechar=None))
        reference = result[0]
        yield reference, 1

    def reducer(self, key, values):
        yield None, (sum(values), key)

    def reducer_sorter(self, key, values):
        for count, key in sorted(values):
            yield count, key

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                reducer=self.reducer
            ),
            MRStep(
                reducer=self. reducer_sorter
            )
        ]


if __name__ == '__main__':
    print()
    VLookUP.run()
    print()
