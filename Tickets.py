class Tickets:

    regular_ticket_price= 3.5
    junior_ticket_price= 2.5
    senior_ticket_price=1
    daily_ticket_price=10
    weekly_ticket_price=40

    def __init__(self, nb_r, nb_j, nb_s, nb_d, nb_w):
        self.__number_regular=nb_r
        self.__number_junior = nb_j
        self.__number_senior = nb_s
        self.__number_daily = nb_d
        self.__number_weekly = nb_w

    def AddTickets(self, nb_r, nb_j, nb_s, nb_d, nb_w):
        self.__number_regular+= nb_r
        self.__number_daily += nb_d
        self.__number_junior+= nb_j
        self.__number_senior+= nb_s
        self.__number_weekly+= nb_w

    def get_nb_reg(self):
        return self.__number_regular

    def get_nb_daily(self):
        return self.__number_daily

    def get_nb_jun(self):
        return self.__number_junior

    def get_nb_senior(self):
        return self.__number_senior

    def get_nb_weekly(self):
        return self.__number_weekly

    def ticketsTotal(self):
        '''Return the total value of tickets'''
        total=  (self.get_nb_reg()*3.5) + (self.get_nb_daily()*10)+ (self.get_nb_jun()*2.5)+ (self.get_nb_senior()*1) + (self.get_nb_weekly()*40)
        return total


    # Setters
    def set_nb_reg(self, reg):
        self.__number_regular=reg

    def set_nb_daily(self, daily):
        self.__number_daily=daily

    def set_nb_jun(self, jun):
        self.__number_junior=jun

    def set_nb_senior(self, senior):
        self.__number_senior=senior

    def set_nb_weekly(self, weekly):
        self.__number_weekly= weekly

    def __eq__(self, other):
        return(self.__number_regular== other.__number_regular and self.__number_daily== other.__number_daily and
               self.__number_junior==other.__number_junior and self.__number_senior==other.__number_senior and
               self.__number_weekly==other.__number_weekly)

    def __repr__(self):
        return(("Regular:{}, Daily:{}, Junior:{}, Senior:{}, Weekly:{}").format(self.__number_regular, self.__number_daily, self.__number_junior, self.__number_senior, self.__number_weekly))
