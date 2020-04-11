from __future__ import unicode_literals
from .common import InfoExtractor


class YoutunerIE(InfoExtractor):
    _VALID_URL = r'http:\/\/youtuner.co\/s\/(?P<id>\d+)'

    def _real_extract(self, url):
        track_id = self._match_id(url)

        webpage = self._download_webpage(url, track_id)

        # Extract required fields
        title = self._search_regex(
            r'<title>(.+)<\/title>',
            webpage, "title"
        )
        download_url = self._search_regex(
            r'(https://[^/]+/audios/[^\.]+\.[^"]+)"/>',
            webpage, "download_url"
        )

        extracted = {
            'id': track_id,
            'url': download_url,
            'title': title,
        }



        return extracted