from tkinter import *
import webbrowser
import random
from tkinter import messagebox, filedialog

class Super:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x700+30+10')
        self.root.title('Super Market')
        self.root.resizable(False, False)

        self.u1 = 'https://www.facebook.com/username'
        self.u2 = 'https://telegram.org'
        self.u3 = 'https://youtube.com'

        self.f5 = Frame(root, bd=2, width=200, height=450, bg="#0B4C5F")
        self.f5.place(x=160, y=400)  
        B1 = Button(self.f5, text='حسابنا علي الفيس بوك', width=26, fg='black', bg='#DBA901', font=('tajawal', 11, 'bold'), command=self.open1)
        B1.place(x=6, y=130)
        B2 = Button(self.f5, text='حسابنا علي التيجرام', width=26, fg='black', bg='#DBA901', font=('tajawal', 11, 'bold'), command=self.open2)
        B2.place(x=6, y=177)
        B3 = Button(self.f5, text='قناتنا علي اليوتيوب', width=26, fg='black', bg='#DBA901', font=('tajawal', 11, 'bold'), command=self.open3)
        B3.place(x=6, y=224)

        # Variables for quantities and total amounts
        self.br_vars = [IntVar() for _ in range(20)]

        # Customer Info Frame
        f1 = Frame(root, bd=2, width=338, height=170, bg='#0B4C5F')
        f1.place(x=961, y=35)
        tit = Label(f1, text=':بيانات المشتري', font=('tajawal', 16, 'bold'), bg='#0B4C5F', fg='tomato')
        tit.place(x=185, y=0)
        his_name = Label(f1, text='اسم المشتري', font=('tajawal', 15), bg='#0B4C5F', fg='white')
        his_name.place(x=230, y=40)
        his_phone = Label(f1, text='رقم المشتري', font=('tajawal', 15), bg='#0B4C5F', fg='white')
        his_phone.place(x=235, y=70)
        bill_num = Label(f1, text='رقم الفاتوره', font=('tajawal', 15), bg='#0B4C5F', fg='white')
        bill_num.place(x=242, y=100)

        self.namo = StringVar()
        self.phono = StringVar()
        self.fatora = StringVar()
        x = random.randint(1000, 10000)
        self.fatora.set(str(x))

        # Total amount variable
        self.total_amount = StringVar()

        self.Ent_name = Entry(f1, justify='center', textvariable=self.namo)
        self.Ent_name.place(x=90, y=42)
        self.Ent_phone = Entry(f1, justify='center', textvariable=self.phono)
        self.Ent_phone.place(x=90, y=72)
        self.Ent_bill = Entry(f1, justify='center', textvariable=self.fatora)
        self.Ent_bill.place(x=90, y=102)
        btn_customer = Button(f1, text='بحث', font=('tajawal', 14), width=10, height=4, bg='white')
        btn_customer.place(x=3, y=40)
        tidd = Label(f1, text='[الفواتير]', font=('tajawal', 17, 'bold'), bg='#0B4C5F', fg='gold')
        tidd.place(x=125, y=135)

        # Bill Display Frame
        f3 = Frame(root, bd=2, width=338, height=399, bg='white')
        f3.place(x=960, y=205)
        scrol_y = Scrollbar(f3, orient=VERTICAL)
        self.textarea = Text(f3, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=LEFT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # Action Buttons Frame
        f4 = Frame(root, bd=2, width=657, height=112, bg='#0B4C5F')
        f4.place(x=641, y=587)

        # Grouping buttons in separate frames
        button_frame = Frame(f4, bg='#0B4C5F')
        button_frame.place(x=0, y=0, relwidth=1, relheight=1)

        # Calculation, Export, and Print Buttons
        calc_export_print_frame = Frame(button_frame, bg='#0B4C5F')
        calc_export_print_frame.grid(row=0, column=0, padx=10, pady=10)
        hesap = Button(calc_export_print_frame, text='الحساب', width=13, height=1, font='tajawal', bg='#DBA901', command=self.calculate_totals)
        hesap.grid(row=0, column=0, padx=5)
        self.fatora_btn = Button(calc_export_print_frame, text='تصدير الفاتوره', width=13, height=1, font='tajawal', bg='#DBA901', command=self.export_bill)
        self.fatora_btn.grid(row=0, column=1, padx=5)

        # Clear and Exit Buttons
        clear_exit_frame = Frame(button_frame, bg='#0B4C5F')
        clear_exit_frame.grid(row=1, column=0, padx=10, pady=10)
        clear = Button(clear_exit_frame, text='افراغ الحقول', width=13, height=1, font='tajawal', bg='#DBA901', command=self.clear_fields)
        clear.grid(row=0, column=0, padx=5)
        exite = Button(clear_exit_frame, text='اغلاق البرنامج', width=13, height=1, font='tajawal', bg='#DBA901', command=self.exit_program)
        exite.grid(row=0, column=1, padx=5)

        # Total amount Label
        total_frame = Frame(button_frame, bg='#0B4C5F')
        total_frame.grid(row=0, column=1, padx=10, pady=10)
        total_label = Label(total_frame, text='إجمالي الحساب', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='gold')
        total_label.grid(row=0, column=0, padx=5)
        self.total_entry = Entry(total_frame, textvariable=self.total_amount, width=24, font=('tajawal', 14))
        self.total_entry.grid(row=0, column=1, padx=5)

        # Electrical Items Frame
        ff3 = Frame(root, bd=2, width=318, height=550, bg="#0B4C5F")
        ff3.place(x=641, y=35)
        ttt = Label(ff3, text='اللوازم الكهؤباءيه', font=('tajawal', 15, 'bold'), bg='#0B4C5F', fg='gold')
        ttt.place(x=120, y=0)
        item_names = ['مكنسه', 'ميكرويف', 'قلايه هواءيه', 'مكيف', 'تلاجه', 'فرن', 'فرن غاز', 'مروحه سقف', 'مقلايه هواءيه', 'فرن كهرباء', 'مروحه ارضيه', 'غساله اوتو', 'غساله عاديه', 'مكواه', 'تليفزيون']
        self.entries = []

        for i, name in enumerate(item_names):
            Label(ff3, text=name, font=('tajawal', 15), bg='#0B4C5F', fg='gold').place(x=233, y=50 + 30*i)
            entry = Entry(ff3, width=12)
            entry.place(x=70, y=50 + 30*i)
            self.entries.append(entry)

        # Additional frames for new categories
        self.create_additional_frames(root)

    def create_additional_frames(self, root):
        # Adding new items for bountiful products
        ff1 = Frame(root, bd=2, width=300, height=420, bg="#0B4C5F")
        ff1.place(x=25, y=35)
        Label(ff1, text='البقوليات', font=('tajawal', 15, 'bold'), bg='#0B4C5F', fg='gold').place(x=100, y=0)
        beans = ["بزر الكتان","بزر الشيا","ملح","رز",'عدس', 'فول', 'حمص', 'فاصوليا', 'لوبيا', 'بازلاء', 'كينوا', 'برغل']
        self.beans_entries = []

        for i, bean in enumerate(beans):
            Label(ff1, text=bean, font=('tajawal', 15), bg='#0B4C5F', fg='gold').place(x=190, y=50 + 30*i)
            entry = Entry(ff1, width=12)
            entry.place(x=70, y=50 + 30*i)
            self.beans_entries.append(entry)

        # Adding new items for household supplies
        ff2 = Frame(root, bd=2, width=300, height=400, bg="#0B4C5F")
        ff2.place(x=340, y=35)
        Label(ff2, text='اللوازم المنزلية', font=('tajawal', 15, 'bold'), bg='#0B4C5F', fg='gold').place(x=100, y=0)
        household_items = ['منشفة', 'ممسحة', 'فرشاة', 'سلة مهملات', 'مقص', 'ملاعق', 'شوكة', 'سكين']
        self.household_entries = []

        for i, item in enumerate(household_items):
            Label(ff2, text=item, font=('tajawal', 15), bg='#0B4C5F', fg='gold').place(x=190, y=50 + 30*i)
            entry = Entry(ff2, width=12)
            entry.place(x=70, y=50 + 30*i)
            self.household_entries.append(entry)

    def open1(self):
        webbrowser.open_new(self.u1)

    def open2(self):
        webbrowser.open_new(self.u2)

    def open3(self):
        webbrowser.open_new(self.u3)

    def calculate_totals(self):
        # Prices for each category
        beans_prices = [1.5, 2, 2.5, 3, 1.5, 2, 2.8, 3, 2.8, 3, 2.5, 3]  # Example prices for the new beans
        household_prices = [5, 3, 4, 6, 2, 1, 2.5, 3]  # Example prices
        electrical_prices = [200, 150, 200, 800, 350, 250, 280, 100, 200, 220, 140, 400, 350, 80, 300]  # Example prices

        # Calculate totals for beans
        total_beans = sum(float(self.beans_entries[i].get() or 0) * beans_prices[i] for i in range(len(self.beans_entries)))

        # Calculate totals for household supplies
        total_household = sum(float(self.household_entries[i].get() or 0) * household_prices[i] for i in range(len(self.household_entries)))

        # Calculate totals for electrical items
        total_electrical = sum(float(entry.get() or 0) * electrical_prices[i] for i, entry in enumerate(self.entries))

        # Calculate grand total
        grand_total = total_beans + total_household + total_electrical
        self.total_amount.set(f"{grand_total:.2f} $")

    def export_bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\tسوبر ماركت الخير يرحب بكم")
        self.textarea.insert(END, "\n===================")
        self.textarea.insert(END, f"\n\t   B.Num:     {self.fatora.get()}")
        self.textarea.insert(END, f"\n\t   Name:     {self.namo.get()}")
        self.textarea.insert(END, f"\n\t   Phone:     {self.phono.get()}")
        self.textarea.insert(END, "\n===================")
        self.textarea.insert(END, f"\n السعر   / العدد   / المشتريات")
        self.textarea.insert(END, "\n===================")

        item_names = ['مكنسه', 'ميكرويف', 'قلايه هواءيه', 'مكيف', 'تلاجه', 'فرن', 'فرن غاز', 'مروحه سقف', 'مقلايه هواءيه', 'فرن كهرباء', 'مروحه ارضيه', 'غساله اوتو', 'غساله عاديه', 'مكواه', 'تليفزيون']
        for i, entry in enumerate(self.entries):
            quantity = entry.get()
            if quantity:
                self.textarea.insert(END, f"\n{item_names[i]} / {quantity} / {quantity}")

        # Add beans and household supplies to bill
        beans_names = ["بزر الكتان","بزر الشيا","ملح","رز",'عدس', 'فول', 'حمص', 'فاصوليا', 'لوبيا', 'بازلاء', 'كينوا', 'برغل']
        for i, entry in enumerate(self.beans_entries):
            quantity = entry.get()
            if quantity:
                self.textarea.insert(END, f"\n{beans_names[i]} / {quantity} / {quantity}")

        household_names = ['منشفة', 'ممسحة', 'فرشاة', 'سلة مهملات', 'مقص', 'ملاعق', 'شوكة', 'سكين']
        for i, entry in enumerate(self.household_entries):
            quantity = entry.get()
            if quantity:
                self.textarea.insert(END, f"\n{household_names[i]} / {quantity} / {quantity}")

        file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file:
            file.write(self.textarea.get('1.0', END))
            file.close()

    def clear_fields(self):
        self.namo.set("")
        self.phono.set("")
        self.fatora.set(str(random.randint(1000, 10000)))
        self.total_amount.set("")
        for entry in self.entries + self.beans_entries + self.household_entries:
            entry.delete(0, END)
        self.textarea.delete('1.0', END)

    def exit_program(self):
        self.root.quit()


root = Tk()
ob = Super(root)
root.mainloop()
