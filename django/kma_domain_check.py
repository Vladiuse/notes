
class DomainCheck(models.Model):
    domain = models.CharField(max_length=100, unique=True)
    is_checked = models.BooleanField(default=False)
    check_id = models.CharField(max_length=250, blank=True)
    res_data = models.JSONField(blank=True, default=dict)

    class Meta:
        ordering = ['-is_checked', 'pk']


    def check_domain(self):
        print('START check_domain', self.domain, self.pk)
        if not self.check_id:
            check_id = self.get_domain_check_id()
            self.check_id = check_id
            print('SAVE ', self.check_id)
            self.save()
        if self.check_id:
            check_data = self.get_checked_data(self.check_id)
            self.res_data = check_data
            self.save()
        if self._is_checked():
            self.is_checked = True
            self.save()
        print(self.status(), len(self.res_data), '*'*10)


    def get_domain_check_id(self):
        # print('START get_domain_check_id')
        data = {
            'url': self.domain
        }
        try:
            res = req.post(api_url, data=data, headers=headers)
            # print(res.status_code)
            # print(res.json())
            # print('*'*100)
            if res.status_code == 200:
                check_id = res.json()['data']['id']
                return check_id
            else:
                print(res.status_code, res.json())
            return ''
        except Exception as error:
            print('Error get_domain_check_id' , error)
            return ''

    def get_checked_data(self,check_id):
        # print('START get_checked_data')
        api_url = f'https://www.virustotal.com/api/v3/analyses/{check_id}'
        try:
            res = req.get(api_url, headers=headers)
            if res.status_code == 200:
                return res.json()
            else:
                print(res.status_code, res.json())
                return dict()
        except Exception as error:
            print('ERROR get_checked_data', self.domain, error)
            return None

    def status(self):
        if self.res_data:
            try:
                return self.res_data['data']['attributes']['status']
            except KeyError:
                return 'KeyError'

    def stats(self):
        if self.is_checked:
            return str(self.res_data['data']['attributes']['stats'])

    def _is_checked(self):
        if self.res_data:
            try:
                if self.res_data['data']['attributes']['status'] == 'completed':
                    return True
            except KeyError:
                pass
        return False


    def is_errors(self):
        if self.is_checked:
            return self.res_data['data']['attributes']['stats']['malicious']
        else:
            return False

    def is_suspicious(self):
        if self.is_checked:
            return self.res_data['data']['attributes']['stats']['suspicious']
        else:
            return False
