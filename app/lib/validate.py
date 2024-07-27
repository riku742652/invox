import re


def image_path(value: str) -> bool:
    '''
        image_pathのバリデーションチェック
        param:
            value <str> 検査値
        return:
            bool True: チェックOK False: チェックNG
    '''
    pattern = r'/image/([a-z0-9])+/([a-z0-9])+/([a-zA-Z0-9])+.jpg'
    return True if re.match(pattern, value) else False
