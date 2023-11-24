from fpdf import FPDF

class Export:
    def __init__(self, bill):
        self.bill = bill

    def call(self):
        pdf = FPDF()
        pdf.add_page('P', 'A4')
        pdf.set_font('Arial', '', 12)
        # center this text
        pdf.text(83, 24, 'Python ATM')
        pdf.text(69, 34, '--------------------------------------')
        pdf.text(38, 46, f'Date: {self.bill.date()}');
        pdf.text(38, 55, f'Time: {self.bill.time()}');
        pdf.text(38, 65, f'Card Holder Name: {self.bill.user().name()}');
        pdf.text(38, 75, f'Withdraw amount: {self.bill.amount()}');
        pdf.text(38, 85, f'Current balance: {self.bill.account_balance()}');
        pdf.output('bill.pdf')
