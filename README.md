# PyPiapro
Python API for [Piarpo (ピアプロ)](http://www.piapro.jp) dataset mining.

PyPiapro is used as a dataset aggregation toolkit used for curating a dataset for
an end-to-end framework for generating Vocaloid song (+ PV) using Deep Learning -
essentially replacing the role of a music producer. The library is currently
under a work in progress and will aim to reach the scope of being able to
interface with the entire site - including accounts, song, illustrations, and lyrics.

## TODO:
- Lyrics:
    - Include improved pagination
    - Define better dataset exportation heuristics (include meta data like tags)
    - Need tmp folder or a temporary directory when storing data somehere...
    - Define a JSON based schema for storing lyrics and associated meta-data.
- Search:
    - Include better interface for search functions
    - Build wrapper libraries for search
    - Implement multiple tagging
    - Pagination
- Songs:
    - Research and look into structure of Piapro's flash player.
    - Extraction of music from site...
- Image:
    - Tag Extraction and Tag Embedding Heuristics
- Accounts:
    - Account sign in, cookies, sessions, etc
    - Upload music and content
    - Messaging interfaces (bots anyone?)
- Package:
    - Package up library as an installer with setup.py and unit testing.
    - Library formation
