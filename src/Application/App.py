from src.Services.ApiService import ApiService
from sys import stderr
import pandas as pd
from datetime import datetime


class App:
    def __init__(self):
        self._api_service = ApiService()

    def api_service(self) -> ApiService:
        return self._api_service

    def process_to_csv(self):
        return_val = self.api_service().run()
        if isinstance(return_val, str):
            return False
        else:
            return Processing(return_val)


class Processing:
    def __init__(self, alldata):
        try:
            print('- Iterate over all items, cast to DF and then to csv.')
            for iter_dict in alldata:
                # print(iter_dict)
                panda_cast = pd.DataFrame.from_dict(iter_dict, orient='index').T
                # print(panda_cast)
                act_date = datetime.today().strftime('%Y_%m_%d')+'_'+str(iter_dict.get('id'))
                panda_cast.to_csv('../../storage/' + str(act_date) + '.csv', index_label=False)
            print('- All .csv created')
        except Exception as e:
            print(e)
            print('- An error occurred while converting to .csv ', file=stderr)


if __name__ == '__main__':
    app = App()
    data = app.process_to_csv()
