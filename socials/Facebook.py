def getDetail(soup):
    fbDetail = {
        'title': 'null',
        'description': 'null',
        'image': 'nulls',
        'url': 'null',
        'app_id': 'null',
    }

    fbTags = {
        'title': 'og:title',
        'description': 'og:description',
        'image': 'og:image',
        'url': 'og:url',
        'app_id': 'fb:app_id',
    }

    for attr, value in fbTags.items():
        try:
            tagContent = soup.select_one('[property="' + value + '"]')
            if tagContent.has_key('content'):
                fbDetail[attr] = tagContent['content']
        except:
            pass

    return fbDetail


