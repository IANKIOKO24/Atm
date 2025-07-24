import customtkinter as ctk
from tkinter import PhotoImage
import json

# Load design profile
with open('design_profile.json', 'r') as f:
    design = json.load(f)

# Set CustomTkinter appearance
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

class StudentsListDashboard:
    def __init__(self):
        # Create main window
        self.root = ctk.CTk()
        self.root.title("Students List Dashboard")
        self.root.geometry("1400x800")
        self.root.configure(fg_color=design['color_palette']['background']['primary'])
        
        # Define fonts
        self.title_font = ctk.CTkFont(family='Inter', size=24, weight='bold')
        self.heading_font = ctk.CTkFont(family='Inter', size=18, weight='normal')
        self.body_font = ctk.CTkFont(family='Inter', size=14, weight='normal')
        self.small_font = ctk.CTkFont(family='Inter', size=12, weight='normal')
        self.caption_font = ctk.CTkFont(family='Inter', size=10, weight='normal')
        
        # Sample data
        self.students_data = [
            {"admission_no": "AD9892434", "roll_no": "35013", "name": "Janet", "class": "III", "section": "A", "gender": "Female", "status": "Active"},
            {"admission_no": "AD9892433", "roll_no": "35013", "name": "Joann", "class": "IV", "section": "B", "gender": "Male", "status": "Active"},
            {"admission_no": "AD9892432", "roll_no": "35011", "name": "Kathleen", "class": "II", "section": "A", "gender": "Female", "status": "Active"},
            {"admission_no": "AD9892431", "roll_no": "35010", "name": "Gifford", "class": "I", "section": "B", "gender": "Male", "status": "Active"},
            {"admission_no": "AD9892430", "roll_no": "35009", "name": "Lisa", "class": "II", "section": "B", "gender": "Female", "status": "Inactive"},
        ]
        
        self.setup_ui()
        
    def setup_ui(self):
        # Configure grid weights
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        
        # Create main sections
        self.create_header()
        self.create_toolbar()
        self.create_controls()
        self.create_table()
        
    def create_header(self):
        """Create the top header section"""
        header_frame = ctk.CTkFrame(
            self.root,
            fg_color=design['color_palette']['background']['primary'],
            height=80
        )
        header_frame.grid(row=0, column=0, sticky="ew", padx=24, pady=(16, 0))
        header_frame.grid_columnconfigure(1, weight=1)
        
        # Left side - Title and breadcrumb
        left_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        left_frame.grid(row=0, column=0, sticky="w", padx=(0, 16))
        
        # Title
        title_label = ctk.CTkLabel(
            left_frame,
            text="Students List",
            font=self.title_font,
            text_color=design['color_palette']['text']['primary']
        )
        title_label.grid(row=0, column=0, sticky="w")
        
        # Breadcrumb
        breadcrumb_label = ctk.CTkLabel(
            left_frame,
            text="Dashboard / Students / All Students",
            font=self.caption_font,
            text_color=design['color_palette']['text']['muted']
        )
        breadcrumb_label.grid(row=1, column=0, sticky="w", pady=(4, 0))
        
        # Right side - Action buttons
        buttons_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        buttons_frame.grid(row=0, column=1, sticky="e")
        
        # Refresh button
        refresh_btn = ctk.CTkButton(
            buttons_frame,
            text="⟳",
            width=40,
            height=36,
            fg_color="transparent",
            hover_color=design['color_palette']['background']['tertiary'],
            border_width=1,
            border_color=design['color_palette']['borders']['subtle'],
            corner_radius=6,
            font=self.body_font,
            text_color=design['color_palette']['text']['secondary']
        )
        refresh_btn.grid(row=0, column=0, padx=(0, 8))
        
        # Print button
        print_btn = ctk.CTkButton(
            buttons_frame,
            text="🖨",
            width=40,
            height=36,
            fg_color="transparent",
            hover_color=design['color_palette']['background']['tertiary'],
            border_width=1,
            border_color=design['color_palette']['borders']['subtle'],
            corner_radius=6,
            font=self.body_font,
            text_color=design['color_palette']['text']['secondary']
        )
        print_btn.grid(row=0, column=1, padx=(0, 8))
        
        # Export dropdown
        export_btn = ctk.CTkButton(
            buttons_frame,
            text="Export ⌄",
            width=80,
            height=36,
            fg_color="transparent",
            hover_color=design['color_palette']['background']['tertiary'],
            border_width=1,
            border_color=design['color_palette']['borders']['subtle'],
            corner_radius=6,
            font=self.body_font,
            text_color=design['color_palette']['text']['secondary']
        )
        export_btn.grid(row=0, column=2, padx=(0, 16))
        
        # Add Student button
        add_student_btn = ctk.CTkButton(
            buttons_frame,
            text="+ Add Student",
            width=120,
            height=36,
            fg_color=design['color_palette']['accent']['blue'],
            hover_color="#6b8fff",
            corner_radius=6,
            font=self.body_font,
            text_color=design['color_palette']['text']['primary']
        )
        add_student_btn.grid(row=0, column=3)
        
    def create_toolbar(self):
        """Create the toolbar section"""
        toolbar_frame = ctk.CTkFrame(
            self.root,
            fg_color=design['color_palette']['background']['secondary'],
            height=60
        )
        toolbar_frame.grid(row=1, column=0, sticky="ew", padx=24, pady=(16, 0))
        toolbar_frame.grid_columnconfigure(4, weight=1)
        
        # Students List label
        section_label = ctk.CTkLabel(
            toolbar_frame,
            text="Students List",
            font=self.heading_font,
            text_color=design['color_palette']['text']['primary']
        )
        section_label.grid(row=0, column=0, sticky="w", padx=(24, 16))
        
        # Date range
        date_label = ctk.CTkLabel(
            toolbar_frame,
            text="📅 07/17/2025 - 07/23/2025",
            font=self.body_font,
            text_color=design['color_palette']['text']['secondary']
        )
        date_label.grid(row=0, column=1, sticky="w", padx=(0, 16))
        
        # Filter button
        filter_btn = ctk.CTkButton(
            toolbar_frame,
            text="🔽 Filter",
            width=80,
            height=32,
            fg_color="transparent",
            hover_color=design['color_palette']['background']['tertiary'],
            border_width=1,
            border_color=design['color_palette']['borders']['subtle'],
            corner_radius=6,
            font=self.body_font,
            text_color=design['color_palette']['text']['secondary']
        )
        filter_btn.grid(row=0, column=2, padx=(0, 16))
        
        # View toggle buttons
        view_frame = ctk.CTkFrame(toolbar_frame, fg_color="transparent")
        view_frame.grid(row=0, column=3, padx=(0, 16))
        
        list_btn = ctk.CTkButton(
            view_frame,
            text="☰",
            width=32,
            height=32,
            fg_color=design['color_palette']['accent']['blue'],
            hover_color="#6b8fff",
            corner_radius=6,
            font=self.body_font
        )
        list_btn.grid(row=0, column=0, padx=(0, 4))
        
        grid_btn = ctk.CTkButton(
            view_frame,
            text="⊞",
            width=32,
            height=32,
            fg_color="transparent",
            hover_color=design['color_palette']['background']['tertiary'],
            border_width=1,
            border_color=design['color_palette']['borders']['subtle'],
            corner_radius=6,
            font=self.body_font,
            text_color=design['color_palette']['text']['secondary']
        )
        grid_btn.grid(row=0, column=1)
        
        # Sort dropdown
        sort_btn = ctk.CTkButton(
            toolbar_frame,
            text="Sort by A-Z ⌄",
            width=120,
            height=32,
            fg_color="transparent",
            hover_color=design['color_palette']['background']['tertiary'],
            border_width=1,
            border_color=design['color_palette']['borders']['subtle'],
            corner_radius=6,
            font=self.body_font,
            text_color=design['color_palette']['text']['secondary']
        )
        sort_btn.grid(row=0, column=5, sticky="e", padx=(0, 24))
        
    def create_controls(self):
        """Create the controls section"""
        controls_frame = ctk.CTkFrame(
            self.root,
            fg_color=design['color_palette']['background']['primary'],
            height=40
        )
        controls_frame.grid(row=2, column=0, sticky="ew", padx=24, pady=(16, 0))
        controls_frame.grid_columnconfigure(2, weight=1)
        
        # Row per page
        rows_label = ctk.CTkLabel(
            controls_frame,
            text="Row Per Page",
            font=self.small_font,
            text_color=design['color_palette']['text']['secondary']
        )
        rows_label.grid(row=0, column=0, sticky="w", padx=(0, 8))
        
        rows_dropdown = ctk.CTkComboBox(
            controls_frame,
            values=["10", "25", "50", "100"],
            width=60,
            height=28,
            fg_color=design['color_palette']['background']['secondary'],
            border_color=design['color_palette']['borders']['subtle'],
            button_color=design['color_palette']['borders']['subtle'],
            corner_radius=6,
            font=self.small_font
        )
        rows_dropdown.set("10")
        rows_dropdown.grid(row=0, column=1, padx=(0, 16))
        
        # Entries label
        entries_label = ctk.CTkLabel(
            controls_frame,
            text="Entries",
            font=self.small_font,
            text_color=design['color_palette']['text']['secondary']
        )
        entries_label.grid(row=0, column=2, sticky="w")
        
        # Search box
        search_entry = ctk.CTkEntry(
            controls_frame,
            placeholder_text="Search",
            width=200,
            height=28,
            fg_color=design['color_palette']['background']['secondary'],
            border_color=design['color_palette']['borders']['subtle'],
            corner_radius=6,
            font=self.small_font,
            text_color=design['color_palette']['text']['primary'],
            placeholder_text_color=design['color_palette']['text']['muted']
        )
        search_entry.grid(row=0, column=3, sticky="e")
        
    def create_table(self):
        """Create the main data table"""
        # Table container
        table_container = ctk.CTkFrame(
            self.root,
            fg_color=design['color_palette']['background']['primary'],
            border_width=1,
            border_color=design['color_palette']['borders']['subtle'],
            corner_radius=8
        )
        table_container.grid(row=3, column=0, sticky="nsew", padx=24, pady=(16, 24))
        table_container.grid_columnconfigure(0, weight=1)
        table_container.grid_rowconfigure(1, weight=1)
        
        # Table header
        self.create_table_header(table_container)
        
        # Scrollable table body
        self.create_table_body(table_container)
        
    def create_table_header(self, parent):
        """Create table header row"""
        header_frame = ctk.CTkFrame(
            parent,
            fg_color=design['color_palette']['background']['secondary'],
            height=48,
            corner_radius=0
        )
        header_frame.grid(row=0, column=0, sticky="ew")
        
        # Configure column weights
        weights = [0, 0, 0, 1, 0, 0, 0, 0]  # Name column gets extra weight
        for i, weight in enumerate(weights):
            header_frame.grid_columnconfigure(i, weight=weight, minsize=100 if i > 0 else 48)
        
        headers = ["", "Admission No", "Roll No", "Name", "Class", "Section", "Gender", "Status"]
        
        for i, header in enumerate(headers):
            if i == 0:  # Checkbox column
                checkbox = ctk.CTkCheckBox(
                    header_frame,
                    text="",
                    width=16,
                    height=16,
                    fg_color=design['color_palette']['accent']['blue'],
                    border_color=design['color_palette']['borders']['subtle']
                )
                checkbox.grid(row=0, column=i, padx=16, pady=12)
            else:
                label = ctk.CTkLabel(
                    header_frame,
                    text=header,
                    font=ctk.CTkFont(size=14, weight='bold'),
                    text_color=design['color_palette']['text']['primary']
                )
                label.grid(row=0, column=i, sticky="w", padx=(16, 8), pady=12)
                
    def create_table_body(self, parent):
        """Create scrollable table body with data rows"""
        # Scrollable frame for table rows
        scrollable_frame = ctk.CTkScrollableFrame(
            parent,
            fg_color=design['color_palette']['background']['primary'],
            corner_radius=0
        )
        scrollable_frame.grid(row=1, column=0, sticky="nsew")
        scrollable_frame.grid_columnconfigure(0, weight=1)
        
        # Create data rows
        for i, student in enumerate(self.students_data):
            self.create_table_row(scrollable_frame, student, i)
            
    def create_table_row(self, parent, student_data, row_index):
        """Create a single table row"""
        row_frame = ctk.CTkFrame(
            parent,
            fg_color=design['color_palette']['background']['primary'],
            height=56,
            corner_radius=0
        )
        row_frame.grid(row=row_index, column=0, sticky="ew", pady=1)
        
        # Configure column weights (same as header)
        weights = [0, 0, 0, 1, 0, 0, 0, 0]
        for i, weight in enumerate(weights):
            row_frame.grid_columnconfigure(i, weight=weight, minsize=100 if i > 0 else 48)
        
        # Checkbox
        checkbox = ctk.CTkCheckBox(
            row_frame,
            text="",
            width=16,
            height=16,
            fg_color=design['color_palette']['accent']['blue'],
            border_color=design['color_palette']['borders']['subtle']
        )
        checkbox.grid(row=0, column=0, padx=16, pady=16)
        
        # Admission No (as link)
        admission_label = ctk.CTkLabel(
            row_frame,
            text=student_data["admission_no"],
            font=self.body_font,
            text_color=design['color_palette']['accent']['blue'],
            cursor="hand2"
        )
        admission_label.grid(row=0, column=1, sticky="w", padx=(16, 8), pady=16)
        
        # Roll No
        roll_label = ctk.CTkLabel(
            row_frame,
            text=student_data["roll_no"],
            font=self.body_font,
            text_color=design['color_palette']['text']['primary']
        )
        roll_label.grid(row=0, column=2, sticky="w", padx=(16, 8), pady=16)
        
        # Name with avatar
        name_frame = ctk.CTkFrame(row_frame, fg_color="transparent")
        name_frame.grid(row=0, column=3, sticky="w", padx=(16, 8), pady=16)
        
        # Avatar placeholder
        avatar = ctk.CTkFrame(
            name_frame,
            width=32,
            height=32,
            corner_radius=16,
            fg_color=design['color_palette']['accent']['blue']
        )
        avatar.grid(row=0, column=0, padx=(0, 12))
        
        # Avatar initial
        initial_label = ctk.CTkLabel(
            avatar,
            text=student_data["name"][0],
            font=ctk.CTkFont(size=14, weight='bold'),
            text_color="white"
        )
        initial_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Name
        name_label = ctk.CTkLabel(
            name_frame,
            text=student_data["name"],
            font=self.body_font,
            text_color=design['color_palette']['text']['primary']
        )
        name_label.grid(row=0, column=1, sticky="w")
        
        # Class
        class_label = ctk.CTkLabel(
            row_frame,
            text=student_data["class"],
            font=self.body_font,
            text_color=design['color_palette']['text']['primary']
        )
        class_label.grid(row=0, column=4, sticky="w", padx=(16, 8), pady=16)
        
        # Section
        section_label = ctk.CTkLabel(
            row_frame,
            text=student_data["section"],
            font=self.body_font,
            text_color=design['color_palette']['text']['primary']
        )
        section_label.grid(row=0, column=5, sticky="w", padx=(16, 8), pady=16)
        
        # Gender
        gender_label = ctk.CTkLabel(
            row_frame,
            text=student_data["gender"],
            font=self.body_font,
            text_color=design['color_palette']['text']['primary']
        )
        gender_label.grid(row=0, column=6, sticky="w", padx=(16, 8), pady=16)
        
        # Status badge
        status_color = design['color_palette']['accent']['success'] if student_data["status"] == "Active" else design['color_palette']['accent']['danger']
        
        status_badge = ctk.CTkLabel(
            row_frame,
            text=f"● {student_data['status']}",
            font=ctk.CTkFont(size=12, weight='normal'),
            text_color=status_color,
            fg_color="transparent"
        )
        status_badge.grid(row=0, column=7, sticky="w", padx=(16, 8), pady=16)
        
        # Add hover effect
        def on_enter(event):
            row_frame.configure(fg_color=design['color_palette']['background']['tertiary'])
        
        def on_leave(event):
            row_frame.configure(fg_color=design['color_palette']['background']['primary'])
            
        row_frame.bind("<Enter>", on_enter)
        row_frame.bind("<Leave>", on_leave)
        
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = StudentsListDashboard()
    app.run()