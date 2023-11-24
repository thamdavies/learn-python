from fpdf import FPDF

class Export:
    def __init__(self, bill):
        self.bill = bill

    def call(self):
        pdf = FPDF()
        pdf.add_page('P', 'A4')
        pdf.set_font('Arial', '', 12)
        pdf.text(75, 25, 'Python ATM')
        pdf.text(50, 35, '-' * 50)
        pdf.text(50, 45, f'Date: {self.bill.date()}');
        pdf.text(50, 55, f'Time: {self.bill.time()}');
        pdf.text(50, 65, f'Card holder: {self.bill.user_name()}');
        pdf.text(50, 75, f'Withdraw amount: {self.bill.amount()}');
        pdf.text(50, 85, f'Current balance: {self.bill.account_balance()}');
        pdf.output('bill.pdf')
