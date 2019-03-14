import requests
from hashlib import md5


class RClientFour(object):

    def __init__(self, username, password):
        self.username = username
        try:
            self.password = md5(password).hexdigest()
        except TypeError:
            self.password = md5(password.encode('utf-8')).hexdigest()
        self.soft_id = '124507'
        self.soft_key = 'a94f2367b53746518d49ebe34e7e13ac'
        self.base_params = {
            'username': self.username,
            'password': self.password,
            'softid': self.soft_id,
            'softkey': self.soft_key,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'Expect': '100-continue',
            'User-Agent': 'ben',
        }

    def rk_create_code(self, im, im_type, timeout=60):
        """
        im: 图片字节
        im_type: 题目类型
        """
        params = {
            'typeid': im_type,
            'timeout': timeout,
        }
        params.update(self.base_params)
        files = {'image': ('a.jpg', im)}
        r = requests.post('http://api.ruokuai.com/create.json', data=params, files=files, headers=self.headers)
        return r.json()

    def rk_report_error(self, im_id):
        """
        im_id:报错题目的ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://api.ruokuai.com/reporterror.json', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    rc = RClientFour('wqh0109663', '***')
    im = open('verify2.gif', 'rb').read()
    print(rc.rk_create_code(im, 3040))
    print(type(rc.rk_create_code(im, 3040)))
    print(rc.rk_create_code(im, 3040).get('Result'))
