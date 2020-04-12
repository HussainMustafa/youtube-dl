from __future__ import unicode_literals
from .common import InfoExtractor


class YoutunerIE(InfoExtractor):
    _VALID_URL = r'http:\/\/youtuner.co\/s\/(?P<id>\d+)'

    _TESTS = [{
        'url': 'http://youtuner.co/s/147665',
        'info_dict': {
            'id': '147665',
            'ext': 'mp3',
            'title': 'Avaliar animes de forma crítica? Por quê? - Anime Crazies #95 - YouTuner',

        },
    }]

    # Extract title & url also will need to add test
    def _real_extract(self, url):

        track_id = self._match_id(url)

        webpage = self._download_webpage(url, track_id)

        # Extract required fields
        title = self._search_regex(
            r'<title>(.+)<\/title>',
            webpage, "title"
        )
        download_url = self._search_regex(
            r'(https:\/\/feedproxy.google.com\/~r\/animecrazies\/~5\/\S+\/.+\.mp3)',
            webpage, "download_url"
        )

        author = self._search_regex(
            r'artists/[^"]+" target="[^"]+">([^<]+)</a>',
            webpage, "author", fatal=False
        )

        
        if author:
            extracted['uploader'] = author


        extracted = {
            'id': track_id,
            'url': download_url,
            'title': title,
        }

        return extracted
