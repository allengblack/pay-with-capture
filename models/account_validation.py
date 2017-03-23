"""pay_with_capture.models"""

import json

class AccountValidation():
    """default response model"""
    _type = ""
    data = None


    def getJson(self):
        return json.dumps(self.__dict__)