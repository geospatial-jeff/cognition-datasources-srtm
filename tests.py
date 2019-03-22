from datasources import tests

from SRTM import SRTM

class SRTMTestCases(tests.BaseTestCases):

    def _setUp(self):

        self.datasource = SRTM
        self.spatial = {
                    "type": "Polygon",
                    "coordinates": [
                      [
                        [
                          -101.28433227539062,
                          46.813218976041945
                        ],
                        [
                          -100.89431762695312,
                          46.813218976041945
                        ],
                        [
                          -100.89431762695312,
                          47.06450941441436
                        ],
                        [
                          -101.28433227539062,
                          47.06450941441436
                        ],
                        [
                          -101.28433227539062,
                          46.813218976041945
                        ]
                      ]
                    ]
                  }
        self.properties = {'eo:gsd': {'eq': 30.0}}
        self.limit = 10

    def test_temporal_search(self):
        # Underlying API doesn't accept temporal
        pass

