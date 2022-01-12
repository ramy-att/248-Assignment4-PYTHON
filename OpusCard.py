class OpusCard:

    def __init__(self, type, name, expiry_mth, expiry_yr):
        self.__type=type
        self.__name=name
        if expiry_mth<1 or expiry_mth>12:
            self.__expiry_mth =0
        else:
            self.__expiry_mth = expiry_mth
        self.__expiry_yr= expiry_yr

    def get_type(self):
        return self.__type

    def get_name(self):
        return self.__name

    def get_month(self):
        return self.__expiry_mth

    def get_yr(self):
        return self.__expiry_yr

    #Setters

    def set_type(self, type):
        self.__type= type

    def set_name(self, name):
        self.__name=name

    def set_month(self, month):
        if month<1 or month>12:
            self.__expiry_mth =0
        else:
            self.__expiry_mth = month

    def set_yr(self, year):
        self.__expiry_yr=year

    def __eq__(self, other):
        return(self.__name==other.__name and self.__type==other.__type and
               self.__expiry_yr==other.__expiry_yr and self.__expiry_mth==other.__expiry_mth)

    def __repr__(self):
        return(("Name:{}, Type:{}, Expiry:{}//{}").format(self.__name, self.__type, self.__expiry_mth, self.__expiry_yr))


