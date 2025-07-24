import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from datetime import datetime, timedelta
import calendar
import json

class MedicalDashboard:
    def __init__(self):
        # Load design profile
        with open('design_profile.json', 'r') as f:
            self.design = json.load(f)
        
        # Extract color palette
        self.colors = self.design['design_system']['color_palette']
        self.typography = self.design['design_system']['typography']
        self.spacing = self.design['design_system']['spacing']
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Medical Dashboard")
        self.root.geometry("1200x800")
        self.root.configure(bg=self.colors['primary']['background'])
        self.root.resizable(True, True)
        
        # Configure grid weights for responsive design
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=2)
        self.root.grid_columnconfigure(2, weight=2)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=2)
        
        # Setup custom styles
        self.setup_styles()
        
        # Create components
        self.create_calendar()
        self.create_charts()
        self.create_stat_cards()
        self.create_appointments_table()
        
    def setup_styles(self):
        """Configure custom ttk styles based on design profile"""
        self.style = ttk.Style()
        
        # Configure dark theme for ttk widgets
        self.style.configure('Dark.TFrame', 
                           background=self.colors['primary']['surface'],
                           borderwidth=0)
        
        self.style.configure('Card.TFrame',
                           background=self.colors['primary']['surface'],
                           relief='flat',
                           borderwidth=1,
                           bordercolor=self.colors['primary']['card'])
        
        self.style.configure('Dark.TLabel',
                           background=self.colors['primary']['surface'],
                           foreground=self.colors['text']['primary'],
                           font=('Segoe UI', self.typography['sizes']['body']))
        
        self.style.configure('Header.TLabel',
                           background=self.colors['primary']['surface'],
                           foreground=self.colors['text']['primary'],
                           font=('Segoe UI', self.typography['sizes']['h3'], 'bold'))
        
        self.style.configure('Title.TLabel',
                           background=self.colors['primary']['background'],
                           foreground=self.colors['text']['primary'],
                           font=('Segoe UI', self.typography['sizes']['h2'], 'bold'))
        
        # Configure Treeview for dark theme
        self.style.configure('Dark.Treeview',
                           background=self.colors['primary']['surface'],
                           foreground=self.colors['text']['primary'],
                           fieldbackground=self.colors['primary']['surface'],
                           borderwidth=0,
                           font=('Segoe UI', self.typography['sizes']['body']))
        
        self.style.configure('Dark.Treeview.Heading',
                           background=self.colors['primary']['surface'],
                           foreground=self.colors['text']['secondary'],
                           font=('Segoe UI', self.typography['sizes']['body'], 'bold'))
    
    def create_calendar(self):
        """Create calendar widget based on design profile"""
        calendar_frame = tk.Frame(self.root, 
                                bg=self.colors['primary']['surface'],
                                relief='flat',
                                bd=0)
        calendar_frame.grid(row=0, column=0, sticky='nsew', 
                          padx=self.spacing['md'], pady=self.spacing['md'])
        
        # Calendar header
        header_frame = tk.Frame(calendar_frame, bg=self.colors['primary']['surface'])
        header_frame.pack(fill='x', pady=(self.spacing['md'], self.spacing['sm']))
        
        # Month/Year title
        current_date = datetime.now()
        month_year = current_date.strftime("%B %Y")
        
        tk.Label(header_frame, text="Calendar", 
                bg=self.colors['primary']['surface'],
                fg=self.colors['text']['primary'],
                font=('Segoe UI', self.typography['sizes']['h3'], 'bold')).pack(anchor='w')
        
        tk.Label(header_frame, text=month_year,
                bg=self.colors['primary']['surface'],
                fg=self.colors['text']['secondary'],
                font=('Segoe UI', self.typography['sizes']['body'])).pack(anchor='w')
        
        # Calendar grid
        cal_grid = tk.Frame(calendar_frame, bg=self.colors['primary']['surface'])
        cal_grid.pack(fill='both', expand=True, padx=self.spacing['sm'])
        
        # Weekday headers
        weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        for i, day in enumerate(weekdays):
            tk.Label(cal_grid, text=day, 
                    bg=self.colors['primary']['surface'],
                    fg=self.colors['text']['muted'],
                    font=('Segoe UI', self.typography['sizes']['caption']),
                    width=3, height=1).grid(row=0, column=i, padx=1, pady=1)
        
        # Calendar days
        cal = calendar.monthcalendar(current_date.year, current_date.month)
        for week_num, week in enumerate(cal, 1):
            for day_num, day in enumerate(week):
                if day == 0:
                    continue
                
                bg_color = self.colors['primary']['surface']
                fg_color = self.colors['text']['primary']
                
                # Highlight current day
                if day == current_date.day:
                    bg_color = self.colors['accent_colors']['blue']
                    fg_color = '#ffffff'
                elif day == 16:  # Example selected day
                    bg_color = self.colors['accent_colors']['teal']
                    fg_color = '#ffffff'
                
                day_btn = tk.Button(cal_grid, text=str(day),
                                  bg=bg_color, fg=fg_color,
                                  font=('Segoe UI', self.typography['sizes']['caption']),
                                  width=3, height=2, relief='flat', bd=0,
                                  cursor='hand2')
                day_btn.grid(row=week_num, column=day_num, padx=1, pady=1)
    
    def create_charts(self):
        """Create bar charts based on design profile"""
        # In Patient Chart
        in_patient_frame = tk.Frame(self.root, bg=self.colors['primary']['surface'])
        in_patient_frame.grid(row=0, column=1, sticky='nsew',
                            padx=self.spacing['md'], pady=self.spacing['md'])
        
        self.create_bar_chart(in_patient_frame, "In Patient Consultation", "300", "+23%", 
                            [250, 180, 320, 380, 290, 420, 350],
                            self.colors['accent_colors']['teal'])
        
        # Out Patient Chart  
        out_patient_frame = tk.Frame(self.root, bg=self.colors['primary']['surface'])
        out_patient_frame.grid(row=0, column=2, sticky='nsew',
                             padx=self.spacing['md'], pady=self.spacing['md'])
        
        self.create_bar_chart(out_patient_frame, "Out Patient Consultation", "108", "+17%",
                            [120, 150, 180, 95, 110, 200, 250],
                            self.colors['accent_colors']['yellow'])
    
    def create_bar_chart(self, parent, title, value, percentage, data, color):
        """Create individual bar chart"""
        # Header
        header_frame = tk.Frame(parent, bg=self.colors['primary']['surface'])
        header_frame.pack(fill='x', pady=self.spacing['md'])
        
        tk.Label(header_frame, text=title,
                bg=self.colors['primary']['surface'],
                fg=self.colors['text']['primary'],
                font=('Segoe UI', self.typography['sizes']['h3'], 'bold')).pack(anchor='w')
        
        value_frame = tk.Frame(header_frame, bg=self.colors['primary']['surface'])
        value_frame.pack(fill='x')
        
        tk.Label(value_frame, text=value,
                bg=self.colors['primary']['surface'],
                fg=self.colors['text']['primary'],
                font=('Segoe UI', self.typography['sizes']['h1'], 'bold')).pack(side='left')
        
        tk.Label(value_frame, text=percentage,
                bg=self.colors['primary']['surface'],
                fg=self.colors['status']['success'],
                font=('Segoe UI', self.typography['sizes']['body'])).pack(side='right')
        
        # Chart
        fig = Figure(figsize=(4, 2.5), facecolor=self.colors['primary']['surface'])
        ax = fig.add_subplot(111)
        ax.set_facecolor(self.colors['primary']['surface'])
        
        weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        bars = ax.bar(weekdays, data, color=color, alpha=0.8, width=0.6)
        
        # Styling
        ax.set_ylim(0, max(data) * 1.2)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_color(self.colors['text']['muted'])
        ax.tick_params(colors=self.colors['text']['muted'], labelsize=8)
        ax.set_yticks([])
        ax.grid(False)
        
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
    
    def create_stat_cards(self):
        """Create stat cards based on design profile"""
        cards_frame = tk.Frame(self.root, bg=self.colors['primary']['background'])
        cards_frame.grid(row=1, column=0, columnspan=3, sticky='ew',
                        padx=self.spacing['md'], pady=self.spacing['sm'])
        
        # Configure grid
        for i in range(4):
            cards_frame.grid_columnconfigure(i, weight=1)
        
        # Card data from design profile
        card_variants = self.design['components']['stat_card']['variants']
        card_data = [
            {"title": "Revenue", "value": "$105", "icon": "$", "color": "#2196f3"},
            {"title": "Out Patient", "value": "105", "icon": "👤", "color": "#4caf50"},
            {"title": "Appointments", "value": "20", "icon": "📅", "color": "#ffc107"},
            {"title": "Lab Results", "value": "5", "icon": "🧪", "color": "#9c27b0"}
        ]
        
        for i, card in enumerate(card_data):
            self.create_stat_card(cards_frame, card, i)
    
    def create_stat_card(self, parent, card_data, column):
        """Create individual stat card"""
        card_frame = tk.Frame(parent, bg=card_data['color'], relief='flat')
        card_frame.grid(row=0, column=column, sticky='ew', 
                       padx=self.spacing['sm'], pady=self.spacing['sm'])
        
        # Content frame
        content_frame = tk.Frame(card_frame, bg=card_data['color'])
        content_frame.pack(fill='both', expand=True, padx=self.spacing['md'], 
                          pady=self.spacing['md'])
        
        # Icon and content layout
        layout_frame = tk.Frame(content_frame, bg=card_data['color'])
        layout_frame.pack(fill='both', expand=True)
        
        # Icon
        icon_label = tk.Label(layout_frame, text=card_data['icon'],
                             bg=card_data['color'], fg='white',
                             font=('Segoe UI', 20))
        icon_label.pack(side='left', anchor='center')
        
        # Content
        text_frame = tk.Frame(layout_frame, bg=card_data['color'])
        text_frame.pack(side='right', fill='both', expand=True)
        
        tk.Label(text_frame, text=card_data['title'],
                bg=card_data['color'], fg='white',
                font=('Segoe UI', self.typography['sizes']['caption']),
                anchor='e').pack(fill='x')
        
        tk.Label(text_frame, text=card_data['value'],
                bg=card_data['color'], fg='white',
                font=('Segoe UI', self.typography['sizes']['h2'], 'bold'),
                anchor='e').pack(fill='x')
    
    def create_appointments_table(self):
        """Create appointments table based on design profile"""
        table_frame = tk.Frame(self.root, bg=self.colors['primary']['surface'])
        table_frame.grid(row=2, column=0, columnspan=3, sticky='nsew',
                        padx=self.spacing['md'], pady=self.spacing['md'])
        
        # Header
        header_frame = tk.Frame(table_frame, bg=self.colors['primary']['surface'])
        header_frame.pack(fill='x', pady=self.spacing['md'])
        
        tk.Label(header_frame, text="Appointments",
                bg=self.colors['primary']['surface'],
                fg=self.colors['text']['primary'],
                font=('Segoe UI', self.typography['sizes']['h3'], 'bold')).pack(side='left')
        
        # Action buttons
        actions_frame = tk.Frame(header_frame, bg=self.colors['primary']['surface'])
        actions_frame.pack(side='right')
        
        week_btn = tk.Button(actions_frame, text="This Week",
                           bg=self.colors['accent_colors']['blue'], fg='white',
                           font=('Segoe UI', self.typography['sizes']['body']),
                           relief='flat', padx=self.spacing['md'], pady=self.spacing['sm'])
        week_btn.pack(side='left', padx=(0, self.spacing['sm']))
        
        view_all_btn = tk.Button(actions_frame, text="View All →",
                               bg=self.colors['primary']['surface'],
                               fg=self.colors['accent_colors']['blue'],
                               font=('Segoe UI', self.typography['sizes']['body']),
                               relief='flat', bd=0, cursor='hand2')
        view_all_btn.pack(side='left')
        
        # Table
        columns = ('sr_no', 'mr_number', 'patient_name', 'status')
        tree = ttk.Treeview(table_frame, columns=columns, show='headings', 
                           style='Dark.Treeview', height=8)
        
        # Configure columns
        tree.heading('sr_no', text='Sr.No')
        tree.heading('mr_number', text='MR Number')
        tree.heading('patient_name', text='Patient Name')
        tree.heading('status', text='Status')
        
        tree.column('sr_no', width=60, anchor='w')
        tree.column('mr_number', width=120, anchor='w')
        tree.column('patient_name', width=200, anchor='w')
        tree.column('status', width=150, anchor='w')
        
        # Sample data
        appointments_data = [
            ('1', '102-23-243', 'Ronald Richards', 'Routine Checkup'),
            ('2', '202-20-312', 'Marvin McKinney', 'Elective'),
            ('3', '102-23-243', 'Brooklyn Simmons', 'Routine Checkup'),
            ('4', '102-23-243', 'Robert Fox', 'Routine Checkup')
        ]
        
        for item in appointments_data:
            tree.insert('', 'end', values=item)
        
        tree.pack(fill='both', expand=True, pady=(0, self.spacing['md']))
        
        # Configure row colors
        tree.tag_configure('routine', background=self.colors['status']['success'])
        tree.tag_configure('elective', background=self.colors['accent_colors']['blue'])
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = MedicalDashboard()
    app.run()