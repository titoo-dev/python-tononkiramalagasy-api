# python-tononkiramalagasy-api

## Api Endpoints:
    ### get artists
        -   /artists/<int:page> [page_offset = 20]
    ### get artist's songs, index was given by artist data
        -   /artists/<int:index>/songs/<int:page> [page_offset = 20] 
    ### get lyrics
        -   /lyrics/<string:artist>/<string:title>