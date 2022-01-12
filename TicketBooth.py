from Tickets import *
from OpusCard import *

class TicketBooth:
    def __init__(self, Tickets, OpusCard):
        self.ticket=Tickets
        self.opus_lst= OpusCard

    def totalVTickets(self):
        return self.ticket.ticketsTotal()

    def equal_val_tickets(self, other):
        return (self.totalVTickets()==other.totalVTickets())

    def equal_tick_dis(self,other):
        return (self.ticket==other.ticket)

    def number_opus_cards(self):
        return len(self.opus_lst)

    def add_opus(self, opus):
        self.opus_lst.append(opus)

    def remove_opus(self,opus):
        self.opus_lst.pop(opus)

    def update_expiry(self,opus, month,year):
        self.opus_lst[opus].set_month(month)
        self.opus_lst[opus].set_yr(year)

    def update_tickets(self, nb_r, nb_j, nb_s, nb_d, nb_w):
        self.ticket.AddTickets(nb_r, nb_j, nb_s, nb_d, nb_w)

    def __eq__(self, other):
        return(self.totalVTickets()==other.totalVTickets() and self.equal_tick_dis(other))

    def __repr__(self):
        x="Regular: {}, Senior:{}, Daily:{}, Weekly:{}, Junior:{}".format(self.ticket.get_nb_reg(),
                                                                                self.ticket.get_nb_senior(),
                                                                                self.ticket.get_nb_daily(),
                                                                                self.ticket.get_nb_weekly(),
                                                                                self.ticket.get_nb_jun())
        y=""
        count=0
        if self.opus_lst:
            for opus in self.opus_lst:
                count+=1
                y+=str(count) +". " +str(opus)+"\n"
        else:
            y+="No opus cards\n"
        return ("Tickets:"+ x+ "\n"+ "Opus cards: \n"+ y)

    def tickets(self):
        return("Regular: {}, Senior:{}, Daily:{}, Weekly:{}, Junior:{}".format(self.ticket.get_nb_reg(),
            self.ticket.get_nb_senior(),self.ticket.get_nb_daily(),self.ticket.get_nb_weekly(), self.ticket.get_nb_jun()))




